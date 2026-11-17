#!/usr/bin/env python3
"""Extract the text a machine sees in a CV and flag what breaks.

Usage: python3 scan.py path/to/cv.pdf|.docx|.txt|.md

Needs pdftotext (poppler) for PDFs. Word files are read with the standard library.
Prints the extracted text, then a list of flags. It only reads; it changes nothing.
"""
import re, subprocess, sys, zipfile
from pathlib import Path

LIGATURE_STEMS = [
    "certi cate", "speci c", "signi cant", "identi ed", "de ned", "de ne", "pro le",
    "of ce", "ef cien", "work ow", "in uence", "con dent", "bene t", "classi ",
    "veri ", "ful ll", "di erent", "e ective", "o er", "a ect",
]
UNITLESS = re.compile(r"\b\d[\d.,]*\s?[KMB]\+?\s+(revenue|sales|budget|ARR|GMV|turnover|savings)\b", re.I)
NUMBER = re.compile(r"\d[\d.,]*\s?(%|x\b)")
BASELINE = re.compile(r"\d[\d.,]*\s?%?\s*(to|→|->)\s*\d|\bfrom\b.*\bto\b|→|->|\bvs\.?\b|\bversus\b|\bbaseline\b|\bof\s+\d", re.I)


def extract(path: Path) -> str:
    suf = path.suffix.lower()
    if suf == ".pdf":
        try:
            return subprocess.run(["pdftotext", "-layout", str(path), "-"],
                                  capture_output=True, text=True, check=True).stdout
        except FileNotFoundError:
            sys.exit("pdftotext not found. Install poppler (brew install poppler / apt install poppler-utils).")
    if suf == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf8", "replace")
        xml = re.sub(r"</w:p>", "\n", xml)
        xml = re.sub(r"<w:tab/>", "\t", xml)
        return re.sub(r"<[^>]+>", "", xml)
    if suf == ".doc":
        sys.exit("Old .doc format. Save it as .docx or PDF and run again.")
    return path.read_text(encoding="utf8", errors="replace")


def flags(text: str):
    out = []
    low = text.lower()
    for stem in LIGATURE_STEMS:
        if re.search(r"\b" + re.escape(stem), low):
            out.append(f"Broken word (lost ligature, likely 'fi', 'fl' or 'ff'): '{stem.strip()}'. Re-export the PDF with ligatures off or from a different app.")
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        if "\ufffd" in s or re.search(r"[\ue000-\uf8ff]", s):
            out.append(f"Line {i}: unreadable character: {s[:80]}")
        if re.fullmatch(r"[€$£¥•·\s]+", s) or re.fullmatch(r"(fi|fl|ff|ffi|ffl)", s):
            out.append(f"Line {i}: symbol on its own line, lost from its number or word: '{s}'")
        if UNITLESS.search(s) and not re.search(r"[€$£¥]|USD|EUR|GBP|NZD|AUD", s):
            out.append(f"Line {i}: money amount with no currency: {s[:90]}")
        if NUMBER.search(s) and not BASELINE.search(s):
            out.append(f"Line {i}: % or x change with no baseline (check by hand, it may sit on the next line): {s[:90]}")
    return out


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    p = Path(sys.argv[1])
    text = extract(p)
    print("=== EXTRACTED TEXT ===")
    print(text)
    print("=== FLAGS ===")
    f = flags(text)
    print("\n".join(f) if f else "No flags.")
    print(f"=== {len(f)} flag(s). The number check is rough; read each one. ===")


if __name__ == "__main__":
    main()

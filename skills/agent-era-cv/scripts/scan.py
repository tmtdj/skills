#!/usr/bin/env python3
"""Extract the text a machine sees in a CV and flag what breaks.

Usage: python3 scan.py path/to/cv.pdf|.docx|.txt|.md

Needs pdftotext (poppler) for PDFs. Word files are read with the standard library.
Prints the extracted text with line numbers, then a list of flags. It only reads; it changes nothing.
Exit codes: 0 = done, 1 = could not read the file, 2 = no readable text (likely a scanned image).
"""
import html, re, subprocess, sys, zipfile
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

TEXT_SUFFIXES = {".txt", ".md", ".markdown", ".text"}
LIGATURE_STEMS = [
    r"certi cate", r"speci c", r"signi cant", r"identi ed", r"de ned\b", r"pro le",
    r"of ce(r|rs|s)?\b", r"ef cien", r"work ow", r"in uence", r"con dent", r"bene t",
    r"classi ", r"veri ", r"ful ll", r"di erent", r"e ective", r"o ered\b", r"a ected\b",
]
LIGATURE_CHARS = re.compile("[\ufb00-\ufb06]")
UNITLESS = re.compile(r"\b\d[\d.,]*\s?[KMB]\+?\s+(revenue|sales|budget|ARR|GMV|turnover|savings)\b", re.I)
NUMBER = re.compile(r"\d[\d.,]*\s?(%|x\b)")
BASELINE = re.compile(
    r"\d[\d.,]*\s?%?\s*(to|→|->)\s*\d|\bfrom\s+\S*\d[^.;]{0,40}?\bto\b|→|->|\bvs\.?\b|\bversus\b|\bbaseline\b|\bup from\b|\bdown from\b",
    re.I)


def fail(msg, code=1):
    print(msg)
    sys.exit(code)


def read_text_file(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16", "replace")
    try:
        return raw.decode("utf-8-sig")
    except UnicodeDecodeError:
        return raw.decode("cp1252", "replace")


def extract(path: Path) -> str:
    suf = path.suffix.lower()
    if suf == ".pdf":
        try:
            out = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, check=True).stdout
        except FileNotFoundError:
            fail("pdftotext not found. Install poppler (brew install poppler / apt install poppler-utils).")
        except subprocess.CalledProcessError:
            fail("Could not read this PDF. It may be locked or damaged. Export it again and retry.")
        return out.decode("utf-8", "replace").replace("\f", "\n")
    if suf == ".docx":
        try:
            with zipfile.ZipFile(path) as z:
                xml = z.read("word/document.xml").decode("utf8", "replace")
        except (zipfile.BadZipFile, KeyError):
            fail("Could not read this Word file. Save it again as .docx or PDF and retry.")
        xml = re.sub(r"<mc:Fallback>.*?</mc:Fallback>", "", xml, flags=re.S)
        xml = re.sub(r"</w:p>", "\n", xml)
        xml = re.sub(r"<w:tab/>", "\t", xml)
        xml = re.sub(r"<w:br/>", "\n", xml)
        return html.unescape(re.sub(r"<[^>]+>", "", xml))
    if suf == ".doc":
        fail("Old .doc format. Save it as .docx or PDF and run again.")
    if suf in TEXT_SUFFIXES:
        return read_text_file(path)
    fail(f"Unsupported file type '{suf}'. Save it as PDF, .docx, .txt or .md and run again.")


def flags(text: str):
    out = []
    low = text.lower()
    for stem in LIGATURE_STEMS:
        if re.search(r"\b" + stem, low):
            word = stem.replace("\\b", "").split("(")[0]
            out.append(f"Broken word (lost ligature, likely 'fi', 'fl' or 'ff'): '{word.strip()}'. Re-export the PDF with ligatures off or from a different app.")
    for i, line in enumerate(text.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        if "\ufffd" in s or re.search(r"[\ue000-\uf8ff]", s):
            out.append(f"Line {i}: unreadable character: {s[:80]}")
        if LIGATURE_CHARS.search(s):
            out.append(f"Line {i}: ligature character that some hiring software misreads: {s[:80]}")
        if re.fullmatch(r"[€$£¥\s]+", s) or re.fullmatch(r"(fi|fl|ff|ffi|ffl)", s):
            out.append(f"Line {i}: symbol on its own line, lost from its number or word: '{s}'")
        if UNITLESS.search(s) and not re.search(r"[€$£¥]|USD|EUR|GBP|NZD|AUD", s):
            out.append(f"Line {i}: money amount with no currency: {s[:90]}")
        if NUMBER.search(s) and not BASELINE.search(s):
            out.append(f"Line {i}: % or x change with no baseline (check by hand, it may sit on the next line): {s[:90]}")
    return out


def main():
    if len(sys.argv) != 2:
        fail(__doc__)
    p = Path(sys.argv[1])
    if not p.is_file():
        fail(f"File not found: {p}")
    text = extract(p)
    if len(re.sub(r"\s", "", text)) < 50:
        fail("No readable text. This is probably a scanned image, and hiring software can't read it either. "
             "Export a text PDF or Word file and run again. Do not score this file.", 2)
    print("=== EXTRACTED TEXT ===")
    for i, line in enumerate(text.splitlines(), 1):
        print(f"{i:4d} | {line}")
    print("=== FLAGS ===")
    f = flags(text)
    print("\n".join(f) if f else "No flags.")
    print(f"=== {len(f)} flag(s). The number check is rough; read each one. ===")


if __name__ == "__main__":
    main()

# skills

Agent skills by Tim. Free to use under the MIT licence.

## agent-era-cv

Your CV was built to prove how much you controlled. Employers now hire for how much you get done, and how fast, with AI. This skill checks your LinkedIn profile or CV for that and helps you fix it.

It does six things:

1. Asks three questions first (your target role, the AI work missing from your CV, and which results were yours alone).
2. Scans the CV the way a machine reads it and flags broken words and numbers with no baseline.
3. Scores nine AI-era skills on a four-level scale adapted from Zapier's hiring rubric, with a quote from your CV for each score.
4. Ranks the changes that would lift your score most.
5. Rewrites your key lines and shows old next to new. It never makes up a number. Where a fact is missing it asks you.
6. Gives you 3 to 5 tasks to do at your job so the missing lines become true, each with the proof it leaves and the CV line it fills. It can save them in a private `cv-work-plan.md`. Run the skill again later and it asks what you finished, turns real results into new lines, rescores you and gives the next tasks.

## Install

```bash
npx skills add timdej/skills
```

Then ask your agent: "Review my CV with agent-era-cv" and attach your CV or LinkedIn profile (PDF, Word or text). For LinkedIn, use its Save to PDF option or paste the text.

Works with Claude Code, Cursor, Codex and other agents the `skills` CLI supports. The scan script needs Python 3, plus `pdftotext` (poppler) for PDFs.

## Licence

MIT licence. The full text is in LICENSE.

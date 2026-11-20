# skills

Agent skills by Tim. Free to use under the MIT licence.

## agent-era-cv

Your CV was built to prove how much you controlled. Employers now hire for what you get done with AI, and the outcomes it moves. This skill checks your LinkedIn profile or CV for that and tells you where to add AI skills and what's missing. It doesn't rewrite your CV. You write the lines.

It does five things:

1. Asks three questions first (your target role, the AI work missing from your CV, and which results were yours alone).
2. Scans the CV the way a machine reads it.
3. Gives you a score out of 10 across ten AI-era skills, based on Zapier's AI fluency hiring rubric.
4. Leads with the top 3 changes: where an AI skill could go and what the line should show, with any question it needs right next to it. It never makes up a fact.
5. Gives you up to 3 tasks to do at your job so the missing lines become true.

The answer fits on one screen. Ask for the full breakdown to see the score for each skill, every flag, and a work plan you can save as a private `cv-work-plan.md`. Run the skill again later and it asks what you finished and rescores you.

## Install

```bash
npx skills add tmtdj/skills
```

Then ask your agent: "Review my CV with agent-era-cv" and attach your CV or LinkedIn profile (PDF, Word or text). For LinkedIn, use its Save to PDF option or paste the text.

Works with Claude Code, Cursor, Codex and other agents the `skills` CLI supports. The scan script needs Python 3, plus `pdftotext` (poppler) for PDFs.

## Licence

MIT licence. The full text is in LICENSE.

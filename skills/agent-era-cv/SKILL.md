---
name: agent-era-cv
description: Scores a CV or resume for AI fluency on a four-level scale, then rewrites its key lines for the agent era without inventing facts. Use when asked to review, score or rewrite a CV.
license: MIT
metadata:
  version: "1.0"
---

# Agent-era CV

Most CVs still prove how much you controlled. Employers now hire for how much you get done, and how fast, with AI.
This skill scores a CV on nine AI-era skills, then rewrites the lines that matter most. Old and new sit side by side so the person can check every word.

## Rules that never bend

1. Never invent a number, tool, product, date, metric or claim. If a fact is missing, write `[ASK: what you need]`.
2. Every number in a new line must appear in the CV or in the person's answers. Check this before you show the output.
3. The person is the subject of every verb. Agents and AI tools are never the subject.
4. Team results get team verbs. Only use solo verbs ("built", "cut", "grew") for work the person did alone.
5. Never frame a win as cutting people. Lead with speed and output.
6. Don't put the person's phone, email or home address in any file you save.
7. Plain English and short lines. No em-dashes, buzzwords or filler words.

## Step 1. Ask first, then wait

Ask these three questions in one message and wait for the answers. Don't score until you have them, or until the person says to go ahead without.

1. What role and location are you targeting? (e.g. "Senior PM, Berlin" or "Founder or CPO, consumer, New Zealand")
2. What do you do with AI that isn't on here? (what you run, how often, what it ships, how you check it)
3. Which results on this CV were yours alone, and which were team results?

If they skip question 3, treat any result that mentions a team as a team result. Ask again in the output.

## Step 2. Scan

1. Get the text a machine sees. Run `python3 scripts/scan.py <file>` (PDF, .docx, .txt or .md). If you can't run it, use `pdftotext -layout` for PDFs, or read the text directly.
2. Write down: roles with dates, every bullet, every number, the skills section, and any AI mention (tool, product, course).
3. If a line gives both a % change and a from-to pair, check the maths matches. If not, ask.
4. Report the flags in plain words: broken words (a PDF that turns "Certificates" into "Certi cates"), symbols cut loose from their numbers, money with no currency, % changes with no baseline or period. The script is rough, so read the CV for more.

## Step 3. Score

Read `references/scoring.md` and follow it exactly. In short:

- Score each of the nine skills on what the page shows, using the written rule:

| Level | What the page must show |
|---|---|
| Unacceptable | No line shows it. |
| Capable | The CV claims it, or names a tool or course, with no outcome. |
| Adoptive | An outcome with a number and a baseline, or a workflow they built that produces a named output regularly or for others. Using a chat tool yourself, however often, is only Capable. |
| Transformative | The person changed how a team or company works, with a number or proof a stranger could check. |

- Quote the CV line that earns each score, or write "no evidence".
- Add a second column for the person's answers from Step 1: the level they'd reach if that work went on the CV.
- Weight the skills by target role using the table in `references/scoring.md`, then work out the overall level with its formula.
- AI work from before agents (for example a GPT-3.5 or GPT-4 chat feature in 2023) counts for building and judgement. It doesn't count for delegating to agents.
- Judgement counts any decision with a result, AI or not. Every other skill needs AI in the line. Pre-AI strengths go in the bridges (Step 4).
- Give the weighted score to two decimals as well as the level.

Then check four things and give a one-line verdict for each:
1. Does it show speed and output (more done, faster), or only size and control (team counts, budgets)?
2. Does it say how AI was used and how the result was checked?
3. Do the numbers have a baseline and a period?
4. Are the verbs honest for team results?

## Step 4. Name the bridges

People who did good work before AI are often one short step from an AI skill. Use the bridge table in `references/scoring.md`. For each bridge, write one line with what they have now and the AI version to add if it's true.

## Step 5. Change list

Rank 5 to 8 changes by how much each lifts the weighted score. One plain line each. Start each with Add, Cut or Reword. Always include, where they apply:
- honest-verb fixes for team results
- rewording cuts framing ("restructured", "reduced costs", "reduced headcount") toward what the change made possible, only if the CV or the person says what that was
- missing baselines and units
- the off-page AI work from Step 1, if it's not on the CV

## Step 6. Rewrite

Read `references/rewrite.md`. Rewrite the 4 to 6 lines that matter most for the target role. Use this formula:

> Accomplished [X] against [baseline], measured by [Y], by doing [Z]. Optional: proved by [W].

- Outcome and baseline first. The person stays the subject.
- Mention agents at most once in the summary and once per role, and only where the speed gain is the point.
- Add "proved by" only if a stranger could check it: a public link, a named test set, real users, a named reviewer.
- Show a table: | Old | New |. Put `[ASK: ...]` wherever a fact is missing.

## Step 7. Check your own work

Before you show anything:
1. **Invented-fact check.** For each new line, list every number, tool and product name. Each must appear in the CV or the answers. If not, replace it with `[ASK: ...]`.
2. **Verb check.** Compare each new verb with the old one and the Step 1 answer. "Helped" must not turn into "led". A team result must not turn into "I". Check every clause in the line. "AI agents write the code" makes the agents the subject. Write "I use AI agents to write the code".
3. **Agent count.** At most one agent mention in the summary and one per role.
4. **Rescore.** Score the nine skills again as if the new lines were filled in. Show before and after.

## Step 8. Output

Use this order. Keep it short.

1. Overall level and weighted score: on the page, with your answers, and after the rewrite. One sentence why.
2. Scan flags.
3. Score table: skill, weight, level on the page, level with your answers, evidence quote.
4. The four checks.
5. Bridges.
6. Ranked change list.
7. Old and new table.
8. Questions: every `[ASK: ...]` gathered into one numbered list.
9. Optional extras (below), only if they asked or it fits.

## Optional extras

- About-me file (private). Offer to draft `about-me.md`: roles, real results, how they work with AI, what they want next. They keep it private and give it to their own AI tools so every draft starts from facts.
- Public resume.md or llms.txt. Only as an extra for people who like it. Never say it helps them get found. Ahrefs found 97% of llms.txt files got zero requests in a month, and Google says such files aren't needed for AI search.

## Cautions to pass on

- Visible AI use can cost you. In a 2025 PNAS study (N=4,439), people who used AI were rated as less competent. The penalty shrank when AI clearly fit the task. So the CV carries the outcome. The full "how" goes in the interview or a proof link.
- 60% of hiring managers want to test, discuss or see proof of AI skills (Resume Genius 2026). Claims with nothing behind them read as filler.

## Files

- `references/scoring.md`: the nine skills, the scoring rule, role weights, overall formula, bridges.
- `references/rewrite.md`: the formula, verb rules, cuts framing, proof rules.
- `references/examples.md`: worked example lines for six jobs, all made up.
- `references/sources.md`: where every number comes from.
- `scripts/scan.py`: text extraction and flags.

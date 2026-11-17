---
name: agent-era-cv
description: Scores a CV or resume for AI fluency on a four-level scale, rewrites its AI lines to show what the person does with AI, what it made possible and how they check it, without inventing facts, and builds a work plan to earn the missing lines for real. Use when someone asks to review, score, rewrite or update their CV or resume, or to check progress on their CV work plan. Not for writing a CV from scratch, cover letters or job posts.
license: MIT
metadata:
  version: "1.2"
---

# Agent-era CV

Most CVs still prove how much you controlled. Employers now hire for how much you get done, and how fast, with AI.
This skill scores a CV on nine AI-era skills, rewrites the lines where AI is or should be part of the work, then gives the person real work to do so the missing lines become true. Old and new sit side by side so the person can check every word.

The rewrite is about how AI changed the work. It is not a general CV edit. Generic gaps (a missing baseline, period or currency) get one line each in a short Trust checks list, not a rewrite.

## Rules that never bend

1. Never invent a number, tool, model, product, date, period, team size, data source, reviewer or claim. If a fact is missing, write `[ASK: what you need]`.
2. Every fact in a new line must appear in the CV or in the person's answers. Check this before you show the output.
3. The person is the subject of each line's main verb. Tools and agents can appear as "using X" or "with X", but they never do the action.
4. Team results get team verbs. Only use solo verbs ("built", "cut", "grew") for work the person says they did alone.
5. Never frame a win as cutting people. Lead with speed and output.
6. Don't put the person's phone, email or home address in any file you save.
7. Plain English and short lines. No em-dashes, buzzwords or filler words.

## Step 0. Look for a work plan

If `cv-work-plan.md` exists in the working folder, or the person attaches one, this is a follow-up run. Go to Step 9 first, then come back to Step 2 with the updated answers.

## Step 1. Ask first, then wait

Ask these three questions in one message and wait for the answers. Don't score until you have them, or until the person says to go ahead without.

1. What role and location are you targeting? (e.g. "Senior PM, Berlin")
2. What do you do with AI that isn't on here? Make it specific to the CV: name the AI lines it has ("What did [AI product] do for users, which models, how were answers checked?") or the work it shows ("Which parts of [product] do agents build, and what do you do?").
3. Which results on this CV were yours alone, and which were team results?

If they skip question 3, keep each line's own verb, but if the line or its role names a team or a team size, ask whether that result was solo or team. If they refuse all three, score the page only, use the latest job title as the target role, and say so.

## Step 2. Scan

1. Run `python3 scripts/scan.py <file>` (PDF, .docx, .txt or .md). If you can't run it, use `pdftotext -layout` for PDFs, or read the text directly.
2. If the script exits with "No readable text", stop. Tell the person the file is probably a scanned image that hiring software can't read either, and ask for a text PDF or Word file. Never score a blank page.
3. Write down: roles with dates, every bullet, every number, the skills section, and every AI mention.
4. If a line gives both a % change and a from-to pair, check the maths matches. If not, ask.
5. Report the flags in plain words. The script is rough, so read the CV for more.
6. Never flag overlapping job dates. People freelance, advise and run side work alongside a job.
7. If the CV is not in English, score and rewrite in its language, and keep the person's exact wording in the Old column.

## Step 3. Score

Read `references/scoring.md` and follow it exactly. Quote the CV line that earns each score, or write "no evidence". Give a second column for the person's answers, scored on the facts they gave, never on what they might add. Show the weighted score to two decimals and the level.

Then give a one-line verdict on each:
1. Does it show speed and output, or only size and control (team counts, budgets)?
2. Does it say how AI was used and how the result was checked?
3. Do the AI lines show what AI made possible, with a number?
4. Are the verbs honest for team results?

## Step 4. Name the bridges

Use the bridge table in `references/scoring.md`. One line each: what they have now, and the AI version to add if it's true.

## Step 5. Pick the lines to rewrite

Pick 4 to 6 lines, ranked by lift (weight x points the line could gain):
1. Lines where the CV or the answers say AI or agents were part of the work.
2. Lines where AI is plausibly part of the work but nobody has said so. You don't write AI in; you ask (see Step 6).
3. A missing line the target role needs, for a high-weight skill that scored low. The Old column says "(none)".

Don't pick a pre-AI line just to add a baseline or a period. List strong pre-AI results under "Keep, pre-AI" with one short reason each, and leave them as they are. Don't pad a strong CV.

## Step 6. Rewrite

Read `references/rewrite.md` and `references/examples.md`. Each new line shows three things:

> Did [what the person did with AI or agents], which made [what possible: speed, output, what one person can now ship], checked by [how they checked the work]. Optional: proved by [W].

- Show a table: | Old | New |. Put `[ASK: ...]` wherever a fact is missing.
- Don't add AI to a line unless the CV or the person says AI was part of that work. For a line in group 2 of Step 5, show the old line and the targeted AI question instead of a new line.
- Count missing facts, not brackets. If a line is missing more than two facts, show the old line and the questions, and leave the new line until they answer. One bracket that asks for two facts counts as two.
- Never copy a value from the examples. Their slots are placeholders, not facts.

Then write **Trust checks**: one line each for every generic gap on the CV, with no rewritten line. Types: missing baseline, missing period, missing currency or unit, cuts framing ("restructured", "reduced costs", "reduced headcount"), solo verbs on team results. These never go in the Old and New table.

## Step 7. Check your own work

Before you show anything, do all four and show a one-line result for each:
1. **Invented-fact check.** List every number, tool, model, product, date, period, team size, data source and reviewer in each new line. Each must appear in the CV or the answers. If not, replace it with `[ASK: ...]`.
2. **Verb check.** "Helped" must not turn into "led". A team result must not turn into "I". Check every clause: "AI agents write the code" makes agents the subject. Write "I use AI agents to write the code".
3. **Agent count.** At most one agent mention in the summary and one per role.
4. **Rescore.** Score the new lines twice. After the rewrite: every `[ASK]` is empty. Possible: every `[ASK]` is filled with a real fact of the kind it asks for. The after-rewrite score can't beat the with-answers score unless every fact in the new lines is sourced. Label the possible score as a ceiling, not a result.

## Step 8. Work plan

The rewrite only fixes how true work is described. Missing lines need real work. Read `references/work-plan.md`.

1. For the target role, and for the current role if different, pick 3 to 5 tasks the person can do at their job, with their clients, or on their own products. Tie each one to a high-weight skill that scored low, or to an `[ASK]` gap.
2. Each task is AI work: what to hand to AI or agents, how to check it, how long, what proof it leaves, and which CV line it would fill.
3. Task sizes ("a 20-case test set", "4 weeks") are suggestions for the person, never facts for the CV. The CV line only gets a number once the person reports a real one.
4. Frame every task as getting more done, faster, or better checked. Never as removing people.
5. Offer to save `cv-work-plan.md` in the working folder, using the template in `references/work-plan.md`. It's private: no phone, email or address in it.

## Step 9. Follow-up run (when a work plan exists)

1. Read `cv-work-plan.md`. For each open task, ask: done, still going, or dropped? For done tasks, ask for the result, the baseline, the period and the proof.
2. Turn only reported results into new CV lines, with Steps 6 and 7. A task marked done with no result stays an `[ASK]`.
3. Update the file: status, result, proof and the new line. Never delete old rows; mark them done or dropped.
4. Rescore, show the score before and after this round, and give the next 3 to 5 tasks.

## Step 10. Output

Keep it short, in this order:
1. Overall level and weighted score: on the page, with your answers, after the rewrite, and possible if every gap is filled with a real fact. One sentence why.
2. Scan flags.
3. Score table: skill, weight, level on the page, level with your answers, evidence quote.
4. The four checks.
5. Bridges.
6. AI rewrite: the Old and New table, the "Keep, pre-AI" list, then the Step 7 check results.
7. Trust checks.
8. Work plan.
9. Questions: targeted AI questions first (what the AI did, which models or agents, what the person did, how they checked it, what it made possible), then every other `[ASK: ...]`, in one numbered list.

## Optional extras

- About-me file (private). Offer to draft `about-me.md`: roles, real results, how they work with AI, what they want next. They give it to their own AI tools so every draft starts from facts.
- Public resume.md or llms.txt. Only for people who like it. Never say it helps them get found. Ahrefs found 97% of llms.txt files got zero requests in a month, and Google says such files aren't needed for AI search.

## Cautions to pass on

- Visible AI use can cost you. In a 2025 PNAS study (N=4,439), people who used AI were rated as less competent. The penalty shrank when AI clearly fit the task. So the CV carries the outcome. The full "how" goes in the interview or a proof link.
- 60% of hiring managers want to test, discuss or see proof of AI skills (Resume Genius 2026). Claims with nothing behind them read as filler.

## Files

- `references/scoring.md`: levels, nine skills, role weights, formula, bridges.
- `references/rewrite.md`: AI line formula, verb rules, trust checks, proof rules.
- `references/examples.md`: made-up AI-centred example lines for six jobs.
- `references/work-plan.md`: task examples by role and the progress file template.
- `references/sources.md`: where every number comes from.
- `scripts/scan.py`: text extraction and flags.

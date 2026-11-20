---
name: agent-era-cv
description: Scores a LinkedIn profile, CV or resume for AI fluency on ten AI-era skills and a four-level scale, recommends where in each role the person could add AI skills and which skills are missing, ranked by impact, and builds a work plan of real tasks to make the missing lines true. Use when someone asks to review, score or check their LinkedIn profile, CV or resume, or to check progress on their CV work plan. Not for writing or rewriting a CV, cover letters or job posts.
license: MIT
metadata:
  version: "2.0"
---

# Agent-era CV

Most CVs still prove how much you controlled. Employers now hire for what you get done with AI, and the outcomes it moves.
This skill scores a LinkedIn profile or CV on ten AI-era skills, then recommends where AI skills could go in each role and which skills are missing, ranked by impact. It gives the person real work to do so the missing lines become true.

It does not rewrite the CV. Writing the lines is the person's job. The skill says where a line could go and what a strong line shows, and the person writes it in their own words.

A LinkedIn profile counts as a CV here. The person can attach the PDF from LinkedIn's Save to PDF option or paste the text. Treat the headline and About section as the top lines, and each role's description as that role's lines. Wherever this skill says CV, read profile or CV.

## Rules that never bend

1. Never invent a number, tool, model, product, date, period, team size, data source, reviewer or claim. Only state facts that appear in the CV or in the person's answers.
2. Don't write CV lines for the person. A recommendation says where a line could go and what it should show. It may show the shape of a strong line as a pattern with empty slots, never filled with facts.
3. Never ask for output counts such as ads a week, videos a month or releases a month. Ask only for facts that change the level: the outcome, a before and after, cost, how the work is checked, and proof links.
4. Never frame a win as cutting people. Lead with speed and outcomes.
5. Don't put the person's phone, email or home address in any file you save.
6. Plain English and short lines. No em-dashes, buzzwords or filler words.
7. Never flag overlapping job dates. People freelance, advise and run side work alongside a job.

## Step 0. Look for a work plan

If `cv-work-plan.md` exists in the working folder, or the person attaches one, this is a follow-up run. Go to Step 7 first, then come back to Step 2 with the updated answers.

## Step 1. Ask first, then wait

Ask these three questions in one message and wait for the answers. Don't score until you have them, or until the person says to go ahead without.

1. What role and location are you targeting? (e.g. "Senior PM, Berlin")
2. What do you do with AI that isn't on here? Make it specific to the CV: name the AI lines it has ("What did [AI product] do for users, which models, how were answers checked?") or the work it shows ("Which parts of [product] do agents build, and what do you do?").
3. Which results on this CV were yours alone, and which were team results?

If they refuse all three, score the page only, use the latest job title as the target role, and say so.

## Step 2. Scan

1. Run `python3 scripts/scan.py <file>` (PDF, .docx, .txt or .md). If you can't run it, use `pdftotext -layout` for PDFs, or read the text directly.
2. If the script exits with "No readable text", stop. Tell the person the file is probably a scanned image that hiring software can't read either, and ask for a text PDF or Word file. Never score a blank page.
3. Write down: roles with dates, every line, every number, the skills section, and every AI mention.
4. If a line gives both a % change and a from-to pair, check the maths matches. If not, ask.
5. Report the flags in plain words. The script is rough, so read the CV for more.
6. If the CV is not in English, score and recommend in its language, and quote the person's exact wording.

## Step 3. Score

Read `references/scoring.md` and follow it exactly. Quote the CV line that earns each score, or write "no evidence". Give a second column for the person's answers, scored on the facts they gave, never on what they might add. Show the weighted score to two decimals and the level, for the page and with their answers.

## Step 4. Recommend

This is the main output. Read `references/examples.md` for what a strong line shows in each job.

1. **Rank by impact.** For each skill, impact = weight x the points it could gain. Work from the highest.
2. **Where to add, per role or section.** Go through the top lines (headline and About, or the summary), then each role from the most recent. For each, say where an AI skill could go and what the line should show:
   > Under [role], add a line showing [skill]: [what it should show].
   Only point to work the CV or the person's answers say happened, or that plainly fits the role. If it hasn't happened yet, say so and send it to the work plan.
3. **What's missing entirely.** List the skills that score Unacceptable for the target role, highest weight first, one line each on what a line for it would need to show.
4. **Every line carries its outcome.** Each recommendation names the outcome the line should show: a metric moved, with a before and after, that came from the AI work. If the person has no outcome yet, the recommendation says that is the gap.
5. **The shape of a strong line.** When it helps, show the pattern, with slots only:
   > Moved [outcome] from [before] to [after] by [what you did with AI or agents], checked by [how you checked the work].
   A link people can open to see the work makes it stronger. Never fill a slot with an invented fact, and never copy a value from `references/examples.md`.
6. **Bridges.** Use the bridge table in `references/scoring.md` for pre-AI strengths: what they have now, and the AI version to show if it's true.
7. **Leave as is.** Name strong pre-AI results that should stay as they are, with one short reason each. Don't pad a strong CV.
8. **Old-world lines.** You may name lines that only show size or control (team counts, budgets, "owned the roadmap"). Quote them. Don't write a replacement.

## Step 5. Trust flags

One plain line each, no rewritten line:
- Missing baseline: "[number] has no starting level."
- Missing period: "[number] has no period."
- Missing currency or unit: "[number] has no currency" or "[number] doesn't say what it counts."
- Cuts framing: "Restructured", "reduced costs", "reduced headcount" or "streamlined the team" read as cuts. Suggest leading with what the change sped up or made possible.
- Solo verb on a team result: if a line uses "built", "cut" or "grew" and the line or its role names a team or team size, say so in one line, e.g. "Line 4 says 'built' and the role names a team of 8. Readers may ask what your part was." Don't flag it if the person said the result was theirs alone.

## Step 6. Work plan

Recommendations only help where the work happened. Missing lines need real work. Read `references/work-plan.md`.

1. For the target role, and for the current role if different, pick 3 to 5 tasks the person can do at their job, with their clients, or on their own products. Tie each one to a high-weight skill that scored low or is missing.
2. Each task is AI work: what to hand to AI or agents, how to check it, how long, what outcome to measure, what proof it leaves, and which recommendation it would make true.
3. Task sizes ("a 20-case test set", "4 weeks") are suggestions for the person, never facts for the CV.
4. Frame every task as getting more done, faster, or better checked. Never as removing people.
5. Offer to save `cv-work-plan.md` in the working folder, using the template in `references/work-plan.md`. It's private: no phone, email or address in it.

## Step 7. Follow-up run (when a work plan exists)

1. Read `cv-work-plan.md`. For each open task, ask: done, still going, or dropped? For done tasks, ask for the outcome, the before and after, the period and the proof.
2. Score reported results in the "with your answers" column. Tell the person which recommendations are now ready for them to write up. Don't write the lines. A task marked done with no result stays open in the plan.
3. If they attach an updated CV, score the page again.
4. Update the file: status, result and proof. Never delete old rows; mark them done or dropped.
5. Show the score before and after this round, and give the next 3 to 5 tasks.

## Step 8. Output

Keep it short, in this order:
1. Overall level and weighted score: on the page, and with your answers. One sentence why.
2. Scan flags.
3. Score table: skill, weight, level on the page, level with your answers, evidence quote.
4. Recommendations: where to add, per role or section, ranked by impact; then skills missing entirely; then bridges; then "leave as is".
5. Trust flags.
6. Work plan.
7. Questions, in one numbered list. Targeted AI questions first: what the AI did, which models or agents, what the person did, how they checked it, the outcome it moved with a before and after, cost, proof links. Never ask for output counts.

## Optional extras

- About-me file (private). Offer to draft `about-me.md` from facts the person gives: roles, real results, how they work with AI, what they want next. They give it to their own AI tools so every draft starts from facts.
- Public resume.md or llms.txt. Only for people who like it. Never say it helps them get found. Ahrefs found 97% of llms.txt files got zero requests in a month, and Google says such files aren't needed for AI search.

## Cautions to pass on

- Visible AI use can cost you. In a 2025 PNAS study (N=4,439), people who used AI were rated as less competent. The penalty shrank when AI clearly fit the task. So the CV leads with the outcome. The full "how" goes in the interview or a proof link.
- 60% of hiring managers want to test, discuss or see proof of AI skills (Resume Genius 2026). Claims with nothing behind them read as filler.

## Files

- `references/scoring.md`: levels, the ten skills, role weights, overall score, bridges.
- `references/examples.md`: made-up patterns of what a strong line shows in six jobs, slots only.
- `references/work-plan.md`: task examples by role and the progress file template.
- `references/sources.md`: where every number comes from.
- `scripts/scan.py`: text extraction and flags.

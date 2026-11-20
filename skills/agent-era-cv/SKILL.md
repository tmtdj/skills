---
name: agent-era-cv
description: Scores a LinkedIn profile, CV or resume out of 10 for AI fluency across ten AI-era skills, leads with the top 3 places to add AI skills and what is missing, and builds a short work plan of real tasks to make the missing lines true. Use when someone asks to review, score or check their LinkedIn profile, CV or resume, or to check progress on their CV work plan. Not for writing or rewriting a CV, cover letters or job posts.
license: MIT
metadata:
  version: "2.1"
---

# Agent-era CV

Most CVs still prove how much you controlled. Employers now hire for what you get done with AI, and the outcomes it moves.
This skill scores a LinkedIn profile or CV out of 10 on ten AI-era skills, then leads with the top 3 changes: where AI skills could go and what is missing. It gives the person real work to do so the missing lines become true. The default answer fits on one screen; the full breakdown is there if they ask.

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
5. Note the flags for Step 5. The script is rough, so read the CV for more.
6. If the CV is not in English, score and recommend in its language, and quote the person's exact wording.

## Step 3. Score (internal)

Read `references/scoring.md` and follow it exactly. For each skill, note the CV line that earns the score, or "no evidence", and a second score for the person's answers, on the facts they gave, never on what they might add. This is your working. The person sees a plain score out of 10 (see `references/scoring.md`), never level names or the table, unless they ask for the full breakdown.

## Step 4. Recommend

This is the main output. Read `references/examples.md` for what a strong line shows in each job.

1. **Rank by impact, in two groups.** Use the impact rule in `references/scoring.md`.
   - **Already true, not on the page:** skills where the person's answers score higher than the page. These come first, because they need no new work.
   - **Needs new work:** skills still low with the answers. These go to the work plan, not to "add a line".
   One line can show several skills. Group them into one recommendation, so the same advice never appears twice.
2. **Where to add.** Say where the line goes (the headline and About, or the summary, or a named role) and what it should show:
   > Under [role], add a line showing [what it should show].
   If the work has no home on the CV yet (for example the person's own products), recommend a new role or section for it.
   Only point to work the CV or the person's answers say happened. If it hasn't happened, it goes in the work plan, never under a role.
   You may list the facts from the answers that the line should carry. Don't join them into a finished CV sentence; that is a rewrite.
3. **Every line carries its outcome.** Each recommendation names the outcome the line should show: a user or business metric moved, with a before and after, that came from the AI work. Speed of work (cycle time, release cadence) is not the outcome on its own. If the person has no outcome yet, say that is the gap.
4. **The shape of a strong line.** When it helps, show the pattern, with slots only:
   > Moved [outcome] from [before] to [after] by [what you did with AI or agents], checked by [how you checked the work].
   Never fill a slot with an invented fact, and never copy a value from `references/examples.md`.
5. **Questions sit with what they unlock.** If a recommendation needs a fact you don't have, put the question right under it: "Tell me: [question]". There is no separate question list.
6. **Fold in, don't list separately.** Lines that only show size or control (team counts, budgets, "owned the roadmap") go inside the recommendation they make room for, quoted, with no replacement written. Pre-AI strengths that map across (see the table in `references/scoring.md`) go inside the recommendation they support. Strong pre-AI results that should stay as they are get one short mention, only if the person might otherwise cut them.
7. **Plain words.** Name skills in plain words. The first time you mention context engineering, explain it: giving the AI the right information before it starts (docs, examples, rules, data).

## Step 5. Problems to fix

Merge the scan flags, the trust checks and any gap questions into one list. Each problem appears once, with its question next to it if it needs one. Types:
- File problems from the scan (broken words, symbols that came loose, a scanned image).
- Numbers with no starting level, no period, or no currency or unit.
- Cuts framing: "restructured", "reduced costs", "reduced headcount" or "streamlined the team" read as cuts. Suggest leading with what the change sped up or made possible.
- Solo verb on a team result: if a line uses "built", "cut" or "grew" and the line or its role names a team or team size, say so plainly, e.g. "These say 'reduced' and 'increased' for team results. Readers may ask what your part was." Don't flag it if the person said the result was theirs alone.
Group like problems into one line (all missing starting levels in one line, not one line each).

## Step 6. Work plan

Recommendations only help where the work happened. Missing lines need real work. Read `references/work-plan.md`.

1. Pick tasks the person can do at their job, with their clients, or on their own products, tied to high-weight skills still low with the answers.
2. Each task is AI work: what to hand to AI or agents, how to check it, how long, what outcome to measure, what proof it leaves.
3. Task sizes ("a 20-case test set", "4 weeks") are suggestions for the person, never facts for the CV.
4. Frame every task as getting more done, faster, or better checked. Never as removing people.
5. The default output shows at most 3 tasks, a title and one line each. The full breakdown has 3 to 5 tasks in full and offers to save `cv-work-plan.md` in the working folder, using the template in `references/work-plan.md`. It's private: no phone, email or address in it.

## Step 7. Follow-up run (when a work plan exists)

1. Read `cv-work-plan.md`. For each open task, ask: done, still going, or dropped? For done tasks, ask for the outcome, the before and after, the period and the proof.
2. Score reported results with the answers. Tell the person which recommendations are now ready for them to write up. Don't write the lines. A task marked done with no result stays open in the plan.
3. If they attach an updated CV, score the page again.
4. Update the file: status, result and proof. Never delete old rows; mark them done or dropped.
5. Show the score out of 10 before and after this round, and give the next tasks.

## Step 8. Output

### Default: fits on one screen

Lead with the answer. Use exactly these parts, in this order, and nothing else:

1. **Verdict, one line.** "Your profile scores [X]/10 as it stands, [Y]/10 with what you told me." Then one short line on why. If they gave no answers, show one score.
2. **Top 3 changes.** The three highest-impact recommendations from Step 4, each two or three lines: where, what it should show, and "Tell me:" with the question if a fact is missing.
3. **Also fix.** The merged list from Step 5, at most 4 lines, highest impact first.
4. **Next 3 things to do.** At most 3 work plan tasks, a title and one line each.
5. **The offer, as the last line:** "Want the full breakdown? It has the score for each skill, every flag, and the full work plan you can save."

No headings other than these, no tables, no level names, no skill numbers. Aim for about 25 lines.

### Full breakdown: only when asked

1. Score table: skill, weight, level on the page, level with your answers, evidence quote. Level names are fine here.
2. Every recommendation, ranked, including the ones past the top 3, and what you already have that maps across.
3. Every flag from Step 5, with its question.
4. The full work plan (3 to 5 tasks) and the offer to save `cv-work-plan.md`.

## Optional extras

- About-me file (private). Offer to draft `about-me.md` from facts the person gives: roles, real results, how they work with AI, what they want next. They give it to their own AI tools so every draft starts from facts.
- Public resume.md or llms.txt. Only for people who like it. Never say it helps them get found. Ahrefs found 97% of llms.txt files got zero requests in a month, and Google says such files aren't needed for AI search.

## Cautions to pass on

- Visible AI use can cost you. In a 2025 PNAS study (N=4,439), people who used AI were rated as less competent. The penalty shrank when AI clearly fit the task. So the CV leads with the outcome. The full "how" goes in the interview or a proof link.
- 60% of hiring managers want to test, discuss or see proof of AI skills (Resume Genius 2026). Claims with nothing behind them read as filler.

## Files

- `references/scoring.md`: levels, the ten skills, role weights, the score out of 10, what maps across from pre-AI work.
- `references/examples.md`: made-up patterns of what a strong line shows in six jobs, slots only.
- `references/work-plan.md`: task examples by role and the progress file template.
- `references/sources.md`: where every number comes from.
- `scripts/scan.py`: text extraction and flags.

# Rewrite rules

## What the rewrite is for

The rewrite shows how AI changed the person's work. It only touches lines where AI or agents are, or plausibly are, part of the work, or a missing line the target role needs. Pre-AI results stay as written and are labelled "keep, pre-AI". Generic gaps go in the Trust checks list, not the rewrite.

## The formula

> Did [what the person did with AI or agents], which made [what possible: speed, output, what one person can now ship], checked by [how they checked the work]. Optional: proved by [W].

It grows out of Laszlo Bock's XYZ formula (Google, 2014): accomplished X, measured by Y, by doing Z. Here Z is the AI work, X is what it made possible, and the check is new.

- Lead with what the person did with AI: "Run my apps alone with a team of AI agents...", "Designed and launched an assistant on [model]...".
- Then what it made possible: what one person now ships, or a before and after if they gave one. Named functions on a live product are enough; do not ask for output counts to complete the line. A number with a baseline beats a claim when they already have one.
- Then how they checked it: a test set, a review step, a named reviewer role, live users, a pass rate.
- The person is the subject of the main verb. Tools and agents sit in the line as "using X" or "with X". They never do the action. Not "Agents built X", not "a workflow that handles X".
- Agents at most once in the summary and once per role.
- "Proved by" is optional. W must be something a stranger could check: a public link, a named test set, live users, a named reviewer role. If nothing like that exists, leave it out. Don't suggest "available on request".
- Named tools and models go in the skills list unless the model choice is the point of the line.

## Never invent

- No new numbers, tools, models, product names, dates, periods, team sizes, data sources, reviewers or claims.
- If the formula needs a fact you don't have, write `[ASK: the exact fact]`, e.g. `[ASK: how Alpha's answers were checked]`.
- Keep the person's real numbers exactly as written. Don't round, convert or combine them.
- Don't add AI to a line unless the CV or the person says AI was part of that work. If AI is plausible but unsaid, show the old line and a targeted AI question.
- Count missing facts, not brackets. If a line is missing more than two facts, don't write a new line yet. Show the old line and the questions. A bracket that asks for two facts counts as two.
- The values in `examples.md` are placeholders. Never copy one into a real rewrite.

## Targeted AI questions

When the CV has few AI lines, generic questions ("what's the baseline?") don't help. Ask about the AI work itself, tied to a named line or product:
- What did [AI product] do for users, which models did it run on, and how were its answers checked?
- Which parts of [product] do agents handle (for example code, marketing, web, video), and what do you do?
- How do you check the work before it ships?
- Is there a live link or other proof a stranger could check?
- What does the work cost, or how much faster is it than before, if you already know?

Never ask for output counts such as ads a week, videos a month or releases a month, and never leave an `[ASK]` for one. If they already gave a number, you may use it. Ask only for facts that change the level: cost, a before and after, how the work is checked, and proof links. These questions go first in the Questions list.

## Honest verbs

| What happened | Verb to use |
|---|---|
| They did it alone | built, wrote, designed, shipped, cut, grew |
| They led a team that did it | Led the team that..., Ran..., ...while I led the X team |
| They were part of a team | Co-led, Part of the team that..., My team... |
| They advised or helped | Advised on, Helped, Supported |
| They designed and ran a product someone else coded | Designed and ran, Took [product] from X to Y as its product lead |
| They run the product alone with AI agents writing the code | Run, Design and ship [product] alone, using AI agents to write the code |

If a line or its role names a team or a team size and uses a solo verb, ask whether the result was solo or team. Don't change the verb until they answer.

## Trust checks

One line each, after the rewrite, with no rewritten line. Never put these in the Old and New table:
- Missing baseline: "[number] has no starting level."
- Missing period: "[number] has no period."
- Missing currency or unit: "[number] has no currency" or "[number] doesn't say what it counts."
- Cuts framing: "Restructured", "reduced costs", "reduced headcount", "streamlined the team" read as cuts. Say what the change made possible, with facts the person gives, or drop it. Never hide a fact the reader needs.
- Solo verb on a team result: name the line and the honest verb.

## Old and new table

| Old | New |
|---|---|
| (the line exactly as on the CV, or "(none)" for a missing line) | (the rewrite, with [ASK: ...] where needed) |

Under it, list "Keep, pre-AI" lines with a short reason each. Then run the self-check in SKILL.md Step 7.

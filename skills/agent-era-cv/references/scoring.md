# Scoring

The scale is adapted from Zapier's AI fluency rubric (Unacceptable, Capable, Adoptive, Transformative). Zapier uses it in interviews. A CV is only words on a page, so this skill uses a written rule. Two people scoring the same CV should get the same result.

## The rule

| Level | Points | What the page must show |
|---|---|---|
| Unacceptable | 0 | No line shows the skill. |
| Capable | 1 | The CV claims it, or names a tool, course or AI product, with no outcome. |
| Adoptive | 2 | An outcome with a number and a baseline (from X to Y, or X in Z weeks), or a repeatable system: a workflow the person built that produces a named output and runs regularly or is used by others. |
| Transformative | 3 | The person changed how a team or company works, with a number, or proof a stranger could check (public link, named test set, live users, named reviewer). |

How to apply it:
- Score what the page says. Don't give credit for what you guess they did.
- Take the highest level any single line earns. One line can count for more than one skill.
- A number without a baseline is still only Capable for an AI skill.
- Using a chat or coding tool yourself, however often ("use ChatGPT daily"), is Capable. It becomes Adoptive only with an outcome and baseline, or when it's a workflow they built that produces something named (releases, reports, prototypes) on a schedule or for others.
- A skill named only in the skills list ("prompt engineering") is Capable for that skill.
- Skill 7 (judgement) counts any product or business decision with a result, with or without AI. Every other skill needs AI in the line.
- Skill 8 (learning speed) needs evidence of change over time (tried, dropped, changed) or a course. Naming the tools someone uses doesn't count for skill 8.
- The person's answers to "what do you do with AI that isn't on here?" go in a second column: the level they'd reach if that work were on the CV, written up with the rule above. Never mix it into the on-page score.
- Pre-agent AI work (for example a GPT-3.5 or GPT-4 chat feature, a machine learning feature, before about 2024) counts for skill 6 (building) and skill 7 (judgement), and skill 3 (evals) if they measured the quality of the AI output. It doesn't count for skill 2 (delegating to agents).
- Pre-AI work (A/B testing, budgets, team leadership) doesn't score on the AI skills. It goes in the bridges list.

## The nine skills

1. **Speeding up work with AI.** AI used in core work, with a before and after. Shows as: cycle time, time to ship, volume handled, ideas tested per month.
2. **Delegating to agents.** Choosing what to hand an agent, writing a clear brief and a definition of done, reviewing what comes back. Shows as: what they run with agents, how often, what ships, how they check it.
3. **Evals.** Saying what good looks like for AI output and checking real outputs against it. Shows as: a test set of N cases, a pass rate from A% to B%, a quality checklist AI work is judged against.
4. **Context engineering.** Giving AI exactly the information it needs. Shows as: context files, prompt or skill libraries a team uses.
5. **Token and cost efficiency.** Knowing what an AI task costs and bringing it down. Shows as: cost per run from X to Y. Evidence that employers ask for this is thin, so weight it low unless the role is technical.
6. **Building.** Making a working version yourself with AI tools. Shows as: shipped apps, prototypes, demos, repos, ideas tested with users.
7. **Judgement and taste.** Picking the right problem when doing the work is cheap. Shows as: decisions made and what happened, ideas killed fast, an AI product chosen and launched with a result.
8. **Learning speed.** How fast their AI use is improving. Shows as: what they tried, dropped and changed in the last 12 months.
9. **Leading teams through AI adoption.** Getting a whole team working the new way. Shows as: team of N moved to agent workflows, cycle time from X to Y. Never as heads removed.

## Weights by target role

3 = core, 2 = useful, 1 = minor. If the target role manages people, set skill 9 to 3.

| Skill | PM | Engineer | Designer | Data / analyst | Marketer | Ops | Founder / exec |
|---|---|---|---|---|---|---|---|
| 1 Speed | 3 | 3 | 3 | 3 | 3 | 3 | 3 |
| 2 Delegating | 3 | 3 | 2 | 2 | 3 | 3 | 2 |
| 3 Evals | 3 | 3 | 2 | 3 | 2 | 2 | 1 |
| 4 Context | 2 | 3 | 1 | 2 | 2 | 2 | 1 |
| 5 Cost | 1 | 2 | 1 | 2 | 1 | 2 | 2 |
| 6 Building | 3 | 2 | 3 | 2 | 1 | 1 | 3 |
| 7 Judgement | 3 | 2 | 3 | 2 | 2 | 2 | 3 |
| 8 Learning | 2 | 2 | 2 | 2 | 2 | 2 | 2 |
| 9 Leading adoption | 1 | 1 | 1 | 1 | 1 | 2 | 3 |

Founder / exec covers founder, CPO, CTO, VP and Head of roles. For a role not listed, pick the closest column and say which.

## Overall level

1. Work out the weighted average: sum of (weight x points) divided by sum of weights.
2. Map it: below 0.5 = Unacceptable. 0.5 to 1.49 = Capable. 1.5 to 2.49 = Adoptive. 2.5 or more = Transformative.
3. Show the sum and the score to two decimals, so the person can check it and see it move. Do the same for the "with your answers" column and for the score after the rewrite. Levels are coarse, so the number is what shows progress.

## Bridges from pre-AI strengths

| They already have | The AI version to add, if true |
|---|---|
| A/B testing, experiments | Evals: a test set for AI output, and its pass rate |
| Budget or P&L ownership | Cost per task: what an AI workflow costs per run, and how they brought it down |
| Leading teams, hiring, coaching | Delegating to agents, and leading the team's move to AI workflows |
| Writing specs, briefs, PRDs | Context engineering: the briefs and context files agents work from |
| Research, user testing | Faster learning loops: ideas tested per month with AI prototypes |
| Process or ops design | Agent workflows with a checkpoint and a named reviewer |
| Shipping products without code (with engineers) | Building: shipping working versions with AI coding tools |

Write each bridge as one line. Only suggest the AI version as something to add if it's true. Never write it into the CV for them.

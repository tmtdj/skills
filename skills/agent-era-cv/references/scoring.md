# Scoring

The scale is adapted from Zapier's AI fluency rubric (Unacceptable, Capable, Adoptive, Transformative). Zapier uses it in interviews. A CV is only words on a page, so this skill uses a written rule. Two people scoring the same CV should get the same result.

## The rule

| Level | Points | What the page must show |
|---|---|---|
| Unacceptable | 0 | No line shows the skill. |
| Capable | 1 | The CV claims it, or names a tool, course or AI product, with no outcome. |
| Adoptive | 2 | An outcome with a number and a baseline (from X to Y, or X compared with the old way), or a repeatable system: a workflow the person built that produces a named output and runs regularly or is used by others. |
| Transformative | 3 | The person changed how a team or company works, with a before and after, or proof a stranger could check (public link, named test set, live users, named reviewer). A team size alone isn't enough. |

How to apply it:
- Score what the page says. Don't give credit for what you guess they did.
- Take the highest level any single line earns. One line can count for more than one skill.
- If you are unsure between two levels, take the lower one.
- A team result scores for the person's own part. If the line doesn't say what they did, it's Capable at most.
- A number without a baseline is still only Capable for an AI skill.
- Using a chat or coding tool yourself, however often ("use ChatGPT daily"), is Capable. It becomes Adoptive only with an outcome and baseline, or when it's a workflow they built that produces something named (releases, reports, prototypes) on a schedule or for others.
- A skill named only in the skills list ("prompt engineering") is Capable for that skill.
- Skill 7 (judgement) counts any product or business decision with a result, with or without AI. Every other skill needs AI in the line.
- Skill 9 (leading adoption) counts advisory clients and agent teams the person runs, when named. "Run my apps alone with a team of AI agents", with no functions named, is Capable for skill 9.
- Skill 2 (delegating) and skill 9 (when it is an agent team the person runs): running agents across several named business functions (for example code, marketing, copy, web, video, audio, ads) for a live product the person runs is Adoptive, with no output counts needed. Live product links, or other proof a stranger could check, make it Transformative. A before and after can still raise a line if they gave one. Never ask for output counts such as ads a week, videos a month or releases a month. Ask only for cost, a before and after, how the work is checked, and proof links.
- Skill 8 (learning speed) needs evidence of change over time (tried, dropped, changed) or a course. Naming the tools someone uses doesn't count for skill 8.
- The person's answers to "what do you do with AI that isn't on here?" go in a second column, scored with the same rule on the facts they gave. Never assume a number they didn't give. Never mix it into the on-page score.
- After the rewrite, score `[ASK]` slots as empty.
- Pre-agent AI work (for example a GPT-3.5 or GPT-4 chat feature, a machine learning feature, whatever the date) counts for skill 6 (building) and skill 7 (judgement), and skill 3 (evals) if they measured the quality of the AI output. It doesn't count for skill 2 (delegating to agents).
- Pre-AI work (A/B testing, budgets, team leadership) doesn't score on the AI skills. It goes in the bridges list.

## The nine skills

1. **Speeding up work with AI.** AI used in core work, with a before and after. Shows as: cycle time, time to ship, or volume compared with the old way.
2. **Delegating to agents.** Choosing what to hand an agent, writing a clear brief and a definition of done, reviewing what comes back. Shows as: the named functions they run with agents, how they check the work, and any proof link or before and after. Several named functions on a live product is enough for Adoptive. Do not ask for output counts.
3. **Evals.** Saying what good looks like for AI output and checking real outputs against it. Shows as: a test set of N cases, a pass rate from A% to B%, a quality checklist AI work is judged against.
4. **Context engineering.** Giving AI exactly the information it needs. Shows as: context files, prompt or skill libraries a team uses.
5. **Token and cost efficiency.** Knowing what an AI task costs and bringing it down. Shows as: cost per run from X to Y. Evidence that employers ask for this is thin, so weight it low unless the role is technical.
6. **Building.** Making a working version yourself with AI tools. Shows as: shipped apps, prototypes, demos, repos, ideas tested with users.
7. **Judgement and taste.** Picking the right problem when doing the work is cheap. Shows as: decisions made and what happened, ideas killed fast, an AI product chosen and launched with a result.
8. **Learning speed.** How fast their AI use is improving. Shows as: what they tried, dropped and changed in the last 12 months.
9. **Leading teams through AI adoption.** Getting a whole team working the new way. Shows as: a team moved to agent workflows, with a before and after if they have one. Counts an employer team, an advisory client's team, or a team of AI agents the person runs, when the line names it. For an agent team the person runs, several named functions on a live product is enough for Adoptive; live product links make it Transformative. Never as heads removed.

## Weights by target role

3 = core, 2 = useful, 1 = minor. If the target role has direct reports, set skill 9 to 3. If they name two target roles, use the first. If they give none, use their latest job title.

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
3. Show the sum and the score to two decimals, so the person can check it and see it move. Do the same for the "with your answers" column, for the score after the rewrite (every `[ASK]` empty), and for the possible score (every `[ASK]` filled with a real fact of the kind it asks for). The possible score is a ceiling to aim at, never a result. Levels are coarse, so the number is what shows progress.

## Bridges from pre-AI strengths

| They already have | The AI version to add, if true |
|---|---|
| A/B testing, experiments | Evals: a test set for AI output, and its pass rate |
| Budget or P&L ownership | Cost per task: what an AI workflow costs per run, and how they brought it down |
| Leading teams, hiring, coaching | Delegating to agents, and leading the team's move to AI workflows |
| Writing specs, briefs, PRDs | Context engineering: the briefs and context files agents work from |
| Research, user testing | Faster learning loops: ideas tested with AI prototypes, compared with the old way |
| Process or ops design | Agent workflows with a checkpoint and a named reviewer |
| Shipping products without code (with engineers) | Building: shipping working versions with AI coding tools |

Write each bridge as one line. Only suggest the AI version as something to add if it's true. Never write it into the CV for them.

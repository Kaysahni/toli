# Checking one eval task

You are auditing a test task, not doing it. The task directory has `task.md`
(the ask), `fixture/` (the files a tested agent searches), `checklist.json`
(the answer key) and maybe `build/`. `../../BRIEF.md` (evals/execution/BRIEF.md)
explains how tasks were meant to be built; read its rules and your task's spec.

Read `task.md`, `checklist.json`, and EVERY file in `fixture/` end to end. Do not
skim, do not rely on grep alone: the point is to catch what a builder missed.
For large CSVs, analyse with a script.

Report problems only, most serious first, each with file and verbatim evidence:

1. **Missing findings.** Anything a careful, correct answer to task.md would
   legitimately report that is not in `findings`.
2. **Wrong exclusions.** A decoy that is actually a real finding, or whose
   `why_not` does not hold up against the files.
3. **Unfair findings.** A finding the files do not clearly support, or whose
   `counts_if` is so strict or loose that grading would be arbitrary.
4. **Wrong answer.** For tasks with `answer`: recompute it independently from
   the files (numbers, dates, recommendation) and say whether it matches.
5. **Giveaways.** Text in task.md or fixture that points at the traps so
   directly the task stops testing careful reading, or anything that reveals it
   is a test.
6. **Inconsistencies** between fixture files that would confuse a careful
   reader and are not intentional traps.

Do not edit any file. End with a verdict line: `VERDICT: ready` or
`VERDICT: needs fixes (n)`.

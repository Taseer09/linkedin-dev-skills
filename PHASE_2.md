# Phase 2: project-to-post review guide

## What this branch adds

skills/li-project/SKILL.md defines the new instruction-based skill.
skills/li-project/examples.md gives illustrative output and behavioral checks.
This is not a standalone application or a trained model. The host assistant
reads the skill instructions and generates the drafts.

Input: a pasted README or project notes. Output: announcement, technical,
and personal-lesson angles, with missing personal information explicitly pending.
Source notes distinguish documentation from evidence and user-reported facts.

The original eleven skills and their behavior remain unchanged. The original
license and attribution remain intact. A separate li-proof command and saved
feedback memory are later phases, not completed features.

## Review and control

Work is proposed on a development branch. Merging into main and releasing are
separate decisions for the project owner. No LinkedIn content is posted.
The owner should receive explanations of changes, validation, limitations,
and any tasks requiring their input at each milestone.

## Manual trial in Claude Code

After checking out the feature/project-to-post branch on your own computer,
run these PowerShell commands from the repository root. This installs only
the new skill at project scope; it does not modify your global skills.

```powershell
New-Item -ItemType Directory -Force .claude/skills | Out-Null
Copy-Item -Recurse -Force skills/li-project .claude/skills/
```

Keep this installation copy local; do not add it to the Git commit. Reopen
Claude Code in this repository, then request /li-project and paste the
NotesIndex fixture from skills/li-project/examples.md. If the command is not
discovered, capture the error rather than claiming installation succeeded.

Check the drafts against the acceptance cases in examples.md. Paste the
response or error back into the project conversation for review. You can use
a real project instead, but remove secrets and provide your actual role.

## Validation status

The skill-format validator passed for the initial version. Two user-supplied
Claude Code transcripts were reviewed on 2026-09-19. They support successful
use in the user's Windows / VS Code workflow; the reviewer did not directly
observe the installation or skill-loading trace.

| Trial | Observed result | Limits |
| --- | --- | --- |
| Complete fictional NotesIndex notes | Three angles, roadmap preserved, no invented metrics, fictional role distinguished from the user, evidence notes and missing voice profile disclosed. | Opening added unsupplied personal activity; fenced copy blocks were not apparent in the pasted transcript. |
| No contribution or lessons supplied | Neutral project drafts, personal lesson pending, contributor question asked, no invented ownership or results. | 'No benchmark has been run' was weakened to results being unavailable in some prose. |

The follow-up instructions explicitly preserve negative facts and uncertainty,
avoid invented personal opening context, and require separate fenced text blocks.
These changes need a post-update model trial; do not count the earlier trials
as validation of the revised version. Other acceptance cases remain untested.
No independent verification of local file changes was performed.

## Refresh an existing local installation

From the repository root, inspect local changes first:

```powershell
git status --short
git branch --show-current
```

If tracked files have edits, pause and review them before pulling. Do not
discard work. On feature/project-to-post, with no conflicting tracked edits:

```powershell
git pull --ff-only origin feature/project-to-post
Copy-Item -Recurse -Force skills/li-project .claude/skills/
```

This replaces the installed copy of li-project with the updated version.
Preserve any deliberate edits to that installation copy before replacing it.
Restart Claude Code and repeat the missing-contribution trial. Check that
'no benchmark has been run' retains its meaning, drafts use fenced blocks,
and the personal lesson stays pending.

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

Frontmatter validation and static review can be performed here. A generated
example is illustrative, not a live model evaluation. Claude execution and
Windows installation require an environment that has those capabilities.
Do not mark those checks passed until actual results are available.

# Contributing

Make changes on a branch and explain the user problem, resulting behavior,
and validation in the pull request. Preserve the upstream MIT notice and
credit. Do not commit voice profiles, private drafts, credentials, or local
installation copies.

Run `python scripts/check_package.py` from the repository. This checks package
structure and utility behavior; it does not evaluate language-model decisions.
For skill changes, run a relevant example in Claude and report actual input,
output, model/environment if known, and limitations. Use fictional data.

Use the default Python standard library for small utilities where practical.
Keep a skill's name aligned with its folder and its description focused on its
actual task. Add an example when it clarifies a decision that failed in testing.
Avoid unsupported promises about truth, human authorship, or post performance.

Preference persistence tests must use an explicitly selected disposable profile.
Never delete or overwrite someone else's real profile as a test cleanup step.

Project owner review precedes merging and public release. A passing package
check alone does not establish that the skills behave correctly in Claude.

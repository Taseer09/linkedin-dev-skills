# Testing and release gates

## Automated package check

Requires Python 3.10+; no third-party Python dependencies.

```text
python scripts/check_package.py
```

Checks 14 skill entry points, JSON package consistency, local Markdown links,
Python syntax, license credit, and executable smoke tests for the two inherited
Python utilities. This is not a Claude behavioral evaluation or full JSON/YAML
schema validation. A user-supplied Windows PowerShell screenshot shows a PASS
on the phase-5-packaging checkout. The screenshot does not show the exact Python
version or commit hash. The three local skill copies refreshed without errors.

## Observed manual trials

User-supplied Claude Code transcripts support project drafting, no invented
personal role when missing, correct claim labels after clarification, selective
preference save, file readback, and removal. See PHASE_2.md, PHASE_3.md, and
PHASE_4.md for exact limitations. Never turn those observations into an accuracy
percentage or claim that every edge case passes.

## Combined trial — core sequence observed

User-supplied Claude transcripts show an approved synthetic LF-002 preference
saved in the isolated profile, li-project reading and applying it, li-proof
reviewing the resulting corrected draft and returning copy-ready text, and
li-feedback removing the preference with a dated log entry and readback.
The steps were observed across several runs, not a single automated evaluation.
The exact loaded revisions and session boundaries were not independently verified.

Initial drafting added unsupported privacy guarantees. After clarification,
the draft opened 'What if Markdown notes could be searched from a Python CLI?'
and retained only supplied functionality, planned semantic search, and
'No benchmark has been run'. The final transcript explicitly shows li-proof
loaded, those claims classified Supported by Documentation, no ownership claim,
and the final copy-ready draft. Earlier omission of corrected copy did not
recur in this explicit-output trial.

Cleanup removed LF-002 and logged removal on 2026-09-20 while preserving the
unrelated paragraph and existing logs. The initial LF-002 save had omitted
an addition-log entry. A subsequent user-supplied edit diff shows LF-003 and
its dated addition-log entry written together after the fix. Historical log entries
were not fabricated during cleanup. No repeat of the whole workflow is needed.

Remaining quality limits: source sentence numbers in the final proof table
were shifted for some claims even though assessments were sound. Fenced-block
rendering is unconfirmed in copied terminal text. The LF-003 trial correctly
left a contradictory question-opening proposal unsaved and explained the
same-scope conflict. The diff shows both rule and log writes; a post-edit
readback is not visible in that particular transcript. LF-003 remains active
only in the isolated test profile until cleanup. This result is not a general accuracy guarantee.

## Combined trial procedure

Install the three current developer skills. Use this isolated profile:
`D:\linkedin-agent\li-feedback-test\voice.md`. If the path already has an
unrelated rule, preserve it and resolve conflicts rather than overwriting it.

1. Invoke li-feedback: approve saving this exact preference to that test path:
   'Scope: technical project announcements. Begin the draft with a short
   question about the project's documented purpose.' This is a synthetic rule
   for an observable integration test, not a permanent personal preference.
2. Start a fresh Claude session. Invoke li-project with only an announcement
   requested, explicitly selecting that profile, and supply:
   'NotesIndex is a local prototype. It imports Markdown into SQLite and
   provides keyword search through a Python CLI. Semantic search is planned.
   No benchmark has been run. No authorship information is supplied.'
3. Confirm the selected profile was read, the draft opens with a relevant
   question, ownership is not invented, and future features stay planned.
4. Invoke li-proof on that actual output plus the same evidence. Check that
   style is not mistaken for a factual claim and unsupported facts are absent.
5. Remove only the test rule's assigned LF ID with li-feedback. Read back the
   file and confirm unrelated content is intact. Do not delete the whole file.

Record the actual output and revision tested. One successful run supports the
workflow; it does not prove perfect preference adherence across all outputs.

## Before release

- [x] Core save/draft/review/remove sequence observed through user-supplied transcripts; limits above.
- [x] Conflict detected and contradictory proposal left unsaved in the LF-003 trial.
- [x] Run package check on Windows and record the result (user-supplied screenshot).
- [x] Project-local skill installation/discovery observed in user trials; plugin mode remains untested.
- [ ] Review changed skills and known limitations; approve merge order.
- [ ] Replace development version with the agreed release version and tag the
      reviewed commit only after owner approval.

Draft PRs are stacked: Phase 2 targets main, Phase 3 targets Phase 2, Phase 4
targets Phase 3, and Phase 5 targets Phase 4. Review them together before choosing
the merge strategy; do not assume merging one publishes all later branches.

## Known inherited limitations

li-human can change technical wording (robust scaling becomes solid scaling)
and remove meaningful Unicode joiners. Its scores are heuristics, not authorship
or truth tests. li-project avoids automatic use of it. The inherited li-post
still calls it and has examples with unsupported details; use the new developer
workflow for source-grounded project content. Original skill examples and
platform-performance assumptions have not received a full audit in this phase.
Plugin-mode discovery and commands have not been exercised here. Individual
project-local skills have been exercised through user-supplied transcripts.

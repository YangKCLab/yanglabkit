# Submissions

Name each candidate directory `<agent-harness>_<model>_<run-id>` so the harness
and model are explicit, for example `codex_gpt-5_20260713-01`. Use a file-safe
lowercase form and add a run ID to distinguish repeated attempts. The matching
`submission_id` must equal the directory name, while `submission.json` records
the full harness, model, provider, date, and run reference.

Start from `../submission-template/` and run the validator before comparison.
The comparison builder replaces these descriptive names with anonymous slot
paths in its review page and keeps the identity mapping in a separate key.

Candidate outputs are intentionally not included in the initial scaffold.

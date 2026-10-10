# Rules for Future AI Coding Work

1. Read this file, [README.md](./README.md), the relevant documents in `docs/`, and the affected code before changing anything.
2. Follow approved decisions in [docs/DECISIONS.md](./docs/DECISIONS.md). If a decision needed by the task is unresolved, ask for approval rather than silently choosing behavior.
3. Keep changes small and focused. Do not implement out-of-scope features, add a frontend framework, introduce an external database, or add paid/AI services without approval.
4. Preserve the core invariant: an assigned team consumes one guide-capacity slot regardless of team size.
5. Enforce eligibility as a hard constraint in both allocators. Never assign an ineligible team-guide pair.
6. Keep greedy and Dinic logic independent of FastAPI, templates, and SQLite so they can be tested directly.
7. Run both algorithms on the same input snapshot. Maximum flow maximizes assignment count; do not describe it as preference-optimal unless a separate approved optimization is implemented.
8. Validate user input server-side, use parameterized SQL, preserve SQLite integrity, and show user-safe errors without hiding failures.
9. Use Jinja2 autoescaping and safe CSV generation. Consider spreadsheet formula injection in exported untrusted values.
10. Add or update tests for every behavior change. Cover correctness invariants and use the approved workload for performance claims.
11. Run the smallest relevant test set, then broader checks when the change warrants them. Report commands and outcomes honestly.
12. Update related documentation when implementation changes an approved behavior or decision.
13. Do not install dependencies unless a dependency manifest changes or a validation command demonstrates a missing dependency.
14. Never commit secrets, local databases, virtual environments, test caches, or generated exports.
15. Do not delete or overwrite unrelated user changes. Inspect repository status before editing and preserve work that is not part of the task.
16. Explain technical decisions in clear, beginner-friendly language when reporting work.

# Test Plan

## Objectives

Verify that data validation, eligibility, capacity rules, both allocators, explanations, comparison, persistence, web behavior, and CSV export are correct. Measure performance up to 10,000 teams without turning unstable timing thresholds into ordinary unit-test failures.

## Test layers

### Unit tests

- Validate team and guide fields, uniqueness rules, and boundary values.
- Test eligibility construction for matching domains and every approved explicit-rule case.
- Test greedy determinism, team/guide ordering, capacity enforcement, and unassigned outcomes.
- Test Dinic on known graphs, including cases where greedy makes fewer assignments.
- Verify assignments are eligible, a team is assigned no more than once, and guide loads do not exceed capacities.
- Verify team size never consumes multiple capacity slots.
- Test load, unused-capacity, assignment-count, and unassigned-reason calculations.

### Integration tests

- Exercise service operations with a temporary SQLite database.
- Check schema constraints, persistence, updates, deletes, and related eligibility behavior.
- Run both algorithms from the same stored input snapshot and compare their normalized results.
- Verify transaction behavior when an operation fails.

### API tests

- Use FastAPI's test client to check success and invalid-input responses for team/guide management and allocation.
- Verify status codes, rendered or structured output shape, and user-safe error messages.
- Test CSV response headers, content, quoting, and assigned and unassigned rows.

### UI tests

- Exercise core journeys: add teams and guides, define eligibility, run a comparison, inspect results, and download CSV.
- Check empty, loading, validation-error, and operation-error states.
- Check keyboard focus and labels for key forms, plus responsive layouts at representative narrow and wide viewports.
- Keep browser/UI test tooling proportional to the project; do not add a frontend framework.

### Performance tests

- Include deterministic generated workloads with 10,000 teams and documented guide count and eligible-edge count/density.
- Measure greedy and Dinic execution separately from database setup and rendering, then optionally measure the end-to-end operation.
- Record runtime, workload parameters, and test machine.
- Agree a numeric runtime target and representative graph density before making performance a pass/fail gate. Team count by itself is insufficient to define graph cost.
- Keep benchmarks selectable separately from the quick correctness suite if timing is variable.
- Verify results from scale workloads still satisfy eligibility, uniqueness, and capacity invariants.

## Required edge cases

- No teams, no guides, and empty eligibility.
- A team with no eligible guide.
- Eligible guides exist but all are full.
- Zero guide capacity.
- Capacity greater than the number of eligible teams.
- More teams than total capacity and fewer teams than total capacity.
- Multiple guides/domains and multiple eligible guides for a team.
- Duplicate team or guide codes under the approved normalization policy.
- Invalid, missing, negative, or out-of-range sizes and capacities.
- Greedy leaves a team unassigned although a reassignment would allow more total assignments.
- Multiple valid maximum assignments and deterministic reporting/tie handling.
- Explicit allow/deny combinations once their semantics are decided.
- CSV values containing commas, quotes, newlines, Unicode, and spreadsheet-sensitive text.
- Database or request failures do not produce success-shaped results or expose internal details.

## Test data and expected sample

Use the requirements' sample: T1 (AI, size 3), T2 (WEB, size 4), T3 (AI, size 3); G1 (AI, capacity 1), G2 (AI, capacity 1), G3 (WEB, capacity 2). A valid expected assignment is T1 -> G1, T2 -> G3, T3 -> G2, with no unassigned teams. The test should assert validity and full allocation rather than assume a particular guide choice unless the approved tie-breaking rules require that exact mapping.

## Completion criteria

- All quick unit, integration, and API tests pass.
- UI journey checks pass for the agreed supported browser/test setup.
- Scale tests run on the documented 10,000-team workload and report graph size and elapsed time.
- No performance claim is made without workload and environment details.

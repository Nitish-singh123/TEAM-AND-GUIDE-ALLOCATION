# Product Requirements Document

## Problem

People assigning project teams to guides need to respect guide capacity and team-guide eligibility. A simple greedy allocation can make locally reasonable choices that prevent a larger overall assignment. Without a clear comparison, it is difficult to see whether teams were left unassigned because they had no eligible guide, because eligible guides were full, or because of the allocation method.

## Target users

- **Primary:** a single coordinator managing teams and guides for a project or academic allocation exercise.
- **Secondary:** a reviewer who needs to inspect, compare, or export allocation results.

The MVP is a local, single-user application. User accounts and authentication are not included.

## Goals

1. Manage teams and guides with unique codes, domains, and their respective size/capacity values.
2. Represent which team-guide pairs are eligible.
3. Run and compare a deterministic greedy allocator and an optimal maximum-cardinality allocator implemented with Dinic's algorithm.
4. Explain assignments, unassigned teams, guide loads, and unused capacity.
5. Export allocation results as CSV.
6. Validate correctness and measure performance on workloads of up to 10,000 teams.

## MVP features

- Create, view, update, and delete teams and guides.
- Record team code, domain, and team size; record guide code, domain, and team capacity.
- Represent explicit team-guide eligibility restrictions. The precise relationship between domain matching and explicit rules must be settled before implementation (see [DECISIONS.md](./DECISIONS.md)).
- Run both allocation algorithms against the same input snapshot.
- Display each algorithm's assignments and unassigned teams, guide loads, unused capacity, and a comparison of assignment counts.
- Provide a plain-language reason for each unassigned team, at minimum distinguishing no eligible guides from eligible guides with no remaining capacity.
- Export results to CSV.
- Use a responsive HTML interface rendered with Jinja2, with lightweight JavaScript only where useful.

## Out of scope

- Authentication, roles, and multi-user access.
- React or another frontend framework.
- PostgreSQL, hosted databases, or other external database services.
- AI APIs, paid services, or external allocation services.
- Scheduling, messaging, notifications, or a full audit/history system.
- Preference-optimized maximum-flow allocation unless separately approved. Ordinary maximum flow maximizes the number of assignments, not preference satisfaction.
- Treating a team's student count as multiple guide-capacity slots.

## Assumptions

- SQLite via Python's built-in `sqlite3` is the only database for the MVP.
- One assigned team consumes one guide-capacity slot, regardless of team size.
- Team size is retained as informational data and must be a positive integer.
- Guide capacity is a non-negative integer number of teams.
- Allocation results are generated on demand from current data; persisting result history is not required initially.
- The application is initially used locally by one coordinator.
- The supplied example domains illustrate expected eligibility: T1 and T3 can use AI guides, and T2 can use a WEB guide. The exact eligibility rule and explicit restriction semantics remain an approval item.
- Algorithm tie-breaking and the exact greedy ordering are not yet approved and must be specified before implementation.

## Acceptance criteria

1. Teams and guides can be managed, and duplicate codes are rejected according to the approved case-sensitivity rule.
2. An allocation never assigns a team to an ineligible guide, assigns a team at most once, or exceeds guide capacity.
3. Team size does not change capacity consumption: each assigned team consumes exactly one slot.
4. The sample data can produce T1 -> G1, T2 -> G3, T3 -> G2, with no unassigned teams; allocations may choose a different valid guide assignment if the agreed deterministic rules permit it.
5. Maximum flow returns an assignment count at least as large as greedy for identical inputs.
6. The result view reports assignments, unassigned teams with reasons, each guide's load, and unused capacity for both methods.
7. CSV output represents assigned and unassigned teams and safely handles special characters in data.
8. Tests cover correctness and a documented performance target on a representative workload containing up to 10,000 teams. Runtime target and graph density must be agreed before the performance gate is finalized.

# Interface Design

## Design goals

The interface should feel clean, professional, and predictable for a coordinator who may not be technical. It should work on narrow mobile screens as well as desktop screens, use plain language, and make allocation results easy to verify.

## Navigation and page structure

Use a consistent page header and navigation for:

- Dashboard / allocation comparison
- Teams
- Guides
- Eligibility rules (or the approved equivalent)

Keep navigation labels visible and clear. Indicate the current page and provide a descriptive page title. Avoid adding navigation for features outside the MVP.

## Forms

- Give every field a persistent visible label; do not rely on placeholder text as a label.
- Explain code uniqueness, domain, positive team size, and non-negative guide capacity near the relevant fields.
- Mark required fields and show validation errors next to the affected controls.
- Preserve valid user-entered values after a validation error.
- Ensure forms are usable by keyboard and have visible focus indicators.
- Use appropriate input types and programmatic label/error associations.
- Confirm destructive actions such as deleting a team or guide; explain the effect on related eligibility records.

## Buttons and feedback

- Use consistent button styles for primary actions, secondary actions, and destructive actions.
- Use specific action text such as “Save team,” “Run comparison,” and “Download CSV.”
- Prevent accidental repeated submission where a request is still running and show a visible loading state while allocation is in progress.
- Show success and failure messages in a consistent location, with text that explains the next step.
- Do not rely on color alone to convey state.

## Tables and results

- Use semantic table markup with a caption or nearby heading and clear column headers.
- On small screens, allow safe horizontal scrolling or present a documented responsive alternative without hiding essential data.
- Keep team code, assigned guide, and assignment status easy to scan.
- Show guide capacity as load versus capacity, plus unused capacity.
- Separate or clearly label greedy and maximum-flow results.
- Make the total assignments and unassigned-team count visible.
- Show a plain-language reason for every unassigned team.
- Do not describe maximum flow as preference-optimal.

## States

- **Empty state:** explain what data is missing and provide a direct action to add teams or guides.
- **Loading state:** identify the operation in progress; prevent duplicate submissions where appropriate.
- **Error state:** show actionable validation or operation feedback without exposing stack traces, SQL, or file paths.
- **Results state:** identify the input snapshot or run context clearly enough that users know which data was compared.

## Accessibility and responsive behavior

- Use semantic headings, landmarks, labels, buttons, and table headers.
- Support keyboard-only operation, logical focus order, and visible focus.
- Maintain readable contrast and do not communicate meaning through color alone.
- Provide text alternatives for any meaningful non-text content.
- Ensure layouts, forms, tables, buttons, and messages remain usable on narrow viewports and at browser zoom.
- Announce important asynchronous status updates accessibly if JavaScript is used.

## Visual direction

Use a restrained neutral palette with one consistent accent color, readable typography, generous spacing, and a small set of reusable styles. Bootstrap may provide layout and components, but avoid adding a frontend framework or a complex design system.

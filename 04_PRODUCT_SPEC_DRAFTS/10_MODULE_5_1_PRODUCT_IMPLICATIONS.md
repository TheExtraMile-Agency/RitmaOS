# Module 5.1 Product Implications Draft

Source raw module:

- `02_RAW_MODULES/5.1-the-build-vigilore-course-companion.md`

Status: Draft product implications only. Not a durable decision.

## Product Thesis Implication

Module 5.1 suggests RitmaOS should include an Applied Ratio Audit workflow.

The workflow should help users take a real system, split it into components, assign each component to the 60/30/10 layers, and convert the result into architecture, pricing, contract, and fragility decisions.

## Applied Ratio Audit

Draft product flow:

1. User describes a system, product, service, or workflow.
2. RitmaOS breaks it into components.
3. Each component gets a layer classification: infrastructure, orchestration, or AI.
4. RitmaOS estimates the real ratio.
5. RitmaOS challenges AI-heavy components.
6. RitmaOS recommends what to build first.

Potential output artifacts:

- system/component breakdown,
- layer-ratio summary,
- biggest infrastructure risk,
- orchestration gaps,
- AI necessity challenge list,
- recommended next build step.

## Thin Wrapper vs Architectured System Diagnostic

RitmaOS should support a diagnostic that classifies systems as:

- Thin Wrapper,
- Hybrid,
- Architectured.

Draft diagnostic questions:

- What percentage still works if the model provider disappears?
- Can the model be swapped quickly?
- What remains if prompts are copied?
- Does model improvement improve the system automatically?
- Does the system keep operating without active human attention?

The output should identify the one change that moves the system one level up.

## Templates Suggested by the Lesson

Module 5.1 implies several reusable templates:

| Template | Purpose |
|---|---|
| System/component breakdown | Turn an "AI system" into named parts and visible layers. |
| AI necessity challenge | Identify model use that should become rules, templates, parsing, routing, or scoring. |
| Architecture-based pricing | Anchor price to replacement cost, delivery cost, value gap, and margin from architecture. |
| Contract/IP strategy prompts | Separate reusable methodology from client deliverables and reason about term length, revenue share, and minimums. |
| Model-provider fragility test | Check whether the system survives model outages, model swaps, copied prompts, and provider changes. |

## Workspace Architecture Connection

The filesystem should make the 60% and 30% visible before AI is added.

Possible workspace structure for an applied audit:

```text
components/
infrastructure/
orchestration/
ai-calls/
pricing/
contract-strategy/
fragility-test/
```

This structure would keep AI prompts from becoming the center of gravity. The user's workspace would show the deterministic core and routing logic as first-class artifacts.

## Pricing and Contract Support

RitmaOS could produce draft strategic notes for:

- replacement-cost anchors,
- delivery-cost breakdowns,
- value-gap pricing,
- retainer versus usage versus revenue-share models,
- deterministic-system confidence,
- IP and methodology boundary questions.

These should remain strategic prompts and product drafts, not legal advice.

## MVP Implication

The Applied Ratio Audit could become a near-term RitmaOS MVP workflow because it turns the central framework into concrete user artifacts.

Minimum useful version:

1. Component breakdown prompt.
2. AI necessity challenge.
3. Thin Wrapper vs Architectured System diagnostic.
4. Architecture-based pricing worksheet.
5. Contract/IP strategy question set.
6. Exportable workspace folders or markdown artifacts.

## Decision Status

No durable decision is created by this module.

Potential future decisions:

- Should Applied Ratio Audit become a named RitmaOS workflow?
- Should Thin Wrapper vs Architectured System become a formal product diagnostic?
- Should RitmaOS generate pricing and contract-strategy artifacts, or keep those as optional service-layer outputs?
- Should applied audit workspaces separate infrastructure, orchestration, and AI into dedicated folders?

# Module 5.1 Framework Extraction: The Build / VigilOre

Source raw module:

- `02_RAW_MODULES/5.1-the-build-vigilore-course-companion.md`

Status: Extracted framework draft. Not a durable decision.

## Core Framework

Module 5.1 turns the 60/30/10 ratio into an applied audit process for real systems.

The reusable flow is:

```text
system -> components -> layer assignment -> ratio audit -> architecture, pricing, contract, fragility implications
```

The key move is to make the hidden non-AI work visible before deciding where a model belongs.

## Component-by-Component System Decomposition

The lesson uses VigilOre as the model for breaking a system into operational components.

Reusable process:

1. Identify each component or agent.
2. Define what the component actually does.
3. Classify the work as infrastructure, orchestration, or AI.
4. Estimate the AI portion against the non-AI portion.
5. Challenge any system where AI exceeds a small minority of the work.

This converts "an AI system" into a concrete architecture map.

## AI Necessity Challenge

The second exercise is the central diagnostic.

Reusable question:

```text
Is this truly AI work, or is a model being used where rules, templates, parsing, scoring, routing, or structured logic should exist?
```

The VigilOre comparator pattern is:

```text
deterministic scoring logic + thresholds + weights + document assessment AI
```

AI is useful, but only after the infrastructure and orchestration layers define the job tightly enough.

## Architecture-Based Pricing

The pricing pattern is value-anchored rather than time-anchored.

Reusable model:

```text
replacement cost -> delivery cost -> value gap -> price point -> margin from architecture
```

The lesson frames margin as coming from infrastructure and orchestration built once, while marginal AI costs remain low.

Pricing inputs:

- salary or vendor alternative,
- manual process cost,
- hosting and tooling costs,
- maintenance time,
- token cost per unit,
- deterministic versus ongoing-human-work ratio,
- value gap large enough for both easy selling and sustainable margin.

## Contract and IP Strategy From Architecture

The contract strategy depends on which layers create the moat.

Reusable distinction:

```text
deliverable = client-facing output or licensed system
methodology = reusable routing logic, parser architecture, scoring logic, operating method
```

The lesson implies:

- deterministic systems can support shorter contracts,
- fragile thin wrappers may need lock-in,
- reusable methodology and orchestration logic may deserve protection,
- minimum monthly fees protect against low usage,
- revenue share only fits when upside and attribution are clear.

This is strategic contract reasoning, not legal drafting.

## Thin Wrapper vs Architectured System Test

The fragility test classifies a system based on dependence on model providers and prompt-level advantage.

Diagnostic questions:

- What still works if the model provider disappears?
- Does model improvement automatically improve the system?
- What remains if competitors copy the prompts?
- Can the model be swapped quickly?
- Does the system continue running without active attention?

Result categories:

| Rating | Meaning |
|---|---|
| Thin Wrapper | Fragile, replaceable, model-dependent, often needs lock-in to protect value. |
| Hybrid | Some structural advantage, but still exposed to model or prompt fragility. |
| Architectured | Deterministic core, replaceable AI layer, durable workflow advantage. |

## RitmaOS Extraction

Module 5.1 suggests RitmaOS should make the 60% and 30% layers visible before AI is added.

The filesystem can support this by separating:

- component maps,
- deterministic infrastructure,
- orchestration rules,
- AI prompts and model calls,
- pricing assumptions,
- contract strategy notes,
- fragility tests.

The workspace architecture should help users see whether they have built an architectured system or only a thin wrapper.

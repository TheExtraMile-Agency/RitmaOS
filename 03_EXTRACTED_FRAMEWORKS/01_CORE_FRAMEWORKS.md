# RitmaOS — Extracted Frameworks

## 1. Folder = Memory

The workspace folder carries persistent context so the AI does not start from zero every session.

Minimum structure:

```text
CLAUDE.md      -> identity and behavior rules
CONTEXT.md     -> current project and what good looks like
REFERENCES.md  -> examples, links, background material
```

## 2. Prompt = Direction

A strong prompt has five possible parts:

```text
Identity
Task
Context
Constraints
Output Format
```

For ongoing projects:

```text
Persistent files carry: Identity + Context
Individual prompts carry: Task + Constraints + Output Format
```

## 3. AI Reliability = Architecture

AI is unreliable in the same way every new computing layer was unreliable at first. The answer is not magic. The answer is engineering:

```text
structure
standards
redundancy
verification
human checkpoints
error handling
```

## 4. Template Pattern

Prompting is programming at a high abstraction layer. You are filling structured slots:

```text
identity slot
task slot
context slot
constraint slot
format slot
```

Wrong context creates wrong output the same way wrong variables create bugs.

## 5. Abstraction Ladder

```text
Book Layer       = prompts and outputs; cheap, generic, easy to copy
Movie Layer      = flows and automations; context-specific, higher value
Video Game Layer = systems that learn; bespoke, interactive, self-improving
```

RitmaOS should not stay at the Book Layer. It should sell the Movie Layer first and build toward the Video Game Layer.

## 6. 60/30/10 AI System Ratio

Well-built AI systems are usually:

```text
60% traditional code / data processing / files / integrations
30% routing / rules / orchestration
10% AI model calls
```

The model is a component. The value is in the operating layer around it.

## 7. Filesystem as Orchestration

The filesystem can do orchestration work that frameworks normally do in code:

```text
numbered folders       -> stage sequencing
CONTEXT.md files       -> context scoping
output folders         -> state and handoff
review files           -> human checkpoints
shared references      -> reusable knowledge
```

## 8. Spec as Leverage Point

The hard work is often the spec, not the AI output. A strong spec describes:

```text
purpose
context
workflow
scenes or stages
constraints
quality rules
output format
review criteria
```

## 9. RitmaOS Product Principle

Do not sell AI. Sell the structure that makes AI useful.

# RitmaOS — Research Notes

## Lesson 1.2: First Folder

Core idea: a simple folder with three files changes AI behavior because it gives the model identity, project context, and references.

Starter files:

- `CLAUDE.md` — who the AI is helping and how it should behave
- `CONTEXT.md` — what the project is and what good looks like
- `REFERENCES.md` — examples, notes, links, and supporting material

RitmaOS implication: the minimum viable version of the system is a structured workspace that carries persistent context across sessions.

## Lesson 1.3: Prompt Structure Framework

Core prompt components:

- Identity
- Task
- Context
- Constraints
- Output Format

For ongoing projects, Identity and Context should live in files. Task, Constraints, and Output Format should live in the active prompt.

RitmaOS implication: the product should separate persistent context from per-task direction.

## Lesson 2.2: AI Reliability as Architecture

Core idea: every computing layer started unreliable and became useful through engineering: standards, error handling, redundancy, verification, and architecture.

RitmaOS implication: AI reliability is not solved by “better prompts” alone. It is solved by building structure around AI.

## Lesson 2.4: Abstraction Ladder

Three layers:

1. Book layer — prompts to outputs, same for everyone
2. Movie layer — flows and automation, context-specific
3. Video game layer — data and smarter systems, bespoke and self-improving

RitmaOS implication: do not productize only prompts or templates. Build the layer above prompts: business-specific workflows, routing, memory, and improvement.

## Lesson 2.5: Orchestration vs Intelligence

Core idea: production AI systems are mostly orchestration, routing, integrations, and traditional software. The AI model is only one component.

Framework:

- 60% traditional code
- 30% rule-based logic and routing
- 10% AI model calls

RitmaOS implication: sell orchestration, not the model.

## Lesson 2.6: Video as Code

Core idea: creative work becomes scalable when it is treated like software: specs, components, constraints, style guides, and reusable systems.

RitmaOS implication: business work can become “work as code” using specs, workflows, reusable prompt components, and review stages.

## Lesson 2.7: Ethics Engine / AI Auditing

Core idea: real AI systems are mostly APIs, async workflows, parsing, data processing, statistics, and review loops. AI calls are a small part of the system.

RitmaOS implication: the long-term product can become a system for workflow execution, data capture, measurement, and continuous improvement.

## GitHub: Interpreted Context Methodology / ICM

Core idea: folder structure can act as agent architecture. Numbered folders become stages. Markdown files carry context. Outputs become handoffs. Human review happens by editing files.

RitmaOS implication: the filesystem itself can be the orchestration layer.

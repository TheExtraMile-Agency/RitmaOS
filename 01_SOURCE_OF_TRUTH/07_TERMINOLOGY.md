# RitmaOS — Terminology

## RitmaOS

A filesystem-based orchestration layer for AI-powered work.

## Workspace

The main folder that contains the business context, workflows, prompts, outputs, review, and memory.

## Context

The background information AI needs to do useful work.

## Persistent context

Information that should be available across many tasks or sessions.

Examples:

- Business profile
- Services
- Customers
- Voice/tone
- Rules
- Examples

## Prompt

The active instruction for a specific task.

## Workflow

A repeatable business process broken into stages.

## Stage

One step inside a workflow.

Examples:

- Intake
- Analysis
- Draft
- Review
- Delivery

## Router

The part of the system that decides which context, prompt, file, tool, workflow, or human checkpoint should be used next.

In the first version, the router may simply be a markdown file plus folder structure.

## Memory

Useful knowledge captured from previous work so it can improve future work.

## Review checkpoint

A human approval or quality-control step before work moves forward.

## Book layer

Raw prompts and outputs. Same for everyone. Easy to copy.

## Movie layer

Context-specific flows and automations.

## Video game layer

Bespoke systems that use data and feedback to improve over time.

## Orchestration

Coordinating AI, files, tools, workflows, and people so work moves reliably through a process.

## AI-readable filesystem

A folder structure organized so an AI agent can understand what to read, what to do, where to put outputs, and what rules to follow.

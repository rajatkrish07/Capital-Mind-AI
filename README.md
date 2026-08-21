# CapitalMind AI

> An AI-focused internal enterprise workspace for real-time LLM conversations, document-grounded RAG, tool calling, and a basic research agent.

CapitalMind AI is my flagship AI Engineering project.

The project is intentionally scoped to remain practical and understandable. The goal is to deeply understand and implement the core concepts behind modern AI applications while building a decent, usable product.

## Project Goal

CapitalMind AI will provide two primary experiences:

1. **AI Workspace** — real-time conversations with an LLM.
2. **Enterprise Knowledge** — upload documents and ask grounded questions using RAG.

Tool calling and a basic research agent will be added as focused extensions so that the project also covers agentic AI without becoming unnecessarily complex.

The primary focus is **AI Engineering**, not backend engineering.

---

## Product Specification

```text
                         CAPITALMIND AI
                    Internal AI Workspace
                              │
             ┌────────────────┴────────────────┐
             │                                 │
       AI CONVERSATIONS                  ENTERPRISE KNOWLEDGE
             │                                 │
       Real-time LLM Chat                 Document Upload
             │                                 │
       Conversation History              Text Extraction
             │                                 │
       Context Management                   Chunking
             │                                 │
       Streaming Responses                  Embeddings
             │                                 │
       Regenerate Response                 Vector Database
             │                                 │
             └──────────────┐        ┌─────────┘
                            │        │
                            ▼        ▼
                       RAG-POWERED CHAT
                            │
                       Query Retrieval
                            │
                       Relevant Context
                            │
                       Grounded Response
                            │
                       Source Citations
                            │
                            ▼
                       TOOL CALLING
                            │
                 ┌──────────┴──────────┐
                 │                     │
             Calculator         Knowledge Search
                 │                     │
                 └──────────┬──────────┘
                            ▼
                      BASIC AGENT
                            │
                  Research Assistant
                            │
              Decide → Tool → Observe
                            │
                            ▼
                       FINAL ANSWER
```

---

## Core AI Capabilities

### 1. LLM Applications

We begin by understanding the LLM application layer before introducing higher-level frameworks.

Topics include:

* LLM mental model
* Models and inference
* System, user and assistant messages
* Prompt construction
* Context windows
* Tokens
* Model parameters
* Structured outputs
* Streaming
* Error handling and retries

The first implementation will use the model provider API directly where that provides better understanding of the underlying mechanics.

---

### 2. Real-Time AI Chat

CapitalMind will provide a usable enterprise-style conversational workspace.

Core capabilities:

* New conversations
* Conversation history
* Context construction
* Real-time streaming
* Response regeneration
* Persistent conversations
* Markdown/code rendering
* Basic error and loading states

The backend functionality required for these operations will remain intentionally lightweight.

---

### 3. Retrieval-Augmented Generation

RAG is the major AI capability of CapitalMind.

#### Document ingestion

```text
Document
   ↓
Text Extraction
   ↓
Cleaning
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector Database
```

#### Query flow

```text
User Question
      ↓
Query Embedding
      ↓
Vector Retrieval
      ↓
Relevant Chunks
      ↓
Context Construction
      ↓
LLM
      ↓
Grounded Answer
      ↓
Source Citations
```

Topics we will understand and implement:

* Document ingestion
* Text extraction
* Chunking
* Chunk overlap
* Embeddings
* Vector representations
* Similarity search
* Vector databases
* Metadata
* Top-k retrieval
* Filtering
* Context construction
* Grounded generation
* Citations
* Retrieval evaluation
* Failure analysis

---

### 4. LangChain

LangChain will be introduced **after the underlying concepts are understood**, rather than being used as a black box from the beginning.

The intended progression is:

```text
Understand primitive
        ↓
Implement / experiment directly
        ↓
Understand the problem LangChain solves
        ↓
Use LangChain abstraction
        ↓
Evaluate whether the abstraction is actually useful
```

LangChain will primarily support areas such as:

* RAG components
* Document loaders
* Text splitters
* Embeddings
* Vector store integrations
* Retrievers
* Prompt templates
* Tool definitions
* Agent implementations

We will still understand what happens underneath these abstractions.

---

### 5. Tool Calling

CapitalMind will contain a small number of meaningful tools.

Initial tools:

* Calculator
* Knowledge-base search
* Optional document metadata lookup

The learning focus is:

```text
User Request
      ↓
LLM
      ↓
Tool Selection
      ↓
Tool Execution
      ↓
Tool Result
      ↓
LLM
      ↓
Final Response
```

Topics include:

* Tool schemas
* Function/tool calling
* Tool selection
* Tool execution
* Tool results
* Validation
* Tool errors
* LLM-to-tool-to-LLM flow

---

### 6. Basic Agent

CapitalMind will contain **one simple research-oriented agent**.

We first understand the underlying agent loop:

```text
User Request
     ↓
LLM / Agent
     ↓
Decide what to do
     ↓
Call Tool
     ↓
Observe Result
     ↓
Decide Again
     ↓
Final Response
```

The agent will demonstrate:

* Agent vs normal LLM application
* Tool selection
* Agent loop
* State/context
* Multi-step tool usage
* Simple research workflow

For the actual implementation, we will use **LangChain's agent capabilities** where appropriate.

**LangGraph will only be introduced if CapitalMind genuinely requires explicit stateful orchestration or more complex workflow control.**

We are intentionally avoiding:

* Multi-agent systems
* Agent swarms
* Complex autonomous workflows
* Building our own production agent runtime

The goal is to understand agents and use modern tooling effectively, not reinvent agent infrastructure.

---

## AI-Assisted Development

AI coding assistants are a deliberate part of the development process.

The goal is **not** to avoid AI-generated code. The goal is to use AI productively without relying on blind vibe coding.

### AI will primarily help with

* Backend boilerplate
* Users/conversations/messages
* API schemas
* Frontend scaffolding
* Repetitive implementation
* Test scaffolding
* Refactoring
* Documentation
* Debugging assistance
* Code review

### Human ownership remains with

* Product decisions
* AI architecture
* AI data flow
* RAG design
* Retrieval strategy
* Tool design
* Agent behavior
* Evaluation strategy
* Important security decisions
* Understanding generated code
* Reviewing and validating AI-generated implementation

The rule is:

> **Generated code can be accepted only when its behavior, purpose and tradeoffs are understood.**

This allows development to be faster while keeping the learning value high.

---

## Development Philosophy

CapitalMind is developed as a **learning-first flagship project**.

We do not want isolated toy projects for every concept.

Instead:

```text
Project Need
     ↓
Prerequisite Concept
     ↓
Deep Understanding
     ↓
Design
     ↓
Implementation
     ↓
Testing
     ↓
Failure Analysis
     ↓
Evaluation
     ↓
Improvement
```

Each major AI concept becomes a real part of CapitalMind.

We move one capability at a time and do not introduce unnecessary complexity before the previous capability is understood.

---

## Backend Scope

CapitalMind is **not another backend-learning project**.

Cogentra already serves that purpose.

Backend functionality such as:

* Users
* Conversations
* Messages
* Basic persistence
* CRUD APIs
* Basic authentication where necessary

will be kept lightweight.

Where appropriate, these parts can be generated with AI, reviewed carefully, tested, and integrated.

The majority of engineering effort remains focused on:

> **LLMs → RAG → Tool Calling → Agents → Evaluation**

---

## Frontend Scope

The frontend will provide a clean internal enterprise AI workspace.

Core UI capabilities:

* Conversation sidebar
* Real-time streaming chat
* New chat
* Regenerate response
* Markdown/code rendering
* Document upload
* Knowledge-base view
* Document processing status
* RAG source citations
* Basic tool/agent interactions
* Responsive layout

The frontend should be polished enough to make the product feel credible, but it will not become a separate frontend engineering project.

---

## Development Roadmap

```text
                    CAPITALMIND AI
                          │
                          ▼
                 FOUNDATION / SETUP
                          │
             ┌────────────┼────────────┐
             │            │            │
         AI Basics     Product      AI-assisted
         Prerequisites  Shell       Foundation
             │
             ▼
                    01. LLM FOUNDATION
             ┌──────────┼──────────┐
             │          │          │
          LLMs       Prompts    Streaming
             │          │          │
             └──────────┼──────────┘
                        ▼
                  02. AI CHAT
             ┌──────────┼──────────┐
             │          │          │
        Conversations  Context   Real-time UI
                        │
                        ▼
                  03. RAG PIPELINE
             ┌──────────┼──────────┐
             │          │          │
         Documents   Chunking   Embeddings
             │          │          │
             └──────────┼──────────┘
                        │
                  Vector Database
                        │
                        ▼
                  04. RAG IN CHAT
             ┌──────────┼──────────┐
             │          │          │
        Retrieval    Context   Grounded
                    Building     Answers
             │
             └──────────────┐
                            ▼
                    Sources / Citations
                            │
                            ▼
                  05. RAG QUALITY
             ┌──────────┼──────────┐
             │          │          │
        Retrieval    Chunking   Evaluation
          Quality    Experiments
             │
             └──────────────┐
                            ▼
                   06. TOOL CALLING
             ┌──────────┼──────────┐
             │          │          │
        Tool Schema  Calculator  KB Search
                            │
                            ▼
                     Tool Execution
                            │
                            ▼
                    07. BASIC AGENT
             ┌──────────┼──────────┐
             │          │          │
         Agent Loop  Tool Use   Research
                                      │
                                      ▼
                               LangChain Agent
                                      │
                         LangGraph only if needed
                                      │
                                      ▼
                  08. AI ENGINEERING QUALITY
             ┌──────────┼──────────┐
             │          │          │
         Evaluation   Cost      Latency
             │
             └──────────┬──────────┘
                        │
                 Reliability
                        │
                        ▼
                CAPITALMIND AI V1
```

---

## Evaluation

Evaluation is part of the development process rather than a final checkbox.

We will evaluate:

* Answer quality
* Retrieval quality
* Grounding
* Citation correctness
* Tool selection
* Agent behavior
* Failure cases
* Latency
* Token usage
* Cost
* Reliability

The objective is not merely:

> "The application works."

The objective is:

> **"We understand why it works, when it fails, and how to improve it."**

---

## V1 Scope

CapitalMind AI V1 will contain:

* Real-time LLM chat
* Conversation history
* Document upload
* Document processing
* Embeddings
* Vector database
* RAG-powered responses
* Source citations
* Basic tool calling
* One simple research agent
* LangChain integration where useful
* Basic AI evaluation
* A usable enterprise-style frontend

---

## Explicitly Out of Scope for V1

The project will not intentionally expand into:

* Multi-agent systems
* Agent swarms
* Complex autonomous workflows
* Microservices
* Kubernetes
* Advanced enterprise IAM/RBAC
* Large-scale distributed infrastructure
* Complex backend abstractions
* Excessive frontend features
* Multiple competing AI frameworks without a real reason

The project will remain focused on the AI engineering concepts that provide the highest learning and interview value.

---

## Final Objective

CapitalMind AI should demonstrate that I can:

* Build an LLM-powered application
* Integrate real-time model interaction
* Design and implement RAG
* Work with embeddings and vector databases
* Build grounded document Q&A
* Implement tool calling
* Understand and build a basic agent
* Use LangChain appropriately
* Understand when lower-level orchestration such as LangGraph is justified
* Evaluate AI system quality
* Debug AI-specific failures
* Make sensible AI architecture decisions
* Use AI coding assistants effectively without blind vibe coding

> **The objective is not to build the biggest AI application. The objective is to build a focused AI system deeply enough that I can explain, debug and defend every important part of it.**

---

## Status

**Project Status:** Initialization

CapitalMind AI will be developed incrementally, one AI capability at a time.

The project will prioritize **clarity, depth, hands-on implementation, evaluation, and practical AI engineering** over unnecessary product complexity.

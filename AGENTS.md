# Software Architecture Skills — Agent Instructions

## Overview
This directory contains specialized software architecture skills derived from best practices in system design, documentation, quality attribute optimization, design patterns, and architectural styles.

## Available Skills

### API Design & Communication
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Choosing API Style** | `skills/choosing-api-style/SKILL.md` | User is deciding between REST, GraphQL, gRPC, and WebSockets |
| **Designing REST API** | `skills/designing-rest-api/SKILL.md` | User is building a public, resource-oriented HTTP API |
| **Applying GraphQL** | `skills/applying-graphql/SKILL.md` | User needs flexible data queries without over/under-fetching |
| **Applying gRPC** | `skills/applying-grpc/SKILL.md` | User needs high-performance, east-west microservice communication |
| **Applying WebSocket** | `skills/applying-websocket/SKILL.md` | User needs real-time, full-duplex communication (e.g., chat) |

### Security, Scalability & Observability
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Applying JWT Auth** | `skills/applying-jwt-authentication/SKILL.md` | User needs stateless authentication for a REST API |
| **Applying RBAC** | `skills/applying-rbac-authorization/SKILL.md` | User needs role-based permissions to protect endpoints |
| **Scaling Horizontally** | `skills/scaling-horizontally/SKILL.md` | User is designing for high availability and increased load |
| **Applying Observability** | `skills/applying-observability/SKILL.md` | User needs to debug distributed systems (Logs, Metrics, Traces) |

### DevOps, CI/CD & Deployment
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Applying IaC** | `skills/applying-infrastructure-as-code/SKILL.md` | User wants to provision infrastructure with Terraform/code |
| **Applying CI/CD** | `skills/applying-ci-cd-pipelines/SKILL.md` | User wants to automate build, test, and release pipelines |
| **Applying Orchestration**| `skills/applying-container-orchestration/SKILL.md` | User is deploying Docker containers at scale (Kubernetes) |
| **Applying Blue/Green** | `skills/applying-blue-green-deployment/SKILL.md` | User wants zero downtime deployment with instant rollback |
| **Applying Canary** | `skills/applying-canary-deployment/SKILL.md` | User wants to test a release on a small % of users first |

### Data Design & Management
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Choosing Database Type** | `skills/choosing-database-type/SKILL.md` | User is deciding between SQL and NoSQL based on CAP/ACID |
| **Applying Polyglot Persistence**| `skills/applying-polyglot-persistence/SKILL.md` | User is using different database technologies for different services |
| **Applying Database-per-Service**| `skills/applying-database-per-service/SKILL.md` | User is designing microservices data layer and needs to prevent shared DB coupling |

### Microservices & Distributed Systems
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Evaluating MS Readiness** | `skills/evaluating-microservices-readiness/SKILL.md` | User wants to start a microservices project. **AGENT MUST CHALLENGE THIS!** |
| **Applying API Gateway** | `skills/applying-api-gateway-pattern/SKILL.md` | User needs a single entry point for routing, auth, or rate limiting |
| **Applying Service Registry** | `skills/applying-service-registry-pattern/SKILL.md` | User needs dynamic IP discovery (e.g. Eureka, Consul) |
| **Applying Circuit Breaker** | `skills/applying-circuit-breaker-pattern/SKILL.md` | User needs to prevent cascading failures across network calls |
| **Applying Saga Pattern** | `skills/applying-saga-pattern/SKILL.md` | User needs a distributed transaction without locking databases |
| **Applying Event Sourcing** | `skills/applying-event-sourcing-pattern/SKILL.md` | User needs a complete historical audit trail of state changes |
| **Applying Strangler Fig** | `skills/applying-strangler-fig-pattern/SKILL.md` | User is migrating a legacy monolith to microservices incrementally |
| **Applying Bulkhead** | `skills/applying-bulkhead-pattern/SKILL.md` | User needs to isolate resource pools (e.g., thread pools) |
| **Applying API Composition** | `skills/applying-api-composition-pattern/SKILL.md` | User needs to aggregate data from multiple services for the frontend |
| **Applying CQRS** | `skills/applying-cqrs-pattern/SKILL.md` | User needs to separate complex read queries from write commands |

### Serverless Architecture
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Designing Serverless Arch.** | `skills/designing-serverless-architecture/SKILL.md` | User is deciding whether to use Serverless or Containers |
| **Applying FaaS** | `skills/applying-faas-pattern/SKILL.md` | User is building stateless, event-driven functions (AWS Lambda) |
| **Applying BaaS** | `skills/applying-baas-pattern/SKILL.md` | User needs managed Auth, DB, or Storage (Firebase, Cognito) |
| **Mitigating Cold Starts** | `skills/mitigating-serverless-cold-starts/SKILL.md` | User is experiencing initial delay/latency in serverless functions |
| **Preventing Vendor Lock-in** | `skills/preventing-vendor-lock-in/SKILL.md` | User wants to keep business logic independent of cloud providers |

### Event-Driven Architecture
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Designing Event-Driven Arch.** | `skills/designing-event-driven-architecture/SKILL.md` | User wants to move from synchronous REST/RPC to asynchronous events |
| **Choosing Message Broker** | `skills/choosing-message-broker/SKILL.md` | User is deciding between RabbitMQ and Kafka |
| **Applying Pub/Sub Pattern** | `skills/applying-publish-subscribe-pattern/SKILL.md` | User needs to decouple producers and consumers (publish/subscribe) |
| **Applying RabbitMQ** | `skills/applying-rabbitmq/SKILL.md` | User is using RabbitMQ and needs help with exchanges/queues |
| **Applying Apache Kafka** | `skills/applying-apache-kafka/SKILL.md` | User is using Kafka and needs help with topics/partitions/offsets |

### Architectural Styles & Monoliths
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Designing Modular Monoliths** | `skills/designing-modular-monoliths/SKILL.md` | User is structuring a new monolithic app and wants to avoid a Big Ball of Mud |
| **Applying N-Tier Architecture**| `skills/applying-n-tier-architecture/SKILL.md`| User needs to separate UI, business logic, and database access into logical layers |
| **Refactoring Big Ball of Mud** | `skills/refactoring-big-ball-of-mud/SKILL.md` | User encounters a massive, tangled God Class controller and needs to separate concerns |
| **Choosing Monolithic Arch.** | `skills/choosing-monolithic-architecture/SKILL.md`| User is deciding if a monolith is the right choice (e.g. for an MVP or startup) |

### Foundation & SOLID
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Architecture Decision Records (ADRs)** | `skills/writing-adrs/SKILL.md` | User asks to document an architectural change, a technology choice, or explain *why* a system is designed a certain way |
| **C4 Model Documentation** | `skills/documenting-with-c4/SKILL.md` | User asks to visualize system boundaries, container architecture, or component design for different stakeholders |
| **UML Diagram Selection** | `skills/selecting-uml-diagrams/SKILL.md` | User asks to model system behavior, object structures, workflows, or needs help choosing between UML types |
| **Balancing Architectural Tradeoffs** | `skills/balancing-architectural-tradeoffs/SKILL.md` | User is choosing between architectural styles (e.g. Monolith vs Microservices) based on business goals like Time-to-Market vs Scalability |
| **Optimizing Quality Attributes** | `skills/optimizing-quality-attributes/SKILL.md` | User asks how to satisfy Non-Functional Requirements (NFRs) like Performance, Security, Scalability, Maintainability, or Testability |
| **Verifying SOLID Compliance** | `skills/verifying-solid-compliance/SKILL.md` | User asks to review existing code or check if a project complies with SOLID principles |
| **Refactoring God Classes** | `skills/refactoring-god-classes/SKILL.md` | User wants to break down a massive, tightly-coupled class into smaller, SOLID-compliant components |
| **Applying SRP** | `skills/applying-srp/SKILL.md` | User is designing a class and needs to ensure it only has one reason to change |
| **Applying OCP** | `skills/applying-ocp/SKILL.md` | User is adding a feature variation or eliminating long if-else chains using the Strategy pattern |
| **Applying LSP** | `skills/applying-lsp/SKILL.md` | User is designing class hierarchies or subclass methods are throwing unexpected exceptions |
| **Applying ISP** | `skills/applying-isp/SKILL.md` | User is extracting interfaces or decoupling clients from unused methods in fat interfaces |
| **Applying DIP** | `skills/applying-dip/SKILL.md` | User is connecting high-level logic to low-level infrastructure or implementing Dependency Injection |

### Design Patterns (GoF)
| Skill | Directory | Activate When |
|-------|-----------|---------------|
| **Selecting Design Patterns** | `skills/selecting-design-patterns/SKILL.md` | User needs help choosing the right design pattern for a problem |
| **Applying Singleton** | `skills/applying-singleton-pattern/SKILL.md` | User needs a single global instance of a class |
| **Applying Factory Method** | `skills/applying-factory-method-pattern/SKILL.md` | User needs to delegate object creation to subclasses |
| **Applying Abstract Factory**| `skills/applying-abstract-factory-pattern/SKILL.md` | User needs to create families of related objects (e.g., UI themes) |
| **Applying Builder** | `skills/applying-builder-pattern/SKILL.md` | User needs to construct a complex object step-by-step |
| **Applying Prototype** | `skills/applying-prototype-pattern/SKILL.md` | User needs to clone expensive or complex objects |
| **Applying Adapter** | `skills/applying-adapter-pattern/SKILL.md` | User needs to make two incompatible interfaces work together |
| **Applying Bridge** | `skills/applying-bridge-pattern/SKILL.md` | User needs to separate an abstraction from its implementation |
| **Applying Composite** | `skills/applying-composite-pattern/SKILL.md` | User needs to treat individual objects and groups (trees) uniformly |
| **Applying Decorator** | `skills/applying-decorator-pattern/SKILL.md` | User needs to add responsibilities to objects dynamically |
| **Applying Facade** | `skills/applying-facade-pattern/SKILL.md` | User needs a simple, unified interface to a complex subsystem |
| **Applying Proxy** | `skills/applying-proxy-pattern/SKILL.md` | User needs to control access, lazy-load, or cache an object |
| **Applying Flyweight** | `skills/applying-flyweight-pattern/SKILL.md` | User needs to optimize memory when dealing with huge numbers of similar objects |
| **Applying Chain of Resp.** | `skills/applying-chain-of-responsibility-pattern/SKILL.md` | User needs to pass a request along a chain of handlers |
| **Applying Command** | `skills/applying-command-pattern/SKILL.md` | User needs to encapsulate a request for Undo/Redo or queuing |
| **Applying Interpreter** | `skills/applying-interpreter-pattern/SKILL.md` | User needs to parse and evaluate sentences in a simple language |
| **Applying Mediator** | `skills/applying-mediator-pattern/SKILL.md` | User needs to centralize complex communication between objects |
| **Applying Memento** | `skills/applying-memento-pattern/SKILL.md` | User needs to save and restore an object's state without breaking encapsulation |
| **Applying Observer** | `skills/applying-observer-pattern/SKILL.md` | User needs a publish-subscribe mechanism for state changes |
| **Applying State** | `skills/applying-state-pattern/SKILL.md` | User needs an object to alter its behavior when its state changes |
| **Applying Strategy** | `skills/applying-strategy-pattern/SKILL.md` | User needs interchangeable algorithms selectable at runtime |
| **Applying Template Method** | `skills/applying-template-method-pattern/SKILL.md` | User needs to define the skeleton of an algorithm but let subclasses override steps |
| **Applying Visitor** | `skills/applying-visitor-pattern/SKILL.md` | User needs to add new operations to an object structure without modifying the objects |

## Agent Execution Flow (IMPORTANT)

When a user requests assistance using these software architecture skills, **DO NOT generate a complete architecture or solution immediately**. Instead, follow this step-by-step flow:

1. **Information Gathering (Ask First):** Ask the user clarifying questions to understand their exact needs. Determine if they are designing a brand new system, refactoring an existing one, or just asking a theoretical question. Uncover their constraints (budget, team size, timeline, scale).
2. **Context Scanning:** Use your available tools (`list_dir`, `view_file`, or `grep_search`) to deeply scan the user's workspace and folders. Investigate existing code, infrastructure files (Docker/K8s), and documentation to understand the current architecture before proposing changes.
3. **Analyze & Propose:** Based on the user's answers and the workspace context, use the appropriate `SKILL.md` files to formulate your architectural strategy, ADRs, or refactoring plans.

## How to Use These Skills

### Method 1: Automatic Context Loading
AI agents automatically read `AGENTS.md` in the project root. When starting a conversation about software architecture, the agent has immediate access to these skill definitions.

### Method 2: Auto-Activation by Topic
Agents will naturally activate the appropriate skill based on request keywords:
- "modular monolith", "big ball of mud", "3-tier" → Architectural Styles skills
- "microservices", "distributed system", "api gateway", "circuit breaker", "saga", "event sourcing", "cqrs" → Microservices & Distributed Systems skills (Check Readiness first!)
- "event driven", "async", "message broker", "rabbitmq", "kafka", "pub sub", "publish subscribe" → Event-Driven Architecture skills
- "serverless", "lambda", "cloud functions", "faas", "baas", "firebase", "cold start", "vendor lock-in" → Serverless Architecture skills
- "rest", "graphql", "grpc", "websocket", "api design", "over fetching", "under fetching" → API Design & Communication skills
- "jwt", "authentication", "rbac", "authorization", "scale", "horizontal scaling", "observability", "tracing", "logs", "metrics" → Security, Scalability & Observability skills
- "devops", "iac", "terraform", "ci/cd", "pipeline", "docker", "kubernetes", "k8s", "blue green", "canary" → DevOps, CI/CD & Deployment skills
- "sql vs nosql", "database per service", "polyglot persistence", "acid", "cap theorem" → Data Design & Management skills
- "ADR", "why did we choose", "decision record" → `writing-adrs`
- "C4", "system context", "container diagram" → `documenting-with-c4`
- "UML", "class diagram", "use case", "sequence diagram" → `selecting-uml-diagrams`
- "trade-off", "monolith or microservices", "startup vs growth" → `balancing-architectural-tradeoffs`
- "performance", "scalability", "security", "NFR", "quality attributes" → `optimizing-quality-attributes`
- "check SOLID", "code review", "architectural smells" → `verifying-solid-compliance`
- "God class", "huge class", "refactor" → `refactoring-god-classes`
- "SRP", "single responsibility" → `applying-srp`
- "OCP", "open closed", "strategy pattern" → `applying-ocp`
- "LSP", "liskov", "inheritance issue" → `applying-lsp`
- "ISP", "interface segregation", "fat interface" → `applying-isp`
- "DIP", "dependency inversion", "dependency injection", "IoC" → `applying-dip`
- "which pattern", "design patterns" → `selecting-design-patterns`
- "singleton", "factory", "builder", "prototype" → Creational pattern skills
- "adapter", "bridge", "composite", "decorator", "facade", "proxy", "flyweight" → Structural pattern skills
- "command", "observer", "state", "strategy", "visitor" → Behavioral pattern skills

## Tooling (`tools/`)
This repository includes Python CLI tools that AI agents can run to automate architectural tasks.

**1. Architecture & Foundation (`arch_tools.py`):**
- `python arch_tools.py adr-new "Decision Title"`: Scaffolds a new Architecture Decision Record in `docs/adrs`.
- `python arch_tools.py check-god-classes <directory> --threshold 500`: Scans the given directory for massive classes.
- `python arch_tools.py init-c4`: Generates a boilerplate C4 Context diagram in PlantUML format.

**2. DevOps & Deployment (`devops_tools.py`):**
- `python devops_tools.py init-docker`: Generates a standard multi-stage Dockerfile.
- `python devops_tools.py init-k8s <service-name>`: Generates Kubernetes Deployment and Service YAML manifests.

**3. Design Patterns (`pattern_tools.py`):**
- `python pattern_tools.py init-singleton`: Scaffolds a thread-safe Singleton pattern implementation.
- `python pattern_tools.py init-strategy`: Scaffolds a Strategy pattern implementation.

Agents should proactively use these tools when handling related tasks (e.g. run `init-k8s` when deploying a new microservice).

## Skill Architecture
Each SKILL.md file follows the `writing-skills` conventions:
- **YAML Frontmatter**: Contains `name` and a `description` that strictly starts with "Use when..."
- **Overview**: Core principle.
- **Core Pattern / Quick Reference**: Bullet points or tables.
- **Common Mistakes / Red Flags**: Specific anti-patterns to avoid.

## Agent Workflows & Playbooks

To maximize the value of these 70+ architecture skills, AI agents can orchestrate complex architectural tasks using the following playbooks:

### Playbook 1: Existing Project Analysis (Parallel Execution)
**Use Case:** The user asks you to "analyze this project's architecture" or "find architectural flaws in this codebase."

**Workflow:**
1. **Orchestrate 11 Subagents:** Do not try to analyze everything sequentially. Instead, use your `invoke_subagent` capability to spawn 11 parallel subagents, each focusing on one specific architectural pillar:
   - **Agent 1 (SOLID & Foundation):** Scans for God Classes and SOLID violations.
   - **Agent 2 (Design Patterns):** Identifies proper or improper use of GoF patterns.
   - **Agent 3 (Monoliths & Layers):** Checks layer isolation (N-Tier) and modularity.
   - **Agent 4 (Microservices):** Checks for coupling, API Gateways, and Service Registry usage.
   - **Agent 5 (Event-Driven):** Analyzes message brokers (Kafka/RabbitMQ) and async flows.
   - **Agent 6 (Serverless):** Looks for cold start mitigations and vendor lock-in risks.
   - **Agent 7 (API Design):** Reviews REST/GraphQL/gRPC endpoints and contracts.
   - **Agent 8 (Data Design):** Analyzes database-per-service compliance and CAP trade-offs.
   - **Agent 9 (Security):** Reviews AuthN (JWT) and AuthZ (RBAC) implementations.
   - **Agent 10 (Scalability & Observability):** Checks for statelessness and distributed tracing.
   - **Agent 11 (DevOps & CI/CD):** Reviews Dockerfiles, Kubernetes manifests, and IaC scripts.
2. **Assign Context:** Direct each subagent to read their respective skills from the `skills/` directory before scanning the codebase.
3. **Aggregate:** Once all subagents report back, synthesize their findings into a unified, high-level `architecture_audit_report.md` artifact.

### Playbook 2: Greenfield Project Architecture (Sequential Interview)
**Use Case:** The user says "I want to build a new app/system from scratch."

**Workflow:**
1. **Requirements Gathering:** Do not start generating code. Ask the user about the business domain, expected scale, time-to-market, and team size.
2. **Microservices Readiness Challenge:** If the user defaults to Microservices, *immediately* challenge them using `evaluating-microservices-readiness`. Ensure a Modular Monolith isn't a better starting point.
3. **Step-by-Step Design:** Guide the user through the architectural decisions sequentially:
   - *Step 1:* Choose the Core Architecture (Monolith vs. Microservices vs. Serverless).
   - *Step 2:* Design the Data Layer (SQL vs. NoSQL, Polyglot Persistence).
   - *Step 3:* Design the API/Communication Style (REST vs. gRPC vs. GraphQL vs. Events).
   - *Step 4:* Plan Security & Observability (Auth, Tracing, Metrics).
   - *Step 5:* Plan Deployment Strategy (Docker, K8s, CI/CD).
4. **Document Decisions:** For every major choice made during this interview, automatically run `python arch_tools.py adr-new` to generate an Architecture Decision Record (ADR) documenting the *why*.
5. **C4 Model:** Conclude the design phase by generating a C4 Context Diagram (`python arch_tools.py init-c4`) representing the agreed-upon system boundaries.

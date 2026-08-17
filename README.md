# Software Architecture Skills for AI Agents

> **Transform your LLM coding and design assistant into an expert Software Architect.**

A production-ready suite of specialized AI agent skills encoding software architecture theory, trade-off analysis, documentation patterns, SOLID principles, and Gang of Four (GoF) Design Patterns. 

## 🌟 Key Features
- 🏗️ **Architectural Trade-offs**: Startup vs Growth phase modeling, Conway's Law.
- 📝 **Documentation Mastery**: C4 Model (Context to Code) and UML selection heuristics.
- ⚙️ **Quality Attributes**: Optimization tactics for Performance, Security, Scalability, Maintainability, and Testability.
- 📜 **Decision Records**: Bulletproof templates for Architecture Decision Records (ADRs).
- 🧩 **SOLID Principles**: Comprehensive checkers and applying strategies for SRP, OCP, LSP, ISP, and DIP.
- 🎨 **Design Patterns**: 23 ready-to-use skills covering all Creational, Structural, and Behavioral patterns.
- 🚀 **Microservices**: Deep guidance on API Gateways, Sagas, CQRS, and Circuit Breakers (with strict readiness checks).

## 📚 Included Skills

### API Design & Communication
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Choosing API Style** | `skills/choosing-api-style/SKILL.md` | Comparing REST, GraphQL, gRPC, and WebSockets. |
| **Designing REST API** | `skills/designing-rest-api/SKILL.md` | Building public, HTTP resource-oriented APIs. |
| **Applying GraphQL** | `skills/applying-graphql/SKILL.md` | Preventing over/under-fetching with typed queries. |
| **Applying gRPC** | `skills/applying-grpc/SKILL.md` | High-performance, East-West internal microservices. |
| **Applying WebSocket** | `skills/applying-websocket/SKILL.md` | Real-time, full-duplex communication with clients. |

### Security, Scalability & Observability
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Applying JWT Auth** | `skills/applying-jwt-authentication/SKILL.md` | Stateless authentication (AuthN) in APIs. |
| **Applying RBAC** | `skills/applying-rbac-authorization/SKILL.md` | Role-based authorization (AuthZ) for endpoints. |
| **Scaling Horizontally** | `skills/scaling-horizontally/SKILL.md` | Managing high traffic with Load Balancers and stateless nodes. |
| **Applying Observability** | `skills/applying-observability/SKILL.md` | Tracing issues via Logs, Metrics, and Distributed Traces. |

### DevOps, CI/CD & Deployment
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Applying IaC** | `skills/applying-infrastructure-as-code/SKILL.md` | Provisioning cloud resources with Terraform/CloudFormation. |
| **Applying CI/CD** | `skills/applying-ci-cd-pipelines/SKILL.md` | Automating code build, test, and release (GitHub Actions). |
| **Applying Orchestration**| `skills/applying-container-orchestration/SKILL.md` | Managing Docker containers in production with Kubernetes. |
| **Applying Blue/Green** | `skills/applying-blue-green-deployment/SKILL.md` | Zero-downtime releases with instant rollback safety. |
| **Applying Canary** | `skills/applying-canary-deployment/SKILL.md` | Risk-managed rollouts targeting a small percentage of users. |

### Data Design & Management
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Choosing Database Type** | `skills/choosing-database-type/SKILL.md` | Comparing SQL vs NoSQL, CAP Theorem, ACID vs BASE. |
| **Applying Polyglot Persistence**| `skills/applying-polyglot-persistence/SKILL.md` | Using different DBs (e.g. Postgres + Redis + Neo4j) together. |
| **Applying Database-per-Service**| `skills/applying-database-per-service/SKILL.md` | Decoupling microservices data layers to prevent shared DBs. |

### Microservices & Distributed Systems
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Evaluating MS Readiness** | `skills/evaluating-microservices-readiness/SKILL.md` | Preventing premature microservice adoption. |
| **Applying API Gateway** | `skills/applying-api-gateway-pattern/SKILL.md` | Routing, authentication, and aggregation for clients. |
| **Applying Service Registry** | `skills/applying-service-registry-pattern/SKILL.md` | Dynamic IP discovery in cloud environments. |
| **Applying Circuit Breaker** | `skills/applying-circuit-breaker-pattern/SKILL.md` | Preventing cascading failures across services. |
| **Applying Saga Pattern** | `skills/applying-saga-pattern/SKILL.md` | Managing distributed transactions. |
| **Applying Event Sourcing** | `skills/applying-event-sourcing-pattern/SKILL.md` | Creating immutable audit trails of state changes. |
| **Applying Strangler Fig** | `skills/applying-strangler-fig-pattern/SKILL.md` | Safely migrating from monoliths to microservices. |
| **Applying Bulkhead** | `skills/applying-bulkhead-pattern/SKILL.md` | Isolating resource pools to contain failures. |
| **Applying API Composition** | `skills/applying-api-composition-pattern/SKILL.md` | Aggregating data from multiple services. |
| **Applying CQRS** | `skills/applying-cqrs-pattern/SKILL.md` | Separating complex read/write operations. |

### Serverless Architecture
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Designing Serverless Arch.** | `skills/designing-serverless-architecture/SKILL.md` | Deciding if Serverless fits the use case. |
| **Applying FaaS** | `skills/applying-faas-pattern/SKILL.md` | Building stateless, event-driven functions (Lambda). |
| **Applying BaaS** | `skills/applying-baas-pattern/SKILL.md` | Using managed Auth, DB, and Storage services. |
| **Mitigating Cold Starts** | `skills/mitigating-serverless-cold-starts/SKILL.md` | Handling latency issues in FaaS platforms. |
| **Preventing Vendor Lock-in** | `skills/preventing-vendor-lock-in/SKILL.md` | Keeping business logic independent of AWS/GCP SDKs. |

### Event-Driven Architecture
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Designing Event-Driven Arch.** | `skills/designing-event-driven-architecture/SKILL.md` | Moving from synchronous to asynchronous design. |
| **Choosing Message Broker** | `skills/choosing-message-broker/SKILL.md` | Deciding between RabbitMQ and Kafka. |
| **Applying Pub/Sub Pattern** | `skills/applying-publish-subscribe-pattern/SKILL.md` | Decoupling producers and consumers. |
| **Applying RabbitMQ** | `skills/applying-rabbitmq/SKILL.md` | Using RabbitMQ exchanges and task queues. |
| **Applying Apache Kafka** | `skills/applying-apache-kafka/SKILL.md` | Using Kafka for high throughput event streaming. |

### Architectural Styles & Monoliths
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Designing Modular Monoliths** | `skills/designing-modular-monoliths/SKILL.md` | Structuring a new monolithic app without it becoming a Big Ball of Mud. |
| **Applying N-Tier Architecture**| `skills/applying-n-tier-architecture/SKILL.md`| Separating UI, business logic, and database access into logical layers. |
| **Refactoring Big Ball of Mud** | `skills/refactoring-big-ball-of-mud/SKILL.md` | Breaking down tangled God Classes into testable N-Tier components. |
| **Choosing Monolithic Arch.** | `skills/choosing-monolithic-architecture/SKILL.md`| Deciding when a monolith is the right choice for an MVP or startup. |

### Foundation & SOLID
| Skill | Directory | Primary Use Cases |
|-------|-----------|-------------------|
| **Architecture Decision Records** | `skills/writing-adrs/SKILL.md` | Documenting structural changes, database choices, or technology shifts. |
| **C4 Model Documentation** | `skills/documenting-with-c4/SKILL.md` | Visualizing systems across 4 levels (Context, Container, Component, Code). |
| **UML Diagram Selection** | `skills/selecting-uml-diagrams/SKILL.md` | Structuring object relations (Class) or behavior (Sequence, Activity). |
| **Architectural Tradeoffs** | `skills/balancing-architectural-tradeoffs/SKILL.md` | Monolith vs Microservices decisions based on time-to-market and team size. |
| **Optimizing Quality Attributes**| `skills/optimizing-quality-attributes/SKILL.md`| Implementing Caching, API Gateways, Horizontal Pod Autoscaling, etc. |
| **Verifying SOLID Compliance** | `skills/verifying-solid-compliance/SKILL.md` | Code reviews for existing projects without rewriting from scratch. |
| **Refactoring God Classes** | `skills/refactoring-god-classes/SKILL.md` | Breaking down massive classes into manageable pieces. |
| **Applying SRP** | `skills/applying-srp/SKILL.md` | Enforcing Single Responsibility Principle. |
| **Applying OCP** | `skills/applying-ocp/SKILL.md` | Eliminating if-else chains using the Strategy Pattern. |
| **Applying LSP** | `skills/applying-lsp/SKILL.md` | Ensuring subclasses respect base class contracts. |
| **Applying ISP** | `skills/applying-isp/SKILL.md` | Breaking down fat interfaces into role-specific ones. |
| **Applying DIP** | `skills/applying-dip/SKILL.md` | Implementing Dependency Injection via Constructor Injection. |

### Design Patterns
All 23 GoF Design Patterns are included, categorized as follows:
- **Creational**: Singleton, Factory Method, Abstract Factory, Builder, Prototype
- **Structural**: Adapter, Bridge, Composite, Decorator, Facade, Proxy, Flyweight
- **Behavioral**: Chain of Responsibility, Command, Interpreter, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor
- **Master Skill**: `selecting-design-patterns/SKILL.md`

## 🤖 Built-in CLI Tools
The repository includes several utility scripts in the `tools/` directory designed for AI agents to automate tasks:
```bash
# --- arch_tools.py (Architecture & Foundation) ---
# Scan a directory for potential God Classes (> 500 lines)
python tools/arch_tools.py check-god-classes ./src --threshold 500

# Create a new Architecture Decision Record (ADR)
python tools/arch_tools.py adr-new "Migrate to PostgreSQL"

# Generate a C4 Context PlantUML template
python tools/arch_tools.py init-c4

# --- devops_tools.py (DevOps & CI/CD) ---
# Generate a multi-stage Dockerfile
python tools/devops_tools.py init-docker

# Generate Kubernetes Deployment and Service manifests
python tools/devops_tools.py init-k8s order-service --replicas 3

# --- pattern_tools.py (Design Patterns) ---
# Scaffold a thread-safe Singleton pattern in Python
python tools/pattern_tools.py init-singleton

# Scaffold a Strategy pattern in Python
python tools/pattern_tools.py init-strategy
```

## 🛠️ Architecture

```text
software-architecture-skills/
├── AGENTS.md                                # Universal AI agent instructions & skill router
├── README.md                                # Project documentation
├── tools/                                   # Automation scripts (arch, devops, patterns)
│   ├── arch_tools.py
│   ├── devops_tools.py
│   └── pattern_tools.py
└── skills/
    ├── writing-adrs/
    ├── documenting-with-c4/
    ├── selecting-uml-diagrams/
    ├── balancing-architectural-tradeoffs/
    ├── optimizing-quality-attributes/
    ├── verifying-solid-compliance/
    ├── refactoring-god-classes/
    ├── applying-srp/
    ├── applying-ocp/
    ├── applying-lsp/
    ├── applying-isp/
    ├── applying-dip/
    ├── selecting-design-patterns/
    ├── applying-singleton-pattern/
    ├── applying-factory-method-pattern/
    ├── ... (20 more pattern skills)
```

## 💡 Example Prompts for AI Agents

You can trigger the AI agent to utilize this skill library by using the following example prompts:

**1. Codebase Audit & Refactoring:**
> *"Scan this repository for any God Classes. If you find one, show me how to refactor it using SOLID principles and generate a class diagram of the proposed solution."*

**2. Greenfield Project Design (Interactive Interview):**
> *"I want to build a new e-commerce application from scratch. Please act as a software architect, interview me about my requirements, challenge my assumptions (especially if I ask for microservices upfront), and guide me through choosing the core architecture, data layer, and API design."*

**3. Applying Design Patterns & Tooling:**
> *"I have a scenario where I have multiple payment methods (Credit Card, PayPal, Crypto). Help me choose the right GoF design pattern for this, and use your built-in pattern tools to scaffold the python code."*

**4. DevOps & Cloud Native Architecture:**
> *"We are migrating our monolith to Kubernetes. Explain the Blue/Green deployment strategy and use your devops tools to generate a multi-stage Dockerfile and a K8s deployment manifest for our order service."*

**5. System Documentation (ADR & C4):**
> *"We've decided to switch from REST to gRPC for our internal microservices communication to reduce latency. Please generate an Architecture Decision Record (ADR) documenting this choice using your tooling."*

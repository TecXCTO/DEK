# DEK
Domain Expert Knowledge

```

Domain expert AI follows a modular, retrieval-first structure. This organization separates the "brain" (the model) from the "memory" (domain data) and the "instructions" (expert logic).
Core Repository Structure
A production-grade domain AI repository is typically organized into these six functional blocks:
text
├── .github/skills/           # 1. AI-Specific Logic
│   └── domain-expert/        # Custom skill definitions for IDEs (e.g., Copilot)
│       └── SKILL.md          # Step-by-step reasoning instructions for the AI
├── data/                     # 2. Domain Knowledge Foundation
│   ├── raw/                  # Unprocessed docs (PDFs, manuals, industry reports)
│   ├── processed/            # Cleaned, chunked Markdown/JSON files
│   └── ontology/             # Knowledge graphs and domain taxonomies
├── agents/                   # 3. Agentic Execution Layer
│   ├── planner.py            # Logic for multi-step reasoning and research tasks
│   ├── tools/                # Specialized tools (SQL executors, web searchers)
│   └── agents.md             # High-level boundaries and styles for agents
├── models/                   # 4. Specialization & Retraining
│   ├── fine-tuning/          # Scripts for LoRA/QLoRA domain adaptation
│   └── prompts/              # System prompt templates for specialized roles
├── evaluation/               # 5. Expert-in-the-Loop Validation
│   ├── test-sets/            # Industry-specific edge cases curated by experts
│   └── metrics/              # RAGAS or custom accuracy measurement scripts
├── infra/                    # 6. Deployment & Governance
│   ├── vector-db/            # Config for databases like Pinecone or Neo4j
│   └── mcp-server/           # Model Context Protocol (MCP) server definitions
└── README.md                 # Project vision and architecture decision logs
Use code with caution.

Key Architectural Components for 2026
Knowledge Engineering Pipeline: Automated tasks that recursively traverse the data/ folder, convert documents to Markdown, and perform SHA-based duplicate checking before indexing into a vector database.
Agent Skills (.github/skills/): A new standard in 2026 for defining "custom skills" directly in the repository. These use SKILL.md files to tell the AI exactly how to handle specialized industry tasks within developer workflows.
Agentic RAG Flow: Instead of a simple search, the code in agents/ allows the AI to strategically decide how to explore its knowledge base, use tools, or even perform Speculative RAG (using a fast specialist model to draft and a generalist model to verify).
Model Context Protocol (MCP): The repository should include an MCP server to provide a secure, standardized way for the AI to interact with external enterprise data (like medical records or financial APIs).
Boundary Enforcement: Use agents.md to define strict rules for the AI, such as "never touch production configs" or "always use React 19 standards," ensuring it acts as a true expert in the specified stack. 

```

# AutoRefactorOps_Mark2
A Formally Constrained Multi-Agent Framework for Semantics-Preserving Code Refactoring

AutoRefactorOps/
│
├── .git/                      # Automatically created by GitHub Desktop
├── .gitignore                 # Tells Git what NOT to track (e.g., __pycache__, .env, venv/)
├── README.md                  # Project overview, setup instructions, and architecture
├── requirements.txt           # Python dependencies (crewai, radon, gitpython, pytest, etc.)
├── .env.example               # Template for environment variables (API keys, settings)
│
├── src/                       # Main source code directory
│   ├── __init__.py
│   ├── main.py                # Entry point: Orchestrates the CrewAI/AutoGen pipeline
│   │
│   ├── config/                # Configuration files
│   │   ├── __init__.py
│   │   ├── settings.py        # Loads thresholds (like your τ for strict tolerance)
│   │   ├── agents.yaml        # CrewAI: Agent definitions, roles, and backstories
│   │   └── tasks.yaml         # CrewAI: Task descriptions and expected outputs
│   │
│   ├── agents/                # Agent definitions and setups
│   │   ├── __init__.py
│   │   ├── discovery.py       # Code Discovery Agent
│   │   ├── refactor.py        # Refactoring Generator Agent
│   │   ├── verification.py    # Adversarial Verification Agent
│   │   └── rollback.py        # Rollback/Merge Agent
│   │
│   ├── mcp_tools/             # The Model Context Protocol Governance ecosystem
│   │   ├── __init__.py
│   │   ├── ast_validator.py   # Cross-verification of pre/post ASTs
│   │   ├── cyclomatic.py      # Radon/SonarQube wrappers for complexity scoring
│   │   ├── test_runner.py     # Safe execution of parameterized unit tests
│   │   └── git_manager.py     # strict Git operations (stash, commit, branch)
│   │
│   └── core/                  # Core framework logic
│       ├── __init__.py
│       ├── state.py           # Manages shared state between agents (AST pre-state, rollback hash)
│       └── metrics.py         # Calculates ΔD, SER, SDR, and ARR metrics
│
├── evaluation/                # Benchmarking and experimental study data (Section 5)
│   ├── __init__.py
│   ├── synthetic_repo/        # The custom dummy repo seeded with "code smells" and unit tests
│   │   ├── target_smelly.py
│   │   └── test_target.py
│   └── run_eval.py            # Script to run the framework against datasets/synthetic repo
│
└── tests/                     # Unit tests for YOUR framework (testing the agents/tools)
    ├── __init__.py
    ├── test_mcp_tools.py
    └── test_ast_validator.py
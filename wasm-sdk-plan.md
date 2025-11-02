# WASM-SDK Repository Structure Plan

## Overview
Creating 5 separate GitHub repositories for the WASM-SDK platform:

### 1. WASM-SDK-CORE (Rust)
**Description**: WASI Preview 2 compatible runtime for Rust community
**Tech Stack**: 
- Rust with Cargo
- Wasmtime integration
- Component Model support
**Structure**:
```
wasm-sdk-core/
├── Cargo.toml
├── Cargo.lock
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   ├── lib.rs
│   └── runtime.rs
├── examples/
│   └── basic_usage.rs
└── tests/
    └── integration_test.rs
```
**Tests**: cargo test (unit + integration)

### 2. WASM-SDK-CORE-JS (JavaScript)
**Description**: Boa-based JavaScript engine for JavaScript community
**Tech Stack**:
- Node.js + npm/pnpm
- Boa engine (Rust-based)
- Jest for testing
**Structure**:
```
wasm-sdk-core-js/
├── package.json
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   └── index.js
├── examples/
│   └── basic-usage.js
└── test/
    └── runtime.test.js
```
**Tests**: Jest

### 3. WASM-SDK-CORE-TS (TypeScript)
**Description**: Boa-based JavaScript engine for TypeScript community
**Tech Stack**:
- TypeScript + Yarn
- Boa engine (Rust-based)
- Jest + ts-jest for testing
**Structure**:
```
wasm-sdk-core-ts/
├── package.json
├── tsconfig.json
├── yarn.lock
├── README.md
├── LICENSE
├── .gitignore
├── .yarn/
├── src/
│   └── index.ts
├── examples/
│   └── basic-usage.ts
└── test/
    └── runtime.test.ts
```
**Tests**: Jest with TypeScript support

### 4. WASM-SDK-CORE-RB (Ruby)
**Description**: Artichoke + Boa for Ruby community
**Tech Stack**:
- Ruby 3.3.6
- Bundler for gem management
- RSpec + Cucumber for testing
**Structure**:
```
wasm-sdk-core-rb/
├── wasm_sdk_core.gemspec
├── Gemfile
├── Gemfile.lock
├── README.md
├── LICENSE
├── .gitignore
├── lib/
│   ├── wasm_sdk_core.rb
│   └── wasm_sdk_core/
│       └── runtime.rb
├── examples/
│   └── basic_usage.rb
├── spec/
│   ├── spec_helper.rb
│   └── runtime_spec.rb
└── features/
    ├── support/
    │   └── env.rb
    └── runtime.feature
```
**Tests**: RSpec + Cucumber

### 5. WASM-SDK-CORE-PY (Python)
**Description**: pyo3 + Boa for Python community
**Tech Stack**:
- Python 3.11+
- pyo3 for Rust-Python bindings
- pytest for testing
**Structure**:
```
wasm-sdk-core-py/
├── setup.py
├── pyproject.toml
├── Cargo.toml
├── README.md
├── LICENSE
├── .gitignore
├── src/
│   └── lib.rs
├── python/
│   └── wasm_sdk_core/
│       └── __init__.py
├── examples/
│   └── basic_usage.py
└── tests/
    └── test_runtime.py
```
**Tests**: pytest

## Common Elements
- README.md with installation, usage, and contribution guidelines
- LICENSE (MIT)
- .gitignore appropriate for each language
- Examples directory with basic usage
- Comprehensive test coverage

//! Runtime implementation for WASM-SDK-CORE
//!
//! Provides the core runtime functionality for executing WebAssembly components
//! with WASI Preview 2 support.

use anyhow::Result;
use std::fmt;
use wasmtime::*;
use wasmtime_wasi::WasiCtxBuilder;

/// Errors that can occur during runtime operations
#[derive(Debug)]
pub enum RuntimeError {
    /// Error during initialization
    InitializationError(String),
    /// Error during execution
    ExecutionError(String),
    /// Configuration error
    ConfigurationError(String),
}

impl fmt::Display for RuntimeError {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            RuntimeError::InitializationError(msg) => write!(f, "Initialization error: {}", msg),
            RuntimeError::ExecutionError(msg) => write!(f, "Execution error: {}", msg),
            RuntimeError::ConfigurationError(msg) => write!(f, "Configuration error: {}", msg),
        }
    }
}

impl std::error::Error for RuntimeError {}

/// Configuration for the WASM runtime
#[derive(Debug, Clone)]
pub struct RuntimeConfig {
    /// Enable WASI support
    pub wasi_enabled: bool,
    /// Maximum memory size in bytes
    pub max_memory: Option<usize>,
    /// Enable component model support
    pub component_model: bool,
}

impl Default for RuntimeConfig {
    fn default() -> Self {
        Self {
            wasi_enabled: true,
            max_memory: Some(1024 * 1024 * 1024), // 1GB
            component_model: true,
        }
    }
}

/// The main runtime structure for executing WebAssembly modules
pub struct Runtime {
    engine: Engine,
    config: RuntimeConfig,
}

impl Runtime {
    /// Create a new runtime with the given configuration
    pub fn new(config: RuntimeConfig) -> Result<Self, RuntimeError> {
        let mut wasmtime_config = Config::new();
        wasmtime_config.wasm_component_model(config.component_model);
        
        let engine = Engine::new(&wasmtime_config)
            .map_err(|e| RuntimeError::InitializationError(e.to_string()))?;

        Ok(Self { engine, config })
    }

    /// Execute a WebAssembly module from bytes
    pub fn execute(&self, wasm_bytes: &[u8]) -> Result<(), RuntimeError> {
        let mut store = Store::new(&self.engine, ());
        
        let module = Module::new(&self.engine, wasm_bytes)
            .map_err(|e| RuntimeError::ExecutionError(e.to_string()))?;

        let instance = Instance::new(&mut store, &module, &[])
            .map_err(|e| RuntimeError::ExecutionError(e.to_string()))?;

        Ok(())
    }

    /// Get the runtime configuration
    pub fn config(&self) -> &RuntimeConfig {
        &self.config
    }

    /// Check if WASI is enabled
    pub fn is_wasi_enabled(&self) -> bool {
        self.config.wasi_enabled
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_runtime_creation() {
        let config = RuntimeConfig::default();
        let runtime = Runtime::new(config);
        assert!(runtime.is_ok());
    }

    #[test]
    fn test_runtime_config() {
        let config = RuntimeConfig {
            wasi_enabled: true,
            max_memory: Some(512 * 1024 * 1024),
            component_model: true,
        };
        let runtime = Runtime::new(config).unwrap();
        assert!(runtime.is_wasi_enabled());
    }
}

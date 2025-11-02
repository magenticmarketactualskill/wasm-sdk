//! WASM-SDK-CORE: A WASI Preview 2 compatible runtime
//!
//! This library provides a runtime environment for WebAssembly components
//! following the Component Model specification and compatible with Wasmtime.

pub mod runtime;

pub use runtime::{Runtime, RuntimeConfig, RuntimeError};

/// Initialize the WASM-SDK-CORE runtime with default configuration
///
/// # Examples
///
/// ```
/// use wasm_sdk_core::init;
///
/// let runtime = init().expect("Failed to initialize runtime");
/// ```
pub fn init() -> Result<Runtime, RuntimeError> {
    Runtime::new(RuntimeConfig::default())
}

/// Get the version of the WASM-SDK-CORE library
pub fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_version() {
        assert!(!version().is_empty());
    }

    #[test]
    fn test_init() {
        let result = init();
        assert!(result.is_ok());
    }
}

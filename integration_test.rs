//! Integration tests for WASM-SDK-CORE

use wasm_sdk_core::{init, Runtime, RuntimeConfig};

#[test]
fn test_default_initialization() {
    let runtime = init();
    assert!(runtime.is_ok(), "Failed to initialize runtime with defaults");
}

#[test]
fn test_custom_configuration() {
    let config = RuntimeConfig {
        wasi_enabled: true,
        max_memory: Some(256 * 1024 * 1024),
        component_model: true,
    };
    
    let runtime = Runtime::new(config);
    assert!(runtime.is_ok(), "Failed to create runtime with custom config");
    
    let runtime = runtime.unwrap();
    assert!(runtime.is_wasi_enabled(), "WASI should be enabled");
}

#[test]
fn test_wasi_disabled_configuration() {
    let config = RuntimeConfig {
        wasi_enabled: false,
        max_memory: Some(128 * 1024 * 1024),
        component_model: false,
    };
    
    let runtime = Runtime::new(config);
    assert!(runtime.is_ok(), "Failed to create runtime with WASI disabled");
    
    let runtime = runtime.unwrap();
    assert!(!runtime.is_wasi_enabled(), "WASI should be disabled");
}

#[test]
fn test_multiple_runtime_instances() {
    let runtime1 = init();
    let runtime2 = init();
    
    assert!(runtime1.is_ok(), "First runtime initialization failed");
    assert!(runtime2.is_ok(), "Second runtime initialization failed");
}

#[test]
fn test_runtime_config_defaults() {
    let config = RuntimeConfig::default();
    
    assert!(config.wasi_enabled, "Default config should have WASI enabled");
    assert!(config.component_model, "Default config should have component model enabled");
    assert!(config.max_memory.is_some(), "Default config should have max memory set");
}

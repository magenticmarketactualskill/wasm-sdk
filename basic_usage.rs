//! Basic usage example for WASM-SDK-CORE
//!
//! This example demonstrates how to initialize and use the WASM-SDK-CORE runtime.

use wasm_sdk_core::{init, Runtime, RuntimeConfig};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("WASM-SDK-CORE Basic Usage Example");
    println!("==================================\n");

    // Initialize with default configuration
    println!("Initializing runtime with default configuration...");
    let runtime = init()?;
    println!("✓ Runtime initialized successfully\n");

    // Check WASI support
    println!("WASI enabled: {}", runtime.is_wasi_enabled());
    
    // Create runtime with custom configuration
    println!("\nCreating runtime with custom configuration...");
    let custom_config = RuntimeConfig {
        wasi_enabled: true,
        max_memory: Some(512 * 1024 * 1024), // 512MB
        component_model: true,
    };
    
    let custom_runtime = Runtime::new(custom_config)?;
    println!("✓ Custom runtime created successfully");
    println!("  Max memory: 512MB");
    println!("  Component model: enabled");

    println!("\nExample completed successfully!");
    Ok(())
}

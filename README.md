# WASM-SDK-CORE

A **WASI Preview 2** compatible runtime packaged for the Rust community. This library provides a robust foundation for executing WebAssembly components following the [Component Model specification](https://component-model.bytecodealliance.org).

## Features

- **WASI Preview 2 Support**: Full compatibility with the latest WASI specification
- **Component Model**: Implements the WebAssembly Component Model
- **Wasmtime Compatible**: Built on top of the industry-standard Wasmtime runtime
- **jco Compatible**: Works seamlessly with JavaScript Component Tools
- **Easy Integration**: Simple API for embedding in Rust applications

## Installation

Add this to your `Cargo.toml`:

```toml
[dependencies]
wasm-sdk-core = "0.1.0"
```

## Quick Start

```rust
use wasm_sdk_core::{init, RuntimeConfig, Runtime};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Initialize with default configuration
    let runtime = init()?;
    
    // Or create with custom configuration
    let config = RuntimeConfig {
        wasi_enabled: true,
        max_memory: Some(512 * 1024 * 1024), // 512MB
        component_model: true,
    };
    let custom_runtime = Runtime::new(config)?;
    
    Ok(())
}
```

## Architecture

The runtime is built on several key components:

- **Runtime**: The main execution environment for WebAssembly modules
- **RuntimeConfig**: Configuration options for customizing runtime behavior
- **Wasmtime Integration**: Leverages Wasmtime for efficient WASM execution

## Examples

Run the basic usage example:

```bash
cargo run --example basic_usage
```

## Testing

Run the test suite:

```bash
# Run all tests
cargo test

# Run with output
cargo test -- --nocapture

# Run specific test
cargo test test_default_initialization
```

## Component Model Support

This runtime fully supports the WebAssembly Component Model, enabling:

- Interface types for rich data exchange
- Component linking and composition
- WASI Preview 2 interfaces
- Cross-language interoperability

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `wasi_enabled` | `bool` | `true` | Enable WASI support |
| `max_memory` | `Option<usize>` | `1GB` | Maximum memory allocation |
| `component_model` | `bool` | `true` | Enable Component Model features |

## Compatibility

- **Wasmtime**: Compatible with Wasmtime 26.0+
- **WASI**: Supports WASI Preview 2
- **Rust**: Requires Rust 1.70 or later

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Resources

- [Component Model Specification](https://component-model.bytecodealliance.org)
- [Wasmtime Documentation](https://docs.wasmtime.dev/)
- [WASI Preview 2](https://github.com/WebAssembly/WASI/tree/main/preview2)

## Support

For issues and questions, please open an issue on the GitHub repository.

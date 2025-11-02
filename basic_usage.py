#!/usr/bin/env python3
"""
Basic usage example for WASM-SDK-CORE-PY
"""

from wasm_sdk_core import init, Runtime, RuntimeConfig, version

print("WASM-SDK-CORE-PY Basic Usage Example")
print("=" * 40)
print()

# Get library version
print(f"Library version: {version()}")
print()

# Initialize with default configuration
print("Initializing runtime with default configuration...")
runtime = init()
print("✓ Runtime initialized successfully")
print()

# Check engine status
print(f"pyo3 enabled: {runtime.is_pyo3_enabled()}")
print(f"pyo3 version: {runtime.pyo3_version()}")
print(f"Boa enabled: {runtime.is_boa_enabled()}")
print(f"Boa version: {runtime.boa_version()}")
print(f"Runtime initialized: {runtime.is_initialized()}")
print()

# Execute Python code
print("Executing Python code...")
try:
    result = runtime.execute_python("2 + 2")
    print(f"Result: {result}")
    print("✓ Python code executed successfully")
except Exception as e:
    print(f"Execution failed: {e}")
print()

# Execute JavaScript code
print("Executing JavaScript code...")
try:
    js_result = runtime.execute_javascript("console.log('Hello from Boa!')")
    print(f"Result: {js_result}")
    print("✓ JavaScript code executed successfully")
except Exception as e:
    print(f"Execution failed: {e}")
print()

# Create runtime with custom configuration
print("Creating runtime with custom configuration...")
custom_config = RuntimeConfig(
    pyo3_enabled=True,
    boa_enabled=True,
    max_memory=512 * 1024 * 1024,  # 512MB
    wasm_support=True
)

custom_runtime = Runtime(custom_config)
print("✓ Custom runtime created successfully")
print(f"  Max memory: {custom_config.max_memory // (1024 * 1024)}MB")
print("  WASM support: enabled")
print()

# Get configuration
config = custom_runtime.get_config()
print("Runtime configuration:")
print(f"  pyo3 enabled: {config.pyo3_enabled}")
print(f"  Boa enabled: {config.boa_enabled}")
print(f"  Max memory: {config.max_memory} bytes")
print(f"  WASM support: {config.wasm_support}")
print()

print("Example completed successfully!")

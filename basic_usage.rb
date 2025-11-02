#!/usr/bin/env ruby
# frozen_string_literal: true

require_relative "../lib/wasm_sdk_core"

puts "WASM-SDK-CORE-RB Basic Usage Example"
puts "====================================="
puts

# Get library version
puts "Library version: #{WasmSdkCore.version}"
puts

# Initialize with default configuration
puts "Initializing runtime with default configuration..."
runtime = WasmSdkCore.init
puts "✓ Runtime initialized successfully"
puts

# Check engine status
puts "Artichoke enabled: #{runtime.artichoke_enabled?}"
puts "Artichoke version: #{runtime.artichoke_version}"
puts "Boa enabled: #{runtime.boa_enabled?}"
puts "Boa version: #{runtime.boa_version}"
puts

# Execute Ruby code
puts "Executing Ruby code..."
result = runtime.execute_ruby("2 + 2")
puts "Result: #{result}"
puts "✓ Ruby code executed successfully"
puts

# Execute JavaScript code
puts "Executing JavaScript code..."
js_result = runtime.execute_javascript("console.log('Hello from Boa!')")
puts "Result: #{js_result.inspect}"
puts "✓ JavaScript code executed successfully"
puts

# Create runtime with custom configuration
puts "Creating runtime with custom configuration..."
custom_config = WasmSdkCore::RuntimeConfig.new(
  artichoke_enabled: true,
  boa_enabled: true,
  max_memory: 512 * 1024 * 1024, # 512MB
  wasm_support: true
)

custom_runtime = WasmSdkCore::Runtime.new(custom_config)
puts "✓ Custom runtime created successfully"
puts "  Max memory: #{custom_config.max_memory / (1024 * 1024)}MB"
puts "  WASM support: enabled"
puts

puts "Example completed successfully!"

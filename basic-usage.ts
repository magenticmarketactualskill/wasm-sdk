/**
 * Basic usage example for WASM-SDK-CORE-TS
 */

import { init, Runtime, version, RuntimeConfig } from '../src/index.js';

console.log('WASM-SDK-CORE-TS Basic Usage Example');
console.log('=====================================\n');

// Get library version
console.log(`Library version: ${version()}\n`);

// Initialize with default configuration
console.log('Initializing runtime with default configuration...');
const runtime: Runtime = init();
console.log('✓ Runtime initialized successfully\n');

// Check Boa engine status
console.log(`Boa engine enabled: ${runtime.isBoaEnabled()}`);
console.log(`Boa engine version: ${runtime.getBoaVersion()}`);
console.log(`Runtime initialized: ${runtime.isInitialized()}\n`);

// Execute simple TypeScript/JavaScript code
console.log('Executing JavaScript code...');
runtime.execute('console.log("Hello from Boa engine!")').then(() => {
  console.log('✓ Code executed successfully\n');
}).catch((error: Error) => {
  console.error('Execution failed:', error.message);
});

// Create runtime with custom configuration
console.log('Creating runtime with custom configuration...');
const customConfig: RuntimeConfig = {
  boaEnabled: true,
  maxMemory: 512 * 1024 * 1024, // 512MB
  wasmSupport: true
};

const customRuntime: Runtime = new Runtime(customConfig);

console.log('✓ Custom runtime created successfully');
console.log(`  Max memory: ${customConfig.maxMemory / (1024 * 1024)}MB`);
console.log('  WASM support: enabled');

// Get configuration
const config = customRuntime.getConfig();
console.log('\nRuntime configuration:');
console.log(`  Boa enabled: ${config.boaEnabled}`);
console.log(`  Max memory: ${config.maxMemory} bytes`);
console.log(`  WASM support: ${config.wasmSupport}`);

console.log('\nExample completed successfully!');

/**
 * Basic usage example for WASM-SDK-CORE-JS
 */

import { init, Runtime, version } from '../src/index.js';

console.log('WASM-SDK-CORE-JS Basic Usage Example');
console.log('=====================================\n');

// Get library version
console.log(`Library version: ${version()}\n`);

// Initialize with default configuration
console.log('Initializing runtime with default configuration...');
const runtime = init();
console.log('✓ Runtime initialized successfully\n');

// Check Boa engine status
console.log(`Boa engine enabled: ${runtime.isBoaEnabled()}`);
console.log(`Boa engine version: ${runtime.getBoaVersion()}\n`);

// Execute simple JavaScript code
console.log('Executing JavaScript code...');
runtime.execute('console.log("Hello from Boa engine!")').then(() => {
  console.log('✓ Code executed successfully\n');
}).catch(error => {
  console.error('Execution failed:', error.message);
});

// Create runtime with custom configuration
console.log('Creating runtime with custom configuration...');
const customRuntime = new Runtime({
  boaEnabled: true,
  maxMemory: 512 * 1024 * 1024, // 512MB
  wasmSupport: true
});

console.log('✓ Custom runtime created successfully');
console.log('  Max memory: 512MB');
console.log('  WASM support: enabled');

console.log('\nExample completed successfully!');

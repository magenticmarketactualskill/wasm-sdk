/**
 * Tests for WASM-SDK-CORE-TS Runtime
 */

import { Runtime, init, version, RuntimeConfig } from '../src/index.js';

describe('WASM-SDK-CORE-TS', () => {
  describe('version', () => {
    test('should return version string', () => {
      expect(version()).toBeDefined();
      expect(typeof version()).toBe('string');
      expect(version()).toMatch(/^\d+\.\d+\.\d+$/);
    });
  });

  describe('init', () => {
    test('should initialize runtime with defaults', () => {
      const runtime = init();
      expect(runtime).toBeInstanceOf(Runtime);
      expect(runtime.isInitialized()).toBe(true);
    });
  });

  describe('Runtime', () => {
    test('should create runtime with default config', () => {
      const runtime = new Runtime();
      expect(runtime.isInitialized()).toBe(true);
      expect(runtime.isBoaEnabled()).toBe(true);
    });

    test('should create runtime with custom config', () => {
      const config: RuntimeConfig = {
        boaEnabled: true,
        maxMemory: 512 * 1024 * 1024,
        wasmSupport: true
      };
      const runtime = new Runtime(config);
      expect(runtime.getConfig().maxMemory).toBe(512 * 1024 * 1024);
    });

    test('should create runtime with partial config', () => {
      const runtime = new Runtime({ maxMemory: 256 * 1024 * 1024 });
      expect(runtime.getConfig().maxMemory).toBe(256 * 1024 * 1024);
      expect(runtime.getConfig().boaEnabled).toBe(true); // default value
    });

    test('should check Boa engine status', () => {
      const runtime = new Runtime();
      expect(runtime.isBoaEnabled()).toBe(true);
    });

    test('should get Boa version', () => {
      const runtime = new Runtime();
      const boaVersion = runtime.getBoaVersion();
      expect(boaVersion).toBeDefined();
      expect(typeof boaVersion).toBe('string');
      expect(boaVersion).toMatch(/^\d+\.\d+\.\d+$/);
    });

    test('should execute JavaScript code', async () => {
      const runtime = new Runtime();
      const result = await runtime.execute('2 + 2');
      expect(result).toBe(4);
    });

    test('should throw error when executing with Boa disabled', async () => {
      const runtime = new Runtime({ boaEnabled: false });
      await expect(runtime.execute('2 + 2')).rejects.toThrow('Boa engine is not enabled');
    });

    test('should handle execution errors', async () => {
      const runtime = new Runtime();
      await expect(runtime.execute('throw new Error("test error")')).rejects.toThrow();
    });

    test('should get runtime configuration', () => {
      const config: RuntimeConfig = {
        boaEnabled: true,
        maxMemory: 256 * 1024 * 1024,
        wasmSupport: false
      };
      const runtime = new Runtime(config);
      const retrievedConfig = runtime.getConfig();
      expect(retrievedConfig.maxMemory).toBe(256 * 1024 * 1024);
      expect(retrievedConfig.wasmSupport).toBe(false);
    });

    test('should return immutable config', () => {
      const runtime = new Runtime();
      const config = runtime.getConfig();
      const originalMemory = config.maxMemory;
      
      // Attempt to modify (should not affect internal config)
      (config as any).maxMemory = 999;
      
      const newConfig = runtime.getConfig();
      expect(newConfig.maxMemory).toBe(originalMemory);
    });

    test('should check initialization status', () => {
      const runtime = new Runtime();
      expect(runtime.isInitialized()).toBe(true);
    });
  });

  describe('Multiple Runtime Instances', () => {
    test('should create multiple independent runtimes', () => {
      const runtime1 = new Runtime({ maxMemory: 512 * 1024 * 1024 });
      const runtime2 = new Runtime({ maxMemory: 256 * 1024 * 1024 });
      
      expect(runtime1.getConfig().maxMemory).toBe(512 * 1024 * 1024);
      expect(runtime2.getConfig().maxMemory).toBe(256 * 1024 * 1024);
    });

    test('should maintain independent states', () => {
      const runtime1 = new Runtime({ boaEnabled: true });
      const runtime2 = new Runtime({ boaEnabled: false });
      
      expect(runtime1.isBoaEnabled()).toBe(true);
      expect(runtime2.isBoaEnabled()).toBe(false);
    });
  });

  describe('Type Safety', () => {
    test('should enforce RuntimeConfig types', () => {
      const config: RuntimeConfig = {
        boaEnabled: true,
        maxMemory: 1024 * 1024 * 1024,
        wasmSupport: true
      };
      
      const runtime = new Runtime(config);
      expect(runtime).toBeInstanceOf(Runtime);
    });

    test('should handle async execution properly', async () => {
      const runtime = new Runtime();
      const promise = runtime.execute('Promise.resolve(42)');
      expect(promise).toBeInstanceOf(Promise);
      const result = await promise;
      expect(result).toBeDefined();
    });
  });
});

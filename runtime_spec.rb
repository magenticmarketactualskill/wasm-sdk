# frozen_string_literal: true

RSpec.describe WasmSdkCore do
  it "has a version number" do
    expect(WasmSdkCore::VERSION).not_to be nil
    expect(WasmSdkCore.version).to eq(WasmSdkCore::VERSION)
  end

  describe ".init" do
    it "initializes runtime with default configuration" do
      runtime = WasmSdkCore.init
      expect(runtime).to be_a(WasmSdkCore::Runtime)
      expect(runtime).to be_initialized
    end
  end

  describe WasmSdkCore::RuntimeConfig do
    it "creates config with default values" do
      config = WasmSdkCore::RuntimeConfig.new
      expect(config.artichoke_enabled).to be true
      expect(config.boa_enabled).to be true
      expect(config.max_memory).to eq(1024 * 1024 * 1024)
      expect(config.wasm_support).to be true
    end

    it "creates config with custom values" do
      config = WasmSdkCore::RuntimeConfig.new(
        artichoke_enabled: false,
        max_memory: 512 * 1024 * 1024
      )
      expect(config.artichoke_enabled).to be false
      expect(config.max_memory).to eq(512 * 1024 * 1024)
    end
  end

  describe WasmSdkCore::Runtime do
    let(:runtime) { WasmSdkCore::Runtime.new }

    describe "#initialize" do
      it "creates runtime with default config" do
        expect(runtime).to be_initialized
        expect(runtime.artichoke_enabled?).to be true
        expect(runtime.boa_enabled?).to be true
      end

      it "creates runtime with custom config" do
        config = WasmSdkCore::RuntimeConfig.new(artichoke_enabled: false)
        custom_runtime = WasmSdkCore::Runtime.new(config)
        expect(custom_runtime.artichoke_enabled?).to be false
      end

      it "creates runtime with hash config" do
        custom_runtime = WasmSdkCore::Runtime.new(max_memory: 256 * 1024 * 1024)
        expect(custom_runtime.config.max_memory).to eq(256 * 1024 * 1024)
      end
    end

    describe "#artichoke_enabled?" do
      it "returns true when Artichoke is enabled" do
        expect(runtime.artichoke_enabled?).to be true
      end

      it "returns false when Artichoke is disabled" do
        config = WasmSdkCore::RuntimeConfig.new(artichoke_enabled: false)
        disabled_runtime = WasmSdkCore::Runtime.new(config)
        expect(disabled_runtime.artichoke_enabled?).to be false
      end
    end

    describe "#boa_enabled?" do
      it "returns true when Boa is enabled" do
        expect(runtime.boa_enabled?).to be true
      end

      it "returns false when Boa is disabled" do
        config = WasmSdkCore::RuntimeConfig.new(boa_enabled: false)
        disabled_runtime = WasmSdkCore::Runtime.new(config)
        expect(disabled_runtime.boa_enabled?).to be false
      end
    end

    describe "#execute_ruby" do
      it "executes Ruby code successfully" do
        result = runtime.execute_ruby("2 + 2")
        expect(result).to eq(4)
      end

      it "raises error when Artichoke is disabled" do
        config = WasmSdkCore::RuntimeConfig.new(artichoke_enabled: false)
        disabled_runtime = WasmSdkCore::Runtime.new(config)
        expect { disabled_runtime.execute_ruby("2 + 2") }.to raise_error(RuntimeError, /Artichoke engine not enabled/)
      end

      it "handles execution errors" do
        expect { runtime.execute_ruby("raise 'test error'") }.to raise_error(RuntimeError, /Ruby execution failed/)
      end
    end

    describe "#execute_javascript" do
      it "executes JavaScript code successfully" do
        result = runtime.execute_javascript("console.log('test')")
        expect(result).to be_a(Hash)
        expect(result[:code]).to eq("console.log('test')")
      end

      it "raises error when Boa is disabled" do
        config = WasmSdkCore::RuntimeConfig.new(boa_enabled: false)
        disabled_runtime = WasmSdkCore::Runtime.new(config)
        expect { disabled_runtime.execute_javascript("test") }.to raise_error(RuntimeError, /Boa engine not enabled/)
      end
    end

    describe "#artichoke_version" do
      it "returns Artichoke version string" do
        expect(runtime.artichoke_version).to be_a(String)
        expect(runtime.artichoke_version).to match(/\d+\.\d+\.\d+/)
      end
    end

    describe "#boa_version" do
      it "returns Boa version string" do
        expect(runtime.boa_version).to be_a(String)
        expect(runtime.boa_version).to match(/\d+\.\d+\.\d+/)
      end
    end

    describe "#get_config" do
      it "returns the runtime configuration" do
        config = runtime.get_config
        expect(config).to be_a(WasmSdkCore::RuntimeConfig)
      end
    end

    describe "multiple instances" do
      it "creates independent runtime instances" do
        runtime1 = WasmSdkCore::Runtime.new(max_memory: 512 * 1024 * 1024)
        runtime2 = WasmSdkCore::Runtime.new(max_memory: 256 * 1024 * 1024)

        expect(runtime1.config.max_memory).to eq(512 * 1024 * 1024)
        expect(runtime2.config.max_memory).to eq(256 * 1024 * 1024)
      end
    end
  end
end

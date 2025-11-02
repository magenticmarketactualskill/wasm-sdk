# frozen_string_literal: true

require "wasm_sdk_core"

# Configure Cucumber
World(Module.new do
  def runtime
    @runtime ||= WasmSdkCore.init
  end
end)

# frozen_string_literal: true

require_relative "wasm_sdk_core/version"
require_relative "wasm_sdk_core/runtime"

# WASM-SDK-CORE-RB
#
# A Ruby gem providing Artichoke and Boa engine integration
# for WebAssembly execution in the Ruby community.
module WasmSdkCore
  class Error < StandardError; end

  # Get the library version
  def self.version
    VERSION
  end
end

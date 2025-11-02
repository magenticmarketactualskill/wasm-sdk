# frozen_string_literal: true

require_relative "lib/wasm_sdk_core/version"

Gem::Specification.new do |spec|
  spec.name = "wasm_sdk_core"
  spec.version = WasmSdkCore::VERSION
  spec.authors = ["WASM-SDK Team"]
  spec.email = ["team@wasm-sdk.org"]

  spec.summary = "Artichoke + Boa powered WASM runtime for Ruby"
  spec.description = "A Ruby gem providing Artichoke and Boa engine integration for WebAssembly execution"
  spec.homepage = "https://github.com/wasm-sdk/wasm-sdk-core-rb"
  spec.license = "MIT"
  spec.required_ruby_version = ">= 3.3.0"

  spec.metadata["homepage_uri"] = spec.homepage
  spec.metadata["source_code_uri"] = spec.homepage
  spec.metadata["changelog_uri"] = "#{spec.homepage}/blob/main/CHANGELOG.md"

  # Specify which files should be added to the gem when it is released.
  spec.files = Dir.glob("{lib,examples}/**/*") + %w[README.md LICENSE]
  spec.bindir = "exe"
  spec.executables = spec.files.grep(%r{\Aexe/}) { |f| File.basename(f) }
  spec.require_paths = ["lib"]

  # Runtime dependencies
  # In a real implementation, this would include artichoke bindings
  # spec.add_dependency "artichoke", "~> 0.1"

  # Development dependencies
  spec.add_development_dependency "rake", "~> 13.0"
  spec.add_development_dependency "rspec", "~> 3.12"
  spec.add_development_dependency "cucumber", "~> 9.0"
  spec.add_development_dependency "rubocop", "~> 1.50"
end

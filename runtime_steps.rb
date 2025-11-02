# frozen_string_literal: true

Given("I have the WASM SDK Core library") do
  expect(WasmSdkCore).to be_a(Module)
end

When("I initialize the runtime") do
  @runtime = WasmSdkCore.init
end

Then("the runtime should be initialized successfully") do
  expect(@runtime).to be_initialized
end

Then("Artichoke should be enabled") do
  expect(@runtime.artichoke_enabled?).to be true
end

Then("Boa should be enabled") do
  expect(@runtime.boa_enabled?).to be true
end

Given("I have an initialized runtime") do
  @runtime = WasmSdkCore.init
end

When("I execute Ruby code {string}") do |code|
  @result = @runtime.execute_ruby(code)
end

Then("the result should be {int}") do |expected|
  expect(@result).to eq(expected)
end

When("I execute JavaScript code {string}") do |code|
  @js_result = @runtime.execute_javascript(code)
end

Then("the JavaScript execution should succeed") do
  expect(@js_result).to be_a(Hash)
  expect(@js_result).to have_key(:result)
end

Given("I have a custom configuration with {int}MB memory") do |memory_mb|
  @config = WasmSdkCore::RuntimeConfig.new(
    max_memory: memory_mb * 1024 * 1024
  )
end

When("I create a runtime with the custom configuration") do
  @runtime = WasmSdkCore::Runtime.new(@config)
end

Then("the runtime should have {int}MB max memory") do |memory_mb|
  expect(@runtime.config.max_memory).to eq(memory_mb * 1024 * 1024)
end

Then("the runtime should be initialized") do
  expect(@runtime).to be_initialized
end

When("I check the Artichoke version") do
  @artichoke_version = @runtime.artichoke_version
end

Then("it should return a valid version string") do
  expect(@artichoke_version).to be_a(String)
  expect(@artichoke_version).to match(/\d+\.\d+\.\d+/)
end

When("I check the Boa version") do
  @boa_version = @runtime.boa_version
end

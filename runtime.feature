Feature: WASM SDK Core Runtime
  As a Ruby developer
  I want to use the WASM SDK Core runtime
  So that I can execute Ruby and JavaScript code

  Scenario: Initialize runtime with default configuration
    Given I have the WASM SDK Core library
    When I initialize the runtime
    Then the runtime should be initialized successfully
    And Artichoke should be enabled
    And Boa should be enabled

  Scenario: Execute Ruby code
    Given I have an initialized runtime
    When I execute Ruby code "2 + 2"
    Then the result should be 4

  Scenario: Execute JavaScript code
    Given I have an initialized runtime
    When I execute JavaScript code "console.log('test')"
    Then the JavaScript execution should succeed

  Scenario: Create runtime with custom configuration
    Given I have a custom configuration with 512MB memory
    When I create a runtime with the custom configuration
    Then the runtime should have 512MB max memory
    And the runtime should be initialized

  Scenario: Get engine versions
    Given I have an initialized runtime
    When I check the Artichoke version
    Then it should return a valid version string
    When I check the Boa version
    Then it should return a valid version string

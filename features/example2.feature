Feature: testing google

  Scenario Outline: visit google and check
    Given we have google installed
    When we visit google
    Then it should have a title "Google"
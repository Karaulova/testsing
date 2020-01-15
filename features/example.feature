Feature: Mul

  Scenario Outline: Calculator
    Given I have a calculator
    When I multiply "<x>" and "<y>"
    Then the calculator returns "<mul>"

    Examples:
        |  x  |  y | mul |
        |  1  |  1 |  1  |
        |  1  |  2 |  2  |
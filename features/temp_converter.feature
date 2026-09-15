@uppgift1
Feature: Temperaturomvandling
  Scenario: Omvandlar Fahrenheit till Celsius
    Given Givet 32
    When Temperatur omvandlas från F till C
    Then Den omvandlade temperaturen förväntas vara 0

  Scenario: Omvandlar Celsius till Fahrenheit
    Given Givet 0
    When Temperatur omvandlas från C till F
    Then Den omvandlade temperaturen förväntas vara 32
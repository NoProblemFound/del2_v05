@uppgift2
Feature: Lagerhållning
  Scenario: Lägga till en produkt
    Given Ett tomt lager
    When Lägger till en produkt "glas" med antal 6
    Then Lagret ska innehålla en produkt med namnet glas och antalet skall vara 6 st

    

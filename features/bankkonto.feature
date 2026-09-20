Feature: Bankkonto
  Scenario: Skapa nytt konto med saldo 0
  Given Ingen konto
  When Skapa ett nytt konto
  Then Saldot är 0

  Scenario: Sätta in pengar
    Given Ett nytt bankkonto
    When Sätter in 100 kronor
    Then Saldot ska vara 100

  Scenario: Ta ut pengar
    Given Ett bankkonto med 500 kronor
    When Tar ut 300 kronor
    Then Saldot ska vara 200

  Scenario: Applicera ränta
    Given Ett bankkonto med 100 kronor
    When Applicerar ränta
    Then Saldot ska vara 105

  Scenario: Överföra pengar mellan två konton
    Given Konto A har 200 kronor
    And Konto B har 300 kronor
    When Överför 100 kronor från konto A till konto B
    Then Saldot på konto A ska vara 100
    And Saldot på konto B ska vara 400
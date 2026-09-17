Feature: Bankkonto
  Scenario: Skapa nytt konto med saldo 0
  Given Ingen konto
  When Skapa ett nytt konto
  Then Saldot är 0


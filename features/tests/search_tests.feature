# Created by alinakarpenko at 3/20/25
Feature: Target search

  Scenario: User can search for  product
    Given Open target main page
    When Search for tea
    Then Verify search worked for tea

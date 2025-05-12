# Created by alinakarpenko at 3/11/25
Feature: Target sign in form opens

  Scenario: Sign In form is open when click sign in
    Given Open target main page
    When Click Sign In
    When Click Sign In in navigation menu
    Then Verify Sign In form opened

  Scenario: Error message is shown when user enters incorrect password
    Given Open sign in page
    When Enter correct email address and click continue
    And Click Sign In with password
    Then Verify error message is shown

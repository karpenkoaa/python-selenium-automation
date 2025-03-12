# Created by alinakarpenko at 3/11/25
Feature: Target sign in form opens

  Scenario: Sign In form is open when click sign in
    Given Open target main page
    When Click Sign In
    When Click Sign In in navigation menu
    Then Verify Sign In form opened

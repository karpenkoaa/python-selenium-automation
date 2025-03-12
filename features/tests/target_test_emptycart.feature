# Created by alinakarpenko at 3/11/25
Feature: Target 'Your cart is empty' message is shown

  Scenario: 'Your cart is empty' message is shown when user's cart is empty
    Given Open target main page
    When Click on Cart icon
    Then Verify correct message is shown
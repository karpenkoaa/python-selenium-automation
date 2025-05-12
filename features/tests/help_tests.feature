# Created by alinakarpenko at 5/3/25
Feature: Tests for Help pages

  Scenario: User can select Help topic Gift Cards
    Given Open Help page for returns
    Then Verify help Returns page opens
    When Select help topic Gift Cards
    Then Verify help Gift Cards opens
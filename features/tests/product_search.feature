Feature: Test Scenarios for Search functionality

  Scenario Outline: User can search for a product on Target
    Given Open target main page
    When Input <search_word> into search field
    And Click on search icon
    Then Product results are shown for <expected_result>
    Examples:
    |search_word |expected_result |
    |tea         | tea            |
    |iphone      |iphone          |
    |dress       |dress           |
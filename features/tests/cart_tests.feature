# Created by alinakarpenko at 3/11/25
Feature: Target 'Your cart is empty' message is shown

  Scenario: 'Your cart is empty' message is shown when user's cart is empty
    Given Open target main page
    When Click on Cart icon
    Then Verify correct message is shown
    And Verify cart page opens

  Scenario: Product is added to the cart
    Given Open target main page
    When Input chair into search field
    And Click on search icon
    And Click Add to cart on the product
    And Confirm Add to Cart button from side navigation
    And Store product name
    And Open Cart Page
    Then Verify Cart has 1 item(s)
    Then Verify cart has correct product

# Created by alinakarpenko at 4/15/25
Feature: Terms and Conditions window

  Scenario: User can open and close Terms and Conditions from sign in page
 Given Open sign in page
 When Store original window
 And Click on Target terms and conditions link
 And Switch to the newly opened window
 Then Verify Terms and Conditions page is opened
 And Close new window
 And Switch back to original window



Feature: Login to Application

  Scenario: Login with valid credentials
    Given I am on the login page
    When I enter username "rahulshettyacademy"
    And I enter password "learning"
    And I select the role as "teach"
    And I check the I Agree checkbox
    And I click login
    Then I should see the home page
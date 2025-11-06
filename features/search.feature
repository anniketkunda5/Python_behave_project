Feature: Search functionality

  @Search @search1
  Scenario: Search for a valid product
    Given I got navigate to home page
    When I enter valid product say "HP" into the search box field
    And I click on Search button
    Then Valid product should get displayed in search results
  @Search
  Scenario: Search for an invalid product
    Given I got navigate to home page
    When I enter invalid product say "MAN" into the search box field
    And I click on Search button
    Then Proper message should be displayed in search result
  @Search
  Scenario:Search without entering any product
    Given I got navigate to home page
    When I dont enter anything into search box field
    And I click on Search button
    Then Proper message should be displayed in search result

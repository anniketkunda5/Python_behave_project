Feature: Register Account functionality
  @Register @pom1
  Scenario:Register with mandatory fields
    Given I navigate to register page
    When I enter below details in the mandatory fields
        |first_name|last_name|telephone  |password |
        |man123    |man456   |7685940312 |dem123   |
    And I click on Continue button
    Then Account should get created
  @Register @pom2
  Scenario: Register With all fields
    Given I navigate to register page
    When I enter details into all fields
        |first_name|last_name|telephone  |password |
        |man123    |man456   |7685940312 |dem123   |
    And I click on Continue button
    Then Account should get created
  @Register @pom3
  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email field
        |first_name|last_name|telephone  |password |
        |man123    |man456   |7685940312 |dem123   |
    And I enter existing account mail into email field
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed
  @Register @pom4
  Scenario: Register without providing any details
    Given I navigate to register page
    When I dont enter anything into fields
    And I click on Continue button
    Then Proper warning message for every mandatory fields should be displayed


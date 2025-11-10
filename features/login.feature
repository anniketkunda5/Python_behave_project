Feature:Login Functionality
  @Login @login1
  Scenario Outline: Login with valid credentials
    Given I navigated to the login page
    When I enter valid email address as "<email>" and valid password as "<password>" into the fields
    And click on login button
    Then I should got logged in
    Examples:
      |email                 |password             |
      |a.kunda@gmail.com     |anniket123|
      |kunda@gmail.com       |12345|
      |a.kunda@gmail.com     |jbhshkduiwg|
  @Login @login2
  Scenario: Login with valid mail and invalid password
    Given I navigated to the login page
    When I enter valid email address as "a.kunda@gmail.com " and invalid password as "ant123" into the fields
    And click on login button
    Then I should get proper warning message
  @Login @login3
  Scenario: Login with invalid credentials
    Given I navigated to the login page
    When I enter invalid email and invalid password into the fields
    And click on login button
    Then I should get proper warning message
  @Login @login4
  Scenario: Login with without entering any credentials
    Given I navigated to the login page
    When I do not enter anything into login and password fields
    And click on login button
    Then I should get proper warning message

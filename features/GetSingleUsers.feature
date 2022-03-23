Feature: Verify if Author Name is correct as per the query parameter in the API GET request.

  @regression
  Scenario: Verify Author Name
    Given the API request
    When we execute the GET API request with first id
    Then check get api request
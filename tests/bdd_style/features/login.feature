Feature: Login
    
    As a User,
    I should be able to log in to Sauce Demo website,
    and access my account
    
    Scenario: Login to Sauce Demo website with valid credential
        Given Sauce Demo login page
        When I enter a valid username
        And with a valid password
        Then I can logged in and access the account

    Scenario: Login to Sauce Demo website with invalid credential
        Given Sauce Demo login page
        When I enter an invalid username
        And with an invalid password
        Then I will see an error message

    Scenario: Login to Sauce Demo website with blocked credential
        Given Sauce Demo login page
        When I enter "locked_out_user" as username
        And with a valid password
        Then I will see an error message about the blocked credential
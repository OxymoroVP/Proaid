Feature: Request access & modification of the medical history
    Background:
        Given that I am a doctor
        And I am signed-in

    Scenario: Send access/edit data request to registered patients successfully.
        Given that I want to send request to access & edit a registered patient’s medical history 
        And I have the patient’s locked file displayed in my screen 
        When I click the request button 
        Then the AMKA section window pops up 
        When I enter the AMKA number
        And the AMKA number is valid and distinctive
        Then I should receive the message: “Request for access & modification of patient’s medical history has been sent!”
        Then I return to my home page

    Scenario: Send access/edit data request to non-registered patients unsuccessfully.
        Given that I am asked to send request to access & edit patient’s medical history 
        When I proceed to click the request button 
        Then the AMKA section window pops up
        When I enter the AMKA number 
        And the AMKA number is invalid or non-distinctive
        Then I should receive the message “Patient with the information provided is not found.”
        And the AMKA section window pops up again to retry the search

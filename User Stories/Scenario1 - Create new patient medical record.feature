Feature: Create a new patient’s history file
    Background:
        Given that I am a doctor
        And I am logged in
        And the patient is unregistered

    Scenario: Create a new patient’s history file
        When I select the “new patient” option AMKA
        Then a blank patient’s form pops up
        And I am asked to fill the gaps with patient’s information
        When i fill the gaps with the patient’s name, date of birth, email AMKA and phone number
        And I create the patient’s medical history
        Then I am informed that the patient’s history file has been successfully created


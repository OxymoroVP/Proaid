Feature: Search a patient
    Background:
        Given that I am a doctor
        And I am logged in

    Scenario: Search and find an unregistered patient
        Given that I want to search an unregistered patient in my database
        When I click the search option
        Then a window pops up
        And I am asked to enter the patient’s AMKA
        When I enter the patient’s AMKA
        And the system searches the AMKA in my database
        And there is a patient with this AMKA in my database
        Then the patient’s file shows up

    Scenario: Search an unregistered patient that doesn’t exist in my database
        Given that I want to search a patient in my database
        When I click the search option
        Then a window pops up
        And I am asked to enter the patient’s AMKA
        When I enter the patient’s AMKA
        And the system searches the AMKA in my database
        But there isn’t a patient with this AMKA in my database
        Then I am informed that the system can not find the patient
        And I am asked to choose an <option>
            | enter AMKA again | return to main page |

    Scenario: Search a registered patient
        Given that I want to search a registered patient 
        When I click the search option
        Then a window pops up 
        And I am asked to enter the patient’s AMKA
        When I enter the patient’s AMKA
        And the system searches the AMKA in registered users’ database
        Then the patient’s locked file shows up

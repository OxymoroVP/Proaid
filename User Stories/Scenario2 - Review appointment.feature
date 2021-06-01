Feature: Review the schedule
    Background:
        Given that I am a doctor
        And I am logged in

    Scenario: Review the desired schedule
        When I select to review my desired schedule
        Then my <desired> schedule with all the appointments and free spaces comes up on the screen
            | daily | weekly |  monthly |
 
    Scenario: Export the desired schedule
        Given that my <desired> schedule is displayed on the screen
            | daily | weekly |  monthly |
        When I select the option
        Then I am asked in which form I want to export the schedule
        When I select the form I want to export the schedule
        Then I am informed that the system exports the schedule 
        And I am informed that the schedule has been successfully exported

    Scenario: Process the desired schedule
        Given that my <desired> schedule is displayed on the screen
            | daily | weekly |  monthly |
        When I select the process option
        Then I am informed that the system processes the schedule 
        And I am informed that the schedule has been successfully <processed>
            | downloaded | printed | exported |

Feature: View appointments
    Background: 
        Given that I am logged in 
        And I am a registered patient

    Scenario: View existing appointments
        When I select view appointments
        And there are appointments scheduled
        Then I see the existing appointments

    Scenario: View non existing appointments
        When I select view appointments
        But there are no appointments scheduled
        Then I am informed that there are no appointments scheduled 

Feature: Edit notification attributes

    Scenario: Edit notification attributes
        Given that I have selected to see my appointments
        When I select an appointment
        Then I should see the message “Edit notification settings” 
        And I have the option to edit the notification time
        And I have the option to edit the notification preference

    Scenario: Edit notification time
        Given that I have selected an appointment 
        When I select to change the notification time
        Then I can edit the notification time
        When I change the notification time
        Then I am informed the notification time has changed successfully

    Scenario: Edit notification preference as a patient
        When I select to change the notification preference
        Then I can edit the notification <preference>
            | with email | with a popup | by text message |
        When I change the notification preference
        Then I am informed the notification preference has changed successfully

    Scenario: Edit notification preference as a doctor
        When I select to change the notification preference
        Then I can edit the notification <preference>
            | with email | with a popup | with sound |
        When I change the notification preference
        Then I am informed the notification preference has changed successfully

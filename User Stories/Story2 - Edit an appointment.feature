Feature: Edit an appointment
    Background:
        Given that I am a doctor
        And I am logged in

    Scenario: Successfully create a new appointment
        Given that I want to create a new appointment
        And my schedule is displayed on the screen
        And there is free space in my schedule
        When I select the specific free hour in my schedule
        Then an empty appointment form pops up 
        And I am asked to enter appointment’s information
        When I enter the patient’s name, the reason for visiting, and the duration of the appointment
        And there is not another appointment that coincides with the new one
        Then I am informed that the appointment has been successfully created
        And I return to my schedule page    
 
    Scenario: Create a new appointment that coincides with another one
        Given that I want to create a new appointment
        And my schedule is displayed on the screen
        And there is free space in my schedule
        When I select the specific free hour in my schedule
        Then an empty appointment form pops up 
        When I enter the patient’s name, the reason for visiting, and the duration of the appointment
        But there is another appointment scheduled before the new one ends
        Then I am informed that the new appointment does not fit in that space

    Scenario: Successfully edit an attribute of an existing appointment
        Given that I want to edit an existing appointment
        When I select the appointment I want to edit
        Then the appointment’s form window pops up
        When I edit an <attribute>
            | name | reason for visiting | duration | time | date |  
        Then I am informed that the appointment is successfully updated
        And I return to my schedule page

    Scenario: Unsuccessfully edit an attribute of an existing appointment 
        Given that I want to edit an existing appointment
        When I select the appointment I want to edit
        Then the appointment’s form window pops up
        When I edit the <attribute>
            | name | reason for visiting | duration | time | date | 
        But there is not another appointment that coincides with the edited one
        Then I am informed that the edited appointment does not fit in that space

    Scenario: Delete an appointment
        Given that I want to delete an appointment
        When I select the appointment I want to delete
        And I choose the delete option
        Then I am asked if i want to delete the appointment
        And I am informed that the appointment has been successfully deleted
        And I return to my schedule page

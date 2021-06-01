Feature: The doctor can approve or reject a requested appointment from a patient
    Background:
	    Given that I am the doctor
	    And I am logged in
        And I have received a notification about a requested appointment

    Scenario: Approve a requested appointment from a patient
	    When I open the notification
	    Then I am asked to approve/reject the requested appointment
	    When I approve the requested appointment
	    Then I am asked to confirm the approval
	    When I confirm the approval
	    Then I am informed that the appointment has been approved
	    And I am informed that the appointment has been scheduled
	    And I am returned to my home page

    Scenario: Reject a requested appointment from a patient
        When I open the notification
	    Then I am asked to approve the requested appointment
	    When I reject the requested appointment
	    Then I am asked to confirm the rejection
	    When I confirm the rejection
	    Then I am informed that the appointment has been rejected
	    And I am returned to my home page

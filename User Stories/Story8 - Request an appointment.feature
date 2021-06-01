Feature: The patient can request an appointment
    Background:
        Given that I am a patient
        And I am logged in

	Scenario: Successfully request an appointment from a doctor previously visited
		Given that I want to request an appointment
        And I have doctors in my previously visited list
		When I choose the corresponding option
		Then the list with the doctors I previously visited pops up
		When I select a doctor from that list
		Then a list with available times and dates for this doctor appears 
		When I choose the time and date of the appointment
		And there is not another appointment that coincides with the new one
		Then I am asked to confirm the request
		When I confirm the request
		Then I am informed that my request has been sent
		And I return to my home page

	Scenario: Request an appointment from a doctor previously visited that coincides with an existing one
		Given that I want to request an appointment
        And I have doctors in my previously visited list
		When I choose the corresponding option
		Then a list with the doctors I previously visited pops up
		When I select a doctor from that list
		Then an empty request form pops up
		And I am asked to enter the appointment information I want
		When I enter the time and the day of the appointment
		And there is another appointment that coincides with the new one
		Then I am informed that I have another appointment at this time and date
		And I am asked to choose another available appointment	
	
	Scenario: Retry requesting an appointment with a doctor
		Given that I have received a notification about an appointment
		And this appointment has been rejected
		When I open this notification
		Then I am informed that my appointment has been rejected
		And I am asked if I want to retry scheduling the appointment
		When I choose to retry scheduling the appointment
		Then I am asked to choose an alternative
		When I choose an alternative
		Then I am asked to confirm the request
		When I confirm the request
		Then I am informed that my request has been sent
		And I return to my home page

    Scenario: Request an appointment without having visited any doctor
        Given that I want to request an appointment
        And that I have not visited any doctor that uses the application
        When I choose the option to request an appointment
        Then I am informed that I do not have any doctors my previously visited list
        And I am informed that I need to book the first appointment by another means
        And I return to my home page

    Scenario: Request an appointment from a doctor that does not have any available
        Given that I want to request an appointment
        And I have doctors in my previously visited list
        When I select the option to request an appointment
        Then the list with the doctors I previously visited pops up
        When I select a doctor from that list
        And that doctor does not have any available appointments
        Then I am informed that this doctor does not have any available appointments
        And I return to my previously visited doctors list

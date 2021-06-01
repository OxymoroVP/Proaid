Feature: Inform a registered user(doctor/patient) before an appointment at the time they chose and with their preferred method
    Background: 
        Given that I am a registered user
        And that I have a scheduled appointment
        And that I have chosen to be notified about that appointment
        And that I have chosen an x amount of time before the appointment before that 	appointment
        And that this x amount of time has come
        And that there is an external system called “Notification System”

    Scenario: System notifies registered user (doctor/patient) about their appointment with email
        Given that I have chosen to be notified about the appointment with an email
        Then the system obtains my registered email address
        And sends a notification email about the appointment to that address

    Scenario: System notifies registered patient about their appointment with a text                         message to their phone
        Given that I am a registered patient
        And that I have chosen to be notified about the appointment with a message to my phone
        Then the system obtains my registered phone number
        And notifies me with a text message about the appointment to that number

    Scenario: System notifies doctor with a pop-up on his screen
        Given that I am a doctor
        And I am logged in
        And that I have chosen to be notified about the appointment with a pop-                        up notification on my screen
        Then the system displays a notification pop-up on my screen to notify me                     about the appointment
        And I am required to confirm that I was notified
        When I confirm that I was notified
        Then I am returned to the page I was before
        But when I do not confirm that I was notified
        Then the system waits for 10 minutes 
        And I am returned to the page I was before

    Scenario: System notifies doctor with a sound notification
        Given that I am a doctor
        And I am logged in
        And that I have chosen to be notified about the appointment with                                    a sound notification
        And I have chosen a preferred sound to be played for the notification
        Then the system plays my preferred sound to notify me of the appointment
        Then the system waits for 10 seconds
        And the system stops playing the sound  
        And I am returned to the page I was before

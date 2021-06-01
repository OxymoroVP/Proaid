Feature: Modify the medical history
    Background:
        Given that I am a doctor
		And I am signed-in
		And the patient is registered 
	
    Scenario: Modify patient’s medical history successfully.
        Given that I am asked to edit patient’s medical history 
        When I proceed to click the edit button on patient’s medical history section 
        And I am asked to enter a valid medical report 
        And I select type of <modification> 
            | comment | details | medical report files | allergies | operations |
        And I enter a valid report for the patient
        And I proceed to save my action
        Then I should receive the message “Patient’s medical history updated successfully!”

    Scenario: Modify patient’s medical history unsuccessfully.
        Given that I am asked to edit patient’s medical history 
        When I proceed to click the edit button on patient’s medical history section
        And I enter a valid report for the patient
        And I do not proceed to save my action 
        Then I should receive the message “Patient’s medical history has not been modified. Proceed?"”

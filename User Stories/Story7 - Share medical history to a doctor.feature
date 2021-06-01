Feature: Share my medical history
    Background:
        Given that I am a registered patient
        And I am signed-in
        And I am asked to share my medical history

    Scenario: Share my medical history successfully.
        When I open my notifications 
        And I select doctor’s request 
        Then I am asked to proceed sharing my medical history 
        When I respond positively
        Then I am informed that my file has been shared successfully

    Scenario: Deny sharing my medical history.
        When I open my notifications 
        And I select doctor’s request 
        Then I am asked to proceed sharing my medical history 
        When I respond negatively
        Then I am informed that doctor’s request has been deleted 

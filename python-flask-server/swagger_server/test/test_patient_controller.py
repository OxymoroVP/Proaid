# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.patient_appointment import PatientAppointment  # noqa: E501
from swagger_server.models.request import Request  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPatientController(BaseTestCase):
    """PatientController integration test stubs"""

    def test_ar_medical_folder_access(self):
        """Test case for ar_medical_folder_access

        Patient responds to doctor's request for medical folder sharing
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/request/{r_id}'.format(d_id=56, r_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_notification(self):
        """Test case for edit_notification

        Edit an appointment's notification
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/appointment/{a_id}'.format(p_id=56, a_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request_appointment(self):
        """Test case for request_appointment

        Request an appointment at an available time and date
        """
        request = Request()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/request'.format(p_id=56),
            method='POST',
            data=json.dumps(request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_review_appointment(self):
        """Test case for review_appointment

        Review a scheduled appointment
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/appointment/{a_id}'.format(p_id=56, a_id=56),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_review_appointments(self):
        """Test case for review_appointments

        Review all scheduled appointments
        """
        appointment = PatientAppointment()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/appointment'.format(p_id=56),
            method='GET',
            data=json.dumps(appointment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

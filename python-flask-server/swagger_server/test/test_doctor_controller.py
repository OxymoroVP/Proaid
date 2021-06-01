# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.appointment import Appointment  # noqa: E501
from swagger_server.models.calendar import Calendar  # noqa: E501
from swagger_server.models.medical_folder import MedicalFolder  # noqa: E501
from swagger_server.models.patient import Patient  # noqa: E501
from swagger_server.models.request import Request  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDoctorController(BaseTestCase):
    """DoctorController integration test stubs"""

    def test_create_appointment(self):
        """Test case for create_appointment

        Create an appointment
        """
        appointment = Appointment()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/calendar/appointment'.format(d_id=56),
            method='POST',
            data=json.dumps(appointment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_appointment_menu(self):
        """Test case for create_appointment_menu

        Create an appointment
        """
        appointment = Appointment()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/appointment'.format(d_id=56),
            method='POST',
            data=json.dumps(appointment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_unregistered_patient(self):
        """Test case for create_unregistered_patient

        Creates a new unregistered patient
        """
        patient = Patient()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient'.format(d_id=56),
            method='POST',
            data=json.dumps(patient),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_appointment(self):
        """Test case for delete_appointment

        Delete an appointment
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/calendar/appointment/{a_id}'.format(d_id=56, a_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_unregistered_patient(self):
        """Test case for delete_unregistered_patient

        Delete unregistered patient
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient/{p_id}'.format(d_id=56, p_id=56),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_doctor_send_request(self):
        """Test case for doctor_send_request

        Send a request
        """
        request = Request()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/request'.format(d_id=56),
            method='POST',
            data=json.dumps(request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_appointment(self):
        """Test case for edit_appointment

        Edit an appointment
        """
        appointment = Appointment()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/calendar/appointment/{a_id}'.format(d_id=56, a_id=56),
            method='PUT',
            data=json.dumps(appointment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_folder(self):
        """Test case for edit_folder

        Edit medical folder of a registered patient
        """
        medicalfolder = MedicalFolder()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/medicalfolder'.format(p_id='p_id_example'),
            method='PUT',
            data=json.dumps(medicalfolder),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_unregistered_folder(self):
        """Test case for edit_unregistered_folder

        Doctor edits an unregistered patient's medical folder
        """
        medicalfolder = MedicalFolder()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient/{p_id}/medicalfolder'.format(p_id=56, d_id=56),
            method='PUT',
            data=json.dumps(medicalfolder),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_edit_unregistered_patient(self):
        """Test case for edit_unregistered_patient

        Edit by patient id
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient/{p_id}'.format(p_id=56, d_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_registered_patient(self):
        """Test case for get_registered_patient

        Get registered patient's info
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}'.format(p_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_schedule(self):
        """Test case for get_schedule

        View schedule
        """
        calendar = Calendar()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/calendar'.format(d_id=56),
            method='GET',
            data=json.dumps(calendar),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_unregistered_folder(self):
        """Test case for get_unregistered_folder

        Get medical folder of a patient by patient id
        """
        medicalfolder = MedicalFolder()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient/{p_id}/medicalfolder'.format(p_id='p_id_example', d_id=56),
            method='GET',
            data=json.dumps(medicalfolder),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_unregistered_patient(self):
        """Test case for get_unregistered_patient

        Get a patient by patient id
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/doctor/{d_id}/patient/{p_id}'.format(p_id=56, d_id=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_patient_ar_appointment(self):
        """Test case for patient_ar_appointment

        Accept/Reject a request for appointment
        """
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/request/{r_id}'.format(p_id=56, r_id=56),
            method='PUT',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.medical_folder import MedicalFolder  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMedicalfolderController(BaseTestCase):
    """MedicalfolderController integration test stubs"""

    def test_get_folder(self):
        """Test case for get_folder

        Get medical folder of a patient by patient id
        """
        medicalfolder = MedicalFolder()
        response = self.client.open(
            '/Omada-Ergasias-7/Proaid/1.14.2/user/patient/{p_id}/medicalfolder'.format(p_id=56),
            method='GET',
            data=json.dumps(medicalfolder),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MedicalFolder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, patient_description: str=None, allergies: List[str]=None, operations: List[str]=None, files: List[object]=None):  # noqa: E501
        """MedicalFolder - a model defined in Swagger

        :param patient_description: The patient_description of this MedicalFolder.  # noqa: E501
        :type patient_description: str
        :param allergies: The allergies of this MedicalFolder.  # noqa: E501
        :type allergies: List[str]
        :param operations: The operations of this MedicalFolder.  # noqa: E501
        :type operations: List[str]
        :param files: The files of this MedicalFolder.  # noqa: E501
        :type files: List[object]
        """
        self.swagger_types = {
            'patient_description': str,
            'allergies': List[str],
            'operations': List[str],
            'files': List[object]
        }

        self.attribute_map = {
            'patient_description': 'PatientDescription',
            'allergies': 'Allergies',
            'operations': 'Operations',
            'files': 'Files'
        }

        self._patient_description = patient_description
        self._allergies = allergies
        self._operations = operations
        self._files = files

    @classmethod
    def from_dict(cls, dikt) -> 'MedicalFolder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MedicalFolder of this MedicalFolder.  # noqa: E501
        :rtype: MedicalFolder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def patient_description(self) -> str:
        """Gets the patient_description of this MedicalFolder.


        :return: The patient_description of this MedicalFolder.
        :rtype: str
        """
        return self._patient_description

    @patient_description.setter
    def patient_description(self, patient_description: str):
        """Sets the patient_description of this MedicalFolder.


        :param patient_description: The patient_description of this MedicalFolder.
        :type patient_description: str
        """

        self._patient_description = patient_description

    @property
    def allergies(self) -> List[str]:
        """Gets the allergies of this MedicalFolder.


        :return: The allergies of this MedicalFolder.
        :rtype: List[str]
        """
        return self._allergies

    @allergies.setter
    def allergies(self, allergies: List[str]):
        """Sets the allergies of this MedicalFolder.


        :param allergies: The allergies of this MedicalFolder.
        :type allergies: List[str]
        """

        self._allergies = allergies

    @property
    def operations(self) -> List[str]:
        """Gets the operations of this MedicalFolder.


        :return: The operations of this MedicalFolder.
        :rtype: List[str]
        """
        return self._operations

    @operations.setter
    def operations(self, operations: List[str]):
        """Sets the operations of this MedicalFolder.


        :param operations: The operations of this MedicalFolder.
        :type operations: List[str]
        """

        self._operations = operations

    @property
    def files(self) -> List[object]:
        """Gets the files of this MedicalFolder.


        :return: The files of this MedicalFolder.
        :rtype: List[object]
        """
        return self._files

    @files.setter
    def files(self, files: List[object]):
        """Sets the files of this MedicalFolder.


        :param files: The files of this MedicalFolder.
        :type files: List[object]
        """

        self._files = files
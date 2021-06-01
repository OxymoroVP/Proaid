# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Patient(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, lastname: str=None, user_id: int=None, amka: str=None, email: str=None, telephone: str=None, folder: object=None):  # noqa: E501
        """Patient - a model defined in Swagger

        :param name: The name of this Patient.  # noqa: E501
        :type name: str
        :param lastname: The lastname of this Patient.  # noqa: E501
        :type lastname: str
        :param user_id: The user_id of this Patient.  # noqa: E501
        :type user_id: int
        :param amka: The amka of this Patient.  # noqa: E501
        :type amka: str
        :param email: The email of this Patient.  # noqa: E501
        :type email: str
        :param telephone: The telephone of this Patient.  # noqa: E501
        :type telephone: str
        :param folder: The folder of this Patient.  # noqa: E501
        :type folder: object
        """
        self.swagger_types = {
            'name': str,
            'lastname': str,
            'user_id': int,
            'amka': str,
            'email': str,
            'telephone': str,
            'folder': object
        }

        self.attribute_map = {
            'name': 'Name',
            'lastname': 'Lastname',
            'user_id': 'UserID',
            'amka': 'AMKA',
            'email': 'email',
            'telephone': 'Telephone',
            'folder': 'folder'
        }

        self._name = name
        self._lastname = lastname
        self._user_id = user_id
        self._amka = amka
        self._email = email
        self._telephone = telephone
        self._folder = folder

    @classmethod
    def from_dict(cls, dikt) -> 'Patient':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Patient of this Patient.  # noqa: E501
        :rtype: Patient
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Patient.


        :return: The name of this Patient.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Patient.


        :param name: The name of this Patient.
        :type name: str
        """

        self._name = name

    @property
    def lastname(self) -> str:
        """Gets the lastname of this Patient.


        :return: The lastname of this Patient.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname: str):
        """Sets the lastname of this Patient.


        :param lastname: The lastname of this Patient.
        :type lastname: str
        """

        self._lastname = lastname

    @property
    def user_id(self) -> int:
        """Gets the user_id of this Patient.


        :return: The user_id of this Patient.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this Patient.


        :param user_id: The user_id of this Patient.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def amka(self) -> str:
        """Gets the amka of this Patient.


        :return: The amka of this Patient.
        :rtype: str
        """
        return self._amka

    @amka.setter
    def amka(self, amka: str):
        """Sets the amka of this Patient.


        :param amka: The amka of this Patient.
        :type amka: str
        """

        self._amka = amka

    @property
    def email(self) -> str:
        """Gets the email of this Patient.


        :return: The email of this Patient.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email: str):
        """Sets the email of this Patient.


        :param email: The email of this Patient.
        :type email: str
        """

        self._email = email

    @property
    def telephone(self) -> str:
        """Gets the telephone of this Patient.


        :return: The telephone of this Patient.
        :rtype: str
        """
        return self._telephone

    @telephone.setter
    def telephone(self, telephone: str):
        """Sets the telephone of this Patient.


        :param telephone: The telephone of this Patient.
        :type telephone: str
        """

        self._telephone = telephone

    @property
    def folder(self) -> object:
        """Gets the folder of this Patient.


        :return: The folder of this Patient.
        :rtype: object
        """
        return self._folder

    @folder.setter
    def folder(self, folder: object):
        """Sets the folder of this Patient.


        :param folder: The folder of this Patient.
        :type folder: object
        """

        self._folder = folder
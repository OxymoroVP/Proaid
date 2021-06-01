# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class PatientAppointment(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, a_id: int=None, _date: str=None, time: str=None, name: str=None, notification: object=None):  # noqa: E501
        """PatientAppointment - a model defined in Swagger

        :param a_id: The a_id of this PatientAppointment.  # noqa: E501
        :type a_id: int
        :param _date: The _date of this PatientAppointment.  # noqa: E501
        :type _date: str
        :param time: The time of this PatientAppointment.  # noqa: E501
        :type time: str
        :param name: The name of this PatientAppointment.  # noqa: E501
        :type name: str
        :param notification: The notification of this PatientAppointment.  # noqa: E501
        :type notification: object
        """
        self.swagger_types = {
            'a_id': int,
            '_date': str,
            'time': str,
            'name': str,
            'notification': object
        }

        self.attribute_map = {
            'a_id': 'a_id',
            '_date': 'date',
            'time': 'time',
            'name': 'name',
            'notification': 'notification'
        }

        self._a_id = a_id
        self.__date = _date
        self._time = time
        self._name = name
        self._notification = notification

    @classmethod
    def from_dict(cls, dikt) -> 'PatientAppointment':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PatientAppointment of this PatientAppointment.  # noqa: E501
        :rtype: PatientAppointment
        """
        return util.deserialize_model(dikt, cls)

    @property
    def a_id(self) -> int:
        """Gets the a_id of this PatientAppointment.


        :return: The a_id of this PatientAppointment.
        :rtype: int
        """
        return self._a_id

    @a_id.setter
    def a_id(self, a_id: int):
        """Sets the a_id of this PatientAppointment.


        :param a_id: The a_id of this PatientAppointment.
        :type a_id: int
        """
        if a_id is None:
            raise ValueError("Invalid value for `a_id`, must not be `None`")  # noqa: E501

        self._a_id = a_id

    @property
    def _date(self) -> str:
        """Gets the _date of this PatientAppointment.


        :return: The _date of this PatientAppointment.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date: str):
        """Sets the _date of this PatientAppointment.


        :param _date: The _date of this PatientAppointment.
        :type _date: str
        """

        self.__date = _date

    @property
    def time(self) -> str:
        """Gets the time of this PatientAppointment.


        :return: The time of this PatientAppointment.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time: str):
        """Sets the time of this PatientAppointment.


        :param time: The time of this PatientAppointment.
        :type time: str
        """

        self._time = time

    @property
    def name(self) -> str:
        """Gets the name of this PatientAppointment.


        :return: The name of this PatientAppointment.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this PatientAppointment.


        :param name: The name of this PatientAppointment.
        :type name: str
        """

        self._name = name

    @property
    def notification(self) -> object:
        """Gets the notification of this PatientAppointment.


        :return: The notification of this PatientAppointment.
        :rtype: object
        """
        return self._notification

    @notification.setter
    def notification(self, notification: object):
        """Sets the notification of this PatientAppointment.


        :param notification: The notification of this PatientAppointment.
        :type notification: object
        """

        self._notification = notification

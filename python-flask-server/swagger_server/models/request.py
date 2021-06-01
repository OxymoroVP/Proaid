# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Request(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, r_id: int=None, sender_id: int=None, receiver_id: int=None, message_id: int=None, accepted: bool=None):  # noqa: E501
        """Request - a model defined in Swagger

        :param r_id: The r_id of this Request.  # noqa: E501
        :type r_id: int
        :param sender_id: The sender_id of this Request.  # noqa: E501
        :type sender_id: int
        :param receiver_id: The receiver_id of this Request.  # noqa: E501
        :type receiver_id: int
        :param message_id: The message_id of this Request.  # noqa: E501
        :type message_id: int
        :param accepted: The accepted of this Request.  # noqa: E501
        :type accepted: bool
        """
        self.swagger_types = {
            'r_id': int,
            'sender_id': int,
            'receiver_id': int,
            'message_id': int,
            'accepted': bool
        }

        self.attribute_map = {
            'r_id': 'r_id',
            'sender_id': 'sender_id',
            'receiver_id': 'receiver_id',
            'message_id': 'message_id',
            'accepted': 'accepted'
        }

        self._r_id = r_id
        self._sender_id = sender_id
        self._receiver_id = receiver_id
        self._message_id = message_id
        self._accepted = accepted

    @classmethod
    def from_dict(cls, dikt) -> 'Request':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Request of this Request.  # noqa: E501
        :rtype: Request
        """
        return util.deserialize_model(dikt, cls)

    @property
    def r_id(self) -> int:
        """Gets the r_id of this Request.


        :return: The r_id of this Request.
        :rtype: int
        """
        return self._r_id

    @r_id.setter
    def r_id(self, r_id: int):
        """Sets the r_id of this Request.


        :param r_id: The r_id of this Request.
        :type r_id: int
        """
        if r_id is None:
            raise ValueError("Invalid value for `r_id`, must not be `None`")  # noqa: E501

        self._r_id = r_id

    @property
    def sender_id(self) -> int:
        """Gets the sender_id of this Request.


        :return: The sender_id of this Request.
        :rtype: int
        """
        return self._sender_id

    @sender_id.setter
    def sender_id(self, sender_id: int):
        """Sets the sender_id of this Request.


        :param sender_id: The sender_id of this Request.
        :type sender_id: int
        """

        self._sender_id = sender_id

    @property
    def receiver_id(self) -> int:
        """Gets the receiver_id of this Request.


        :return: The receiver_id of this Request.
        :rtype: int
        """
        return self._receiver_id

    @receiver_id.setter
    def receiver_id(self, receiver_id: int):
        """Sets the receiver_id of this Request.


        :param receiver_id: The receiver_id of this Request.
        :type receiver_id: int
        """

        self._receiver_id = receiver_id

    @property
    def message_id(self) -> int:
        """Gets the message_id of this Request.


        :return: The message_id of this Request.
        :rtype: int
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id: int):
        """Sets the message_id of this Request.


        :param message_id: The message_id of this Request.
        :type message_id: int
        """

        self._message_id = message_id

    @property
    def accepted(self) -> bool:
        """Gets the accepted of this Request.


        :return: The accepted of this Request.
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted: bool):
        """Sets the accepted of this Request.


        :param accepted: The accepted of this Request.
        :type accepted: bool
        """

        self._accepted = accepted

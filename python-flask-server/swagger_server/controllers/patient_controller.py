import connexion
import six

from swagger_server.models.patient_appointment import PatientAppointment  # noqa: E501
from swagger_server.models.request import Request  # noqa: E501
from swagger_server import util


def ar_medical_folder_access(d_id, r_id):  # noqa: E501
    """Patient responds to doctor&#39;s request for medical folder sharing

    FR7 - The registered patient must be able to share their medical history with a doctor # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param r_id: A request&#39;s unique id
    :type r_id: int

    :rtype: None
    """
    return 'do some magic!'


def edit_notification(p_id, a_id):  # noqa: E501
    """Edit an appointment&#39;s notification

    FR11 - The registered patient must be able to edit their notification method for their appointment # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param a_id: Appointment&#39;s unique ID
    :type a_id: int

    :rtype: None
    """
    return 'do some magic!'


def request_appointment(p_id, request):  # noqa: E501
    """Request an appointment at an available time and date

    FR8 - The registered patient must be able to request an appointment at an available time and date # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param request: A patient&#39;s request for an appointment
    :type request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        request = Request.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def review_appointment(p_id, a_id):  # noqa: E501
    """Review a scheduled appointment

    FR12 - The registered patient must be able to review their scheduled appointments # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param a_id: Appointment&#39;s id
    :type a_id: int

    :rtype: None
    """
    return 'do some magic!'


def review_appointments(p_id, appointment):  # noqa: E501
    """Review all scheduled appointments

    FR12 - The registered patient must be able to review their scheduled appointments # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param appointment: A list of a patient&#39;s booked appointments
    :type appointment: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        appointment = PatientAppointment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

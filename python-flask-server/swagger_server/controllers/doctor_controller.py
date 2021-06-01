import connexion
import six

from swagger_server.models.appointment import Appointment  # noqa: E501
from swagger_server.models.calendar import Calendar  # noqa: E501
from swagger_server.models.medical_folder import MedicalFolder  # noqa: E501
from swagger_server.models.patient import Patient  # noqa: E501
from swagger_server.models.request import Request  # noqa: E501
from swagger_server import util


def create_appointment(d_id, appointment):  # noqa: E501
    """Create an appointment

    NOFR - Doctor creates a new appointment through the schedule GUI # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param appointment: New appointment
    :type appointment: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        appointment = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_appointment_menu(d_id, appointment):  # noqa: E501
    """Create an appointment

    NOFR - Doctor creates an appointment through a menu # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param appointment: New appointment
    :type appointment: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        appointment = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_unregistered_patient(patient, d_id):  # noqa: E501
    """Creates a new unregistered patient

    FR3 - The doctor must be able to create a new patient&#39;s history file # noqa: E501

    :param patient: Unregisterd Patient object to be created
    :type patient: dict | bytes
    :param d_id: Doctor&#39;s unique id
    :type d_id: int

    :rtype: None
    """
    if connexion.request.is_json:
        patient = Patient.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_appointment(d_id, a_id):  # noqa: E501
    """Delete an appointment

    FR1 - The doctor must be able to edit their scheduled appointments # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param a_id: Appointment&#39;s unique ID
    :type a_id: int

    :rtype: None
    """
    return 'do some magic!'


def delete_unregistered_patient(d_id, p_id):  # noqa: E501
    """Delete unregistered patient

    NOFR -The doctor can delete an Unregistered Patient # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param p_id: Patient&#39;s unique id
    :type p_id: int

    :rtype: None
    """
    return 'do some magic!'


def doctor_send_request(d_id, request):  # noqa: E501
    """Send a request

    FR5 - The doctor must be able to request access to view and modify a patient’s medical history # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param request: The request to be sent
    :type request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        request = Request.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_appointment(d_id, a_id, appointment):  # noqa: E501
    """Edit an appointment

    FR1 - The doctor must be able to edit their scheduled appointments # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param a_id: Appointment&#39;s unique ID
    :type a_id: int
    :param appointment: The appointment object
    :type appointment: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        appointment = Appointment.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_folder(p_id, medicalfolder):  # noqa: E501
    """Edit medical folder of a registered patient

    FR6 - The doctor must be able to modify their assigned patient&#39;s medical history # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: str
    :param medicalfolder: Medical folder to be updated
    :type medicalfolder: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medicalfolder = MedicalFolder.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_unregistered_folder(p_id, d_id, medicalfolder):  # noqa: E501
    """Doctor edits an unregistered patient&#39;s medical folder

    FR6 - The doctor must be able to modify their assigned patient&#39;s medical history # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param medicalfolder: Medical folder to be updated
    :type medicalfolder: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medicalfolder = MedicalFolder.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def edit_unregistered_patient(p_id, d_id):  # noqa: E501
    """Edit by patient id

    NOFR - The doctor can edit Unregistered Patient&#39;s attributes # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param d_id: Doctor&#39;s unique id
    :type d_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_registered_patient(p_id):  # noqa: E501
    """Get registered patient&#39;s info

    NOFR - The doctor must be able to view a registered patient&#39;s details # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int

    :rtype: None
    """
    return 'do some magic!'


def get_schedule(d_id, calendar):  # noqa: E501
    """View schedule

    FR2 - The doctor must be able to review their schedule # noqa: E501

    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param calendar: The doctor&#39;s displayed schedule
    :type calendar: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        calendar = Calendar.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_unregistered_folder(p_id, d_id, medicalfolder):  # noqa: E501
    """Get medical folder of a patient by patient id

    NOFR -The doctor must be able to view an unregistered patient&#39;s medical folder # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: str
    :param d_id: Doctor&#39;s unique id
    :type d_id: int
    :param medicalfolder: Medical folder to be received
    :type medicalfolder: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medicalfolder = MedicalFolder.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_unregistered_patient(p_id, d_id):  # noqa: E501
    """Get a patient by patient id

    NOFR - The doctor must be able to view an unregistered  patient&#39;s details # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param d_id: Doctor&#39;s unique id
    :type d_id: int

    :rtype: None
    """
    return 'do some magic!'


def patient_ar_appointment(p_id, r_id):  # noqa: E501
    """Accept/Reject a request for appointment

    FR9 - The doctor must be able to accept/reject a request for appointment # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param r_id: Request&#39;s unique id
    :type r_id: int

    :rtype: None
    """
    return 'do some magic!'

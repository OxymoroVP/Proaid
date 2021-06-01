import connexion
import six

from swagger_server.models.medical_folder import MedicalFolder  # noqa: E501
from swagger_server import util


def get_folder(p_id, medicalfolder):  # noqa: E501
    """Get medical folder of a patient by patient id

    FR6 - The doctor must be able to view their assigned patient&#39;s medical history # noqa: E501

    :param p_id: Patient&#39;s unique id
    :type p_id: int
    :param medicalfolder: Medical folder to be updated
    :type medicalfolder: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        medicalfolder = MedicalFolder.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

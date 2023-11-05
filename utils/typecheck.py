from uuid import UUID
from shared.view_tools import exceptions


def validateUUID(uuid_id: str, error_message: str = "Invalid uuid string"):
    try:
        UUID(uuid_id)
    except ValueError:
        raise exceptions.ApiException(error_message)

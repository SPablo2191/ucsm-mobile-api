from enum import Enum
class TableStatus(Enum):
    """
    Use to filter per table row status
    Return:
    ACTIVE => It is an active register
    INACTIVE => It is not an active register
    """
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
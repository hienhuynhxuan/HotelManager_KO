import enum


class Status(enum.Enum):
    ThereIsRoom = "There Is Room"
    OutOfRoom = "Out Of Room"
    Reserve = "Reserve"


class UserRole(enum.Enum):
    ADMIN = "Quản trị viên"
    USER = "Lễ Tân"

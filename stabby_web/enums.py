from enum import Enum


class Module(Enum):
    Dashboard = "dashboard"
    Knives = "knives"
    Sharpeners = "sharpeners"


class FormType(Enum):
    Add = "add"
    Edit = "edit"

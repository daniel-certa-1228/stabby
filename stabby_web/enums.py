from enum import Enum


class Modules(Enum):
    Dashboard = "dashboard"
    Knives = "knives"
    Sharpeners = "sharpeners"


class FormTypes(Enum):
    Add = "add"
    Edit = "edit"


class UnitsOfMeasure(Enum):
    inches = 1
    centimeters = 2


class ViewTypes(Enum):
    KnifeGrid = 1
    SharpenerGrid = 2
    KnifeDetail = 3
    SharpenerDetail = 4
    KnifeAddEdit = 5
    SharpenerAddEdit = 6
    BladeAddEdit = 7
    KnifeWorkLogAddEdit = 8
    SharpenerWorkLogAddEdit = 9,
    KnifePhotoAddEdit = 10,
    SharpenerPhotoAddEdit = 11,

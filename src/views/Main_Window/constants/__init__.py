from enum import Enum
from PyQt6.QtGui import QColor


class COLORS(Enum):
    DARK = QColor(39, 60, 117)


class VIEWS(Enum):
    MENU_BAR = '0'
    IMAGE_SECTION = '1'
    FORM_SECTION = '2'



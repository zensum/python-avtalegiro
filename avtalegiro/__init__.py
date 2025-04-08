"""File parsers for Nets AvtaleGiro and OCR Giro files."""

from typing import List

from avtalegiro.constants import *
from avtalegiro.enums import *
from avtalegiro.objects import *
from avtalegiro.utils import *

from avtalegiro import constants, enums, objects, utils  # isort: skip

__version__ = '1.3.0'

__all__: List[str] = constants.__all__ + enums.__all__ + objects.__all__ + utils.__all__

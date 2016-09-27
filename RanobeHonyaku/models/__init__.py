"""
This guarantees that we have all db classes, but also means that we might import things we don't need.
But then again, if we don't do this, we must be very careful about circular references.
We also bypass from db.admiral import Admiral and simply use from db import Admiral.
Overall, importing everything sounds like a reasonable choice.
"""

from RanobeHonyaku.models.series import *
from RanobeHonyaku.models.chapter import *
from RanobeHonyaku.models.user import *


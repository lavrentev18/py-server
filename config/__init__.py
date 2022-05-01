from dotenv import load_dotenv

load_dotenv(".env")

"""Config application"""

from .app import *
from .database import *
from .views import *

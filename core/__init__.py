"""Core packages for fullstack server"""

__all__ = [
  "app",
  "router",
  "DB",
  "templateEngine"
]

from core.server import app
from core.router import router
from core.database import DB
from core.view import templateEngine

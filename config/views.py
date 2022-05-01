import os

TEMPLATES_DIR = os.path.abspath(
  os.path.join(
      os.path.dirname(__file__), 
      '..', 
      os.getenv("TEMPLATES_DIR", "views")
    )
  )

TEMPLATES_EXTENSION = os.getenv("TEMPLATES_EXTENSION", ".jinja.html")

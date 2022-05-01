up_query = """
CREATE TABLE IF NOT EXISTS posts (
  id SERIAL PRIMARY KEY,
  title VARCHAR(30) NOT NULL,
  description TEXT
)
"""

down_query = """
DROP TABLE IF EXISTS posts
"""

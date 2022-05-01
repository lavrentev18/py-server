from core import DB

query = """
INSERT INTO posts ("title", "description") VALUES
  ('Post #1', 'Post #1 description'),
  ('Post #2', 'Post #2 description'),
  ('Post #3', 'Post #3 description'),
  ('Post #4', 'Post #4 description'),
  ('Post #5', 'Post #5 description'),
  ('Post #6', 'Post #6 description'),
  ('Post #7', 'Post #7 description'),
  ('Post #8', 'Post #8 description'),
  ('Post #9', 'Post #9 description'),
  ('Post #10', 'Post #10 description');
"""

def seed():
  try:
    DB.connect()

    DB.execute(query)

    DB.disconnect()
    print("Seed is complete")
  except Exception as e:
    print(f"[SEED ERROR({e.__class__})]: Detailed: {e}", flush = True)
    raise e

seed()

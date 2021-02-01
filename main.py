import os
from dotenv import load_dotenv

load_dotenv()
KEY_ID = os.getenv("KEY_ID")
SECRET_KEY = os.getenv("SECRET_KEY")

print(KEY_ID, SECRET_KEY)

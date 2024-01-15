import os
from dotenv import load_dotenv

load_dotenv()

class TestConfig:
    API_KEY = os.getenv("TEST_API_KEY")
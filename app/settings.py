import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

RECEIVER_PASSWORD = env("RECEIVER_PASSWORD")

DEBUG = env.bool("DEBUG", default=False)
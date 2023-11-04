import environ
from pathlib import Path

env = environ.Env(
    VITE_PRODUCT_NAME=(str, None),
    DJ_SHARED_FRONTEND_URL=(str, None),
    DJ_SHARED_FRONTEND_ICON_URL=(str, None),
    DJ_SHARED_FRONTEND_AUTH_CALLBACK=(str, None),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / ".env")

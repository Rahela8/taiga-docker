from .common import *

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = "64.233.167.109" #vers prec: "smtp.gmail.com"
EMAIL_PORT = 587  # 465 se usi SSL
EMAIL_HOST_USER = "raheladoc23@gmail.com"
EMAIL_HOST_PASSWORD = "thwruylduoqxavyz"
DEFAULT_FROM_EMAIL = "raheladoc23@gmail.com"


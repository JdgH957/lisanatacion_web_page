import logging

APP_LOGGER = logging.getLogger('app')
APP_LOGGER.setLevel(
    logging.DEBUG
    )

SECRET_KEY = "tu_clave_super_segura"
ALGORITHM = "HS256"
EXPIRATION_ACCESS_MINUTES = 60
EXPIRATION_REFRESH_MINUTES = 1440

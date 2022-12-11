

dict_conf = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(name)s | %(asctime)s | %(lineno)d | %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "base",
            "stream": "ext://sys.stdout",
        },
        "file_e": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "base",
            "filename": "error.log",
            "mode": "a",
        },
        "file_w": {
            "class": "logging.FileHandler",
            "level": "WARNING",
            "formatter": "base",
            "filename": "warning.log",
            "mode": "a",
        },
        "file_i": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "base",
            "filename": "info.log",
            "mode": "a",
        },
        "file_d": {
            "class": "logging.FileHandler",
            "level": "DEBUG",
            "formatter": "base",
            "filename": "debug.log",
            "mode": "a",
        },
    },
    "loggers": {
        "calc_logger": {
            "level": "INFO",
            "handlers": ["console", "file_d", "file_e", "file_i", "file_w"],
        },
        "utils_logger": {
            "level": "INFO",
            "handlers": ["console", "file_d", "file_e", "file_i", "file_w"],
        }
    }
}
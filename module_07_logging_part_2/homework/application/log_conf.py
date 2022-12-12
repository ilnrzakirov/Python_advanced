import json
import logging
from logging.handlers import HTTPHandler

class ASCIIFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        return record.getMessage().isascii()


class ToFlask(HTTPHandler):
  def to_flask(self, record):
    record = {'record': json.dumps(record.__dict__)}
    return record


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
        "time_handler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "INFO",
            "formatter": "base",
            "filename": "utils.log",
            "when": "S",
            "interval": 10,
            "backupCount": "2",
        },
        "http_handler": {
            "()": ToFlask,
            "level": "INFO",
            "host": "localhost:5005",
            "method": "POST",
            "url": "/log"
        }
    },
    "filters": {
        "ascii": {
            "()": ASCIIFilter
        }
    },
    "loggers": {
        "calc_logger": {
            "level": "INFO",
            "handlers": ["console", "file_d", "file_e", "file_i", "file_w", "http_handler"],
            "filters": ["ascii", ],
        },
        "utils_logger": {
            "level": "INFO",
            "handlers": ["console", "file_d", "file_e", "file_i", "file_w", "time_handler"],
        }
    },
}

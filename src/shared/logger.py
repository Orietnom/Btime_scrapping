import os
from loguru import logger
from datetime import datetime
import pytz
import sys
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


BASE_DIR = Path(__file__).resolve().parent.parent.parent
LOG_DIR = (BASE_DIR / 'logs').resolve()
LOG_DIR.mkdir(parents=True, exist_ok=True)

today = datetime.now(pytz.timezone("America/Sao_Paulo")).strftime("Log_%Y%m%d.log")
log_path = os.path.join(LOG_DIR, 'win_catalog.log')

logger.remove()

logger.add(
    log_path,
    rotation="00:00",
    retention="30 days",
    compression="zip",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function} | {message} | {extra}",
    level="DEBUG",
    enqueue=True,
)

logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}:{function}</cyan> | <level>{message}</level>",
    level="DEBUG",
    enqueue=True,
)

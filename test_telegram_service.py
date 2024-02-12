from utils.telegram_service import send_telegram_message
import warnings
warnings.filterwarnings("ignore")
import time
import os
from dotenv import load_dotenv
import paramiko
from datetime import datetime
from prefect.futures import PrefectFuture
from prefect import flow, task, get_run_logger
import prefect
from utils.telegram_service import send_telegram_message
load_dotenv()


telegram_msg = """
<b><i><u>Title: Happy Chinese New Year</u></i></b>

<b>Desciption: a celebration of the arrival of spring and the beginning of a new year on the lunisolar calendar</b>
"""

send_telegram_message(telegram_msg)
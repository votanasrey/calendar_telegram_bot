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
from utils.reader_csv_service import call_read_csv
load_dotenv()

dir = "./data/calendar_data.csv"

def read_data(): 
    data = call_read_csv(dir) 
    return data


@task
def task_full_operation():
    pass

@flow(timeout_seconds=900, retry_delay_seconds=900, log_prints=True, retries=3)
def flow_full_operation():
    start_time = datetime.now()
    logger     = get_run_logger()

    task_full_operation()

    end_time = datetime.now()
    logger.info('Duration: {}'.format(end_time - start_time))



if __name__ == "__main__":
    flow_full_operation()
import time
import random
from celery import Celery
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

app = Celery('tasks',
             broker='amqp://prabhakar:prabha@rabbit:5672',
             backend='rpc://')


@app.task()
def longtime_add(x, y):
    logger.info("*"*80)
    logger.info('Got Request - Starting work ')
    
    random_number = x = random.randint(10,20)
    logger.info(f'Waiting - {random_number} seconds')
    time.sleep(random_number)
    
    logger.info(f'Work Finished with result {x}+{y} = {x + y}')
    logger.info("*"*80)
    return x + y

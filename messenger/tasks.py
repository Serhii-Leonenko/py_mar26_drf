from celery import shared_task

from messenger.utils import long_time_function


@shared_task()
def long_task():
    long_time_function()

    return "Done!"

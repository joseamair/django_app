from celery import shared_task

@shared_task
def sharedtask()->None:
    """
    This is a shared task that can be called by any Django app.
    """
    return None

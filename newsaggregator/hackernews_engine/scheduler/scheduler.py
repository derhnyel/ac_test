from apscheduler.schedulers.background import BackgroundScheduler
from hackernews_engine import tasks
from datetime import datetime


def start():
    """Create BackgroundScheduler instance and run task on intervals"""
    scheduler = BackgroundScheduler(timezone="Asia/Beirut")
    now = datetime.now()
    scheduler.add_job(tasks.main,args=['top'],trigger="interval",minutes=30,id="FetchTopTaskid",replace_existing=True,misfire_grace_time=None,next_run_time=now)# add task to backgroud scheduler and run at intervals
    scheduler.add_job(tasks.main,args=['new'],trigger="interval",minutes=30,id="FetchNewTaskid",replace_existing=True,misfire_grace_time=None,next_run_time=now)# add task to backgroud scheduler and run at intervals
    scheduler.start()
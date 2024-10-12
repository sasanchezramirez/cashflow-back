from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from dependency_injector.wiring import inject, Provide
import logging

logger = logging.getLogger(__name__)

class SchedulerService:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        logger.info("Scheduler started.")

    def schedule_monthly_task(self, func):
        trigger = CronTrigger(day=11, hour=1, minute=38)
        self.scheduler.add_job(func, trigger)
        logger.info("Monthly task scheduled.")

    def schedule_weekly_task(self, func):
        trigger = CronTrigger(day_of_week='mon', hour=0, minute=1)
        self.scheduler.add_job(func, trigger)
        logger.info("Weekly task scheduled for every Monday.")



    def shutdown(self):
        self.scheduler.shutdown()
        logger.info("Scheduler shut down.")

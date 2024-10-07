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
        trigger = CronTrigger(day=7, hour=23, minute=37)
        self.scheduler.add_job(func, trigger)
        logger.info("Monthly task scheduled.")

    def shutdown(self):
        self.scheduler.shutdown()
        logger.info("Scheduler shut down.")

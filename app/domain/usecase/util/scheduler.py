from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from app.domain.usecase.budget_balance_usecase import BudgetBalanceUseCase
import logging

logger = logging.getLogger(__name__)

class SchedulerService:
    def __init__(self, budgetBalanceUseCase: BudgetBalanceUseCase):
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()
        self.schedule_monthly_task(budgetBalanceUseCase.monthly_task)
        self.schedule_weekly_task(budgetBalanceUseCase.weekly_task)
        logger.info("Scheduler started.")

    def schedule_monthly_task(self, func):
        trigger = CronTrigger(day=12, hour=15, minute=26)
        self.scheduler.add_job(func, trigger)
        logger.info("Monthly task scheduled.")

    def schedule_weekly_task(self, func):
        trigger = CronTrigger(day_of_week='sat', hour=15, minute=15)
        self.scheduler.add_job(func, trigger)
        logger.info("Weekly task scheduled for every Monday.")



    def shutdown(self):
        self.scheduler.shutdown()
        logger.info("Scheduler shut down.")

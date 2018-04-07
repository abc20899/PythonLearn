from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    print("Hello World")


# BlockingScheduler
sched = BlockingScheduler()
# 每隔2小时执行一次任务
# sched.add_job(job_function, 'interval', hours=2)
# 任务开始于 2010-10-10 at 9:30 停止于 2014-06-15 at 11:00
# sched.add_job(job_function, 'interval', hours=2, start_date='2010-10-10 09:30:00', end_date='2014-06-15 11:00:00')
sched.add_job(job_function, 'interval', seconds=2)
sched.start()

'''
interval参数
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
'''

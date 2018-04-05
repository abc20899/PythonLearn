import time
from apscheduler.schedulers.blocking import BlockingScheduler


def test_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

scheduler = BlockingScheduler()
'''
 #该示例代码生成了一个BlockingScheduler调度器，使用了默认的默认的任务存储MemoryJobStore，
 以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。
'''
scheduler.add_job(test_job, 'interval', seconds=5, id='test_job')
'''
 #该示例中的定时任务采用固定时间间隔（interval）的方式，每隔5秒钟执行一次。
 #并且还为该任务设置了一个任务id
'''
scheduler.start()


#sched.add_job(job_function, 'interval', hours=2)

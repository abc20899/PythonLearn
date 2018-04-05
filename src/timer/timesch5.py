'''
scheduler 事件
scheduler 可以添加事件监听器，并在特殊的时间触发。


关闭 job
scheduler.shutdown()
scheduler.shutdown(wait=False)
'''
from sched import scheduler

from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR


def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')
# 添加监听器
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

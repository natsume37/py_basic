import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
from settings import *


def email_send():
    yag_server = yagmail.SMTP(user="1957074599@qq.com", password="hkhcbzleakcgdgfa", host='smtp.qq.com')
    email_to = ['2047672631@qq.com', ]
    # email_to = ['natsume37@outlook.com', ]
    email_title = "Mr.liu 每日打卡提醒来喽！"
    email_content = """今天别忘了工学云打卡偶！
                            ding
    """
    # '2047672631@qq.com',
    yag_server.send(email_to, email_title, email_content)
    LOGGER.info("发送完成")
    yag_server.close()


if __name__ == '__main__':
    LOGGER.info("任务开始执行")
    try:
        sched = BlockingScheduler()
        sched.add_job(email_send, 'interval', days=1, id='my_job_id')
        sched.start()
    except Exception as e:
        LOGGER.warning(e)
        yag_server = yagmail.SMTP(user="1957074599@qq.com", password="hkhcbzleakcgdgfa", host='smtp.qq.com')
        # email_to = ['2047672631@qq.com', ]
        email_to = ['natsume37@outlook.com', '2047672631@qq.com']
        email_title = "程序报错警告、请联系管理员"
        email_content = f"程序出错了！！{e}"
        # '2047672631@qq.com',
        yag_server.send(email_to, email_title, email_content)
        LOGGER.info("发送完成")
        yag_server.close()

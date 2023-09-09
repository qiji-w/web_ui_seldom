import os
import sys
import click
import seldom
from selenium.webdriver import ChromeOptions

from config import privatization_config
from util.tools import email

root_dir = os.path.dirname(__file__)
sys.path.append(root_dir)


@click.command()
@click.option("-e", "--env", default="https://pri-poc.mastergo.com/", type=str, help="环境")
@click.option("-u", "--user", default="mastergo-e2e@jwzg.com", type=str, help="账号")
@click.option("-p", "--pwd", default="mastergoe2e!", type=str, help="密码")
@click.option("-ml", "--mail_url", default="https://pri.mastergo.com/push-service/messages/send/smtp", type=str,
              help="邮箱地址")
@click.option("-m", "--mail", default="wangbingqi@jwzg.com", type=str, help="发送邮箱")
@click.option("-t", "--title", default="测试e2e", type=str, help="邮箱标题")
@click.option("-c", "--content", type=str, help="邮箱内容")
@click.option("-d", "--disk_url", type=str,
              default="http://172.28.20.124/monitor/prometheus/172-28-20-124/api/v1/query",
              help="磁盘地址")
@click.option("-h", "--hub", default="https://selenium-hub.mastergo.com", type=str, help="selenium-hub")
def run(env: str, user: str, pwd: str, mail_url: str, mail: str, title: str, content: str, disk_url: str, hub: str, ):
    privatization_config.TEST_URL = env
    privatization_config.TEST_ACCOUNT = user
    privatization_config.TEST_PASSWORD = pwd
    # selenium-hub
    # seldom.ChromeConfig.command_executor = hub

    chrome_options = ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser = {
        "browser": "chrome",
        "executable_path": f"/root/.wdm/drivers/chromedriver/linux64/112.0.5615/chromedriver",
        "options": chrome_options
    }

    seldom.main(
        path="page/test_workbench01.py",
        browser=browser,
        # browser="gc",
        title="MG-私有化测试报告",
        report="report.html",
        tester="杨硕硕",
        description="私有化-自动化测试用例",
        debug=False  # debug 开关 True/False
    )
    if content:
        email(mail_url, mail, title, disk_url, content)
    else:
        email(mail_url, mail, title, disk_url)


if __name__ == '__main__':
    run()

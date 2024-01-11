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
@click.option("-e", "--env", default="https://mastergo.com/login", type=str, help="环境")
@click.option("-u", "--user", default="mastergo-e2e@jwzg.com", type=str, help="账号")
@click.option("-p", "--pwd", default="mastergoe2e!", type=str, help="密码")
@click.option("-h", "--hub", default="https://selenium-hub.mastergo.com", type=str, help="selenium-hub")
def run(env: str, user: str, pwd: str, hub: str, ):
    privatization_config.TEST_URL = env
    privatization_config.TEST_ACCOUNT = user
    privatization_config.TEST_PASSWORD = pwd
    # selenium-hub
    # seldom.ChromeConfig.command_executor = hub

    chrome_options = ChromeOptions()
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.add_argument('lang=zh_CN.UTF-8')
    # chrome_options.add_argument('headless')
    # chrome_options.add_argument('--no-sandbox')
    # chrome_options.add_argument('--disable-dev-shm-usage')

    browser = {
        "browser": "chrome",
        "executable_path": f"/Users/wangbingqi/work/python/web_app_ui_seldom/120.0.6099.109/chromedriver",
        "options": chrome_options
    }

    seldom.main(
        path="page/test_workbench01.py",
        browser=browser,
        # browser="gc",
        title="MG-私有化测试报告",
        report="report.html",
        tester="如果奇迹有颜色",
        description="私有化-自动化测试用例",
        debug=False  # debug 开关 True/False
    )


if __name__ == '__main__':
    run()

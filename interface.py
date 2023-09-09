import os
import time
import hashlib

import click
import htmlmin
import requests

from util.tools import disk


@click.command()
@click.option("-p", "--path", default=".", type=str, help="mastergo_test目录")
@click.option("-ml", "--mail_url", default="https://127.0.0.1/push-service/messages/send/smtp", type=str,
              help="邮箱地址")
@click.option("-m", "--mail", default="wangbingqi@jwzg.com", type=str, help="发送邮箱")
@click.option("-t", "--title", default="接口自动化", type=str, help="邮箱标题")
@click.option("-d", "--disk_url", type=str,
              default="http://127.0.0.1/monitor/prometheus/172-28-20-124/api/v1/query",
              help="磁盘地址")
@click.option("-b", "--debug", type=str,
              default="true",
              help="debug")
@click.option("-e", "--env", type=str,
              default="pri",
              help="env")
@click.option("-a", "--apiurl", type=str,
              default="127.0.0.1",
              help="apiurl")
def interface(path: str = '',
              mail_url: str = "https://127.0.0.1/push-service/messages/send/smtp",
              mail: str = "wangbingqi@jwzg.com",
              title: str = "接口自动化",
              disk_url: str = "http://127.0.0.1/monitor/prometheus/172-28-20-124/api/v1/query",
              debug: str = "true",
              env: str = "pri",
              apiurl: str = "https://pri.mastergo.com",
              ):
    # 初始化删除
    if (os.path.exists(f'{path}/api_test.html')):
        os.unlink(f'{path}/api_test.html')
        time.sleep(2)

    if (os.path.exists(f'{path}/rbac_test.html')):
        os.unlink(f'{path}/rbac_test.html')
        time.sleep(2)

    # 执行
    if (os.path.exists(f'{path}/mastergo_test')):
        print(f'{path}/mastergo_test')
        command = f'DEBUG={debug} ENV={env} API_URL={apiurl} {path}/mastergo_test'
        os.system(command)
        time.sleep(3)

    # 压缩
    if (os.path.exists(f'{path}/api_test.tar.gz')):
        os.unlink(f'{path}/api_test.tar.gz')
        time.sleep(2)

    if (os.path.exists(f'{path}/rbac_test.tar.gz')):
        os.unlink(f'{path}/rbac_test.tar.gz')
        time.sleep(2)

    command = f'tar -czvf {path}/api_test.tar.gz {path}/api_test.html'
    os.system(command)
    time.sleep(2)

    command = f'tar -czvf {path}/rbac_test.tar.gz {path}/rbac_test.html'
    os.system(command)
    time.sleep(2)

    # 发送
    APP_ID = "e2e"
    APP_SECRET = "cCbiFGmLwSKceFrIOkMy"
    timestamp = str(int(time.time()))
    key = f"{APP_ID}{APP_SECRET}{timestamp}".encode(encoding='UTF-8', errors='strict')
    s = hashlib.sha256()
    s.update(key)
    token = s.hexdigest()
    Authentication = f"MGS-{APP_ID}-{timestamp}-{token}"

    with open(f'{path}/api_test.tar.gz', mode="rb") as file:
        api_testTar = file.read()
    with open(f'{path}/rbac_test.tar.gz', mode="rb") as file:
        rbac_testTar = file.read()

    files = [
        ('[]file', ('api_test.tar.gz', api_testTar)),
        ('[]file', ('rbac_test.tar.gz', rbac_testTar)),
    ]

    payload = {
        "subject": title,
        "[]receiver": mail,
        "html": f'磁盘百分比: {disk(disk_url)}\n\n',
    }

    res = requests.post(mail_url, headers={"X-MG-Authentication": Authentication}, data=payload, files=files)
    print(res.text)


if __name__ == '__main__':
    interface()

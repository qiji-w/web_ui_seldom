import os
import time
import hashlib

import htmlmin
import requests

root_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
reports = os.path.join(root_dir, "reports")


def disk(url: str = "http://127.0.0.1/monitor/prometheus/172-28-20-124/api/v1/query"):
    """
    磁盘容量百分比
    """
    data = {
        "query": '(node_filesystem_size_bytes{fstype=~"ext4|xfs"} - on(device) node_filesystem_avail_bytes{fstype=~"ext4|xfs"}) / on(device) node_filesystem_size_bytes{fstype=~"ext4|xfs"}'}
    try:
        s = requests.post(url=url, data=data, verify=False)
        num = round(float(s.json()["data"]["result"][0]["value"][1]), 2)
        return str(round(num * 100)) + "%"

    except Exception as e:
        return '< 获取数据失败 >'


def compressHtml():
    if (os.path.exists(f'{reports}/report.tar.gz')):
        os.unlink(f'{reports}/report.tar.gz')
        time.sleep(2)

    command = f'tar -czvf ./reports/report.tar.gz ./reports/report.html'
    os.system(command)
    time.sleep(2)


def reportPath(val: str) -> str:
    if (os.path.isdir(reports)):
        file_path = os.path.join(reports, val)
        if (os.path.exists(file_path)):
            return file_path


def email(url: str = "https://127.0.0.1/push-service/messages/send/smtp", mail: str = "wangbingqi@jwzg.com",
          title: str = "测试e2e", disk_url: str = "http://127.0.0.1/monitor/prometheus/172-28-20-124/api/v1/query",
          content: str = None):
    compressHtml()

    APP_ID = "e2e"
    APP_SECRET = "cCbiFGmLwSKceFrIOkMy"
    timestamp = str(int(time.time()))
    key = f"{APP_ID}{APP_SECRET}{timestamp}".encode(encoding='UTF-8', errors='strict')
    s = hashlib.sha256()
    s.update(key)
    token = s.hexdigest()
    Authentication = f"MGS-{APP_ID}-{timestamp}-{token}"

    # with open(reportPath('report.html'), mode="rb") as file:
    #     html = file.read()
    # with open(reportPath('cc.png'), mode="rb") as file:
    #     png = file.read()
    with open(reportPath('report.tar.gz'), mode="rb") as file:
        reportTar = file.read()
    with open(reportPath('report.html'), mode="r") as file:
        html_txt = file.read()
    minified = htmlmin.minify(html_txt, remove_empty_space=True)

    files = [
        # ('[]file', ('report.html', html)),
        ('[]file', ('report.tar.gz', reportTar)),
        # ('[]file', ('report.png', png))
    ]

    if content:
        payload = {
            "subject": title,
            "[]receiver": mail,
            "html": f'磁盘百分比: {disk(disk_url)}\n\n' + content,
        }
    else:
        payload = {
            "subject": title,
            "[]receiver": mail,
            "html": f'磁盘百分比: {disk(disk_url)}\n\n' + minified,
        }

    res = requests.post(url, headers={"X-MG-Authentication": Authentication}, data=payload, files=files)
    print(res.text)


def TextFileSearch(txtFile, string):
    """
    查找文本文件中指定字符串
    """
    count = 0
    listLine = []
    data = []
    f = open(txtFile, 'r', encoding='utf-8')
    for line in f.readlines():
        if string in line:
            listLine.append(count)
            data.append(line)
        count += 1
    f.close()
    # 行数
    if len(listLine):
        print(data)
        for i in range(len(listLine)):
            print("在" + txtFile + "第" + str(listLine[i]) + " 行已找到.")


if __name__ == '__main__':
    print(interface())

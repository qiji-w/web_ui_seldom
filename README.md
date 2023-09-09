# 项目
> 
> WEB UI 自动化测试项目.
> 
> ui框架-seldom：https://github.com/SeldomQA/seldom
> 
> 设计模式: poium [page object]: https://github.com/SeldomQA/poium


# 项目结构

目录结构：

```
mge2e/
├── README.md
├── case
│   ├── client
│   │   ├── test_login.py
│   │   └── test_logout.py
│   ├── grow
│   │   └── testcase.py
│   └── importAndExport
│       └── test_import.py
├── common
├── config
├── drivers
├── pages
│   ├── client.py
│   ├── community.py
│   ├── login.py
│   ├── official_website.py
│   └── workbench.py
├── reports
│   └── seldom_log.log
├── requirements.txt
├── run.py
├── suite
│   ├── suite_dingding_login.json
│   ├── suite_email_login_and_logout.json
│   ├── suite_mobile_login_and_logout.json
│   └── suite_register.json
└── test_data
```

* `pages/` page层封装目录，集合页面中的各个元素定位信息；
* `case/` 测试用例目录，存放具体的用例；
* `test_data/` 测试数据目录；
* `reports/` 测试报告目录；
* `common/` 一些公用方法和工具;
* `config/` 配置文件;
* `run.py` 运行入口;

# 开发规范
## 一、page文件命名格式
1. 按照页面划分page文件
```
├── pages/
│   ├── login.py：登录相关相关
│   ├── workbench_page.py：工作台相关
│   ├── community.py：社区相关
│   ├── team.py：团队相关
│   ├── official_website.py：官网相关
│   ├── file.py：文件页相关
```

2. 每次修改完pages文件夹下的文件之后，及时合并master并提交

## 二、元素命名格式
### 1. 命名格式
- 类：驼峰法命名【eg: LoginPage】
- 元素：全部小写字母，下划线连接【eg: btn_import_figma_url_tab】
### 2. 元素命名格式统一前缀
- “btn_”元素：按钮类元素
```
btn_password_login = Element(xpath='//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/span', describe="密码登录按钮")

btn_dingding_login = Element(xpath='//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/button', describe="钉钉登录按钮")
```

- “input_”元素：输入类元素
```
input_username = Element(xpath='//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/input[1]', describe="用户名输入")

input_password = Element(xpath='//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[7]/input', describe="密码输入")
```

- “view_”元素：查看类元素
```
view_welcome = Element(xpath='//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[1]', describe="欢迎回来")
```

### 3. 元素根据页面位置，放在固定类下
```
1. 结构
├── pages/
│   ├── workbench_page.py


2. workbench_page.py下有多个类：    
├── pages/
│   ├── workbench_page.py
│   │    ├── class Import(Page)
│   │    ├── class Files(Page)
│   │    ├── class Community(Page)
│   │    ├── class Others(Page)

3. 工作台下的元素，划分为导入类、社区类、文件类以及其他类，那么元素分类为：
├── pages/
│   ├── workbench_page.py
│   │    ├── class Import(Page)
│   │    │    ├── btn_import_home（导入主按钮）
│   │    │    ├── btn_import_figma_url_tab（figma链接导入tab）
│   │    │    ├── input_import_figma_url（figma链接输入框）
│   │    │    ├── ...
│   │    ├── class Files(Page)
│   │    │    ├── btn_new_file(新建按钮）
│   │    │    ├── btn_open_file(打开文件)
│   │    │    ├── ...
│   │    ├── class Community(Page)
│   │    │    ├── view_resource_title(优质资源)
│   │    │    ├── btn_resource_look_more(查看更多优质资源)
│   │    │    ├── ...
│   │    ├── class Others(Page)
│   │    │    ├── btn_avatar(用户头像)
│   │    │    ├── btn_logout(退出登录)
│   │    │    ├── ...
```

# 运行用例

```python
> python run.py

              __    __
   ________  / /___/ /___  ____ ____
  / ___/ _ \/ / __  / __ \/ __ ` ___/
 (__  )  __/ / /_/ / /_/ / / / / / /
/____/\___/_/\__,_/\____/_/ /_/ /_/  v2.10.2
-----------------------------------------
                             @itest.info

[WDM] - ====== WebDriver manager ======
[WDM] - Current google-chrome version is 103.0.5060
[WDM] - Get LATEST chromedriver version for 103.0.5060 google-chrome
[WDM] - Driver [/Users/huxw/.wdm/drivers/chromedriver/mac64/103.0.5060.53/chromedriver] found in cache

XTestRunner Running tests...

----------------------------------------------------------------------
2022-07-08 17:51:02 log.py | INFO | 📖 127.0.0.1/files/login
2022-07-08 17:51:06 log.py | INFO | ✅ Find 1 element: xpath=//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/input[1]  -> input 'mg_qa@jwzg.com'.
2022-07-08 17:51:07 log.py | INFO | ✅ Find 1 element: xpath=//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[8]/div[1]/div[2]/button  -> click.
2022-07-08 17:51:08 log.py | INFO | ✅ Find 1 element: xpath=//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[8]/div[1]/div[1]/input  -> input '951210'.
2022-07-08 17:51:08 log.py | INFO | ✅ Find 1 element: xpath=//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[10]/button  -> click.
2022-07-08 17:51:10 logging.py | INFO | 🔍 Find element: xpath=//*[@id="app"]/div[1]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div/div[2]/button[2]. 导入主按钮
2022-07-08 17:51:11 logging.py | INFO | ✅ click().
2022-07-08 17:51:11 logging.py | INFO | 🔍 Find element: xpath=/html/body/div[5]/div[2]/div/div[2]/div/div[1]/span[2]. figma链接导入tab
2022-07-08 17:51:12 logging.py | INFO | ✅ click().
2022-07-08 17:51:12 logging.py | INFO | 🔍 Find element: xpath=/html/body/div[5]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/input. figma链接输入框
2022-07-08 17:51:13 logging.py | INFO | ✅ send_keys('https://www.figma.com/file/1dboj6x10LYEvg8UTA0hkR/TEST_%E7%AE%AD%E5%A4%B4').
2022-07-08 17:51:18 logging.py | INFO | 🔍 Find element: xpath=/html/body/div[5]/div[2]/div/div[2]/div/div[3]/button. 链接导入按钮
2022-07-08 17:51:19 logging.py | INFO | ✅ click().
2022-07-08 17:51:25 log.py | INFO | 👀 assertText -> 导入完成.
.12022-07-08 17:51:25 log.py | SUCCESS | generated html file: file:////Users/huxw/code/python/mg-e2e/reports/2022_07_08_17_50_59_result.html
Generating HTML reports...
2022-07-08 17:51:25 log.py | SUCCESS | generated log file: file:////Users/huxw/code/python/mg-e2e/reports/seldom_log.log

```

# 测试报告

![](report.jpeg)

import time
from datetime import datetime
from time import sleep

import seldom

from selenium.webdriver.common.by import By
from element.login import IndLoginPage
from element.privatization_workbench import WorkbenchPage


# @seldom.skip()
class WorkbenchTest01(seldom.TestCase):
    """
    主要包含场景：登录
    """

    def start_class(self):
        login_page = IndLoginPage(self.driver)
        login_page.open("https://jsai.cc/ai-muses/gallery")

        self.max_window()
        sleep(8)
        self.execute_script("window.scrollTo(0, 1500)")
        sleep(2)

    def test_01_elements_children(self):
        """element子元素使用"""
        workbenchPage = WorkbenchPage(self.driver)
        wappers = workbenchPage.wappers

        # workbenchPage.imgWarper_close.click()  # 由于elements中的子元素没有联想方法,故通过element获取方法集

        print("获取第1个子元素",wappers[0].get_attribute("class"))

        result = wappers[0].find_element(By.XPATH, '//*[@class="masonry-column-wrap__20le_"][1]//img').get_attribute(
            "src")
        print("获取第1个子元素中的 第一个子元素的 img属性值: ",result)

    def test_02_elements_forEach_lick(self):
        """elements遍历点击"""
        workbenchPage = WorkbenchPage(self.driver)
        imgWarper = workbenchPage.imgWarper
        print("图片集数量：", len(imgWarper))

        for ele in imgWarper:
            # 向下滚动至目标元素可见
            self.execute_script("arguments[0].scrollIntoView();", ele)
            sleep(2)

            if ele.is_displayed():
                ele.click()
                sleep(4)
                workbenchPage.imgWarper_close.click()
                sleep(4)
"""
selenium之滚动鼠标滑动页面

一、滑动至顶部
输入搜索内容后，点击百度一下，滑动页面至底部

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
 
driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
 
# 等待元素出现，再执行操作
WebDriverWait(driver, 20).until(lambda driver:driver.find_element('id', 'kw')).send_keys('selenium')
WebDriverWait(driver, 20).until(lambda driver:driver.find_element('id', 'su')).click()
 
time.sleep(2)
# 模拟鼠标滚轮，滑动至页面底部
js = "window.scrollTo(0, document.body.scrollHeight)"
driver.execute_script(js)

二、滑动至顶部

time.sleep(2)
# 模拟鼠标滑动到顶部
js = "window.scrollTo(0,0)"
driver.execute_script(js)

三、滑动到具体位置

time.sleep(1)
js = "window.scrollTo(0, 500)"   # 向下滑动500个像素
driver.execute_script(js)
time.sleep(1)
js = "window.scrollTo(0, -500)"   # 向上滑动500个像素
driver.execute_script(js)
 
js = "window.scrollTo(500, 0)"   # 向右滑动500个像素
js = "window.scrollTo(-500, 0)"   # 向左滑动500个像素

四、滑动至目标元素可见

# 目标元素
ele = driver.find_element('xpath', '/html/body/div[1]/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[2]/div[3]/div[1]/div/a')
# 向下滚动至目标元素可见
js = "arguments[0].scrollIntoView();"
driver.execute_script(js, ele)
# 向上滚动至目标元素可见
js = "arguments[0].scrollIntoView(false);"
driver.execute_script(js, ele)
"""
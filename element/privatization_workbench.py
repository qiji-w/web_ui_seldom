from poium import Page, Element, Elements


class WorkbenchPage(Page):
    """私有化环境-工作台页面元素定位"""

    imgWarper = Elements(
        xpath='//*[@class="masonry-column-wrap__20le_"]//*[@class="sc-gAjuZT goIZrq"]',
        timeout=5,
        describe='即时AI设计-图片集',
    )

    imgWarper_close = Element(
        xpath='//*[@id="basePopup"]//*[@class="sc-dZoequ hZtqbR"]',
        timeout=5,
        describe='即时AI设计-图片集关闭btn',
    )

    wappers = Elements(
        xpath='//*[@class="masonry-column-wrap__20le_"]',
        timeout=5,
        describe='测试-即时AI设计-获取子元素',
    )
from poium import Page, Element


class IndLoginPage(Page):
    """
        独立登陆页面：https://127.0.0.1/files/login
    """
    # 微信登陆按钮
    btn_wechat = Element(xpath=r'//*[@class="login-register-wechat"]',
                         timeout=10,
                         describe="微信登陆按钮")

    # 钉钉登陆按钮
    btn_dingding = Element(xpath=r'//*[@class="login-register-ding-ding"]',
                           timeout=10,
                           describe="钉钉登陆按钮")

    # 蓝湖登陆按钮
    btn_lanhu = Element(xpath=r'//*[@class="login-register-lanhu"]',
                        timeout=10,
                        describe="蓝湖登陆按钮")

    # 手机号/邮箱 输入框
    input_phone_email = Element(xpath=r'//input[1]',
                                timeout=10,
                                describe="手机号/邮箱 输入框")

    # 验证码输入框
    input_verification_code = Element(xpath=r'//*[@class="register-code"]/input',
                                      timeout=10,
                                      describe="验证码输入框")

    # 获取验证码按钮
    btn_send_verification_code = Element(xpath=r'//*[@class="register-code-btn"]/button',
                                         timeout=10,
                                         describe="获取验证码按钮")

    # 开始使用按钮
    btn_begin = Element(xpath=r'//*[@class="light-btn"]',
                        timeout=10,
                        describe="开始使用按钮")

    # 切换密码登陆按钮
    btn_switch_password = Element(xpath=r'//*[@class="operations-wrap"]/div[1]',
                                  timeout=10,
                                  describe="切换密码登陆按钮")

    # 前往注册按钮
    btn_register = Element(xpath=r'//*[@class="text-btn" and contains(text(), "前往注册")]',
                           timeout=10,
                           describe="前往注册按钮")

    # 账号输入框
    input_username = Element(xpath='//*[@id="app"]//div[@class="email-phone-wrap"]//input[@placeholder="手机号/邮箱"]',
                             describe="用户名")
    # 密码输入框
    input_password = Element(xpath='//*[@id="app"]//div[@class="email-phone-wrap"]//input[@placeholder="密码"]',
                             describe="密码")

    # 忘记密码
    btn_forget_password = Element(
        xpath=r'//*[@id="app"]/div[1]/div[2]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[5]/span',
        timeout=10,
        describe="忘记密码按钮")

    # 私有化登录-【使用账号登录】按钮
    login_with_account_button = Element(
        css='#app > div.login_container > div.midd > div > button',
        timeout=10,
        describe='使用账号登录按钮'
    )

    # 私有化登录-【请输入邮箱】
    enter_mailbox = Element(
        css='#app > article > section > div.main > div.operation > div > div > div:nth-child(2) > input',
        timeout=10,
        describe='请输入邮箱'
    )

    # 私有化登录-【请输入密码】
    enter_password = Element(
        css='#app > article > section > div.main > div.operation > div > div > div:nth-child(3) > input',
        timeout=10,
        describe='请输入密码'
    )

    # 私有化登录-【开始使用】按钮
    start_use_button = Element(
        css='#app > article > section > div.main > div.operation > div > div > div.btn-wrap > button',
        timeout=10,
        describe='开始使用'
    )

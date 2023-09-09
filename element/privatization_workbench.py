from poium import Page, Element, Elements


class WorkbenchPage(Page):
    """私有化环境-工作台页面元素定位"""

    # 新建团队按钮
    new_team_button = Element(
        css='.add_team_wrap',
        timeout=5,
        describe='新建团队'
    )

    # 输入团队名称
    input_team_name = Element(
        css='input[placeholder="输入团队名称"]',
        timeout=5,
        describe='输入团队名称输入框'
    )

    # 输入团队描述
    input_team_desc = Element(
        css='textarea[placeholder="输入团队描述"]',
        timeout=5,
        describe='输入团队描述文本框'
    )

    # 创建新团队弹窗页面-创建团队按钮
    create_team_button = Element(
        css='body > div.master-dailog > div.mas-dialog__wrapper > div > div > div > div.left-content > button > span',
        timeout=5,
        describe='创建新团队弹窗页面-创建团队按钮'
    )

    # 创建团队成功的toast提醒
    create_team_toast = Element(
        css='body > div.toast.h5.mas-toast-container-normal.transition.transiton_top > div.mas-toast-content',
        timeout=5,
        describe='创建团队成功的toast提醒'
    )

    # 关闭创建团队成功之后的邀请成员弹窗
    close_member_invitation_window = Element(
        xpath='//*[@id="app"]/div[3]/div[2]/div/div[1]/div',
        timeout=5,
        describe='关闭创建团队成功之后的邀请成员弹窗'
    )

    # 点击主页
    homepage = Element(
        xpath='//li[@id="home"]',
        timeout=5,
        describe='点击主页'
    )

    # 点击草稿箱
    drafts = Element(
        xpath='//li[@id="drafts"]',
        timeout=5,
        describe='点击草稿箱'
    )

    # 点击分享给我的
    share_with_me = Element(
        xpath='//li[@id="shared"]',
        timeout=5,
        describe='点击分享给我的'
    )

    # 草稿箱-草稿箱tab
    drafts_tab = Element(
        css='.tab',
        timeout=5,
        index=0,
        describe='草稿箱-草稿箱tab'
    )

    # 草稿箱-这里还没有文件
    no_file = Element(
        css='.title.h2.text-tran-50',
        timeout=5,
        describe='草稿箱-草稿箱tab空-这里还没有文件'
    )

    # 草稿箱-回收站tab
    personal_recycle_bin_tab = Element(
        css='.tab',
        timeout=5,
        index=1,
        describe='草稿箱-回收站tab'
    )

    # 主页-标题
    homepage_title = Element(
        css='.project_header_title.h1 span',
        timeout=5,
        describe='主页-标题'
    )

    # 分享给我的-标题
    share_with_me_title = Element(
        css='.project_header_title.h1 span',
        timeout=5,
        describe='分享给我的-标题'
    )

    # 团队落地页-右上角新建项目按钮
    create_project_button = Element(
        css='.m-button.m-button--sm.m-button--secondary',
        timeout=5,
        index=0,
        describe='团队落地页-右上角新建项目按钮'
    )

    # 新建项目弹窗-项目名称输入框
    input_project_name = Element(
        css='input[placeholder="项目名称"]',
        timeout=5,
        describe='新建项目弹窗-项目名称输入框'
    )

    # 新建项目弹窗-确认按钮
    create_project_determine_button = Element(
        xpath='//*[@id="app"]/div[3]/div[2]/div/div[3]/button[2]',
        timeout=5,
        describe='新建项目弹窗-确认按钮'
    )

    # 项目落地页title
    project_header_title = Element(
        css='div.project_header_title.h1 > span',
        timeout=5,
        describe='项目落地页title'
    )

    # 项目落地页-新建文件按钮
    create_file_button = Element(
        css='button[data-onborading="create"]',
        timeout=5,
        describe='项目落地页-新建文件按钮'
    )

    # 文件页左上角面包屑-项目名称
    project_name_div = Element(
        xpath='//*[@id="app"]/div[1]/span/div[1]/div[1]/div[2]/div[2]/div',
        # css='#app > div.layout_container > span > div.nav_container > div.nav_menu > div.file-info.h5 > div.project-name > div',
        timeout=5,
        describe='文件页左上角面包屑-项目名称'
    )

    # 文件页左上角面包屑-文件名
    file_name_div = Element(
        xpath='//*[@id="app"]/div[1]/span/div[1]/div[1]/div[2]/div[3]',
        timeout=5,
        describe='文件页左上角面包屑-文件名'
    )

    # 项目落地页第一个文件的名字
    project_first_file_name = Element(
        css='.thumb_name.truncate',
        timeout=5,
        describe='项目落地页第一个文件的名字',
    )

    # 文件右键-重命名
    context_click_rename = Element(
        xpath='//*[@id="app"]/div[2]/div/div[6]/div',
        timeout=5,
        describe='文件-右键重命名'
    )

    # 文件右键-创建副本
    context_click_create_copy = Element(
        xpath='//*[@id="app"]/div[2]/div/div[5]/div',
        timeout=5,
        describe='文件右键-创建副本'
    )

    # 文件右键-删除
    context_click_delete = Element(
        xpath='//*[@id="app"]/div[2]/div/div[7]/div',
        timeout=5,
        describe='文件右键-删除'
    )

    # 项目落地页重命名文件名字-输入框
    project_first_file_rename_input = Element(
        css='.rename_input input',
        timeout=5,
        describe='项目落地页重命名文件名字-输入框'
    )

    # 文件副本名字
    first_file = Element(
        css='.thumb_name.truncate',
        timeout=5,
        describe='文件列表第一个文件',
        index=0
    )

    # 文件名字列表
    file_name_list = Elements(
        css='.thumb_name.truncate',
        timeout=5,
        describe='文件名字列表',
    )

    # 左侧导航栏-项目名称
    project_name = Element(
        xpath='//*[starts-with(@id,"team_") and starts-with(@class,"team-list-wrap")]/div/div/div/div/div/li/div[1]',
        timeout=5,
        index=1,
        describe='左侧导航栏-项目名称'
    )

    # 左侧导航栏-项目名称右键-重命名
    project_context_click_rename = Element(
        xpath='//*[@id="app"]/div[2]/div/div[1]/div/div[1]/div[2]/div',
        timeout=5,
        describe='左侧导航栏-项目名称右键-重命名'
    )

    # 左侧导航栏-项目名称右键-删除
    project_context_click_delete = Element(
        xpath='//*[@id="app"]/div[2]/div/div[2]/div/div[1]/div[2]/div',
        timeout=5,
        describe='左侧导航栏-项目名称右键-删除'
    )

    # 左侧导航栏-团队名称
    team_name = Element(
        xpath='//*[starts-with(@id,"team_li_")]',
        timeout=5,
        index=1,
        describe='左侧导航栏-团队名称'
    )
    # 团队库设置
    team_setting = Element(
        xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div/div/div[1]/div/div[2]/div[1]/span[4]',
        timeout=5,
        describe='左侧导航栏-团队名称-第1个团队名称'
    )

    # 团队库设置删除按钮
    team_setting_deleteBtn = Element(
        xpath='//*[@id="item"]/div[2]/button[span="删除团队"]',
        timeout=5,
        describe='左侧导航栏-团队名称-第1个团队名称'
    )

    # 左侧导航栏-第1个团队名称
    team_name_setup1 = Element(
        xpath='//*[starts-with(@id,"team_li_")]',
        timeout=5,
        describe='左侧导航栏-团队名称-第1个团队名称'
    )
    # 左侧导航栏-第2个团队名称
    team_name_setup2 = Element(
        xpath='//*[starts-with(@id,"team_li_")]',
        timeout=5,
        index=2,
        describe='左侧导航栏-团队名称-第1个团队名称'
    )

    # 左侧导航栏-团队名称右键-重命名
    team_context_click_rename = Element(
        xpath='//*[@id="app"]/div[2]/div/div[1]/div/div[1]/div[2]/div',
        timeout=5,
        describe='左侧导航栏-团队名称右键-重命名'
    )

    # 左侧导航栏-团队名称右键-删除团队
    team_context_click_delete = Element(
        xpath='//*[@id="app"]/div[2]/div/div[3]/div/div[1]/div[2]/div',
        timeout=5,
        describe='左侧导航栏-团队名称右键-删除团队'
    )

    # 删除项目-确认按钮
    project_delete_confirm_button = Element(
        xpath='//*[@id="app"]/div[3]/div[2]/div/div[3]/button[2]',
        timeout=5,
        describe='删除项目-确认按钮'
    )

    # 团队落地页-暂无项目
    no_project = Element(
        css='.title.h2.text-tran-50',
        timeout=5,
        describe='团队落地页-暂无项目'
    )

    # 删除团队二次弹窗-团队名称输入框
    team_delete_input_name = Element(
        css='input[placeholder="请输入团队名称"]',
        timeout=5,
        describe='删除团队二次弹窗-团队名称输入框'
    )

    # 删除团队二次弹窗-确认按钮
    team_delete_confirm_button = Element(
        xpath='//*[@id="app"]/div[3]/div[2]/div/div[3]/button[2]/span',
        timeout=5,
        describe='删除团队二次弹窗-确认按钮'
    )

    # 回收站-文件右键-恢复
    recycle_bin_recover = Element(
        css='.mas-menu-item-left-title-wrap div',
        timeout=5,
        index=0,
        describe='回收站-文件右键-恢复'
    )

    # 回收站-文件右键-永久删除
    recycle_bin_permanently_delete = Element(
        css='.mas-menu-item-left-title-wrap div',
        timeout=5,
        index=1,
        describe='回收站-文件右键-永久删除'
    )

    # 回收站-永久删除-确认按钮
    recycle_bin_permanently_delete_confirm = Element(
        css='.m-button.m-button--sm.m-button--destructive',
        timeout=5,
        describe='回收站-永久删除-确认按钮'
    )

    # 团队落地页-回收站tab
    team_recycling_tab = Element(
        css='span[data-tours-name="team_recycling"]',
        timeout=5,
        describe='团队落地页-回收站tab'
    )

    # 团队落地页-设置tab
    team_setting_tab = Element(
        css='span[data-tours-name="team_setting"]',
        timeout=5,
        describe='团队落地页-设置tab'
    )
    # 团队落地页-成员tab
    team_member_tab = Element(
        css='span[data-tours-name="team_member"]',
        timeout=5,
        describe='团队落地页-成员tab'
    )
    # 团队落地页-字体tab
    team_font_tab = Element(
        css='span[data-tours-name="team_font"]',
        timeout=5,
        describe='团队落地页-字体tab'
    )
    # 团队落地页-项目tab
    team_project_tab = Element(
        css='span[data-tours-name="team_project"]',
        timeout=5,
        describe='团队落地页-项目tab'
    )

    # 我的团队
    my_team = Element(
        css='.list_info.truncate',
        timeout=5,
        index=0,
        describe='我的团队'
    )

    # 我的团队-团队项目
    my_team_project = Element(
        css='.list_info.truncate',
        timeout=5,
        index=1,
        describe='我的团队-团队项目'
    )

    # 我的团队-自动化团队项目
    automate_team_project = Element(
        css='.list_info.truncate',
        timeout=5,
        index=4,
        describe='自动化团队项目'
    )


    # 我的团队-团队项目-新建分组右侧分组按钮
    new_group_right = Element(
        css='#header_sort > div.sort-right > div.v-popover > div > div > div > div',
        timeout=5,
        describe='我的团队-团队项目-新建分组右侧分组按钮'
    )
    # 我的团队-团队项目-新建分组右侧分组按钮-文件分组
    new_group_right_file = Element(
        css='.vue-popover-theme > div > div.tooltip-inner.popover-inner > div:nth-child(1) > div > div > div:nth-child(3)',
        timeout=5,
        describe='我的团队-团队项目-新建分组右侧分组按钮-文件分组'
    )

    # 我的团队-团队项目-新建分组
    new_group = Element(
        css='.new-group',
        timeout=5,
        describe='我的团队-团队项目-新建分组'
    )

    # 新建分组弹窗-请输入内容
    input_group_name = Element(
        css='input[placeholder="请输入内容"]',
        timeout=5,
        describe='新建分组弹窗-请输入内容'
    )

    # 新建分组弹窗-确定按钮
    new_group_confirm_button = Element(
        xpath='//*[text()=" 确定 "]',
        timeout=5,
        describe='新建分组弹窗-确定按钮'
    )

    # 分组名称
    new_group_name = Element(
        css='.groupName.p4',
        timeout=5,
        index=0,
        describe='分组名称'
    )

    # 分组名称hover-更多
    right_more = Element(
        css='.right__more',
        timeout=5,
        index=0,
        describe='分组名称hover-更多'
    )

    # 分组名称-重命名
    group_rename = Element(
        xpath='//*[@id="app"]/div[2]/div/div[3]/div',
        timeout=5,
        describe='分组名称-重命名'
    )

    # 分组名称-删除
    group_remove = Element(
        xpath='//*[@id="app"]/div[2]/div/div[2]/div',
        timeout=5,
        describe='分组名称-删除'
    )

    # 删除分组弹窗-确认按钮
    group_remove_confirm_button = Element(
        xpath='//*[text()=" 确认 "]',
        timeout=5,
        describe='删除分组弹窗-确认按钮'
    )

    # 主页-视图切换图标
    views_switch = Element(
        xpath='//*[@id="header_sort"]/div[2]/div',
        timeout=5,
        describe='主页-视图切换图标'
    )

    # 主页-列表视图-文件名称表头
    file_name_header = Element(
        css='.filename.column',
        timeout=5,
        describe='列表视图-文件名称表头'
    )

    # 主页-网格视图-最近打开
    recent_open = Element(
        css='.select-group-label-name',
        timeout=5,
        describe='主页-网格视图-最近打开'
    )

    # 工作台-右上角头像
    head_portrait = Element(
        css='.name-container.bg-g-blue.text-white',
        timeout=5,
        describe='工作台-右上角头像'
    )

    # 工作台-右上角头像-切换深色模式/浅色模式
    switch_theme = Element(
        css='li[data-tours-name="theme"] > span:nth-child(2)',
        timeout=5,
        describe='工作台-右上角头像-切换深色模式/浅色模式选项'
    )

    # 工作台-右上角头像-设置
    personal_setting = Element(
        css='li[data-tours-name="setting"] > span:nth-child(2)',
        timeout=5,
        describe='工作台-右上角头像-设置'
    )

    # 工作台-右上角头像-退出登录
    personal_logout = Element(
        css='li[data-tours-name="logout"] > span:nth-child(2)',
        timeout=5,
        describe='工作台-右上角头像-退出登录'
    )

    # 团队成员tab-修改备注名按钮
    nick_name_button = Element(
        css='div.username-block > button',
        timeout=5,
        describe='团队成员tab-修改备注名按钮'
    )

    # 备注名输入框-请输入名称
    input_nick_name = Element(
        css='input[placeholder="请输入名称"]',
        timeout=5,
        describe='备注名输入框-请输入名称'
    )

    # 团队成员tab-成员名称
    team_member_name = Element(
        css='span.main-name.select-text.h6',
        timeout=5,
        describe='团队成员tab-成员名称'
    )

    # 画布页-左上角菜单按钮
    left_corner_menu = Element(
        xpath='//*[@id="app"]/div[1]/span/div[1]/div[1]/div[1]/div[1]/div/div/div/div',
        timeout=5,
        describe='画布页-左上角菜单按钮'
    )

    # 画布页-左上角菜单-返回
    left_corner_menu_return = Element(
        css='span[data-tours-name=back_to_files]',
        timeout=5,
        describe='画布页-左上角菜单-返回'
    )

    # 画布页-文件名右侧下拉按钮
    file_name_right_drop_down_button = Element(
        css='div.file_button.transition > svg',
        timeout=5,
        describe='画布页-文件名右侧下拉按钮'
    )
    # 文件容器按钮
    file_group_button = Element(
        css='#topContainer > div.left_btn > div:nth-child(2)',
        timeout=5,
        describe='画布页-文件容器按钮'
    )
    # 画布
    file_canvas_button = Element(
        css='#canvas',
        timeout=5,
        describe='画布页-画布'
    )
    # 画布页-添加到历史版本
    add_to_version_history = Element(
        css='span[data-tours-name=add_to_version_history]',
        timeout=5,
        describe='画布页-添加到历史版本'
    )

    # 画布页-查看历史版本
    show_version_history = Element(
        css='span[data-tours-name=show_version_history]',
        timeout=5,
        describe='画布页-查看历史版本'
    )

    # 添加到历史版本-标题
    version_history_title = Element(
        css='input[placeholder="标题"]',
        timeout=5,
        describe='添加到历史版本-标题'
    )

    # 添加到历史版本-更改内容
    version_history_content = Element(
        css='textarea[placeholder="请描述更改内容"]',
        timeout=5,
        describe='添加到历史版本-更改内容'
    )

    # 添加到历史版本-保存按钮
    version_history_save = Element(
        xpath="//*[text()='保存']",
        timeout=5,
        describe='添加到历史版本-保存按钮'
    )

    # 最近的历史版本标题
    recent_history_version_title = Element(
        css='div.top',
        timeout=5,
        index=1,
        describe='最近的历史版本标题'
    )

    # 返回编辑按钮
    return_to_edit = Element(
        xpath='//*[@id="topContainer"]/div[1]/button',
        timeout=5,
        describe='返回编辑按钮'
    )

    # 图层tab
    layer_tab = Element(
        css='div.tab_bar.border-b-block > div > div > div:nth-child(1)',
        timeout=5,
        describe='图层tab'
    )

    # 组件tab
    section_tab = Element(
        xpath='//*[@class="tab_item transition h6"]',
        timeout=5,
        describe='组件tab'
    )

    # 组件宫格、列表模式切换按钮
    section_views_switch = Element(
        css='div.component-lib-header > div:nth-child(2)',
        timeout=5,
        describe='组件宫格、列表模式切换按钮'
    )

    # 组件宫格、列表模式切换按钮悬停文案
    section_views_switch_hover = Element(
        css='div.tooltip-main > div > div',
        timeout=5,
        describe='组件宫格、列表模式切换按钮悬停文案'
    )

    # 左侧树列表第一个图层
    first_layer = Element(
        css='div.item_name.name_container.truncate.highest_frame',
        timeout=5,
        index=0,
        describe='左侧树列表第一个图层'
    )

    # 图层重命名输入框
    rename_layer_input = Element(
        css='div.item_name.input_container input.mas-basis-input',
        timeout=5,
        describe='图层重命名输入框'
    )

    # plugin_sandbox
    plugin_sandbox = Element(
        css='.plugin-sandbox',
        timeout=5,
        describe='图层重命名输入框'
    )

    # plugin-iframe
    plugin_iframe = Element(
        id_='plugin-iframe',
        timeout=5,
        describe='图层重命名输入框'
    )

    # 矩阵复制插件-列
    plugin_column = Element(
        css='input[placeholder="1-100"]',
        timeout=5,
        index=0,
        describe='矩阵复制插件-列'
    )

    # 矩阵复制插件-列间距
    column_space = Element(
        css='input[placeholder="0-999"]',
        timeout=5,
        index=0,
        describe='矩阵复制插件-列间距'
    )

    # 矩阵复制插件-行
    plugin_line = Element(
        css='input[placeholder="1-100"]',
        timeout=5,
        index=1,
        describe='矩阵复制插件-行'
    )

    # 矩阵复制插件-行间距
    line_space = Element(
        css='input[placeholder="0-999"]',
        timeout=5,
        index=1,
        describe='矩阵复制插件-行间距'
    )

    # 矩阵复制插件-复制按钮
    copy_btn = Element(
        css='div.copy-btn',
        timeout=5,
        describe='矩阵复制插件-行间距'
    )

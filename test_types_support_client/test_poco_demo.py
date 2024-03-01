#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time: 2024/3/1 19:48
# @Author: xiaob
# @File: test_pocp_demo.PY
# @Desc: poco自动化测试

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import logging

# 链接指定设备
# dev1 = Android("127.0.0.1:7555")
# poco = AndroidUiautomationPoco(dev1, screenshot_each_action=False)
# 链接设备默认
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


def test_poco_demo():
    logging.getLogger("poco").setLevel(logging.WARNING)
    icon = poco(text="国经纵横")
    icon.click()
    poco(text="国经纵横").click() #点击图标登录
    print(poco.adb_client.devices()) #获取安卓设备
    print(poco.adb_client.adb_path) #adb.exe路径信息
    print(poco.adb_client.get_cpufreq()) #当前cpu频率
    print(poco.adb_client.get_ip_address()) #ip信息
    print(poco.adb_client.list_app()) #列出安装的apk
    print(device().get_current_resolution()) #获取屏幕当前的分辨率
    print(poco.get_screen_size()) #获取手机分辨率
    print(poco(text="国经纵横").get_name()) #获取元素name属性
    print(poco(textMatches=".*?纵横").get_name()) #模糊匹配查询
    print(poco(text="国经纵横").get_position()) #获取位置
    print(poco(text="国经纵横").get_bounds()) #获取元素边缘信息
    print(poco(text="国经纵横").get_name()) #获取元素name,android.widget.TextView
    print(poco(text="国经纵横").get_text()) #获取元素text,国经纵横
    print(poco(text="国经纵横").get_size()) #获取元素size

    w, h = device().get_current_resolution()
    print('UI元素的名称: {}'.format(icon.attr('name'))) #返回UI元素的名称
    print('用户是否可见: {}'.format(icon.attr('visible'))) #用户是否可见 ，返回布尔值
    print('UI元素的字符串值: {}'.format(icon.attr('text'))) #返回UI元素的字符串值
    print('运行时UI元素的类型名: {}'.format(icon.attr('type'))) #返回远程运行时UI元素的类型名
    print('UI元素的位置: {}'.format(icon.attr('pos'))) #返回UI元素的位置
    print('尺寸百分比[宽度,高度]: {}'.format(icon.attr('size'))) #返回尺寸百分比[宽度，高度]，根据屏幕显示0~1
    print('其他属性信息: {}'.format(icon.attr('...'))) #返回SDK实现的其他属性
    print(icon.attr('pos'))
    print(int(icon.attr('pos')[0]*w), int(icon.attr('pos')[1]*h))
    touch([int(icon.attr('pos')[0]*w), int(icon.attr('pos')[1]*h)]) #处理当前设备上坐标信息

    if icon.exists():
        icon.click()  # 点击
    elif poco(text="设置服务器地址").get_text() == '设置服务器地址':
        poco(text="设置服务器地址").long_click()  # 长按,pos按下坐标,duration按下时间
        # poco(text="设置服务器地址").long_click(duration=3)
    elif poco(text="服务域").get_text() == '服务域':
        # poco.scroll(direction='vertical', duration=2, percent=0.8)  # 向右水平滑动,percent滑动百分比,duration滑动时间
        poco.scroll(direction='horizontal', duration=2, percent=0.8)  # 向左水平滑动
        poco(text="完成").click()
    elif poco(text="+86").get_text() == '+86':
    # 滑动,direction方向,'上','下','左','右'-'up','down','left','right',duration操作执行的时间间隔,Raises当找不到元素时会报错,raise PocoNoSuchNodeException(self)
        poco(text="+86").swipe('up', duration=0.5)
        poco(text="+86").swipe('down', duration=1.0)
        poco(text="+86").swipe('left', duration=1.5)
        poco(text="+86").swipe('right', duration=2.0)
    elif poco(text="登录").get_text() == '登录':
    # 把登录元素拖动到密码元素上(拖拽),target参数的目标,duration操作执行的时间间隔,Raises当找不到元素时会报错,raise PocoNoSuchNodeException(self)
        poco(text="登录").drag_to(poco(text="密码"), duration=3.0)
    else:
        print('国经纵横apk不存在')

    while icon.exists():
        icon.focus('center').click()
        icon.focus([0.5, 0.8]).drag_to(icon.focus([0.5, 0.1]))
        poco.pan() #平移
        poco(text="+86").start_gesture().hold(1).to(poco(text="密码")).hold(1).to(poco(text="登录")).hold(1).to(poco(text="设置服务器地址")).hold(1).up()  # 建序列化的手势动作
        # coordinates_list坐标列表,duration两个坐标间间隔时间,steps执行每2个点之间的运行步数,当解锁九宫格每一步没必要再拆分,所以steps设为1
        device().touch_proxy.swipe_along([[250, 500], [300, 500], [300, 700], [600, 700]], duration=3, steps=3)
        icon.pinch()  # 双指操作
        # 画两条竖向平行线 - 从[250, 550]到[250, 700]，持续10秒，分5步，第2根手指偏移量(200,0)
        device().touch_proxy.two_finger_swipe([250, 550], [250, 700], duration=10, steps=5, offset=(200, 0))
        device().touch_proxy.two_finger_swipe([150, 1000],[700, 1000]) # 画两条横向平行线 - 从[150, 1000]到[700, 1000]，其余参数全部用默认
        poco(text="+86").wait_for_appearance(timeout=1) #等待一个元素出现
        poco.wait_for_all([poco(text="+86"), poco(text="密码"), poco(text="登录")], timeout=1) #等待多个元素都出现
        poco.wait_for_any([poco(text="+86"), poco(text="密码"), poco(text="登录")], timeout=1) #等待任一元素出现
        break

    # 直接查询其节点及子节点信息
    for pname in poco("android.widget.TextView").offspring("android.widget.LinearLayout").offspring(
            "com.olym.zxcbmjt:id/ll_line_phone").offspring("android.widget.LinearLayout").child(
            "com.android.settings:id/dashboard_tile")[2].offspring("android:id/title"):
        print(pname.get_text())

    si = poco("android.widget.TextView").offspring("android.widget.LinearLayout").attr('size')
    print(si)

    for i in poco("android.widget.TextView").offspring("android.widget.LinearLayout").children():
        print(i.attr('name'))

    # 获取父节点、子节点
    for each in poco("com.huawei.android.launcher:id/workspace_screen").child("android.view.ViewGroup").children():
        print(each.get_text())

    # 在子节点下-返回上级或多级父节点
    for i in poco(text="设置服务器地址").parent().sibling():
        print('设置图标节点name值：{},size值: {}'.format(i.attr('name'), i.attr('size')))

    # 如果要获取更上层父节点的话，需要在对象后添加继续添加parent()参数
    for j in poco(text="设置服务器地址").parent().parent():
        print('设置图标节点name值：{},size值: {}'.format(j.attr('name'), j.attr('size')))

    # 空间顺序选择
    name_list = list(poco("android.widget.TextView").child())
    print(len(name_list))
    for i in range(len(name_list)):
        print(poco("android.widget.TextView").child()[i])
        print(poco("android.widget.TextView").child()[i].attr('text'))
    print('='.center(90, "="))
    name1 = poco("android.widget.TextView").child()[0].attr('text')
    print(name1)
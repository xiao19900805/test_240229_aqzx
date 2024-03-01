#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time: 2024/3/1 19:48
# @Author: xiaob
# @File: test_airtest_demo.PY
# @Desc: airtest自动化测试

from airtest.core.android import Android
from airtest.core.api import *
import logging


def test_airtest_demo():
    logging.getLogger("airtest").setLevel(logging.WARNING)

    device: Android = init_device('Android')
    is_locked = device.is_locked()
    print(f'is_locked: {is_locked}')

    if is_locked:
        device.unlock()

    device.wake()

    app_list = device.list_app()
    print(f'app list {app_list}')

    uuid = device.uuid
    print(f'uuid {uuid}')

    display_info = device.get_display_info()
    print(f'display info {display_info}')

    resolution = device.get_render_resolution()
    print(f'resolution {resolution}')

    ip_address = device.get_ip_address()
    print(f'ip address {ip_address}')

    top_activity = device.get_top_activity()
    print(f'top activity {top_activity}')

    is_keyboard_shown = device.is_keyboard_shown()
    print(f'is keyboard shown {is_keyboard_shown}')

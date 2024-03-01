## airtest.core.android.android.Android 为例

1. get_default_device：获取默认 device
2. uuid：获取当前 Device 的 UUID
3. list_app：列举所有 App
4. path_app：打印输出某个 App 的完整路径
5. check_app：检查某个 App 是否在当前设备上
6. start_app：启动某个 App
7. start_app_timing：启动某个 App，然后计算时间
8. stop_app：停止某个 App
9. clear_app：清空某个 App 的全部数据
10. install_app：安装某个 App
11. install_multiple_app：安装多个 App
12. uninstall_app：卸载某个 App
13. snapshot：屏幕截图
14. shell：获取 Adb Shell 执行的结果
15. keyevent：执行键盘操作
16. wake：唤醒当前设备
17. home：点击 HOME 键
18. text：向设备输入内容
19. touch：点击屏幕某处的位置
20. double_click：双击屏幕某处的位置
21. swipe：滑动屏幕，由一点到另外一点
22. pinch：手指捏和操作
23. logcat：日志记录操作
24. getprop：获取某个特定属性的值
25. get_ip_address：获取 IP 地址
26. get_top_activity：获取当前 Activity
27. get_top_activity_name_and_pid：获取当前 Activity 的名称和进程号
28. get_top_activity_name：获取当前 Activity 的名称
29. is_keyboard_shown：判断当前键盘是否出现了
30. is_locked：设备是否锁定了
31. unlock：解锁设备
32. display_info：获取当前显示信息，如屏幕宽高等
33. get_display_info：同 display_info
34. get_current_resolution：获取当前设备分辨率
35. get_render_resolution：获取当前渲染分辨率
36. start_recording：开始录制
37. stop_recording：结束录制
38. adjust_all_screen：调整屏幕适配分辨率
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from airtest.core.android import Android
# 链接指定设备
dev1 = Android("127.0.0.1:7555")
poco = AndroidUiautomationPoco(dev1, screenshot_each_action=False)
print("start...")
poco(text="国经纵横").long_click()
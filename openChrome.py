from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time, sys

chrome_driver_path = "chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument("--window-size=200,100")

# ==================== 配置 ====================
num_windows = 12  # 需要打开的窗口数量
num_tabs = 16  # 每个浏览器窗口打开的标签页数量
window_width = 800  # 每个窗口的宽度
window_height = 80  # 每个窗口的高度
gap = 32  # 窗口之间的间距
base_url = "http://localhost:888/"
# ==================== 配置 ====================

drivers = []

for i in range(num_windows):
    x = 0
    y = i * gap

    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
    driver.set_window_position(x, y)
    driver.set_window_size(window_width, window_height)
    driver.get(base_url)

    for tab_index in range(1, num_tabs):
        driver.execute_script(f"window.open('{base_url}');")
        time.sleep(0.1)

    driver.switch_to.window(driver.window_handles[0])
    drivers.append(driver)
    time.sleep(0.5)

input("按下回车键关闭程序")
for driver in drivers:
    driver.quit()

sys.exit(0)
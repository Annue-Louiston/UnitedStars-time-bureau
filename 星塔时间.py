import datetime
import tkinter as tk

# 月份映射
chinese_months = {
    1: "首阳",
    2: "绀香",
    3: "莺时",
    4: "槐序",
    5: "鸣蜩",
    6: "季夏",
    7: "兰秋",
    8: "南宫",
    9: "菊月",
    10: "子春",
    11: "葭月",
    12: "冰月"
}

# 时间域映射（完整32个域，每个域45分钟）
time_domains = [
    ("子暝", "00:45"),  # 00:00 - 00:45
    ("独语", "01:30"),  # 00:45 - 01:30
    ("孤愁", "02:15"),  # 01:30 - 02:15
    ("木草", "03:00"),  # 02:15 - 03:00
    ("夜乡", "03:45"),  # 03:00 - 03:45
    ("星眠", "04:30"),  # 03:45 - 04:30
    ("半壁", "05:15"),  # 04:30 - 05:15
    ("启明", "06:00"),  # 05:15 - 06:00
    ("雀鸣", "06:45"),  # 06:00 - 06:45
    ("休梦/revive", "07:30"),  # 06:45 - 07:30
    ("蹄驰", "08:15"),  # 07:30 - 08:15
    ("青云", "09:00"),  # 08:15 - 09:00
    ("云望", "09:45"),  # 09:00 - 09:45
    ("碧天", "10:30"),  # 09:45 - 10:30
    ("流岩", "11:15"),  # 10:30 - 11:15
    ("灶午", "12:00"),  # 11:15 - 12:00
    ("炎时", "12:45"),  # 12:00 - 12:45
    ("曝日", "13:30"),  # 12:45 - 13:30
    ("光喧", "14:15"),  # 13:30 - 14:15
    ("城躁", "15:00"),  # 14:15 - 15:00
    ("悦童", "15:45"),  # 15:00 - 15:45
    ("同映", "16:30"),  # 15:45 - 16:30
    ("金阳", "17:15"),  # 16:30 - 17:15
    ("炊袅", "18:00"),  # 17:15 - 18:00
    ("月云", "18:45"),  # 18:00 - 18:45
    ("夜霞", "19:30"),  # 18:45 - 19:30
    ("海潮", "20:15"),  # 19:30 - 20:15
    ("星鹭", "21:00"),  # 20:15 - 21:00
    ("江寒", "21:45"),  # 21:00 - 21:45
    ("霜寂", "22:30"),  # 21:45 - 22:30
    ("星运", "23:15"),  # 22:30 - 23:15
    ("梦晨", "00:00")   # 23:15 - 00:00
]

def get_current_time_info():
    now = datetime.datetime.now()
    current_hour = now.hour
    current_minute = now.minute
    current_month = now.month
    current_day = now.day

    # 获取当前月份的古雅名称
    month_name = chinese_months[current_month]

    # 计算当前时间所在的域
    total_minutes = current_hour * 60 + current_minute  # 当前时间的总分钟数
    domain_index = total_minutes // 45 % 32  # 每45分钟一个域，一天32个域

    # 获取对应的域名称和时间
    domain_name, domain_time = time_domains[domain_index]

    # 计算当前时间在域中的分区
    domain_start_minutes = domain_index * 45  # 当前域的起始分钟数
    minutes_into_domain = total_minutes - domain_start_minutes  # 当前时间在域中的分钟数
    zone_index = minutes_into_domain // 5  # 每5分钟一个区，计算当前时间所在的区

    return month_name, current_day, domain_name, zone_index + 1  # 返回月份、日期、域名称、区编号

def update_time():
    month_name, current_day, domain_name, zone_index = get_current_time_info()
    time_string = f"星塔位于：{month_name}路{current_day}号 之 {domain_name}域 第{zone_index} 区"
    label.config(text=time_string)
    root.after(60000, update_time)  # 每分钟更新一次

def close_window():
    root.destroy()  # 关闭窗口

# 创建悬浮窗口
root = tk.Tk()
root.title("星塔时间")
root.overrideredirect(True)  # 去掉窗口边框
root.attributes('-topmost', True)  # 窗口置顶
root.attributes('-alpha', 0.8)  # 设置窗口透明度为 80%
root.configure(bg='#f0f0f0')  # 设置背景颜色

# 创建一个标签用于显示时间
label = tk.Label(root, text="", font=("Arial", 12, "bold"), bg="#f0f0f0", fg="#333333", padx=10, pady=5)
label.pack(pady=10)

# 添加关闭按钮
close_button = tk.Button(root, text="关闭", command=close_window, font=("Arial", 10), bg="#ff4d4d", fg="white", padx=10, pady=5)
close_button.pack(pady=5)

# 更新时间
update_time()

# 设置窗口位置到屏幕右上角
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.update_idletasks()  # 确保窗口尺寸已经更新
window_width = root.winfo_width()
window_height = root.winfo_height()
root.geometry(f"+{screen_width - window_width - 10}+30")  # 距离屏幕右边10像素，顶部30像素

root.mainloop()
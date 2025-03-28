import tkinter as tk
from datetime import datetime

# 创建主窗口
root = tk.Tk()
root.attributes('-alpha', 0.7)  # 设置窗口透明度为70%
root.attributes('-topmost', True)  # 窗口置顶
root.overrideredirect(True)  # 去除窗口边框

# 设置窗口大小和位置
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 200
window_height = 50
x = (screen_width - window_width) // 2
y = 0
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# 创建标签显示时间
label = tk.Label(root, font=('Arial', 20), fg='green', bg='black')
label.pack(fill='both', expand=True)

# 更新时间函数
def update_time():
    now = datetime.now().strftime('%H:%M:%S')
    label.config(text=now)
    root.after(1000, update_time)  # 每秒更新一次

# 启动时间更新
update_time()

# 鼠标拖动事件处理
def start_move(event):
    root.x = event.x
    root.y = event.y

def stop_move(event):
    root.x = None
    root.y = None

def on_move(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f'+{x}+{y}')

# 创建关闭按钮
close_button = tk.Canvas(root, width=10, height=10, bg='white', highlightthickness=0, bd=0)
close_button.create_oval(0, 0, 10, 10, fill='white', outline='white')
close_button.bind('<Button-1>', lambda e: root.destroy())
close_button.place(relx=1.0, x=-2, y=2, anchor='ne')

# 绑定鼠标事件
label.bind('<Button-1>', start_move)
label.bind('<ButtonRelease-1>', stop_move)
label.bind('<B1-Motion>', on_move)

# 运行主循环
root.mainloop()
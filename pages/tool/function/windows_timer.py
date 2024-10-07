import os
from datetime import datetime, timedelta
from base.notify import notify

class WindowsTimer:
    # 操作字典，映射操作名到系统命令
    operations = {
        "关机": "shutdown /s /t {delay}",
        "重启": "shutdown /r /t {delay}",
        # "睡眠": "rundll32.exe powrprof.dll,SetSuspendState 0,1,0",
        # "注销": "shutdown -l"
    }

    cancel_commands = {
        "关机": "shutdown /a" if os.name == 'nt' else "sudo shutdown -c",
        "重启": "shutdown /a" if os.name == 'nt' else "sudo shutdown -c",
    }

    def __init__(self):
        self.scheduled_operation = None

    def schedule_operation(self, hour, minute, second, operation, label):
        """Debug"""
        # print(hour)
        # print(minute)
        # print(second)
        # print(operation)

        """设置定时操作"""
        current_time = datetime.now()
        target_time = current_time + timedelta(hours=hour, minutes=minute, seconds=second)
        delay_seconds = int((target_time - current_time).total_seconds())

        # 处理时间过短的情况
        if delay_seconds <= 5:
            msg = "设定的时间应当在未来。"
            notify(3, True, 5, "Windows 定时操作", msg, "ic_fluent_timer_filled")
            return
        
        if operation in self.operations:
            command = self.operations[operation].format(delay=delay_seconds)
            os.system(command)
            self.scheduled_operation = operation
            msg = f"已设定：于 {target_time} 执行 <strong>{operation}</strong>"
            notify(1, True, 5, "Windows 定时操作", msg, "ic_fluent_timer_filled")
            label.setText(f"已设定：于 {target_time} 执行 <strong>{operation}</strong>")
            label.resizeTo(350, 32)
        else:
            msg = f"未知操作: <strong>{operation}</strong>"
            notify(4, True, 5, "Windows 定时操作", msg, "ic_fluent_timer_filled")

    def cancel_operation(self, operation=None, label=None):
        """取消操作"""
        operation = operation or self.scheduled_operation
        if operation in self.cancel_commands:
            os.system(self.cancel_commands[operation])
            msg = f"已取消 <strong>{operation}</strong> 操作"
            notify(1, True, 5, "Windows 定时操作", msg, "ic_fluent_timer_off_filled")
            self.scheduled_operation = None
            label.resizeTo(0, 32)
        else:
            msg = f"无法取消 <strong>{operation}</strong> 或<strong>未知操作</strong>"
            notify(4, True, 5, "Windows 定时操作", msg, "ic_fluent_timer_off_filled")


# 调用示例
if __name__ == "__main__":
    scheduler = WindowsTimer()
    
    # 设置操作（例如，1分钟后关机）
    scheduler.schedule_operation(0, 1, 0, "关机")
    
    # 取消操作
    scheduler.cancel_operation("关机")  # 或者 scheduler.cancel_operation() 取消上一个操作

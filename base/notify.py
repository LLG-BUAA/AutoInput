from PyQt5.QtCore import Qt

from siui.core import SiGlobal

def notify(type_, auto_close=False, auto_close_duration=1, title="", text="", icon="ic_fluent_hand_wave_regular"): # 标准-0  成功-1  提示-2  警告-3  错误-4

    fold_after = auto_close_duration if auto_close is True else None
    SiGlobal.siui.windows["MAIN_WINDOW"].LayerRightMessageSidebar().send(
        title=title,
        text=text,
        msg_type=type_,
        fold_after=fold_after*1000,
        icon=SiGlobal.siui.iconpack.get(icon),
    )
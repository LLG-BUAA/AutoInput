import random

import numpy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from siui.components import SiCircularProgressBar, SiLineEdit, SiOptionCardLinear, SiTitledWidgetGroup, SiWidget, \
    SiLineEditWithDeletionButton, SiLineEditWithItemName
from siui.components.combobox import SiComboBox
from siui.components.menu import SiMenu
from siui.components.page import SiPage
from siui.components.progress_bar import SiProgressBar
from siui.components.slider import SiSliderH
from siui.components.spinbox.spinbox import SiIntSpinBox, SiDoubleSpinBox
from siui.components.widgets import (
    SiCheckBox,
    SiDenseHContainer,
    SiDraggableLabel,
    SiIconLabel,
    SiLabel,
    SiLongPressButton,
    SiPixLabel,
    SiPushButton,
    SiRadioButton,
    SiSimpleButton,
    SiSwitch,
    SiToggleButton,
)
from siui.components.widgets.navigation_bar import SiNavigationBarH, SiNavigationBarV
from siui.components.widgets.table import SiTableView
from siui.core import SiColor
from siui.core import SiGlobal
from siui.core import Si

from base.option_card import OptionCardPlaneForWidgetDemos

from pages.tool.function.windows_timer import WindowsTimer
windowstimer = WindowsTimer()

class Tool(SiPage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setPadding(64)
        self.setScrollMaximumWidth(1000)
        self.setScrollAlignment(Qt.AlignLeft)
        self.setTitle("工具")

        # 创建控件组
        self.titled_widgets_group = SiTitledWidgetGroup(self)
        self.titled_widgets_group.setSpacing(32)
        self.titled_widgets_group.setAdjustWidgetsSize(True)  # 禁用调整宽度

        # 定时功能
        with self.titled_widgets_group as group:
            group.addTitle("定时功能")

            # 文字标签
            self.label_for_text = OptionCardPlaneForWidgetDemos(self)
            self.label_for_text.setSourceCodeURL("https://github.com/ChinaIceF/PyQt-SiliconUI/blob/main/siui/components"
                                                 "/widgets/label.py")
            self.label_for_text.setTitle("Windows 定时操作")

            self.windowstimer_label_01 = SiLabel(self)
            self.windowstimer_label_01.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.windowstimer_label_01.setText(":")
            self.windowstimer_label_01.resize(8, 32)
            self.windowstimer_label_02 = SiLabel(self)
            self.windowstimer_label_02.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.windowstimer_label_02.setText(":")
            self.windowstimer_label_02.resize(8, 32)
            self.windowstimer_label_1 = SiLabel(self)
            self.windowstimer_label_1.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.windowstimer_label_1.setText("在")
            self.windowstimer_label_1.resize(32, 32)
            self.windowstimer_label_2 = SiLabel(self)
            self.windowstimer_label_2.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.windowstimer_label_2.setText("之后")
            self.windowstimer_label_2.resize(32, 32)
            self.windowstimer_label_3 = SiLabel(self)
            self.windowstimer_label_3.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)
            self.windowstimer_label_3.setText("执行")
            self.windowstimer_label_3.resize(32, 32)

            self.hour_int_spin_box = SiIntSpinBox(self)
            self.hour_int_spin_box.resize(125, 32)
            self.minute_int_spin_box = SiIntSpinBox(self)
            self.minute_int_spin_box.resize(125, 32)
            self.second_int_spin_box = SiIntSpinBox(self)
            self.second_int_spin_box.resize(125, 32)

            self.windowstimer_combobox = SiComboBox(self)
            self.windowstimer_combobox.resize(100, 32)
            self.windowstimer_combobox.addOption("关机")
            self.windowstimer_combobox.addOption("重启")
            self.windowstimer_combobox.addOption("睡眠")
            self.windowstimer_combobox.addOption("注销")
            self.windowstimer_combobox.menu().setShowIcon(False)
            self.windowstimer_combobox.menu().setIndex(0)

            self.windowstimer_h_container = SiDenseHContainer(self)
            self.windowstimer_h_container.setFixedHeight(32)
            self.windowstimer_h_container.addWidget(self.windowstimer_label_1, "left")
            self.windowstimer_h_container.addWidget(self.hour_int_spin_box, "left")
            self.windowstimer_h_container.addWidget(self.windowstimer_label_01, "left")
            self.windowstimer_h_container.addWidget(self.minute_int_spin_box, "left")
            self.windowstimer_h_container.addWidget(self.windowstimer_label_02, "left")
            self.windowstimer_h_container.addWidget(self.second_int_spin_box, "left")
            self.windowstimer_h_container.addWidget(self.windowstimer_label_2, "left")
            self.windowstimer_h_container.addWidget(self.windowstimer_combobox, "right")
            self.windowstimer_h_container.addWidget(self.windowstimer_label_3, "right")


            self.windowstimer_set_info = SiLabel(self)
            self.windowstimer_set_info.resize(250, 32)
            self.windowstimer_set_info.setText("")
            self.windowstimer_set_info.setSiliconWidgetFlag(Si.AdjustSizeOnTextChanged)

            self.windowstimer_button_start = SiPushButton(self)
            self.windowstimer_button_start.resize(125, 32)
            self.windowstimer_button_start.attachment().setText("启动")
            self.windowstimer_button_start.setHint("切换到 <strong>启动</strong> 状态")
            self.windowstimer_button_start.clicked.connect(
                lambda: windowstimer.schedule_operation(
                    int(self.hour_int_spin_box.lineEdit().text()),
                    int(self.minute_int_spin_box.lineEdit().text()),
                    int(self.second_int_spin_box.lineEdit().text()),
                    self.windowstimer_combobox.value_label.text(),
                    self.windowstimer_set_info))

            self.windowstimer_button_cancel = SiPushButton(self)
            self.windowstimer_button_cancel.resize(125, 32)
            self.windowstimer_button_cancel.attachment().setText("取消")
            self.windowstimer_button_cancel.setHint("切换到 <strong>取消</strong> 状态")
            self.windowstimer_button_cancel.clicked.connect(
                lambda: windowstimer.cancel_operation(label=self.windowstimer_set_info))

            self.windowstimer_button_h_container = SiDenseHContainer(self)
            self.windowstimer_button_h_container.setFixedHeight(32)
            self.windowstimer_button_h_container.addWidget(self.windowstimer_set_info, "left")
            self.windowstimer_button_h_container.addWidget(self.windowstimer_button_cancel, "right")
            self.windowstimer_button_h_container.addWidget(self.windowstimer_button_start, "right")

            self.label_for_text.body().setAdjustWidgetsSize(True)
            self.label_for_text.body().addWidget(self.windowstimer_h_container)
            self.label_for_text.body().addWidget(self.windowstimer_button_h_container)
            self.label_for_text.body().addPlaceholder(12)
            self.label_for_text.adjustSize()

            # <- 添加到控件组
            group.addWidget(self.label_for_text)


        # 添加页脚的空白以增加美观性
        self.titled_widgets_group.addPlaceholder(64)

        # 设置控件组为页面对象
        self.setAttachment(self.titled_widgets_group)

    def reloadStyleSheet(self):
        super().reloadStyleSheet()

        # 标签
        # 文字标签
        self.windowstimer_set_info.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.windowstimer_label_01.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.windowstimer_label_02.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.windowstimer_label_1.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.windowstimer_label_2.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.windowstimer_label_3.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.demo_label1.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.demo_label2.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.demo_label3.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.demo_label_hinted.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        self.demo_label_with_svg.setStyleSheet("color: {}".format(SiGlobal.siui.colors["TEXT_A"]))
        # 标签动画
        self.demo_label_ani.setColorTo(SiGlobal.siui.colors["INTERFACE_BG_E"])
        # 可拖动标签
        self.demo_draggable_label.setColorTo(SiGlobal.siui.colors["INTERFACE_BG_E"])

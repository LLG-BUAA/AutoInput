from pages.home import Home
from pages.tool import Tool

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDesktopWidget

import siui
from siui.core import SiColor, SiGlobal
from siui.templates.application.application import SiliconApplication

class MySiliconApp(SiliconApplication):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        screen_geo = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1024, 380)
        self.resize(1366, 916)
        self.move((screen_geo.width() - self.width()) // 2, (screen_geo.height() - self.height()) // 2)
        self.layerMain().setTitle("Silicon UI Gallery")
        self.setWindowTitle("Silicon UI Gallery")
        self.setWindowIcon(QIcon("./img/empty_icon.png"))

        self.layerMain().addPage(Home(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_home_filled"),
                                 hint="主页", side="top")
        
        self.layerMain().addPage(Tool(self),
                                 icon=SiGlobal.siui.iconpack.get("ic_fluent_toolbox_filled"),
                                 hint="工具", side="top")
        
        # self.layerMain().addPage(ExampleIcons(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_diversity_filled"),
        #                          hint="图标包", side="top")
        # self.layerMain().addPage(ExampleWidgets(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_box_multiple_filled"),
        #                          hint="控件", side="top")
        # self.layerMain().addPage(ExampleContainer(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_align_stretch_vertical_filled"),
        #                          hint="容器", side="top")
        # self.layerMain().addPage(ExampleOptionCards(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_list_bar_filled"),
        #                          hint="选项卡", side="top")
        # self.layerMain().addPage(ExampleDialogs(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_panel_separate_window_filled"),
        #                          hint="消息与二级界面", side="top")
        # self.layerMain().addPage(ExamplePageControl(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_wrench_screwdriver_filled"),
        #                          hint="页面控制", side="top")
        # self.layerMain().addPage(ExampleFunctional(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_puzzle_piece_filled"),
        #                          hint="功能组件", side="top")

        # self.layerMain().addPage(About(self),
        #                          icon=SiGlobal.siui.iconpack.get("ic_fluent_info_filled"),
        #                          hint="关于", side="bottom")

        self.layerMain().setPage(0)

        SiGlobal.siui.reloadAllWindowsStyleSheet()

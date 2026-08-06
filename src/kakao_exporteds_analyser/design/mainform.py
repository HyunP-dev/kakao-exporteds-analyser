################################################################################
## Form generated from reading UI file 'mainform.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt, QUrl
from PySide6.QtGui import QAction
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QComboBox,
    QDockWidget,
    QMenu,
    QMenuBar,
    QStatusBar,
    QTabWidget,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(914, 573)
        self.loadAction = QAction(MainWindow)
        self.loadAction.setObjectName("loadAction")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.chatsView = QTreeWidget(self.tab)
        self.chatsView.setObjectName("chatsView")
        self.chatsView.setRootIsDecorated(False)
        self.chatsView.setUniformRowHeights(True)

        self.verticalLayout_3.addWidget(self.chatsView)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.resultCmbBox = QComboBox(self.tab_2)
        self.resultCmbBox.addItem("")
        self.resultCmbBox.addItem("")
        self.resultCmbBox.addItem("")
        self.resultCmbBox.setObjectName("resultCmbBox")

        self.verticalLayout_4.addWidget(self.resultCmbBox)

        self.resultView = QWebEngineView(self.tab_2)
        self.resultView.setObjectName("resultView")
        self.resultView.setUrl(QUrl("about:blank"))

        self.verticalLayout_4.addWidget(self.resultView)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 914, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.sendersView = QTreeWidget(self.dockWidgetContents)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "\ub2c9\ub124\uc784")
        self.sendersView.setHeaderItem(__qtreewidgetitem)
        self.sendersView.setObjectName("sendersView")
        self.sendersView.setRootIsDecorated(False)
        self.sendersView.setUniformRowHeights(True)
        self.sendersView.setSortingEnabled(True)

        self.verticalLayout.addWidget(self.sendersView)

        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.loadAction)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow",
                "\uce74\uce74\uc624\ud1a1 \ub300\ud654 \ubd84\uc11d\uae30",
                None,
            )
        )
        self.loadAction.setText(
            QCoreApplication.translate(
                "MainWindow", "\ub300\ud654 \ubd88\ub7ec\uc624\uae30", None
            )
        )
        ___qtreewidgetitem = self.chatsView.headerItem()
        ___qtreewidgetitem.setText(
            2, QCoreApplication.translate("MainWindow", "\ub0b4\uc6a9", None)
        )
        ___qtreewidgetitem.setText(
            1,
            QCoreApplication.translate("MainWindow", "\ubcf4\ub0b8 \uc2dc\uac01", None),
        )
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "\ub2c9\ub124\uc784", None)
        )
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab),
            QCoreApplication.translate("MainWindow", "\ub300\ud654 \ub0b4\uc6a9", None),
        )
        self.resultCmbBox.setItemText(
            0,
            QCoreApplication.translate(
                "MainWindow",
                "\uc720\uc800\ubcc4 \ud65c\ub3d9 \uc2dc\uac04 \ubd84\uc11d \uacb0\uacfc",
                None,
            ),
        )
        self.resultCmbBox.setItemText(
            1,
            QCoreApplication.translate(
                "MainWindow",
                "\ucc44\ud305\ubc29\uc758 \ud65c\uc131 \uc2dc\uac04 \ubd84\uc11d \uacb0\uacfc",
                None,
            ),
        )
        self.resultCmbBox.setItemText(
            2,
            QCoreApplication.translate(
                "MainWindow",
                "\ub300\ud654 \uc218 \uc0c1\uc704 10\uba85\uc758 \ub300\ud654 \ube44\uc728 \ubd84\uc11d \uacb0\uacfc",
                None,
            ),
        )

        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tab_2),
            QCoreApplication.translate("MainWindow", "\ubd84\uc11d \uacb0\uacfc", None),
        )
        self.menu.setTitle(
            QCoreApplication.translate("MainWindow", "\ud30c\uc77c", None)
        )
        self.menu_2.setTitle(
            QCoreApplication.translate("MainWindow", "\ub3c4\uc6c0\ub9d0", None)
        )
        self.dockWidget.setWindowTitle(
            QCoreApplication.translate(
                "MainWindow", "\ucc38\uc5ec\uc790 \ubaa9\ub85d", None
            )
        )
        ___qtreewidgetitem1 = self.sendersView.headerItem()
        ___qtreewidgetitem1.setText(
            1, QCoreApplication.translate("MainWindow", "\ub300\ud654 \uc218", None)
        )


# retranslateUi

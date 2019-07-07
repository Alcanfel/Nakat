# -*-coding: utf8-*-
# 202225 -темный
# D0D0D0 - для ячейки таблицы
# 778899 - для контрура ячейки таблицы
# 616367 - цвет шрифта (серый)
# FFFFFF - цвет шрифта (белый)
# 202225 - цвет границ крайнего (самый темный)
# 2F3136 - цвет границ среднего (средний темный)
# 36393F - цвет границ внутреннего (легкий тем
# ный)
# Стиль для главного окна
style_2 = """
/* Цвет нижней границы*/ 
QTabWidget::pane {
    border-top: 2px solid #2F3136;

}

/* отсутп бара от левого края */ 
QTabWidget::tab-bar {
    left: 10px;
}

/* ячейка бара */ 
QTabBar::tab {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #2F3136, stop: 0.4 #2F3136,
                                stop: 0.5 #2F3136, stop: 1.0 #2F3136);
    border: 1px solid #2F3136;
    border-bottom-color: #2F3136; /* same as the pane color */
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
    min-width: 8ex;
    padding: 6px;
    gridline-color: #616367;
    color: #616367;


}

/* ячейка бара при нажатии и фокуса*/ 
QTabBar::tab:selected, QTabBar::tab:hover{
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                                stop: 0 #36393F, stop: 0.4 #36393F,
                                stop: 0.5 #36393F, stop: 1.0 #36393F);
    color: #FFFFFF;
}

/* при не нажатии на ячейку бара*/ 
QTabBar::tab:!selected {
    margin-top: 2px; /* make non-selected tabs look smaller */
}

QMainWindow {
background-color: #2F3136;
}


"""

# Стиль для класса аудит

style_1 = """

QPushButton {
background-color: #36393F;
color: #D4D4D4;
gridline-color: #fffff8;
font-size: 12pt;
font-family: "Georgia";
border-radius: 10px;
border-style: inset;
padding: 3px;
}

QPushButton:hover {
background-color: #616367;
color: #FFFFFF;
}

QPushButton:pressed {
font-size: 13pt;
}


QLineEdit {
background-color: #616367;
border: 1px solid gray;
border-radius: 10px;
padding: 2px 14px;
selection-background-color: darkgray;
font-size: 12pt;
font-family: "Georgia";
}


QLabel {
background-color: #616367;
color: #fffff8;
border: 1px solid #616367;
border-radius: 10px;
padding: 3px;
font-size: 15pt;
font-family: "Courier New";
}

QTextEdit{
background-color: #D0D0D0;
color: black;
font-family: "Courier New";
padding: 5px;
font-size: 12pt;
selection-background-color: darkgray;
}

QCheckBox {
    background-color: #D0D0D0;
    spacing: 5px;
}

QCheckBox::indicator {
    width: 13px;
    height: 13px;
}



"""

# Стиль для таблицы
style = """ 

QTableWidget {
gridline-color: #fffff8;
font-size: 10pt;
}

QWidget {
background-color: #616367;
color: #fffff8;
}
QTableWidget::section{
border-style: none;
border-bottom: 1px solid #778899;
margin-bottom:5px;
margin-top:5px

}
QTableWidget::item {
background-color: #D0D0D0;
border-style: outset;
border-radius: 0px;
border-color:#778899; 
color: black;
padding: 2px;
font-family: "Courier New";
}
QTableWidget::item:selected {
background-color: #D0D0D0;
color: black; 
border-color: #778899;
font-family: "Courier New";
}
QTableWidget QTableCornerButton::section { 
background-color: #778899;
border: 0px solid #616367;  
font-family: "Calibri";
}
QHeaderView::section {
background-color: #778899;
padding: 4px;
border: 1px solid #616367;
font-size: 12pt;
font-family: "Courier New";

QLineEdit {
background-color: #D0D0D0;
border: 1px solid gray;
border-radius: 10px;
padding: 2px 14px;
selection-background-color: darkgray;
font-size: 12pt;
font-family: "Georgia";
}


QLabel {
color: #616367;
border: 1px solid #616367;
border-radius: 10px;
padding: 3px;
font-size: 15pt;
font-family: "Courier New";
}


QTextEdit{
background-color: #D0D0D0;
color: black;
font-family: "Courier New";
padding: 5px;
font-size: 12pt;
selection-background-color: darkgray;
}
}

"""

if __name__ == "__main__":
    pass
# Nama  : Muharromi Ali Ilham
# NIM   : F1D02410082
# Kelas : C

DASHBOARD_QSS = """
QMainWindow {
    background-color: #f0f2f5;
}

QWidget {
    font-family: "Segoe UI", Arial, sans-serif;
    font-size: 12px;
    color: #2c3e50;
}
QLabel#titleLabel {
    font-size: 20px;
    font-weight: bold;
    color: #ffffff;
    background: qlineargradient(
        x1:0, y1:0, x2:1, y2:0,
        stop:0 #2c3e50, stop:1 #3498db
    );
    border-radius: 8px;
    padding: 12px 20px;
    margin-bottom: 4px;
}
QFrame#toolbarFrame {
    background-color: #ffffff;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    padding: 8px 12px;
}

QFrame#toolbarFrame QLabel {
    font-size: 11px;
    font-weight: bold;
    color: #636e72;
    padding: 0 2px;
}
QComboBox {
    background-color: #ffffff;
    border: 1.5px solid #b2bec3;
    border-radius: 5px;
    padding: 4px 10px;
    min-height: 24px;
    font-size: 11px;
    color: #2d3436;
}
QComboBox:hover {
    border-color: #3498db;
}
QComboBox:focus {
    border-color: #2980b9;
    background-color: #ebf5fb;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 24px;
    border-left: 1px solid #dcdde1;
    border-top-right-radius: 5px;
    border-bottom-right-radius: 5px;
    background-color: #f8f9fa;
}
QComboBox::down-arrow {
    width: 10px;
    height: 10px;
}
QComboBox QAbstractItemView {
    background-color: #ffffff;
    border: 1px solid #b2bec3;
    selection-background-color: #3498db;
    selection-color: #ffffff;
    padding: 4px;
    outline: none;
}
QPushButton {
    font-size: 11px;
    font-weight: bold;
    padding: 6px 16px;
    border-radius: 6px;
    border: none;
    min-height: 26px;
}
QPushButton#btnRefresh {
    background-color: #3498db;
    color: #ffffff;
}
QPushButton#btnRefresh:hover {
    background-color: #2980b9;
}
QPushButton#btnRefresh:pressed {
    background-color: #1f6da3;
}
QPushButton#btnExport1, QPushButton#btnExport2 {
    background-color: #27ae60;
    color: #ffffff;
}
QPushButton#btnExport1:hover, QPushButton#btnExport2:hover {
    background-color: #219a52;
}
QPushButton#btnExport1:pressed, QPushButton#btnExport2:pressed {
    background-color: #1b8a44;
}
QPushButton#btnPrev, QPushButton#btnNext {
    background-color: #6c5ce7;
    color: #ffffff;
    padding: 5px 20px;
    font-size: 11px;
}
QPushButton#btnPrev:hover, QPushButton#btnNext:hover {
    background-color: #5a4bd1;
}
QPushButton#btnPrev:pressed, QPushButton#btnNext:pressed {
    background-color: #4a3db8;
}
QPushButton#btnPrev:disabled, QPushButton#btnNext:disabled {
    background-color: #b2bec3;
    color: #dfe6e9;
}
QGroupBox#summaryGroup {
    background-color: #ffffff;
    border: 1px solid #dcdde1;
    border-radius: 8px;
    margin-top: 14px;
    padding: 14px 10px 10px 10px;
    font-size: 13px;
    font-weight: bold;
    color: #2c3e50;
}
QGroupBox#summaryGroup::title {
    subcontrol-origin: margin;
    subcontrol-position: top left;
    left: 14px;
    padding: 0 6px;
    background-color: #ffffff;
    color: #2c3e50;
}
QGroupBox#summaryGroup QLabel#summaryKey {
    font-size: 11px;
    font-weight: normal;
    color: #636e72;
    padding: 2px 0;
}
QGroupBox#summaryGroup QLabel#summaryVal {
    font-size: 12px;
    font-weight: bold;
    color: #2d3436;
    padding: 2px 0;
}
QTableWidget {
    background-color: #ffffff;
    alternate-background-color: #f8f9fa;
    gridline-color: #ecf0f1;
    border: 1px solid #dcdde1;
    border-radius: 6px;
    font-size: 11px;
    selection-background-color: #3498db;
    selection-color: #ffffff;
    outline: none;
}
QTableWidget::item {
    padding: 4px 8px;
}
QTableWidget::item:selected {
    background-color: #3498db;
    color: #ffffff;
}
QHeaderView::section {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #34495e, stop:1 #2c3e50
    );
    color: #ffffff;
    padding: 6px 8px;
    font-weight: bold;
    font-size: 11px;
    border: none;
    border-right: 1px solid #415b76;
    border-bottom: 2px solid #2980b9;
}
QHeaderView::section:hover {
    background: qlineargradient(
        x1:0, y1:0, x2:0, y2:1,
        stop:0 #3d566e, stop:1 #34495e
    );
}
QLabel#pageLabel {
    font-size: 11px;
    font-weight: bold;
    color: #636e72;
    padding: 4px;
}
QSplitter::handle {
    background-color: #dcdde1;
    width: 3px;
    margin: 4px 2px;
    border-radius: 1px;
}
QSplitter::handle:hover {
    background-color: #3498db;
}
FigureCanvasQTAgg {
    border: 1px solid #dcdde1;
    border-radius: 6px;
}
QScrollBar:vertical {
    background-color: #f0f2f5;
    width: 10px;
    margin: 0;
    border-radius: 5px;
}
QScrollBar::handle:vertical {
    background-color: #b2bec3;
    min-height: 30px;
    border-radius: 5px;
}
QScrollBar::handle:vertical:hover {
    background-color: #636e72;
}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
    height: 0;
}
QScrollBar:horizontal {
    background-color: #f0f2f5;
    height: 10px;
    margin: 0;
    border-radius: 5px;
}
QScrollBar::handle:horizontal {
    background-color: #b2bec3;
    min-width: 30px;
    border-radius: 5px;
}
QScrollBar::handle:horizontal:hover {
    background-color: #636e72;
}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
    width: 0;
}
QMessageBox {
    background-color: #ffffff;
}
QMessageBox QLabel {
    font-size: 12px;
    color: #2c3e50;
}
QMessageBox QPushButton {
    background-color: #3498db;
    color: #ffffff;
    padding: 6px 24px;
    border-radius: 5px;
}
QMessageBox QPushButton:hover {
    background-color: #2980b9;
}
"""
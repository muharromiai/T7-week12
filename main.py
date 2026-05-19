# Nama  : Muharromi Ali Ilham
# NIM   : F1D02410082
# Kelas : C

import sys
from PySide6.QtWidgets import QApplication
from views.dashboard_window import DashboardWindow
from styles.dashboard_qss import DASHBOARD_QSS

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(DASHBOARD_QSS)
    window = DashboardWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
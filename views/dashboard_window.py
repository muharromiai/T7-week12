# Nama  : Muharromi Ali Ilham
# NIM   : F1D02410082
# Kelas : C

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QComboBox,
    QPushButton,
    QLabel,
    QGroupBox,
    QGridLayout,
    QHeaderView,
    QFileDialog,
    QMessageBox,
    QSplitter,
    QFrame,
)
from PySide6.QtCore import Qt
from models.data_loader import (
    load_csv,
    get_dataset_path,
    unique_values,
    filter_rows,
    compute_summary,
)
from views.chart_widget import ChartCanvas
CHART_TYPES = [
    "Bar: Biaya per Region",
    "Scatter: Usia vs Biaya",
    "Pie: Distribusi Insurance Plan",
    "Histogram: Distribusi BMI",
]
FILTER_COLUMNS = {
    "gender": "Gender",
    "smoker": "Smoker",
    "region": "Region",
    "insurance_plan": "Insurance Plan",
}
ROWS_PER_PAGE = 100
class DashboardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(
            "Medical Insurance — Muharromi Ali Ilham (F1D02410082)"
        )
        self.setMinimumSize(1280, 780)
        self.header = []
        self.all_rows = []
        self.filtered_rows = []
        self.col_map = {}
        self.current_page = 0
        self._load_data()
        self._build_ui()
        self._apply_filters()

    def _load_data(self):
        path = get_dataset_path()
        self.header, self.all_rows = load_csv(path)
        self.col_map = {name: i for i, name in enumerate(self.header)}

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(12, 12, 12, 12)
        main_layout.setSpacing(8)

        title = QLabel("Dashboard Medical Insurance Cost")
        title.setObjectName("titleLabel")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        toolbar = self._build_toolbar()
        main_layout.addWidget(toolbar)

        splitter = QSplitter(Qt.Orientation.Horizontal)

        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        left_layout.setContentsMargins(0, 0, 0, 0)
        left_layout.setSpacing(6)

        self.summary_group = self._build_summary_panel()
        left_layout.addWidget(self.summary_group)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        left_layout.addWidget(self.table, stretch=1)

        page_bar = QHBoxLayout()
        self.btn_prev = QPushButton("Prev")
        self.btn_prev.setObjectName("btnPrev")
        self.btn_prev.clicked.connect(self._prev_page)
        self.btn_next = QPushButton("Next")
        self.btn_next.setObjectName("btnNext")
        self.btn_next.clicked.connect(self._next_page)
        self.lbl_page = QLabel()
        self.lbl_page.setObjectName("pageLabel")
        self.lbl_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page_bar.addWidget(self.btn_prev)
        page_bar.addStretch()
        page_bar.addWidget(self.lbl_page)
        page_bar.addStretch()
        page_bar.addWidget(self.btn_next)
        left_layout.addLayout(page_bar)

        splitter.addWidget(left_panel)

        right_panel = QWidget()
        right_layout = QVBoxLayout(right_panel)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(6)

        self.chart1 = ChartCanvas(width=6, height=3.5)
        self.chart2 = ChartCanvas(width=6, height=3.5)
        right_layout.addWidget(self.chart1, stretch=1)
        right_layout.addWidget(self.chart2, stretch=1)

        splitter.addWidget(right_panel)
        splitter.setStretchFactor(0, 5)
        splitter.setStretchFactor(1, 5)

        main_layout.addWidget(splitter, stretch=1)

    def _build_toolbar(self):
        frame = QFrame()
        frame.setObjectName("toolbarFrame")
        frame.setFrameShape(QFrame.Shape.StyledPanel)
        layout = QHBoxLayout(frame)
        layout.setContentsMargins(10, 6, 10, 6)

        self.filter_combos = {}
        for col_key, label_text in FILTER_COLUMNS.items():
            lbl = QLabel(f"{label_text}:")
            combo = QComboBox()
            combo.setMinimumWidth(120)
            combo.addItem("Semua")
            col_idx = self.col_map[col_key]
            combo.addItems(unique_values(self.all_rows, col_idx))
            combo.currentTextChanged.connect(self._apply_filters)
            self.filter_combos[col_key] = combo
            layout.addWidget(lbl)
            layout.addWidget(combo)

        layout.addSpacing(12)

        lbl_c1 = QLabel("Chart 1:")
        self.combo_chart1 = QComboBox()
        self.combo_chart1.addItems(CHART_TYPES)
        self.combo_chart1.setCurrentIndex(0)
        self.combo_chart1.currentTextChanged.connect(self._update_charts)

        lbl_c2 = QLabel("Chart 2:")
        self.combo_chart2 = QComboBox()
        self.combo_chart2.addItems(CHART_TYPES)
        self.combo_chart2.setCurrentIndex(1)
        self.combo_chart2.currentTextChanged.connect(self._update_charts)

        layout.addWidget(lbl_c1)
        layout.addWidget(self.combo_chart1)
        layout.addWidget(lbl_c2)
        layout.addWidget(self.combo_chart2)

        layout.addStretch()

        btn_refresh = QPushButton("Refresh")
        btn_refresh.setObjectName("btnRefresh")
        btn_refresh.clicked.connect(self._on_refresh)
        layout.addWidget(btn_refresh)

        btn_export1 = QPushButton("Export Chart 1")
        btn_export1.setObjectName("btnExport1")
        btn_export1.clicked.connect(lambda: self._export_chart(self.chart1, "chart1"))
        layout.addWidget(btn_export1)

        btn_export2 = QPushButton("Export Chart 2")
        btn_export2.setObjectName("btnExport2")
        btn_export2.clicked.connect(lambda: self._export_chart(self.chart2, "chart2"))
        layout.addWidget(btn_export2)

        return frame

    def _build_summary_panel(self):
        group = QGroupBox("Ringkasan Statistik")
        group.setObjectName("summaryGroup")
        self.summary_layout = QGridLayout(group)
        self.summary_labels = {}
        return group

    def _apply_filters(self):
        filters = {}
        for col_key, combo in self.filter_combos.items():
            filters[self.col_map[col_key]] = combo.currentText()
        self.filtered_rows = filter_rows(self.all_rows, filters)
        self.current_page = 0
        self._populate_table()
        self._update_summary()
        self._update_charts()

    def _populate_table(self):
        total = len(self.filtered_rows)
        total_pages = max(1, (total + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        self.current_page = min(self.current_page, total_pages - 1)

        start = self.current_page * ROWS_PER_PAGE
        end = min(start + ROWS_PER_PAGE, total)
        page_rows = self.filtered_rows[start:end]

        self.table.setUpdatesEnabled(False)
        self.table.setSortingEnabled(False)
        self.table.setRowCount(len(page_rows))
        self.table.setColumnCount(len(self.header))
        self.table.setHorizontalHeaderLabels(self.header)

        for r, row in enumerate(page_rows):
            for c, val in enumerate(row):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setItem(r, c, item)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Interactive
        )
        self.table.setSortingEnabled(True)
        self.table.setUpdatesEnabled(True)

        self.lbl_page.setText(
            f"Halaman {self.current_page + 1} / {total_pages}  "
            f"(baris {start + 1}-{end} dari {total})"
        )
        self.btn_prev.setEnabled(self.current_page > 0)
        self.btn_next.setEnabled(self.current_page < total_pages - 1)

    def _prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self._populate_table()

    def _next_page(self):
        total_pages = max(1, (len(self.filtered_rows) + ROWS_PER_PAGE - 1) // ROWS_PER_PAGE)
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self._populate_table()

    def _update_summary(self):
        for i in reversed(range(self.summary_layout.count())):
            widget = self.summary_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()
        self.summary_labels.clear()

        stats = compute_summary(self.filtered_rows, self.header)
        for idx, (key, value) in enumerate(stats.items()):
            lbl_key = QLabel(f"{key}:")
            lbl_key.setObjectName("summaryKey")

            lbl_val = QLabel(str(value))
            lbl_val.setObjectName("summaryVal")

            self.summary_layout.addWidget(lbl_key, idx, 0)
            self.summary_layout.addWidget(lbl_val, idx, 1)

    def _draw_chart(self, canvas, chart_name):
        drawers = {
            CHART_TYPES[0]: canvas.draw_bar_chart,
            CHART_TYPES[1]: canvas.draw_scatter_chart,
            CHART_TYPES[2]: canvas.draw_pie_chart,
            CHART_TYPES[3]: canvas.draw_histogram,
        }
        drawer = drawers.get(chart_name)
        if drawer and self.filtered_rows:
            drawer(self.filtered_rows, self.header)

    def _update_charts(self):
        self._draw_chart(self.chart1, self.combo_chart1.currentText())
        self._draw_chart(self.chart2, self.combo_chart2.currentText())

    def _on_refresh(self):
        self._load_data()
        for combo in self.filter_combos.values():
            combo.blockSignals(True)
            combo.setCurrentIndex(0)
            combo.blockSignals(False)
        self._apply_filters()

    def _export_chart(self, canvas, default_name):
        path, _ = QFileDialog.getSaveFileName(
            self, "Export Chart ke PNG", f"{default_name}.png", "PNG Files (*.png)"
        )
        if path:
            canvas.export_to_png(path)
            QMessageBox.information(
                self, "Export Berhasil", f"Chart berhasil disimpan ke:\n{path}"
            )
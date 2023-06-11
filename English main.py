import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Auto install")
        self.setGeometry(200, 200, 800, 500)
        self.create_file_install_tab()
        self.create_software_delete_tab()
        self.create_dependency_install_tab()
        self.create_package_update_tab()
        self.create_version_tab()

        # Add tab widget to main window
        self.tab_widget = QTabWidget(self)
        self.tab_widget.addTab(self.file_install_tab, "File Install")
        self.tab_widget.addTab(self.software_delete_tab, "Software Delete")
        self.tab_widget.addTab(self.dependency_install_tab, "Dependency Install")
        self.tab_widget.addTab(self.package_update_tab, "Package Update")
        self.tab_widget.addTab(self.version_tab, "About")

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)

    def create_file_install_tab(self):
        self.file_install_tab = QWidget()
        self.file_install_tab_layout = QVBoxLayout()
        self.file_install_button_layout = QHBoxLayout()
        self.file_install_label = QLabel("Please select a .deb file to install:", self.file_install_tab)
        self.file_install_label.setFont(QFont("Arial", 14))
        self.file_install_button = QPushButton("Select File", self.file_install_tab)
        self.file_install_button.clicked.connect(self.choose_file)
        self.file_install_button.setFont(QFont("Arial", 14))
        self.file_install_button_layout.addWidget(self.file_install_button)
        self.install_button = QPushButton("Install", self.file_install_tab)
        self.install_button.clicked.connect(self.install_file)
        self.install_button.setFont(QFont("Arial", 14))
        self.file_install_button_layout.addWidget(self.install_button)
        self.file_install_tab_layout.addWidget(self.file_install_label)
        self.file_install_tab_layout.addLayout(self.file_install_button_layout)
        self.file_install_tab.setLayout(self.file_install_tab_layout)

    def choose_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,"Select .deb File", "","Debian Package Files (*.deb)", options=options)
        if filename:
            self.file_install_button.setText(filename)

    def install_file(self):
        cmd = "sudo dpkg -i %s" % (self.file_install_button.text())
        os.system(cmd)
        QMessageBox.about(self, "Message", "Installation completed")

    def create_software_delete_tab(self):
        self.software_delete_tab = QWidget()
        self.software_delete_tab_layout = QVBoxLayout()
        self.software_delete_input_layout = QHBoxLayout()
        self.software_delete_label = QLabel("Enter the software name to delete (support wildcard *):", self.software_delete_tab)
        self.software_delete_label.setFont(QFont("Arial", 14))
        self.software_delete_input = QLineEdit(self.software_delete_tab)
        self.software_delete_input.setFont(QFont("Arial", 14))
        self.software_delete_input_layout.addWidget(self.software_delete_input)
        self.software_delete_button_layout = QHBoxLayout()
        self.software_delete_remove_button = QPushButton("Remove without config", self.software_delete_tab)
        self.software_delete_remove_button.clicked.connect(self.remove_software_without_config)
        self.software_delete_remove_button.setFont(QFont("Arial", 14))
        self.software_delete_button_layout.addWidget(self.software_delete_remove_button)
        self.software_delete_remove_all_button = QPushButton("Remove all including config", self.software_delete_tab)
        self.software_delete_remove_all_button.clicked.connect(self.remove_software_with_config)
        self.software_delete_remove_all_button.setFont(QFont("Arial", 14))
        self.software_delete_button_layout.addWidget(self.software_delete_remove_all_button)
        self.software_delete_tab_layout.addWidget(self.software_delete_label)
        self.software_delete_tab_layout.addLayout(self.software_delete_input_layout)
        self.software_delete_tab_layout.addLayout(self.software_delete_button_layout)
        self.software_delete_tab.setLayout(self.software_delete_tab_layout)

    def remove_software_without_config(self):
        cmd = "sudo apt-get remove %s" % (self.software_delete_input.text())
        os.system(cmd)
        QMessageBox.about(self, "Message", "Removal completed")

    def remove_software_with_config(self):
        cmd = "sudo apt-get --purge remove %s" % (self.software_delete_input.text())
        os.system(cmd)
        QMessageBox.about(self, "Message", "Removal completed")

    def create_dependency_install_tab(self):
        self.dependency_install_tab = QWidget()
        self.dependency_install_tab_layout = QVBoxLayout()
        self.dependency_install_button_layout = QHBoxLayout()
        self.dependency_automatic_button = QPushButton("Install missing dependencies", self.dependency_install_tab)
        self.dependency_automatic_button.clicked.connect(self.install_missing_dependencies)
        self.dependency_automatic_button.setFont(QFont("Arial", 14))
        self.dependency_install_button_layout.addWidget(self.dependency_automatic_button)
        self.dependency_update_button = QPushButton("Update Package List", self.dependency_install_tab)
        self.dependency_update_button.clicked.connect(self.update_package_list)
        self.dependency_update_button.setFont(QFont("Arial", 14))
        self.dependency_install_button_layout.addWidget(self.dependency_update_button)
        self.dependency_install_tab_layout.addLayout(self.dependency_install_button_layout)
        self.dependency_install_tab.setLayout(self.dependency_install_tab_layout)

    def install_missing_dependencies(self):
        cmd = "sudo apt-get --fix-broken install -y"
        os.system(cmd)
        QMessageBox.about(self, "Message", "Installation completed")

    def update_package_list(self):
        cmd = "sudo apt-get update"
        os.system(cmd)
        QMessageBox.about(self, "Message", "Package list updated")

    def create_package_update_tab(self):
        self.package_update_tab = QWidget()
        self.package_update_tab_layout = QVBoxLayout()
        self.package_update_button_layout = QHBoxLayout()
        self.update_button = QPushButton("Update Package List", self.package_update_tab)
        self.update_button.clicked.connect(self.update_package_list)
        self.update_button.setFont(QFont("Arial", 14))
        self.package_update_button_layout.addWidget(self.update_button)
        self.package_update_tab_layout.addLayout(self.package_update_button_layout)
        self.package_update_tab.setLayout(self.package_update_tab_layout)

    def create_version_tab(self):
        self.version_tab = QWidget()
        self.version_tab_layout = QVBoxLayout()
        self.version_label = QLabel(" Auto install v1.0", self.version_tab)
        self.version_label.setFont(QFont("Arial", 20))
        self.version_tab_layout.addWidget(self.version_label)
        self.version_tab.setLayout(self.version_tab_layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

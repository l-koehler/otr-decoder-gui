"""
PyQt OTR Decoder - A PyQt-GUI for the proprietary decoder published by onlinetvrecorder.com

THE DECODER IS NOT MY WORK AND NOT TO BE DISTRIBUTED WITH THIS PROGRAM - download
the static 64-bit version from https://www.onlinetvrecorder.com/v2/software/Linux
and place the 'otrdecoder' executable into the same folder as this python file. (or edit line 77)

Copyright (C) 2023 Lorenz Köhler

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import sys, os, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QFileDialog, QMessageBox, QCheckBox

# Create a subclass of QWidget to create the main window
class DecoderUI(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('OTR Decoder 1.2')
        self.setGeometry(100, 100, 400, 250)

        # Create labels, input boxes, and buttons
        label1 = QLabel('Username:', self)
        label1.setGeometry(30, 30, 80, 30)

        self.username_input = QLineEdit('Default Username', self)
        self.username_input.setGeometry(120, 30, 200, 30)

        label2 = QLabel('Password:', self)
        label2.setGeometry(30, 70, 80, 30)

        self.password_input = QLineEdit(self)
        self.password_input.setGeometry(120, 70, 200, 30)
        self.password_input.setEchoMode(QLineEdit.Password)  # Set echo mode to Password

        label3 = QLabel('File:', self)
        label3.setGeometry(30, 110, 80, 30)

        self.file_input = QLineEdit(self)
        self.file_input.setGeometry(120, 110, 160, 30)

        # Create a checkbox
        self.overwrite = QCheckBox('Overwrite', self)
        self.overwrite.setGeometry(30, 150, 150, 30)

        confirm_button = QPushButton('Confirm', self)
        confirm_button.setGeometry(150, 150, 100, 30)
        confirm_button.clicked.connect(self.confirm_button_clicked)

        file_button = QPushButton('…', self)
        file_button.setGeometry(290, 110, 30, 30)
        file_button.clicked.connect(self.select_file)

    def confirm_button_clicked(self):
        # Retrieve the content of the inputs
        username = self.username_input.text()
        password = self.password_input.text()
        input_file = os.path.abspath(self.file_input.text()) # The selection button returns a abspath anyways, but the user could manually type something.
        overwrite = self.overwrite.isChecked()
        output_dir = os.path.dirname(input_file)

        # Construct the command
        otr_decoder_path = "./otrdecoder"
        command = [otr_decoder_path, f"-i {input_file}", f"-e {username}", f"-p {password}"]
        if overwrite:
            command.append("-f")
        else:
            command.append(f"-o {output_dir}")

        # Execute the command
        try:
            subprocess.run(command, check=True)
            QMessageBox.information(self, 'Success!', "Decoding finished without errors!")
        except subprocess.CalledProcessError as e:
            error_message = f"Command '{e.cmd}' returned non-zero exit code {e.returncode}"
            QMessageBox.critical(self, "Decoding failed", error_message)

    def select_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getOpenFileName(self, 'Select File', '', 'All Files (*)', options=options)
        if file_name:
            self.file_input.setText(file_name)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DecoderUI()
    window.show()
    sys.exit(app.exec_())

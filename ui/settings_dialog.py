import os
import re
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QFrame,
    QMessageBox,
)


class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("VideoMind Settings")
        self.setFixedSize(480, 360)
        self.setModal(True)

        self.config_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "backend", "src", "config.py")
        )

        self._setup_ui()
        self._load_config()

    def _setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(18)

        # Dialog Title
        title = QLabel("⚙ VideoMind Configuration")
        title.setObjectName("settings_title")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Divider
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        layout.addWidget(line)

        # STT Whisper Model Choice
        stt_label = QLabel("Speech-to-Text Model (Whisper):")
        stt_label.setObjectName("settings_label")
        layout.addWidget(stt_label)

        self.stt_combo = QComboBox()
        self.stt_combo.setObjectName("settings_combo")
        self.stt_combo.addItems(["tiny", "base", "small", "medium", "large-v3"])
        layout.addWidget(self.stt_combo)

        # LLM Output Model Choice
        llm_label = QLabel("LLM Output Model (Ollama):")
        llm_label.setObjectName("settings_label")
        layout.addWidget(llm_label)

        self.llm_input = QLineEdit()
        self.llm_input.setObjectName("settings_input")
        self.llm_input.setPlaceholderText("e.g. llama3.2, mistral")
        layout.addWidget(self.llm_input)

        layout.addStretch()

        # Action Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setObjectName("settings_cancel_btn")
        self.cancel_btn.clicked.connect(self.reject)

        self.save_btn = QPushButton("Save Settings")
        self.save_btn.setObjectName("settings_save_btn")
        self.save_btn.clicked.connect(self._save_config)

        btn_layout.addWidget(self.cancel_btn)
        btn_layout.addWidget(self.save_btn)

        layout.addLayout(btn_layout)

    def _load_config(self):
        stt_val = "medium"
        llm_val = "llama3.2"

        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r", encoding="utf-8") as f:
                    content = f.read()

                model_match = re.search(r'model\s*=\s*["\']([^"\']+)["\']', content)
                output_match = re.search(r'output_model\s*=\s*["\']([^"\']+)["\']', content)

                if model_match:
                    stt_val = model_match.group(1)
                if output_match:
                    llm_val = output_match.group(1)
            except Exception as e:
                print(f"[Settings] Failed to read config: {e}")

        index = self.stt_combo.findText(stt_val)
        if index >= 0:
            self.stt_combo.setCurrentIndex(index)
        else:
            self.stt_combo.addItem(stt_val)
            self.stt_combo.setCurrentText(stt_val)

        self.llm_input.setText(llm_val)

    def _save_config(self):
        new_stt = self.stt_combo.currentText().strip()
        new_llm = self.llm_input.text().strip()

        if not new_llm:
            QMessageBox.warning(self, "Invalid Input", "Output model cannot be empty!")
            return

        new_content = f'''model = "{new_stt}" 
#change the model to "base" or "tiny" for lower end systems but note that this will drastically degrade the performance of the project. if you want higher performance use "large-v3" but this is for very high end systems as the processing could take hours depending upon the video and system configuration. also if the video you are passing is not in english the "medium" model will perform significantly worse in situations like this you have to use "large-v3" model.
output_model = "{new_llm}"
#this model gives the output. the better model you choose more precise result you will see but the output may delay based on the system. also make sure whatever model you choose that model is downloaded or the project is going to throw an error, if not downloaded open command prompt or terminal and write - 
#                                                               ollama pull model_name
# if you are not sure about this part i suggest you to do some research on the subject.
'''
        try:
            with open(self.config_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            QMessageBox.information(self, "Settings Saved", f"Configuration updated!\nSpeech-to-Text: {new_stt}\nLLM: {new_llm}")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to save settings: {e}")

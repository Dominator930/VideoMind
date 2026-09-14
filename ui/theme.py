LIGHT_THEME = """
/* Light Theme - White, Cyan, Black Text */
QMainWindow, QWidget#central_widget {
    background-color: #FFFFFF;
    color: #111111;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

QWidget {
    color: #111111;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* Header */
QLabel#header {
    font-size: 24px;
    font-weight: 700;
    color: #00838F;
    background-color: #E0F7FA;
    padding: 16px 24px;
    border-bottom: 2px solid #00ACC1;
}

QPushButton#header_back_btn {
    background-color: #00BCD4;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: 600;
    border-radius: 8px;
    padding: 6px 14px;
    border: none;
}

QPushButton#header_back_btn:hover {
    background-color: #00838F;
}

/* Sources Sidebar */
QWidget#sidebar_container {
    background-color: #F4FBFD;
    border-right: 1px solid #B2EBF2;
}

QLabel#sources_title {
    font-size: 16px;
    font-weight: 700;
    color: #00838F;
    padding: 12px 16px 4px 16px;
}

QListWidget#sources {
    background-color: transparent;
    border: none;
    padding: 8px;
    color: #111111;
    font-size: 14px;
}

QListWidget#sources::item {
    padding: 10px 12px;
    border-radius: 8px;
    margin-bottom: 6px;
    background-color: #FFFFFF;
    border: 1px solid #E0F7FA;
    color: #111111;
}

QListWidget#sources::item:selected {
    background-color: #00BCD4;
    color: #FFFFFF;
    font-weight: 600;
}

QListWidget#sources::item:hover {
    background-color: #E0F7FA;
    color: #00838F;
}

/* Screen 1: File Selection & Loading Cards */
QFrame#selection_card {
    background-color: #FFFFFF;
    border: 2px dashed #00BCD4;
    border-radius: 20px;
}

QFrame#selection_card:hover {
    border: 2px dashed #00838F;
    background-color: #F4FBFD;
}

QPushButton#select_button {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00BCD4, stop:1 #00ACC1);
    color: #FFFFFF;
    font-size: 20px;
    font-weight: 700;
    border: none;
    border-radius: 14px;
    padding: 20px 40px;
}

QPushButton#select_button:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #26C6DA, stop:1 #00BCD4);
}

QFrame#loading_card {
    background-color: #F4FBFD;
    border: 1px solid #B2EBF2;
    border-radius: 16px;
    padding: 20px;
}

QLabel#loading_title {
    font-size: 20px;
    font-weight: 700;
    color: #00838F;
}

QLabel#loading_status {
    font-size: 14px;
    color: #424242;
}

QProgressBar {
    border: 2px solid #B2EBF2;
    border-radius: 10px;
    text-align: center;
    background-color: #FFFFFF;
    color: #111111;
    font-weight: 600;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #00BCD4, stop:1 #00838F);
    border-radius: 8px;
}

/* Screen 2: Gemini/Claude Style Chat Interface */
QScrollArea#chat_scroll_area {
    background-color: #FFFFFF;
    border: none;
}

QWidget#chat_scroll_widget {
    background-color: #FFFFFF;
}

/* User Message Bubble */
QFrame#user_bubble {
    background-color: #E0F7FA;
    border: 1px solid #B2EBF2;
    border-radius: 18px;
    border-bottom-right-radius: 4px;
    padding: 14px 18px;
}

QLabel#user_bubble_text {
    font-size: 15px;
    color: #004D40;
    font-weight: 500;
}

/* AI Message Card (Gemini/Claude style) */
QFrame#ai_card {
    background-color: #F8FDFE;
    border: 1px solid #E0F7FA;
    border-radius: 18px;
    border-top-left-radius: 4px;
    padding: 16px 20px;
}

QLabel#ai_avatar_label {
    font-size: 14px;
    font-weight: 700;
    color: #00838F;
}

QTextBrowser#ai_card_text {
    background-color: transparent;
    border: none;
    font-size: 15px;
    color: #111111;
}

/* Bottom Chat Input Bar */
QFrame#input_bar_frame {
    background-color: #FFFFFF;
    border-top: 1px solid #E0F7FA;
    padding: 12px 20px;
}

QLineEdit#question_input {
    background-color: #F4FBFD;
    border: 2px solid #00BCD4;
    border-radius: 24px;
    padding: 12px 22px;
    font-size: 15px;
    color: #111111;
}

QLineEdit#question_input:focus {
    border: 2px solid #00838F;
    background-color: #FFFFFF;
}

QPushButton#send_button {
    background-color: #00838F;
    color: #FFFFFF;
    font-size: 15px;
    font-weight: 700;
    border-radius: 22px;
    padding: 12px 24px;
    border: none;
}

QPushButton#send_button:hover {
    background-color: #00ACC1;
}

QPushButton#send_button:disabled {
    background-color: #CCCCCC;
    color: #666666;
}

/* Bottom Bar Buttons (Circular Icon Buttons) */
QPushButton#theme_button, QPushButton#settings_button {
    background-color: #E0F7FA;
    border: 2px solid #00BCD4;
    border-radius: 25px;
    color: #00838F;
}

QPushButton#theme_button:hover, QPushButton#settings_button:hover {
    background-color: #00BCD4;
    color: #FFFFFF;
}

/* Settings Dialog */
QDialog {
    background-color: #FFFFFF;
    color: #111111;
}

QLabel#settings_title {
    font-size: 20px;
    font-weight: 700;
    color: #00838F;
}

QLabel#settings_label {
    font-size: 14px;
    font-weight: 600;
    color: #111111;
}

QComboBox#settings_combo, QLineEdit#settings_input {
    background-color: #FFFFFF;
    border: 1.5px solid #00BCD4;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 14px;
    color: #111111;
}

QPushButton#settings_save_btn {
    background-color: #00BCD4;
    color: #FFFFFF;
    font-weight: 700;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}

QPushButton#settings_save_btn:hover {
    background-color: #00838F;
}

QPushButton#settings_cancel_btn {
    background-color: #E0E0E0;
    color: #111111;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}
"""

DARK_THEME = """
/* Dark Theme - Black, Gold/Orange Mix, White Text */
QMainWindow, QWidget#central_widget {
    background-color: #0A0A0A;
    color: #FFFFFF;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

QWidget {
    color: #FFFFFF;
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
}

/* Header */
QLabel#header {
    font-size: 24px;
    font-weight: 700;
    color: #FFB300;
    background-color: #141414;
    padding: 16px 24px;
    border-bottom: 2px solid #FF8C00;
}

QPushButton#header_back_btn {
    background-color: #FF9800;
    color: #000000;
    font-size: 13px;
    font-weight: 700;
    border-radius: 8px;
    padding: 6px 14px;
    border: none;
}

QPushButton#header_back_btn:hover {
    background-color: #FFB300;
}

/* Sources Sidebar */
QWidget#sidebar_container {
    background-color: #121212;
    border-right: 1px solid #27272A;
}

QLabel#sources_title {
    font-size: 16px;
    font-weight: 700;
    color: #FFB300;
    padding: 12px 16px 4px 16px;
}

QListWidget#sources {
    background-color: transparent;
    border: none;
    padding: 8px;
    color: #FFFFFF;
    font-size: 14px;
}

QListWidget#sources::item {
    padding: 10px 12px;
    border-radius: 8px;
    margin-bottom: 6px;
    background-color: #1F1F1F;
    border: 1px solid #333333;
    color: #FFFFFF;
}

QListWidget#sources::item:selected {
    background-color: #FF9800;
    color: #000000;
    font-weight: 700;
}

QListWidget#sources::item:hover {
    background-color: #332600;
    color: #FFB300;
}

/* Screen 1: File Selection & Loading Cards */
QFrame#selection_card {
    background-color: #141414;
    border: 2px dashed #FF9800;
    border-radius: 20px;
}

QFrame#selection_card:hover {
    border: 2px dashed #FFD700;
    background-color: #1A170C;
}

QPushButton#select_button {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FFB300, stop:1 #FF6F00);
    color: #000000;
    font-size: 20px;
    font-weight: 800;
    border: none;
    border-radius: 14px;
    padding: 20px 40px;
}

QPushButton#select_button:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FFC107, stop:1 #FF8C00);
}

QFrame#loading_card {
    background-color: #141414;
    border: 1px solid #FF8C00;
    border-radius: 16px;
    padding: 20px;
}

QLabel#loading_title {
    font-size: 20px;
    font-weight: 700;
    color: #FFB300;
}

QLabel#loading_status {
    font-size: 14px;
    color: #CCCCCC;
}

QProgressBar {
    border: 2px solid #FF8C00;
    border-radius: 10px;
    text-align: center;
    background-color: #141414;
    color: #FFFFFF;
    font-weight: 600;
}

QProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FFB300, stop:1 #FF6F00);
    border-radius: 8px;
}

/* Screen 2: Gemini/Claude Style Chat Interface */
QScrollArea#chat_scroll_area {
    background-color: #0A0A0A;
    border: none;
}

QWidget#chat_scroll_widget {
    background-color: #0A0A0A;
}

/* User Message Bubble */
QFrame#user_bubble {
    background-color: #2E1F00;
    border: 1px solid #FF9800;
    border-radius: 18px;
    border-bottom-right-radius: 4px;
    padding: 14px 18px;
}

QLabel#user_bubble_text {
    font-size: 15px;
    color: #FFE082;
    font-weight: 500;
}

/* AI Message Card (Gemini/Claude style) */
QFrame#ai_card {
    background-color: #141414;
    border: 1px solid #27272A;
    border-radius: 18px;
    border-top-left-radius: 4px;
    padding: 16px 20px;
}

QLabel#ai_avatar_label {
    font-size: 14px;
    font-weight: 700;
    color: #FFB300;
}

QTextBrowser#ai_card_text {
    background-color: transparent;
    border: none;
    font-size: 15px;
    color: #FFFFFF;
}

/* Bottom Chat Input Bar */
QFrame#input_bar_frame {
    background-color: #0A0A0A;
    border-top: 1px solid #1F1F1F;
    padding: 12px 20px;
}

QLineEdit#question_input {
    background-color: #141414;
    border: 2px solid #FF9800;
    border-radius: 24px;
    padding: 12px 22px;
    font-size: 15px;
    color: #FFFFFF;
}

QLineEdit#question_input:focus {
    border: 2px solid #FFD700;
    background-color: #1F1A0A;
}

QPushButton#send_button {
    background-color: #FF8C00;
    color: #000000;
    font-size: 15px;
    font-weight: 700;
    border-radius: 22px;
    padding: 12px 24px;
    border: none;
}

QPushButton#send_button:hover {
    background-color: #FFB300;
}

QPushButton#send_button:disabled {
    background-color: #333333;
    color: #666666;
}

/* Bottom Bar Buttons (Circular Icon Buttons) */
QPushButton#theme_button, QPushButton#settings_button {
    background-color: #1F1F1F;
    border: 2px solid #FF9800;
    border-radius: 25px;
    color: #FFB300;
}

QPushButton#theme_button:hover, QPushButton#settings_button:hover {
    background-color: #FF9800;
    color: #000000;
}

/* Settings Dialog */
QDialog {
    background-color: #121212;
    color: #FFFFFF;
}

QLabel#settings_title {
    font-size: 20px;
    font-weight: 700;
    color: #FFB300;
}

QLabel#settings_label {
    font-size: 14px;
    font-weight: 600;
    color: #FFFFFF;
}

QComboBox#settings_combo, QLineEdit#settings_input {
    background-color: #1E1E1E;
    border: 1.5px solid #FF9800;
    border-radius: 8px;
    padding: 8px 12px;
    font-size: 14px;
    color: #FFFFFF;
}

QPushButton#settings_save_btn {
    background-color: #FF9800;
    color: #000000;
    font-weight: 700;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}

QPushButton#settings_save_btn:hover {
    background-color: #FFB300;
}

QPushButton#settings_cancel_btn {
    background-color: #333333;
    color: #FFFFFF;
    font-weight: 600;
    border-radius: 8px;
    padding: 10px 20px;
    border: none;
}
"""

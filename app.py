import unicodedata
import flet as ft
import pyperclip

# --- 以前の TennisInputFormApp クラスをそのままここに記述します ---
# (中身は省略しますが、直前の main.py と全く同じ内容をコピーしてください)
# ... [TennisInputFormApp クラスの全内容をここに貼り付けてください] ...

def main(page: ft.Page):
    app = TennisInputFormApp()
    app.main(page)

# Webサーバーとして動かすための標準的な記述
if __name__ == "__main__":
    ft.app(target=main, port=8000)
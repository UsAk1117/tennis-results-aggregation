import os
import flet as ft

# --- ここにあなたの本来のコード（クラスなど）をすべて書いてください ---
# 例えば TennisInputFormApp の定義はここにありますよね？
class TennisInputFormApp(ft.Control):
    def build(self):
        return ft.Text("ここに本来のフォーム画面が入ります")
# -----------------------------------------------------------

def main(page: ft.Page):
    # ここで本来のクラスを呼び出します
    # ※もしクラス名が TennisInputFormApp でなければ、ここを修正してください！
    app = TennisInputFormApp()
    page.add(app)

if __name__ == "__main__":
    # RenderでWebとして動かすための設定
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=main, port=port, view=ft.AppView.WEB_BROWSER)
import os
import flet as ft

# 【クラス定義】
class TennisInputFormApp(ft.Control):
    def build(self):
        # 本来のフォームの要素をここに追加
        return ft.Text("テニス入力フォーム")

# 【メイン関数】
def main(page: ft.Page):
    page.add(TennisInputFormApp())

# 【起動設定】
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=main, port=port, view=ft.AppView.WEB_BROWSER)

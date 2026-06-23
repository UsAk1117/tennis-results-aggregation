import os
import flet as ft
import pyperclip

class TennisInputFormApp:
    def __init__(self):
        # 必要な変数の初期化
        self.result_textbox = ft.TextField(label="生成されたノート", multiline=True, min_lines=8)

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "テニス試合結果 入力フォーム"
        self.page.scroll = ft.ScrollMode.AUTO

        # UIコンポーネントの作成
        header = ft.Text("テニス試合結果 入力フォーム", size=20, weight="bold")
        name_field = ft.TextField(label="部員名")
        score_field = ft.TextField(label="スコア")
        
        def copy_text(e):
            if self.result_textbox.value:
                pyperclip.copy(self.result_textbox.value)
                self.page.show_snack_bar(ft.SnackBar(ft.Text("コピーしました！")))

        # --- 重要：リストに格納して一括で追加 ---
        controls = [
            header,
            name_field,
            score_field,
            ft.Row([
                ft.ElevatedButton("クリア", on_click=lambda e: setattr(self.result_textbox, 'value', '') or self.page.update()),
                ft.ElevatedButton("全体をコピー", on_click=copy_text)
            ]),
            ft.Card(content=ft.Container(content=self.result_textbox, padding=10))
        ]
        
        page.add(*controls)

if __name__ == "__main__":
    app = TennisInputFormApp()
    port = int(os.environ.get("PORT", 10000))
    # view=... を削除し、ポートとホストのみ指定
    ft.app(target=app.main, port=port, host="0.0.0.0")
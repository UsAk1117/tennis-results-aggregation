import os
import unicodedata
import flet as ft
import pyperclip

class TennisInputFormApp:
    def __init__(self):
        self.MEMBER_LIST = ["誰田", "誰谷", "誰本", "誰逃", "誰口"]
        self.UNIV_LIST = ["何処大", "壮大", "寛大", "期待大", "橙大"]
        self.temp_our = None
        self.wo_status = "normal"

    def main(self, page: ft.Page):
        self.page = page
        self.page.title = "テニス試合結果 入力フォーム"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.padding = 15

        # コンポーネント定義
        self.score_entry = ft.TextField(label="スコア", expand=True)
        self.result_textbox = ft.TextField(label="生成されたノート", multiline=True, min_lines=8)
        self.opp_player_entry = ft.TextField(expand=True, label="相手選手名")
        self.our_player_combo = ft.Dropdown(options=[ft.dropdown.Option(m) for m in self.MEMBER_LIST], label="部員名")
        self.opp_univ_combo = ft.Dropdown(options=[ft.dropdown.Option(u) for u in self.UNIV_LIST], label="相手大学")
        
        # ボタンクリックロジック（簡略化版）
        def copy_to_clipboard(e):
            pyperclip.copy(self.result_textbox.value)
            self.page.show_snack_bar(ft.SnackBar(ft.Text("コピーしました！")))

        # --- ここが重要：すべてのUIを一括で定義してページに追加 ---
        page.add(
            ft.Text("テニス試合結果 入力フォーム", size=20, weight="bold"),
            ft.Row([
                ft.ElevatedButton("🗑️ クリア", on_click=lambda e: setattr(self.result_textbox, 'value', '') or self.page.update()),
                ft.FilledButton("📋 全体をコピー", on_click=copy_to_clipboard)
            ]),
            ft.Divider(),
            ft.Card(content=ft.Container(content=ft.Column([
                ft.Text("試合入力", weight="bold"),
                self.our_player_combo,
                self.opp_player_entry,
                self.opp_univ_combo,
                self.score_entry,
            ]), padding=10)),
            ft.Card(content=ft.Container(content=self.result_textbox, padding=10))
        )
        # 最後に強制更新
        page.update()

if __name__ == "__main__":
    app = TennisInputFormApp()
    port = int(os.environ.get("PORT", 8000))
    # Render環境で安定させるために host="0.0.0.0" を指定
    ft.app(target=app.main, port=port, host="0.0.0.0")
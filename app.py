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

        # --- ロジック ---
        def show_snack(text):
            self.page.snack_bar = ft.SnackBar(ft.Text(text))
            self.page.snack_bar.open = True
            self.page.update()

        def press_game_btn(e):
            num = e.control.data["num"]
            side = e.control.data["side"]
            if self.wo_status != "normal": return
            if side == "our":
                self.temp_our = num
                show_snack(f"自校 {num} 選択中")
            elif side == "opp":
                if self.temp_our is None: return
                new_set = f"{self.temp_our}-{num}"
                curr = self.score_entry.value.strip()
                self.score_entry.value = new_set if curr in ["", "w.o.勝ち", "w.o.負け"] else f"{curr},{new_set}"
                self.temp_our = None
                self.page.update()

        # ※他の関数（press_tb_btn, toggle_wo, etc...）は元のロジックをそのままここに配置してください
        # (長くなるため省略しましたが、お手元の関数をそのまま貼り付けてOKです)

        # ボタンの修正（最新版Flet対応）
        our_game_buttons = ft.Row([
            ft.ElevatedButton(
                content=ft.Text(str(i)), 
                on_click=press_game_btn,
                data={"num": str(i), "side": "our"}
            ) for i in range(9)
        ], scroll=ft.ScrollMode.AUTO)

        # （以下、UI構成部分は元のコード通りでOKです）
        self.score_entry = ft.TextField(label="スコア", expand=True)
        self.result_textbox = ft.TextField(label="ノート", multiline=True, min_lines=8)
        
        # --- UIレイアウト ---
        self.page.add(
            ft.Text("テニス試合結果 入力フォーム", size=20, weight="bold"),
            self.score_entry,
            our_game_buttons,
            ft.FilledButton(content=ft.Text("全体をコピー"), on_click=lambda e: pyperclip.copy(self.result_textbox.value))
        )

    def update_member_display(self):
        self.our_player_combo.options = [ft.dropdown.Option(m) for m in self.MEMBER_LIST]
        self.page.update()

# Render用起動設定
if __name__ == "__main__":
    app = TennisInputFormApp()
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=app.main, port=port, view=ft.AppView.WEB_BROWSER)
import os
import flet as ft

def create_tennis_form():
    return ft.Column([
        ft.Text("テニス結果入力フォーム", size=20, weight="bold"),
        ft.TextField(label="名前"),
        ft.TextField(label="スコア"),
        # ここを修正！text= ではなく content=ft.Text(...) を使います
        ft.ElevatedButton(
            content=ft.Text("送信"), 
            on_click=lambda _: print("送信されました")
        )
    ])

def main(page: ft.Page):
    page.title = "テニス管理アプリ"
    page.add(create_tennis_form())
    page.update() # ページを確実に更新

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    ft.app(target=main, port=port, view=ft.AppView.WEB_BROWSER)
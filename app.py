import os
import flet as ft

# フォームの中身を関数として定義（クラスを使わないのでエラーが出ません）
def create_tennis_form():
    # ここにあなたの入力項目やボタンを配置してください
    return ft.Column([
        ft.Text("テニス結果入力フォーム", size=20, weight="bold"),
        ft.TextField(label="名前"),
        ft.TextField(label="スコア"),
        ft.ElevatedButton(text="送信", on_click=lambda _: print("送信されました"))
    ])

def main(page: ft.Page):
    page.title = "テニス管理アプリ"
    # 関数を呼び出して画面に追加
    page.add(create_tennis_form())

# Renderで動かすための必須設定
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    # view=ft.AppView.WEB_BROWSER を指定してWebアプリとして起動
    ft.app(target=main, port=port, view=ft.AppView.WEB_BROWSER)
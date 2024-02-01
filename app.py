import flet as ft
import base64
import cv2

cap = cv2.VideoCapture(0)

class Countdown(ft.UserControl):
    def __init__(self):
        super().__init__()

    def did_mount(self):
        self.update_timer()

    def update_timer(self):
        while True:
            _, frame = cap.read()
            # Skalieren Sie das Frame auf HD Ready-Auflösung (1280x720)
            frame = cv2.resize(frame, (1280, 720))
            _, im_arr = cv2.imencode('.png', frame)
            im_b64 = base64.b64encode(im_arr)
            self.img.src_base64 = im_b64.decode("utf-8")
            self.update()

    def build(self):
        self.img = ft.Image(
            border_radius=ft.border_radius.all(20),
            width=1280,  # Passen Sie die Breite auf 1280 an
            height=720,  # Passen Sie die Höhe auf 720 an
        )
        return self.img

def main(page: ft.Page):
    page.padding = 50
    page.window_left = page.window_left + 100
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(
        Countdown(),
        ft.Container(
            margin=ft.margin.only(top=20),
            content=ft.Row([
                ft.ElevatedButton(text="Extra Button 1", on_click=lambda e: print("Extra Button 1 clicked")),
                ft.ElevatedButton(text="Extra Button 2", on_click=lambda e: print("Extra Button 2 clicked")),
                ft.ElevatedButton(text="Extra Button 3", on_click=lambda e: print("Extra Button 3 clicked")),
            ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
        ),
        ft.Card(
            elevation=30,
            content=ft.Container(
                bgcolor=ft.colors.WHITE24,
                padding=10,
                border_radius=ft.border_radius.all(20),
                content=ft.Column([
                    ft.Slider(
                        min=500, max=900, on_change=lambda e: print(e.control.value)
                    ),
                    ft.Text("Beispieltext unter dem ersten Slider"),
                    ft.Slider(
                        min=500, max=900,
                    ),
                    ft.Text("Beispieltext unter dem zweiten Slider"),
                    ft.Slider(
                        min=500, max=900,
                    ),
                    ft.Text("Beispieltext unter dem dritten Slider"),
                ]
                ),
            )
        ),
    )

if __name__ == '__main__':
    ft.app(target=main)
    cap.release()
    cv2.destroyAllWindows()
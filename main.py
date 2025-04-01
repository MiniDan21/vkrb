import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk


class VideoApp:
    def __init__(self, root, video_source):
        self.root = root
        self.root.title("Video Background App")
        self.root.geometry("360x640")
        self.root.resizable(False, False)

        # Захват видео
        self.video_source = video_source
        self.cap = cv2.VideoCapture(self.video_source)

        # Холст для видео
        self.canvas = tk.Canvas(root, width=360, height=640)
        self.canvas.pack()

        # Кнопки
        self.create_buttons()

        # Обновление видео
        self.update_frame()

    def create_buttons(self):
        # 🔴 — консольный вывод
        self.btn1 = ttk.Button(self.root, text="🔴", command=self.red_button_action)
        self.btn1.place(x=10, y=10)

        # 🟢 — меняет текст
        self.btn2 = ttk.Button(self.root, text="🟢", command=self.green_button_action)
        self.btn2.place(x=300, y=10)

        # 🔵 — закрытие
        self.btn3 = ttk.Button(self.root, text="🔵", command=self.root.quit)
        self.btn3.place(x=10, y=600)

    def red_button_action(self):
        print("Красная кнопка нажата")

    def green_button_action(self):
        self.btn2.config(text="Нажата!")

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (360, 640))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(frame)
            self.photo = ImageTk.PhotoImage(image=image)
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.root.after(30, self.update_frame)

    def __del__(self):
        if self.cap.isOpened():
            self.cap.release()


if __name__ == "__main__":
    root = tk.Tk()
    app = VideoApp(root, "out.mp4")  # Замените на свой путь к видео
    root.mainloop()

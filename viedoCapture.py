import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk  # Pillow-Bibliothek für die Bildverarbeitung

class Exercise:
    def __init__(self, name):
        self.name = name

    def start(self):
        # Hier implementieren Sie die Logik für die jeweilige Übung
        print(f"Starte die Übung: {self.name}")

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness App")
        self.root.geometry("600x400")  # Größe des Hauptfensters

        # Kamera-Label
        self.video_label = tk.Label(root, height=15, width=30)
        self.video_label.pack()

        # Übungsauswahl
        self.exercise_label = tk.Label(root, text="Wähle eine Übung:")
        self.exercise_label.pack()

        self.exercise_var = tk.StringVar(root)
        exercises = ["Liegestütze", "Kniebeugen", "Plank"]  # Fügen Sie weitere Übungen hinzu
        self.exercise_dropdown = tk.OptionMenu(root, self.exercise_var, *exercises)
        self.exercise_dropdown.config(width=20)  # Breite des Auswahlmenüs
        self.exercise_dropdown.pack()

        # Start-Button
        self.start_button = tk.Button(root, text="Start", command=self.start_workout, height=3, width=20)
        self.start_button.pack()

        # Kamera initialisieren (noch nicht starten)
        self.cap = cv2.VideoCapture(0)
        self.camera_started = False

    def start_workout(self):
        exercise_name = self.exercise_var.get()
        if exercise_name:
            exercise = Exercise(exercise_name)
            exercise.start()
            messagebox.showinfo("Workout gestartet", f"Starte das Workout für {exercise_name}!")
            # Starte die Kameraanzeige
            self.start_camera()
        else:
            messagebox.showwarning("Ungültige Eingabe", "Bitte wählen Sie eine Übung aus.")

    def start_camera(self):
        if not self.camera_started:
            self.camera_started = True
            self.show_camera()

    def show_camera(self):
        _, frame = self.cap.read()
        photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.video_label.configure(image=photo)
        self.video_label.image = photo
        if self.camera_started:
            self.root.after(10, self.show_camera)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()

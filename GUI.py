import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from push_up import PushUpCounter
from knee import KneeCounter
#from curly import *Hier könnte Ihre Klasse stehen*

class FitnessApp:
    def __init__(self, root):
        root.attributes('-fullscreen', True)  # Hauptfenster auf Vollbild
        root.bind('<Escape>', lambda event: root.attributes('-fullscreen', False))  # Escape-Taste zum Beenden des Vollbildmodus
        
        # Fenstergröße wenn Fullscreen beendet ist
        self.root = root
        self.root.title("Fitness App")
        self.root.geometry("600x400")  # Größe des Hauptfensters

        # Video Beschriftung
        self.video_label = tk.Label(root, height=15, width=40)
        self.video_label.pack()

        # Beschriftung fürs Dropdown
        self.exercise_label = tk.Label(root, text="Wähle eine Übung:")
        self.exercise_label.pack()

        # Dropdown für die Übungsauswahl
        exercises = ["Push_up", "Kniebeugen", "Bizeps"]
        self.exercise_var = tk.StringVar(root, exercises[0])
        self.exercise_var.set("")  # Erste Auswahl auf NULL setzten
        self.exercise_dropdown = tk.OptionMenu(root, self.exercise_var, *exercises)
        self.exercise_dropdown.config(width=20) # Größe des Auswahlmenüs
        self.exercise_dropdown.pack()

        # Startbutton
        self.start_button = tk.Button(root, text="Start", command=self.start_workout, height=3, width=20)
        self.start_button.pack()

        # Infos zur Steuerung
        self.info_label = tk.Label(root, text="Zum Beenden q drücken")
        self.info_label.pack(pady=10)
        self.info_label = tk.Label(root, text="Drücke Esc um Vollbildmodus zubeenden")
        self.info_label.pack(pady=10)

        # Kamera initialisieren
        self.cap = cv2.VideoCapture(0)

        # Konfiguration für HD-Qualität
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                     
        self.camera_started = False
        self.current_exercise = None

    # Ausführung der Übungen mit abfrage welche Ausgeführt werden soll
    def start_workout(self):
        exercise_name = self.exercise_var.get()
        if exercise_name:
            # Vergleich mit der Auswahl aus dem Dropdownmenu
            if exercise_name == "Push_up":
                self.current_exercise = PushUpCounter()
                self.current_exercise.run_push()  # Direkt die Übung starten
                self.stop_workout()  # Übung nach dem Durchlauf beenden
            elif exercise_name == "Kniebeugen":
                self.current_exercise = KneeCounter()
                self.current_exercise.run_knee()  # Direkt die Übung starten
                self.stop_workout()  # Übung nach dem Durchlauf beenden
            elif exercise_name == "Bizeps":
                # self.current_exercise = CurlsCounter()
                # self.current_exercise.run_curly()  # Direkt die Übung starten
                self.stop_workout()  # Übung nach dem Durchlauf beenden
            else:
                # Für andere Übungen könnten hier entsprechende Klassen hinzugefügt werden
                pass
            messagebox.showinfo("Workout gestartet", f"Starte das Workout für {exercise_name}!")
            self.start_camera()
            self.start_button.pack_forget()
        else:
            messagebox.showwarning("Ungültige Eingabe", "Bitte wählen Sie eine Übung aus.")

    # Übungen beenden
    def stop_workout(self):
        if hasattr(self, 'current_exercise'):
            self.current_exercise.stop()
            messagebox.showinfo("Workout beendet", f"Beende das Workout für {self.current_exercise.name}!")
            self.stop_camera()
            self.start_button.pack()

    # Kamera starten
    def start_camera(self):
        if not self.camera_started:
            self.camera_started = True
            self.exercise_label.pack_forget()
            self.start_button.pack_forget()
            self.exercise_dropdown.pack_forget()
            self.video_label.pack(expand=True, fill=tk.BOTH)
            self.show_camera()

    # Ausschalten der Kamera
    def stop_camera(self):
        if self.camera_started:
            self.camera_started = False
            self.video_label.pack_forget()

    # Kamerabild anzeigen
    def show_camera(self):
        _, frame = self.cap.read()
        frame = cv2.resize(frame, (1280, 720))      #Größe des Aufnahme Fensters
        photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.video_label.configure(image=photo)
        self.video_label.image = photo
        if self.camera_started:
            self.root.after(10, self.show_camera)

# Soll erst in der Main ausgeführt werden (Verhindert sofortiges Starten)
if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()

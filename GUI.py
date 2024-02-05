import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
from push_up import PushUpCounter
from knee import KneeCounter

class FitnessApp:
    def __init__(self, root):
        root.attributes('-fullscreen', True)  # Setzen Sie das Hauptfenster auf Vollbild
        root.bind('<Escape>', lambda event: root.attributes('-fullscreen', False))  # Escape-Taste zum Beenden des Vollbildmodus
        
        self.root = root
        self.root.title("Fitness App")
        self.root.geometry("600x400")  # Größe des Hauptfensters

        self.video_label = tk.Label(root, height=15, width=40)
        self.video_label.pack()

        self.exercise_label = tk.Label(root, text="Wähle eine Übung:")
        self.exercise_label.pack()

        exercises = ["Push_up", "Kniebeugen"]
        self.exercise_var = tk.StringVar(root, exercises[0])
        self.exercise_dropdown = tk.OptionMenu(root, self.exercise_var, *exercises)
        self.exercise_dropdown.config(width=20) # Größe des Auswahlmenüs
        self.exercise_dropdown.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_workout, height=3, width=20)
        self.start_button.pack()

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_workout, height=3, width=20)
        self.stop_button.pack()
        self.stop_button.pack_forget()

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app, height=3, width=20)
        self.exit_button.pack()
        self.exit_button.pack_forget()

        self.info_label = tk.Label(root, text="Zum Beenden q drücken")
        self.info_label.pack(pady=10)
        self.info_label = tk.Label(root, text="Drücke Esc um Vollbildmodus zubeenden")
        self.info_label.pack(pady=10)

        # Kamera initialisieren (noch nicht starten)
        self.cap = cv2.VideoCapture(0)

        # Konfiguration für HD-Qualität
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                     
        self.camera_started = False
        self.current_exercise = None


        self.update_menu()

    def update_menu(self):
        exercises = ["Push_up", "Kniebeugen"]
        self.exercise_var.set("")  # Setzen Sie den Wert auf einen leeren String
        self.exercise_dropdown["menu"].delete(0, "end")  # Löschen Sie alle vorherigen Einträge

        for exercise in exercises:
            self.exercise_dropdown["menu"].add_command(label=exercise, command=tk._setit(self.exercise_var, exercise))    

    def start_workout(self):
        exercise_name = self.exercise_var.get()
        if exercise_name:
            if exercise_name == "Push_up":
                self.current_exercise = PushUpCounter()
                self.current_exercise.run_push()  # Direkt die Übung starten
                self.stop_workout()  # Übung nach dem Durchlauf beenden
            elif exercise_name == "Kniebeugen":
                self.current_exercise = KneeCounter()
                self.current_exercise.run_knee()  # Direkt die Übung starten
                self.stop_workout()  # Übung nach dem Durchlauf beenden

            else:
                # Für andere Übungen könnten hier entsprechende Klassen hinzugefügt werden
                pass
            messagebox.showinfo("Workout gestartet", f"Starte das Workout für {exercise_name}!")
            self.start_camera()
            self.start_button.pack_forget()
            self.stop_button.pack()
            self.exit_button.pack()
            self.update_menu()
        else:
            messagebox.showwarning("Ungültige Eingabe", "Bitte wählen Sie eine Übung aus.")

    def stop_workout(self):
        if hasattr(self, 'current_exercise'):
            self.current_exercise.stop()
            messagebox.showinfo("Workout beendet", f"Beende das Workout für {self.current_exercise.name}!")
            self.stop_camera()
            self.stop_button.pack_forget()
            self.start_button.pack()
            self.exit_button.pack_forget()

    def start_camera(self):
        if not self.camera_started:
            self.camera_started = True
            self.exercise_label.pack_forget()
            self.start_button.pack_forget()
            self.exercise_dropdown.pack_forget()
            self.video_label.pack(expand=True, fill=tk.BOTH)
            self.show_camera()
            self.update_menu()

    def stop_camera(self):
        if self.camera_started:
            self.camera_started = False
            self.video_label.pack_forget()

    def show_camera(self):
        _, frame = self.cap.read()
        frame = cv2.resize(frame, (1280, 720))      #Größe des Aufnahme Fensters
        photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.video_label.configure(image=photo)
        self.video_label.image = photo
        if self.camera_started:
            self.root.after(10, self.show_camera)

    def exit_app(self):
        self.stop_workout()
        self.root.destroy()
        self.stop_camera()

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()

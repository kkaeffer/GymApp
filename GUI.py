import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk  # Pillow-Bibliothek für die Bildverarbeitung
import knee as Knee
#import push_up as Push_up

class Exercise:
    def __init__(self, name):
        self.name = name
        # import knee as name
        import push_up as Push_up

    def start(self):
        # Hier implementieren Sie die Logik für die jeweilige Übung
        print(f"Starte die Übung: {self.name}")

    def stop(self):
        # Hier implementieren Sie die Logik zum Beenden der Übung
        print(f"Beende die Übung: {self.name}")

class FitnessApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Fitness App")
        self.root.geometry("1280x720")  # Größe des Hauptfensters

        # Kamera-Label
        self.video_label = tk.Label(root, height=15, width=40)
        self.video_label.pack()
        #self.video_label.grid(row=0, column=0, columnspan=2)

        # Übungsauswahl
        self.exercise_label = tk.Label(root, text="Wähle eine Übung:")
        self.exercise_label.pack()
        #self.exercise_label.grid(row=10, column=0, columnspan=2)

        self.exercise_var = tk.StringVar(root)
        exercises = [Exercise("Push_up"), Knee("Kniebeugen")]  # Fügen Sie weitere Übungen hinzu
        #exercises = [Exercise("Auswahl")], Push_up("Push_up")#,  Knee("Kniebeugen")]  # Fügen Sie weitere Übungen hinzu
        self.exercise_dropdown = tk.OptionMenu(root, self.exercise_var, *exercises)
        self.exercise_dropdown.config(width=20)  # Breite des Auswahlmenüs
        self.exercise_dropdown.pack()
        #self.exercise_label.grid(row=12, column=8, columnspan=90)

        # Start-Button
        self.start_button = tk.Button(root, text="Start", command=self.start_workout, height=3, width=20)
        self.start_button.pack()
        #self.exercise_label.grid(row=6, column=0, columnspan=2)

         # Stop-Button
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_workout, height=3, width=20)
        self.stop_button.pack()
        self.stop_button.pack_forget()  # Der Stop-Button ist zu Beginn nicht sichtbar

        # Kamera initialisieren (noch nicht starten)
        self.cap = cv2.VideoCapture(0) 

        # Konfiguration für HD-Qualität
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
                     
        self.camera_started = False

    def start_workout(self):
        exercise_name = self.exercise_var.get()
        if exercise_name:
            if exercise_name == "Push_up":
                self.current_exercise = Push_up(exercise_name)
            elif exercise_name == "Kniebeugen":
                self.current_exercise = Knee(exercise_name)
            else:
                pass

            self.current_exercise.start()
            messagebox.showinfo("Workout gestartet", f"Starte das Workout für {exercise_name}!")
            # Starte die Kameraanzeige
            self.start_camera()
            # Aktiviere den Stop-Button und deaktiviere den Start-Button
            self.start_button.pack_forget()
            self.stop_button.pack()
        else:
            messagebox.showwarning("Ungültige Eingabe", "Bitte wählen Sie eine Übung aus.")

    def stop_workout(self):
        if hasattr(self, 'current_exercise'):
            self.current_exercise.stop()
            messagebox.showinfo("Workout beendet", f"Beende das Workout für {self.current_exercise.name}!")
            # Stoppe die Kameraanzeige
            self.stop_camera()
            # Deaktiviere den Stop-Button und aktiviere den Start-Button
            self.stop_button.pack_forget()
            self.start_button.pack()

    def start_camera(self):
        if not self.camera_started:
            self.camera_started = True
            self.exercise_label.pack_forget()
            self.start_button.pack_forget()
            self.exercise_dropdown.pack_forget()
            self.video_label.pack(expand=True, fill=tk.BOTH)
            self.show_camera()

    def stop_camera(self):
        if self.camera_started:
            self.camera_started = False
            self.video_label.pack_forget()

    def show_camera(self):
        _, frame = self.cap.read()
        frame = cv2.resize(frame, (1280, 720))     #Kamera größe - schneidet beim vergrößern ab 
        photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
        self.video_label.configure(image=photo)
        self.video_label.image = photo
        if self.camera_started:
            self.root.after(10, self.show_camera)

if __name__ == "__main__":
    root = tk.Tk()
    app = FitnessApp(root)
    root.mainloop()

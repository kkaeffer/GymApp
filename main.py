import cv2
import mediapipe as mp

class FitnessApp:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.mp_holistic = mp.solutions.holistic
        self.holistic = self.mp_holistic.Holistic()
        self.count_reps = 0

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("Failed to capture video.")
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.holistic.process(frame_rgb)

            if results.pose_landmarks:
                # Hier könntest du die Logik für die Kniebeugenimplementierung hinzufügen
                # Zum Beispiel könntest du die Landmarks für die Knie verwenden.

                # Zeige die Landmarks im Video an
                self.show_landmarks(frame, results.pose_landmarks)

            cv2.imshow("Fitness App", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break
            elif key == ord('s'):
                self.count_reps += 1
                print(f"Kniebeugen: {self.count_reps}")

        self.cap.release()
        cv2.destroyAllWindows()

    def show_landmarks(self, frame, landmarks):
        for lm in landmarks.landmark:
            h, w, c = frame.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            cv2.circle(frame, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

if __name__ == "__main__":
    app = FitnessApp()
    app.run()

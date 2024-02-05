# knee.py
import cv2
import mediapipe as md
import math

md_drawing = md.solutions.drawing_utils
md_pose = md.solutions.pose

class KneeCounter:
    def __init__(self):
        self.count = 0

    def calculate_angle(self, a, b, c):
        angle_radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = (angle_degrees + 360) % 360  # Normalisierung auf den Bereich [0, 360]
        return angle_degrees

    def run_knee(self):
        count = 0
        position = None

        cap = cv2.VideoCapture(0)

        with md_pose.Pose(
                min_detection_confidence=0.7,
                min_tracking_confidence=0.7) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Leere Kamera")
                    break

                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                result = pose.process(image)

                imlist = []

                if result.pose_landmarks:
                    md_drawing.draw_landmarks(
                        image, result.pose_landmarks, md_pose.POSE_CONNECTIONS)
                    for id, im in enumerate(result.pose_landmarks.landmark):
                        h, w, _ = image.shape
                        X, Y = int(im.x * w), int(im.y * h)
                        imlist.append([id, X, Y])

                if len(imlist) != 0:
                    hip_landmark = imlist[23]  # Linkes Hüftgelenk
                    knee_landmark = imlist[25]  # Linkes Knie
                    ankle_landmark = imlist[27]  # Linkes Fußgelenk

                    # Berechnung der Winkel für die Kniebeugen
                    thigh_angle = self.calculate_angle(hip_landmark[1:], knee_landmark[1:], ankle_landmark[1:])

                    # Wenn der Winkel nahe bei 90 Grad liegt, wird eine Kniebeuge gezählt
                    if 70 <= thigh_angle <= 110 and position != "down":
                        position = "down"
                        count += 1
                        print(count)
                    elif thigh_angle > 120:
                        position = "up"
                    else:
                        position = None

                cv2.imshow("Squat counter", cv2.flip(image, 1))
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

        return count

    def start(self):
        print("Kniebeugen-Übung gestartet.")
        self.run_knee()

if __name__ == "__main__":
    knee_counter = KneeCounter()
    knee_counter.start()
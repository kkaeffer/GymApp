# knee.py
#Import der OpenCV, Mediapipe und Math Bibliotheken
import cv2
import mediapipe as md
import math
from counter import countfunc

#Variablendefinition
md_drawing = md.solutions.drawing_utils
md_pose = md.solutions.pose

#Klassendefinition
class KneeCounter:
    def __init__(self):
        self.count = 0
    #Funktion zur Winkelberechnung
    def calculate_angle(self, a, b, c):
        angle_radians = math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0])
        angle_degrees = math.degrees(angle_radians)
        angle_degrees = (angle_degrees + 360) % 360  # Normalisierung auf den Bereich [0, 360]
        return angle_degrees

    #Funktionsdefinition
    def run_knee(self):
        #Variablendefinition
        count = 0
        position = None

        #Videoaufnahme
        cap = cv2.VideoCapture(0)

        #Mindestanforderung an Gewissheit
        with md_pose.Pose(
                min_detection_confidence=0.7,
                min_tracking_confidence=0.7) as pose:
            #Check ob Aufnahme moeglich, ansonsten Abbruch
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("Fehler")
                    break
                
                #Farbanpassung
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                result = pose.process(image)

                #Leere Liste für die Landmarks initialisieren
                imlist = []

                #Ueberprüfen, ob Pose Landmarks im Ergebnis vorhanden sind
                if result.pose_landmarks:
                    #Zeichnen der Landmarks
                    md_drawing.draw_landmarks(
                        image, result.pose_landmarks, md_pose.POSE_CONNECTIONS)
                    #Ueber Landmarks iterieren und Bildabmessungen erfassen
                    for id, im in enumerate(result.pose_landmarks.landmark):
                        h, w, _ = image.shape
                        #Koordinaten in Pixel umrechnen
                        X, Y = int(im.x * w), int(im.y * h)
                        #In die Liste einfuegen
                        imlist.append([id, X, Y])

                if len(imlist) != 0:
                    hip_landmark = imlist[23]  #Linkes Hueftgelenk
                    knee_landmark = imlist[25]  #Linkes Knie
                    ankle_landmark = imlist[27]  #Linkes Fußgelenk

                    #Berechnung der Winkel für die Kniebeugen
                    thigh_angle = self.calculate_angle(hip_landmark[1:], knee_landmark[1:], ankle_landmark[1:])

                    #Wenn der Winkel nahe bei 90 Grad liegt, wird eine Kniebeuge gezaehlt
                    if 70 <= thigh_angle <= 110 and position != "down":
                        position = "down"
                        count += 1
                        print(count)
                    elif thigh_angle > 120:
                        position = "up"
                    else:
                        position = None

                #Anzeige eines Counters und Hinweistext
                countfunc(image, count)
                cv2.putText(image, f'Q zum Beenden', (370, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                #Spiegele das gesamte Bild horizontal
                image = cv2.flip(image, 1)

                #Fenster nicht im Vollbildmodus -> Könnte das Bild verzerren
                cv2.namedWindow("Squat Counter", cv2.WINDOW_NORMAL)            
                       

                #Fenstergröße
                cv2.resizeWindow("Squat Counter", 980, 690)
                cv2.imshow("Squat Counter", cv2.flip(image, 1))
                key = cv2.waitKey(1)

                #Zum Beenden q drücken
                if key == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

        return count

    def start(self):
        print("Kniebeugen-Übung gestartet.")
        self.run_knee()
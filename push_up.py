#pushUp.py
#Import der OpenCV und Mediapipe Bibliotheken
import cv2
import mediapipe as md
from counter import countfunc

#Variablendefinition
md_drawing = md.solutions.drawing_utils
md_pose = md.solutions.pose

#Klassendefinition
class PushUpCounter:
    def __init__(self):
        
        #Variablendefinition
        self.count = 0
        self.position = None

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
                    #Schulter-Landmarks, pruefen ob in korrekter Reihenfolge
                    if imlist[11][2] <= imlist[12][2] and imlist[12][2] <= imlist[13][2]:
                        self.position = "down"
                    #Nun umgekehrte Reihenfolge und hochzaehlen
                    elif imlist[11][2] >= imlist[12][2] and imlist[12][2] >= imlist[13][2]:
                        self.position = "up"
                        self.count += 1
                        print(self.count)
                    else:
                        self.position = None

                #Text + Count Anzeige
                #font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(image, f'Push-ups: {self.count}', (10, 40), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
                #cv2.putText(image, f'Q zum Beenden', (390, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
                
                countfunc(image, self.count)
                cv2.putText(image, f'Q zum Beenden', (370, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

                #Spiegele das gesamte Bild horizontal
                image = cv2.flip(image, 1)

                #Fenster benennen und Vollbild schalten
                cv2.namedWindow("Push-up Counter", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Push-up Counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("Push-up Counter", cv2.flip(image, 1))
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import numpy as np
#from counter import countfunc

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class CurlCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)

        # Initialize Mediapipe Pose
        self.pose = mp_pose.Pose(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def calculate_angle(self, a, b, c):
        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
        angle = np.abs(radians*180.0/np.pi)

        if angle > 180.0:
            angle = 360 - angle

        return angle 

    def run_curl(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = self.pose.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
                elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
                wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]

                angle = self.calculate_angle(shoulder, elbow, wrist)

                # Curl counter logic
                if angle > 160:
                    self.stage = "down"
                if angle < 30 and self.stage == 'down':
                    self.stage = "up"
                    self.counter += 1
                    print(self.counter)

            except:
                pass

            # Render curl counter
            cv2.putText(image, 'Counter: {}'.format(self.counter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

            # Render detections
            mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                    mp_drawing.DrawingSpec(color=(245,117,66), thickness=2, circle_radius=2), 
                                    mp_drawing.DrawingSpec(color=(245,66,230), thickness=2, circle_radius=2) 
                                    )               

            #countfunc(image, self.count)
            cv2.putText(image, f'Q zum Beenden', (370, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            #Spiegele das gesamte Bild horizontal
            image = cv2.flip(image, 1)

            # #Fenster benennen und Vollbild schalten
            cv2.namedWindow("Curls Counter", cv2.WND_PROP_FULLSCREEN)
            cv2.setWindowProperty("Curls Counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.imshow("Curls Counter", cv2.flip(image, 1))
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    curl_counter = CurlCounter()
    curl_counter.run_curl()
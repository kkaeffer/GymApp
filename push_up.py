# pushUp.py
import cv2
import mediapipe as md

md_drawing = md.solutions.drawing_utils
md_pose = md.solutions.pose

class PushUpCounter:
    def __init__(self):
        
        self.count = 0
        self.position = None

        cap = cv2.VideoCapture(0)

        with md_pose.Pose(
                min_detection_confidence=0.7,
                min_tracking_confidence=0.7) as pose:
            while cap.isOpened():
                success, image = cap.read()
                if not success:
                    print("empty camera")
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
                    if imlist[11][2] <= imlist[12][2] and imlist[12][2] <= imlist[13][2]:
                        self.position = "down"
                    elif imlist[11][2] >= imlist[12][2] and imlist[12][2] >= imlist[13][2]:
                        self.position = "up"
                        self.count += 1
                        print(self.count)
                    else:
                        self.position = None

                # Text + Count Anzeige
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(image, f'Push-ups: {self.count}', (10, 40), font, 1, (0, 0, 0), 2, cv2.LINE_AA)
                cv2.putText(image, f'q zum Beenden', (390, 40), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
                
                # Spiegele das gesamte Bild horizontal
                image = cv2.flip(image, 1)

                # Fullscreen
                cv2.namedWindow("Push-up Counter", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("Push-up Counter", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
                cv2.imshow("Push-up Counter", cv2.flip(image, 1))
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break

        cap.release()
        cv2.destroyAllWindows()

    def get_count(self):
        return self.count

# if __name__ == "__main__":
#     PushUpCounter()
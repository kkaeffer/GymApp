import cv2

def counter(image, count):
    #Counter wird definiert
    cv2.putText(image, f'Counter: {count}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    #Counter wird aufs Bild gelegt
    cv2.imshow("Push-up counter", image)

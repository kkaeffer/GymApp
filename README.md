# GymApp

## Was ist die GymApp?

Die GymApp ist eine Python-Anwendung, welche im Rahmen des KI-Unterrichts erstellt wurde. Sie ermöglicht es Fitnessübungen wie Kniebeugen oder Liegestütze mithilfe einer künstlichen Intelligenz zu optimieren. Durch gewisse "Landmarks" werden am Körper Punkte wie bspw. die Schulter oder das Handgelenk erkannt und mittels Winkelberechnung festgestellt, ob die Übung korrekt ausgeführt wurde. Desweiteren wird durch einen Zähler der Fortschritt mitdokumentiert.

## Wie starte ich das Programm auf meinem Computer

### Python installieren

Downloaden Sie unter <https://www.python.org/downloads/> den Installer für Python und beachten Sie das die Version nur 3.6 bis 3.8 ist. Nur diese Versionen werden von MediaPipe unterstützt.
Führen Sie den Installer aus.
Wichtig: Installationsmaske "Hinzufügen zur Path-Variable" ankreuzen.

### pip installieren

Laden Sie Sich die zip-Datei <https://bootstrap.pypa.io/pip/pip.pyz> herunter
Gehen Sie auf die Webseite <https://pip.pypa.io/en/stable/installation/> für mehr Informationen

### OpenCV und Mediapipe installieren
In Visual Studio Code können Sie mittels des Terminals und dem Kommando "pip install mediapipe" und "pip install opencv-python".
Die Bibliotheken werden nun heruntergeladen und stehen danach zur Verfügung.

## Bedienungsanleitung

- Zum starten Klicken Sie in das GUI.py Programm
- Danach können Sie das Ausführfenster mit der Tastkombination Strg + Umschalttaste + D öffnen
- Links sollte sich dann ein Fenster öffnen mit einem Button "Ausführen und debuggen" bzw bei englischer Einstellung "Run and debug". Bitte betätigen Sie diesen.
- Achten Sie hierbei darauf den "Python Debugger" zu nutzen.
- Die Anwendung öffnet sich.

### Menu

![Menu](image.png)

- Beim Anklicken des oberen Buttons können Sie Ihre gewünschte Übung aussuchen.
- Klicken Sie den Start-Button um die Übung zu starten.
Die Kameraaufnahme wird gestartet
- Um die Übung zu beenden, nutzen Sie die Taste "Q" auf ihrer Tastatur.
- Um den Vollbildmodus zu beenden drücken Sie auf "Esc".

### In der Übung

- Am oberen linken Bildschirmrand können Sie während der Ausführung die Anzahl der Wiederholungen sehen.
- Um das Beste aus Ihrer Fitness rauszuholen ist der Zähler nicht begrenzt.
- Um die Übung zu beenden, können Sie auf Ihrer Tastatur "Q" betätigen.

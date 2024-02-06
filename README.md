# GymApp

## Was ist die GymApp?

Die GymApp ist eine Python-Anwendung, welche im Rahmen des KI-Unterrichts erstellt wurde. Sie ermöglicht es Fitnessübungen wie Kniebeugen oder Liegestütze mithilfe einer künstlichen Intelligenz zu optimieren. Durch gewisse "Landmarks" werden am Körper Punkte wie bspw. die Schulter oder das Handgelenk erkannt und mittels Winkelberechnung festgestellt, ob die Übung korrekt ausgeführt wurde. Desweiteren wird durch einen Zähler der Fortschritt mitdokumentiert.

## Installierungen und vor Einstellungen

### Visual Studio Code und Python Extension Pack installieren

Installieren Sie Visual Studio Code von der offiziellen Website: [Visual Studio Code](https://code.visualstudio.com/download)
Installieren Sie das Python Extension Pack über die Erweiterungsverwaltung von Visual Studio Code oder alternativ verwenden Sie PyCharm.

### Python installieren

Downloaden Sie unter [Python.org](https://www.python.org/downloads/) den Installer für Python und beachten Sie das die Version nur 3.6 bis 3.8 ist. Nur diese Versionen werden von MediaPipe unterstützt.
Führen Sie den Installer aus.
Wichtig: Installationsmaske "Hinzufügen zur Path-Variable" ankreuzen.

### pip installieren

Laden Sie Sich die [zip-Datei](https://bootstrap.pypa.io/pip/pip.pyz) herunter
Führen Sie den Befehl im CMD Fenster aus "py get-pip.py"
Gehen Sie auf die Webseite [pip](https://pip.pypa.io/en/stable/installation/) für mehr Informationen

### OpenCV und Mediapipe installieren

In Visual Studio Code können Sie mittels des Terminals und dem Kommando "pip install mediapipe", "pip install opencv-python", "pip install tkinter".
Die Bibliotheken werden nun heruntergeladen und stehen danach zur Verfügung.

### Python-Interpreter auswählen

    - Öffnen Sie Visual Studio Code und drücken Sie F1.
    - Wählen Sie "Select Interpreter" und wählen Sie die installierte Python-Version (3.7.9).

## Ausführen

- Zum starten Klicken Sie in das main.py Programm
- Danach können Sie das Ausführfenster mit der Tastkombination Strg + Umschalttaste + D öffnen
- Links sollte sich dann ein Fenster öffnen mit einem Button "Ausführen und debuggen" bzw bei englischer Einstellung "Run and debug". Bitte betätigen Sie diesen.
- Achten Sie hierbei darauf den "Python Debugger" zu nutzen.
- Die Anwendung öffnet sich.

## Im Programm

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

Viel Spaß beim Ausführen des Projekts! 😊

Ihr Team GymApp

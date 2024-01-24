import cv2
import tkinter as tk
from PIL import Image, ImageTk

def detect_persons(frame):
    hog = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = hog.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for i, (x, y, w, h) in enumerate(faces, 1):
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Person {i}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

def update_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_with_detections = detect_persons(frame)
        photo = ImageTk.PhotoImage(image=Image.fromarray(frame_with_detections))
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo

    root.after(10, update_frame)

def close_camera():
    cap.release()
    root.destroy()

cap = cv2.VideoCapture(0)

root = tk.Tk()
root.title("Detección de Rostros")

canvas = tk.Canvas(root, width=cap.get(cv2.CAP_PROP_FRAME_WIDTH), height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
canvas.pack()

update_frame()

root.protocol("WM_DELETE_WINDOW", close_camera)
root.mainloop()

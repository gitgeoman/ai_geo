import cv2
from random import randrange

#loading pre-trained model from cv2 data from https://github.com/kipr/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
trained_face_data = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#launching camera
webcam = cv2.VideoCapture(0)  # here can be video

#reading data loop
while True:
    successful_frame_read, frame = webcam.read()
    grayscale_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(grayscale_img)
    print(f'Actual face coordinates: {face_coordinates}')

    # draw rectangles
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(256), randrange(256), randrange(256)), 2)
    cv2.imshow('face detector', frame)
    # cv2.waitKey(1)

    key = cv2.waitKey(1)
    if key==81 or key==113:
        break

print("code completed")
webcam.release()

import numpy as np
from time import sleep
import sys,os
import list_mouvement

MARGIN = 10  # pixels
ROW_SIZE = 10  # pixels
FONT_SIZE = 2
FONT_THICKNESS = 1
TEXT_COLOR = (255, 0, 0)  # blue
FPS = 30 # frame per second

sys.path.append('F:/openpose/build/python/openpose/Release');
os.environ['PATH']  = os.environ['PATH'] + ';' + 'F:/openpose/build/x64/Release;' +  'F:/openpose/build/bin;'
import pyopenpose as op
import cv2

use_open_pose   = True
fps_wait        = 40
time_s          = 0

if use_open_pose:
    opWrapper = op.WrapperPython()
    opWrapper.configure(dict(model_folder="F:/openpose/models/"))
    opWrapper.start()
    datum = op.Datum()
    fps_wait = 10

cap = cv2.VideoCapture("Enregistrements\\Videos_20230602_115702\\20230602_115702_Kinect_8.mkv")

if not cap.isOpened():
    print("Erreur ouverture fichier video")

while cap.isOpened():
    success, frame = cap.read()
    time_s += 1/FPS

    if not success:
        sleep(0.02)
        continue

    if use_open_pose:
        datum.cvInputData = frame
        opWrapper.emplaceAndPop([datum])

        poseKeypoints = datum.poseKeypoints

        if poseKeypoints.size > 1:
            for keypoints in poseKeypoints:
                temps = 0
                cv2.putText(frame,  temps, (neck_x, neck_y), cv2.FONT_HERSHEY_PLAIN, FONT_SIZE, TEXT_COLOR, FONT_THICKNESS)

    if use_open_pose:
        cv2.imshow("output data", frame)
        cv2.imshow("OpenPose test", datum.cvOutputData)
    else:
        cv2.imshow("OpenPose test", frame)

    key = cv2.waitKey(fps_wait) & 0xFF
    if key == 27 or key == ord('q'):
        break

cv2.destroyAllWindows()
# # Hand Tracing Module
#
# import cv2
# import mediapipe as mp
# import time
# import math
# import numpy as np
#
#
# class handDetector():
#     def __init__(self, mode=False, maxHands=2, detectionCon=0.1, trackCon=0.9):
#         self.mode = mode
#         self.maxHands = maxHands
#         self.detectionCon = detectionCon
#         self.trackCon = trackCon
#
#         self.mpHands = mp.solutions.hands
#         self.hands = self.mpHands.Hands(
#             self.mode, self.maxHands, self.detectionCon, self.trackCon)
#         self.mpDraw = mp.solutions.drawing_utils
#         self.tipIds = [4, 8, 12, 16, 20]
#
#     def findHands(self, img, draw=True):
#         imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         self.results = self.hands.process(imgRGB)
#         # print(results.multi_hand_landmarks)
#
#         if self.results.multi_hand_landmarks:
#             for handLms in self.results.multi_hand_landmarks:
#                 if draw:
#                     self.mpDraw.draw_landmarks(
#                         img, handLms, self.mpHands.HAND_CONNECTIONS)
#
#         return img
#
#     def findPosition(self, img, handNo=0, draw=True):
#         xList = []
#         yList = []
#         bbox = []
#         self.lmList = []
#         if self.results.multi_hand_landmarks:
#             myHand = self.results.multi_hand_landmarks[handNo]
#             for id, lm in enumerate(myHand.landmark):
#                 # print(id, lm)
#                 h, w, c = img.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)
#                 xList.append(cx)
#                 yList.append(cy)
#                 # print(id, cx, cy)
#                 self.lmList.append([id, cx, cy])
#                 if draw:
#                     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
#
#             xmin, xmax = min(xList), max(xList)
#             ymin, ymax = min(yList), max(yList)
#             bbox = xmin, ymin, xmax, ymax
#
#             if draw:
#                 cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
#                               (bbox[2] + 20, bbox[3] + 20), (0, 255, 0), 2)
#
#         return self.lmList, bbox
#
#     def fingersUp(self):
#         fingers = []
#         # Thumb
#         if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
#             fingers.append(1)
#         else:
#             fingers.append(0)
#
#         # Fingers
#         for id in range(1, 5):
#             if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
#                 fingers.append(1)
#             else:
#                 fingers.append(0)
#
#             # totalFingers = fingers.count(1)
#
#         return fingers
#
#     def findDistance(self, p1, p2, img, draw=True, r=15, t=3):
#         x1, y1 = self.lmList[p1][1:]
#         x2, y2 = self.lmList[p2][1:]
#         cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
#
#         if draw:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), t)
#             cv2.circle(img, (x1, y1), r, (255, 0, 255), cv2.FILLED)
#             cv2.circle(img, (x2, y2), r, (255, 0, 255), cv2.FILLED)
#             cv2.circle(img, (cx, cy), r, (0, 0, 255), cv2.FILLED)
#             length = math.hypot(x2 - x1, y2 - y1)
#
#         return length, img, [x1, y1, x2, y2, cx, cy]
#
#
# def main():
#     pTime = 0
#     cTime = 0
#     cap = cv2.VideoCapture(0)
#     detector = handDetector()
#
#     while True:
#         success, img = cap.read()
#         img = detector.findHands(img)
#         lmList, bbox = detector.findPosition(img)
#         if len(lmList) != 0:
#             print(lmList[4])
#
#         cTime = time.time()
#         fps = 1 / (cTime - pTime)
#         pTime = cTime
#
#         cv2.putText(img, str(int(fps)), (10, 70),
#                     cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
#
#         cv2.imshow("Image", img)
#         # cv2.waitKey(1)
#         if cv2.waitKey(1) & 0xFF == 27:
#             cv2.destroyAllWindows()
#             break
#
#
# if __name__ == "__main__":
#     main()


import cv2
import mediapipe as mp
def main():
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    # For static images:
    IMAGE_FILES = []
    with mp_hands.Hands(
        static_image_mode=True,
        max_num_hands=2,
        min_detection_confidence=0.5) as hands:
      for idx, file in enumerate(IMAGE_FILES):
        # Read an image, flip it around y-axis for correct handedness output (see
        # above).
        image = cv2.flip(cv2.imread(file), 1)
        # Convert the BGR image to RGB before processing.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        # Print handedness and draw hand landmarks on the image.
        print('Handedness:', results.multi_handedness)
        if not results.multi_hand_landmarks:
          continue
        image_height, image_width, _ = image.shape
        annotated_image = image.copy()
        for hand_landmarks in results.multi_hand_landmarks:
          print('hand_landmarks:', hand_landmarks)
          print(
              f'Index finger tip coordinates: (',
              f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
              f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
          )
          mp_drawing.draw_landmarks(
              annotated_image,
              hand_landmarks,
              mp_hands.HAND_CONNECTIONS,
              mp_drawing_styles.get_default_hand_landmarks_style(),
              mp_drawing_styles.get_default_hand_connections_style())
        cv2.imwrite(
            '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))
        # Draw hand world landmarks.
        if not results.multi_hand_world_landmarks:
          continue
        for hand_world_landmarks in results.multi_hand_world_landmarks:
          mp_drawing.plot_landmarks(
            hand_world_landmarks, mp_hands.HAND_CONNECTIONS, azimuth=5)

    # For webcam input:
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(
        model_complexity=0,
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
      while cap.isOpened():
        success, image = cap.read()
        if not success:
          print("Ignoring empty camera frame.")
          # If loading a video, use 'break' instead of 'continue'.
          continue

        # To improve performance, optionally mark the image as not writeable to
        # pass by reference.
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(image)

        # Draw the hand annotations on the image.
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
          for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
          break
    cap.release()

if __name__ == "__main__":
    main()


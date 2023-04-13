# import cv2 as cv
# import numpy as np
# import screen_brightness_control as scb
# from cvzone.HandTrackingModule import HandDetector
#
#
# def main():
#     cap = cv.VideoCapture(0)
#     hd = HandDetector()
#     val = 0
#     while 1:
#         _, img = cap.read()
#         # print(type(cap.read()))
#         hands, img = hd.findHands(img)
#
#         if hands:
#             lm = hands[0]['lmList']
#             print(lm)
#
#             length, info, img = hd.findDistance(lm[8][0:2], lm[4][0:2], img)
#             print(length)
#             blevel = np.interp(length, [25, 400], [0, 100])
#             val = np.interp(length, [0, 100], [400, 150])
#             blevel = int(blevel)
#             # print(blevel)
#
#             scb.set_brightness(blevel)
#
#             cv.rectangle(img, (20, 150), (85, 400), (0, 255, 255), 4)
#             cv.rectangle(img, (20, int(val)), (85, 400), (0, 0, 255), -1)
#             cv.putText(img, str(blevel) + '%', (20, 430), cv.FONT_HERSHEY_COMPLEX, 1,
#                        (255, 0, 0), 3)
#
#         cv.imshow('frame', img)
#
#         if cv.waitKey(1) & 0xFF == 27:
#             cv.destroyAllWindows()
#             break
#
#
# if __name__ == "__main__":
#     main()

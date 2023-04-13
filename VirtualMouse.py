# import cv2
# import mediapipe
# import numpy
# import autopy
#
# cap = cv2.VideoCapture(0)
# initHand = mediapipe.solutions.hands  # Initializing mediapipe
# # Object of mediapipe with "arguments for the hands module"
# mainHand = initHand.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
# draw = mediapipe.solutions.drawing_utils  # Object to draw the connections between each finger index
# wScr, hScr = autopy.screen.size()  # Outputs the high and width of the screen (1920 x 1080)
# pX, pY = 0, 0  # Previous x and y location
# cX, cY = 0, 0  # Current x and y location
#
#
# def handLandmarks(colorImg):
#     landmarkList = []  # Default values if no landmarks are tracked
#
#     landmarkPositions = mainHand.process(colorImg)  # Object for processing the video input
#     landmarkCheck = landmarkPositions.multi_hand_landmarks  # Stores the out of the processing object (returns False on empty)
#     if landmarkCheck:  # Checks if landmarks are tracked
#         for hand in landmarkCheck:  # Landmarks for each hand
#             for index, landmark in enumerate(
#                     hand.landmark):  # Loops through the 21 indexes and outputs their landmark coordinates (x, y, & z)
#                 draw.draw_landmarks(img, hand,
#                                     initHand.HAND_CONNECTIONS)  # Draws each individual index on the hand with connections
#                 h, w, c = img.shape  # Height, width and channel on the image
#                 centerX, centerY = int(landmark.x * w), int(
#                     landmark.y * h)  # Converts the decimal coordinates relative to the image for each index
#                 landmarkList.append([index, centerX, centerY])  # Adding index and its coordinates to a list
#
#     return landmarkList
#
#
# def fingers(landmarks):
#     fingerTips = []  # To store 4 sets of 1s or 0s
#     tipIds = [4, 8, 12, 16, 20]  # Indexes for the tips of each finger
#
#     # Check if thumb is up
#     if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
#         fingerTips.append(1)
#     else:
#         fingerTips.append(0)
#
#     # Check if fingers are up except the thumb
#     for id in range(1, 5):
#         if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][2]:  # Checks to see if the tip of the finger is higher than the joint
#             fingerTips.append(1)
#         else:
#             fingerTips.append(0)
#
#     return fingerTips
#
#
# while True:
#     check, img = cap.read()  # Reads frames from the camera
#     imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
#     lmList = handLandmarks(imgRGB)
#     # cv2.rectangle(img, (75, 75), (640 - 75, 480 - 75), (255, 0, 255), 2)
#
#     if len(lmList) != 0:
#         x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
#         x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
#         finger = fingers(lmList)  # Calling the fingers function to check which fingers are up
#         if finger[1] == 1 and finger[4] == 1:
#             print("group:4 Product development lab, Electronics and Intrumentation Engineering")
#         if finger[1] == 1 and finger[3] == 1:
#             print("group 4: members : 1)robin 2)mihir 3)siddharth 4)ram 5) ashok")
#         if finger[1] == 1 and finger[2] == 1:
#             print("PD lab : PROFESSOR : Arjun Yadav sir")
#         if finger[1] == 1 and finger[2] == 0:  # Checks to see if the pointing finger is up and thumb finger is down
#             x3 = numpy.interp(x1, (75, 640 - 75),
#                               (0, wScr))  # Converts the width of the window relative to the screen width
#             y3 = numpy.interp(y1, (75, 480 - 75),
#                               (0, hScr))  # Converts the height of the window relative to the screen height
#
#             cX = pX + (x3 - pX) / 7  # Stores previous x locations to update current x location
#             cY = pY + (y3 - pY) / 7  # Stores previous y locations to update current y location
#
#             autopy.mouse.move(cX,
#                               cY)  # Function to move the mouse to the x3 and y3 values (wSrc inverts the direction)
#             pX, pY = cX, cY  # Stores the current x and y location as previous x and y location for next loop
#
#         if finger[1] == 0 and finger[0] == 1:  # Checks to see if the pointer finger is down and thumb finger is up
#             autopy.mouse.click()  # Left click
#
#     cv2.imshow("Webcam", img)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
import cv2
import mediapipe
import numpy
import autopy
#import screen_brightness_control as scb
from cvzone.HandTrackingModule import HandDetector

def main():
    cap = cv2.VideoCapture(0)
    initHand = mediapipe.solutions.hands  # Initializing mediapipe
    # Object of mediapipe with "arguments for the hands module"
    mainHand = initHand.Hands(min_detection_confidence=0.50, min_tracking_confidence=0.20)
    draw = mediapipe.solutions.drawing_utils  # Object to draw the connections between each finger index
    wScr, hScr = autopy.screen.size()  # Outputs the high and width of the screen (1920 x 1080)
    pX, pY = 0, 0  # Previous x and y location
    cX, cY = 0, 0  # Current x and y location
    hd = HandDetector()
    val = 0
    oye = False


    def handLandmarks(colorImg):
        landmarkList = []  # Default values if no landmarks are tracked

        landmarkPositions = mainHand.process(colorImg)  # Object for processing the video input
        landmarkCheck = landmarkPositions.multi_hand_landmarks  # Stores the out of the processing object (returns False on empty)
        if landmarkCheck:  # Checks if landmarks are tracked
            for hand in landmarkCheck:  # Landmarks for each hand
                for index, landmark in enumerate(
                        hand.landmark):  # Loops through the 21 indexes and outputs their landmark coordinates (x, y, & z)
                    draw.draw_landmarks(img, hand,
                                        initHand.HAND_CONNECTIONS)  # Draws each individual index on the hand with connections
                    h, w, c = img.shape  # Height, width and channel on the image
                    centerX, centerY = int(landmark.x * w), int(
                        landmark.y * h)  # Converts the decimal coordinates relative to the image for each index
                    landmarkList.append([index, centerX, centerY])  # Adding index and its coordinates to a list

        return landmarkList


    def fingers(landmarks):
        fingerTips = []  # To store 4 sets of 1s or 0s
        tipIds = [4, 8, 12, 16, 20]  # Indexes for the tips of each finger

        # Check if thumb is up
        if landmarks[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)

        # Check if fingers are up except the thumb
        for id in range(1, 5):
            if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 3][
                2]:  # Checks to see if the tip of the finger is higher than the joint
                fingerTips.append(1)
            else:
                fingerTips.append(0)

        return fingerTips


    while True:
        check, img = cap.read()  # Reads frames from the camera
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Changes the format of the frames from BGR to RGB
        lmList = handLandmarks(imgRGB)
        # cv2.rectangle(img, (75, 75), (640 - 75, 480 - 75), (255, 0, 255), 2)

        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]  # Gets index 8s x and y values (skips index value because it starts from 1)
            x2, y2 = lmList[12][1:]  # Gets index 12s x and y values (skips index value because it starts from 1)
            finger = fingers(lmList)  # Calling the fingers function to check which fingers are up
            if finger[1] == 1 and finger[4]== 0 and finger[3]==0 and finger[2] == 1 and finger[0]==0 :
                print("""Virtual mouse using hand gesture recognition is a technology that allows users to \n"""
                      "control the cursor on a computer \n"
                      "screen using hand gestures. The system typically uses a webcam or \n"
                      "camera to capture images of the user's hand, which are processed using \n"
                      "the OpenCV library in Python. The hand gestures are recognized by analyzing \n"
                      " the contours of the hand and comparing them to pre-defined templates. \n"
                      " The recognized gestures are then mapped to cursor movements on the screen, enabling \n"
                      "users to control the cursor without the need for a physical mouse. \n"
                      "This technology has a wide range of potential applications,\n "
                      "from gaming to assistive technology for people with disabilities.\n")
            if finger[1] == 1 and finger[3] == 0 and finger[4]==0 and finger[2] == 0 and finger[0] ==1:
                 print("Virtual Mouse Using Hand Gesture Recogntion ")
                 print ("SUBJECT:- PRODUCT DEVELOPMENT LAB ")
                 print ("PROFESSOR :- DR. ARJUN SINGH YADAV ")
                 print ("Contibuted by :")
                 print ("1)Robin Kumar Saw (120EI0896) /n")
                 print( "2)Mihir Bibhuty  (120EI0879) /n")
                 print(  "3) Siddharth Kumar Panda (120EI0888) /n")
                 print("4) Ramnarayan Sahu (120EI0729) /n")
                 print("5) Ashok Kumar Saini (120EI0895) /n")



            if finger[1] == 1 and finger[0] == 1 and finger[3] == 1 and finger[4] == 1 and finger[2] == 1:
                print(
                    "WELCOME TO OUR PROJECT,VIRTUAL MOUSE using hand gesture recognition /n For help these are instructions /n")
                print("1.For using pointer raise index finer and rest fold rest of fingers /n")
                print("2.For clicking function raise your index finger and last finger and fold your rest of finger /n")
                print(
                    "3. For knowing details about our project raise you index and middle finger and rest finger folded /n")
                print(
                    "4.For knowing contributions in this project raise your thumb and index finger and rest finger folded /n")
                print("5.TO close this raise your index ,middle and ring finger up and rest fingers down./n")
                print("6. TO print it again keep your all fingers up")
            #     print("PD lab : PROFESSOR : Arjun Yadav sir")
            # if finger[1] == 1 and finger[0] == 1 and finger[2] ==0 and finger[3] == 0 and finger[4] == 0:
            #     while 1:
            #         _, img = cap.read()
            #         # print(type(cap.read()))
            #         hands, img = hd.findHands(img)
            #
            #         if hands:
            #             lm = hands[0]['lmList']
            #             #print(lm)
            #
            #             length, info, img = hd.findDistance(lm[8][0:2], lm[4][0:2], img)
            #             #print(length)
            #             blevel = numpy.interp(length, [15, 150], [0, 100])
            #             val = numpy.interp(length, [0, 100], [400, 150])
            #             blevel = int(blevel)
            #             # print(blevel)
            #
            #             scb.set_brightness(blevel)
            #
            #             cv2.rectangle(img, (20, 150), (85, 400), (0, 255, 255), 4)
            #             cv2.rectangle(img, (20, int(val)), (85, 400), (0, 0, 255), -1)
            #             cv2.putText(img, str(blevel) + '%', (20, 430), cv2.FONT_HERSHEY_COMPLEX, 1,
            #                        (255, 0, 0), 3)
            #             #cv.imshow('frame', img)
            #             #if cv2.waitKey(1) & 0xFF == finger[4]==1:
            #                # break

            if finger[1] == 1 and finger[2] == 0 and finger[0] == 0 and finger[3] == 0 and finger[4] == 0:  # Checks to see if the pointing finger is up and thumb finger is down
                x3 = numpy.interp(x1, (75, 640-250),
                                  (0, wScr))  # Converts the width of the window relative to the screen width
                y3 = numpy.interp(y1, (75, 480 - 200),
                                  (0, hScr))  # Converts the height of the window relative to the screen height

                cX = pX + (x3 - pX) / 7  # Stores previous x locations to update current x location
                cY = pY + (y3 - pY) / 7  # Stores previous y locations to update current y location

                autopy.mouse.move(cX,
                                  cY)  # Function to move the mouse to the x3 and y3 values (wSrc inverts the direction)
                pX, pY = cX, cY  # Stores the current x and y location as previous x and y location for next loop
            if finger[2] == 1 and finger[0] == 0 and finger[3] == 1 and finger[4] == 0 and finger[1] == 1:
                oye = True
            if finger[1] == 1 and finger[4] == 1 and finger[3] == 0 and finger[0] ==0 and finger[2]==0:
                # _, img = cap.read()
                # # print(type(cap.read()))
                # hands, img = hd.findHands(img)
                # # Checks to see if the pointer finger is down and thumb finger is up
                # if hands:
                #     lm = hands[0]['lmList']
                #     # print(lm)
                #
                #     length, info, img = hd.findDistance(lm[8][0:2], lm[4][0:2], img)
                #     print(length)

                    #if length<50:
                        autopy.mouse.click()

                #autopy.mouse.click()  # Left click


        cv2.imshow("Webcam", img)
        if cv2.waitKey(1) &  0xff ==('q') or oye :
            break

if __name__ == "__main__":
    main()
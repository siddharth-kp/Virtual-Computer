from cvzone.HandTrackingModule import HandDetector
import cv2
import os
import numpy as np


def main():
    # Parameters
    width, height = 900, 540
    gestureThreshold = 200
    folderPath = "Presentation"

    # Camera Setup
    cap = cv2.VideoCapture(0)
    cap.set(3, width)
    cap.set(4, height)

    # Hand Detector
    detectorHand = HandDetector(detectionCon=0.8, maxHands=1)

    # Variables

    imgNumber = 0
    hs, ws = int(120 * 1), int(213 * 1)  # width and height of small image
    gestureThreshold = 500
    buttonPressed = False
    buttonCounter = 0
    buttonDelay = 30

    # Get list of presentation images
    pathImages = sorted(os.listdir(folderPath), key=len)
    print(pathImages)

    while True:
        # Get image frame
        success, img = cap.read()  # bool, 480P 640P 3
        # print(type(success))
        # print(img.shape)
        img = cv2.flip(img, 1)
        pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
        imgCurrent = cv2.imread(pathFullImage)

        # Find the hand and its landmarks
        hands, img = detectorHand.findHands(img)  # with draw
        # Draw Gesture Threshold line
        cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0, 255, 0), 10)

        if hands and buttonPressed is False:  # If hand is detected

            hand = hands[0]
            cx, cy = hand["center"]
            fingers = detectorHand.fingersUp(hand)  # List of which fingers are up
            print(fingers)

            if cy <= gestureThreshold:  # If hand is at the height of the face
                if fingers == [1, 0, 0, 0, 0]:
                    print("Left")

                    if imgNumber > 0:
                        buttonPressed = True
                        imgNumber -= 1

                if fingers == [0, 0, 0, 0, 1]:
                    print("Right")

                    if imgNumber < len(pathImages) - 1:
                        imgNumber += 1
                        buttonPressed = True

        # ButtonPressed iteration
        if buttonPressed:
            buttonCounter += 1
            if buttonCounter > buttonDelay:
                buttonCounter = 0
                buttonPressed = False

        imgSmall = cv2.resize(img, (ws, hs))
        h, w, _ = imgCurrent.shape
        imgCurrent[0:hs, w - ws: w] = imgSmall

        cv2.imshow("Slides", imgCurrent)
        cv2.imshow("Image", img)

        key = cv2.waitKey(1)

        if cv2.waitKey(1) & 0xFF == 27:
            cv2.destroyAllWindows()
            break


if __name__ == "__main__":
    main()

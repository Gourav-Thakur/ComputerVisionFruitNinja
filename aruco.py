import cv2

arucoDictType = cv2.aruco.DICT_5X5_100
arucoDict = cv2.aruco.getPredefinedDictionary(arucoDictType)
arucoParams = cv2.aruco.DetectorParameters()

capture = cv2.VideoCapture(0)

prev = (-1, -1)

def detectAruco(img):
    global prev

    (corners, ids, rejected) = cv2.aruco.detectMarkers(img, arucoDict, parameters=arucoParams)

    if len(corners) > 0:
        ids = ids.flatten()

        for (markerCorner, markerId) in zip(corners, ids):
            corners = markerCorner.reshape((4, 2))
            (topLeft, topRight, bottomRight, bottomLeft) = corners

            # topRight = (int(topRight[0]), int(topRight[1]))
            # topLeft = (int(topLeft[0]), int(topLeft[1]))
            # bottomRight = (int(bottomRight[0]), int(bottomRight[1]))
            # bottomLeft = (int(bottomLeft[0]), int(bottomLeft[1]))

            cx = (topLeft[0] + bottomRight[0])/2.0
            cy = (topLeft[1] + bottomRight[1])/2.0

            prev = (cx, cy)

        return (cx, cy)
    
    return prev

def showAruco():
    while True:
        isTrue, frame = capture.read()

        if isTrue:
            (cx, cy) = detectAruco(frame)

            if cx != -1:
                cv2.circle(frame, (int(cx), int(cy)), 10, (0, 0, 255), -1)

            cv2.imshow("frame", frame)
            if cv2.waitKey(16) & 0xFF == ord("q"):
                break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    showAruco()
import cv2
import numpy as np
import random
import aruco

capture = cv2.VideoCapture(0)


def main():
    length = 1500
    width = 1500

    circleX = 200
    circleY = 400
    t = 0
    ui = random.randint(-50, 50)
    u = ui
    v = 0
    s0 = random.randint(200, 800)
    a = 1

    ux = 15

    score = 0

    while True:
        isTrue, frame = capture.read()
        if isTrue:
            (cx, cy) = aruco.detectAruco(frame)
        
        (length, width, _) = frame.shape

        if cx != -1:
                cv2.circle(frame, (int(cx), int(cy)), 10, (0, 0, 255), -1)

        cv2.ellipse(frame, (int(circleX), int(circleY)), (20, 20), 0, 0, 360, 255, -1)
        
        frame = cv2.flip(frame, 1)

        if(abs(cx-circleX)<=20 and abs(cy-circleY)<=20):
            score+=1

            t = 0
            ui = random.randint(-50, 50)
            u = ui
            v = 0
            s0 = random.randint(200, 800)
            a = 1

            ux = 15
             

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break
        
        circleX += ux
        circleY = s0 + u * t + (0.5 * a * t * t)
        v = u + a * t

        if circleY>length:
            u = -v+1
            t = 0
            s0 = length

        if circleY < 0:
            u = -v+1
            t = 0
            s0 = 0

        if circleX > width or circleX < 0:
            ux = -ux
        
        
        t += 1

        cv2.putText(frame, f"Score: {score}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.imshow("Game Window", frame)
        
    cv2.destroyAllWindows()
    # print(score)

if __name__ == "__main__":
    main()
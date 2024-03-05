import numpy as np
import cv2
import model.main
import detect

video = cv2.VideoCapture("win-20221219-16-35-22-pro_MvA292jB.mp4")

if not video.isOpened():
    print("0")

cv2.waitKey(10)

a=0

while video.isOpened():

    pon, frame = video.read()
    image = frame
    copy_img = np.copy(image)

    cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
    cv2.resizeWindow('Video', 960, 540)

    image = model.main.detect(frame)
    color_coverted = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    width = 960
    height = 540
    dim = (width, height)
    frameF = cv2.resize(image, dim)
    copy_img = cv2.resize(copy_img, dim)

    copy_img = detect.mask(copy_img)
    copy_img = detect.cenny(copy_img)

    lines = cv2.HoughLinesP(copy_img, 2, np.pi / 180, 100, np.array([()]), 40, 2)
    a_lines = detect.average_slope_intercept(copy_img, lines)
    line_img = detect.display_lines(frameF, a_lines)
    final_frame = cv2.addWeighted(frameF, 0.8, line_img, 0.5, 1)

    x1 = (a_lines[0][0] + a_lines[1][0]) / 2
    x2 = (a_lines[0][2] + a_lines[1][2]) / 2
    y1 = (a_lines[0][1] + a_lines[1][1]) / 2
    y2 = (a_lines[0][3] + a_lines[1][3]) / 2

    cr_line = cv2.line(final_frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 0), 2)

    cv2.imshow('Video', final_frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        video.release()
        cv2.destroyAllWindows()

video.release()
cv2.destroyAllWindows()
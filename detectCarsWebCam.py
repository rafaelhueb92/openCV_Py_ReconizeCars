import cv2


def readCar(frame, scaleFactorValue, minSizeValue):

    classified = cv2.CascadeClassifier('cars.xml')

    # frame = cv2.imread(<path of image")

    imageGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    carsDetected = classified.detectMultiScale(
        imageGray, scaleFactor=scaleFactorValue, minSize=minSizeValue)

    print("Cars detected:" + " " + str(len(carsDetected)))

    return carsDetected


def detectCars(Output, scaleFactor, minSize):

    video = cv2.VideoCapture(0)  # You can input a path of a video file too

    if not Output is None:
        frame_width = int(video.get(3))
        frame_height = int(video.get(4))

        out = cv2.VideoWriter(Output, cv2.VideoWriter_fourcc(
            'M', 'J', 'P', 'G'), 10, (frame_width, frame_height))

    else:
        out = None

    while True:

        connected, frame = video.read()

        if connected != True:
            break

        carsFrame = readCar(frame, scaleFactor, minSize)

        for (x, y, w, h) in carsFrame:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)

        if not out is None:
            out.write(frame)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) == ord("q"):
            break

    video.release()
    out.release()
    cv2.destroyAllWindows()


detectCars('carsOut.avi', 1.09, (30, 30))

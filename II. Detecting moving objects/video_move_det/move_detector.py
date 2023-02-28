import cv2, time
from datetime import datetime
import pandas

# pandas DataFrame
df = pandas.DataFrame(columns=["Start", "End"])

# video variables and lists
video = cv2.VideoCapture(0)
first_frame = None
video.read()
time.sleep(1)

status_list = [None, None]
times = []

while True:
    check, frame = video.read()

    # status = 1 when object enters a frame
    status = 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 40, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
    status_list.append(status)

    # keeping only last dwo items of the list
    status_list = status_list[-2:]

    # object enters the frame
    if status_list[-2] == 0 and status_list[-1] == 1:
        times.append(datetime.now())

    # object lefts the frame
    if status_list[-2] == 1 and status_list[-1] == 0:
        times.append(datetime.now())

    key = cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

    cv2.imshow("Your cam", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

print(status_list)
print(times)

for i in range(0, len(times), 2):
    df = df.append({"Start": times[i], "End": times[i+1]}, ignore_index=True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()



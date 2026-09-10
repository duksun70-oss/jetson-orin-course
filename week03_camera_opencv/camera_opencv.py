import cv2, time

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit('Camera open failed')

count = 0
start = time.time()
while True:
    ok, frame = cap.read()
    if not ok:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 80, 160)
    cv2.imshow('camera', frame)
    cv2.imshow('edges', edges)
    count += 1
    if cv2.waitKey(1) & 0xFF == 27:
        break

elapsed = max(time.time() - start, 1e-6)
print('Average FPS:', count / elapsed)
cap.release()
cv2.destroyAllWindows()

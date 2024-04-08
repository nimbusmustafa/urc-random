import cv2

def record_video():
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("Error: Failed to open the camera")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('mallet.mp4', fourcc, 20.0, (frame_width, frame_height))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Error: Failed to capture frame")
            break

    cap.release()
    out.release()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    record_video()

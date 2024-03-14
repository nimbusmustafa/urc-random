import cv2
import os

# Set GStreamer debug level to suppress warnings
os.environ['GST_DEBUG'] = '3'

def FrameCapture(camera_index=2):
    output_folder = "bottle2"
    os.makedirs(output_folder, exist_ok=True)

    vidObj = cv2.VideoCapture(camera_index)
    count = 0
    count1 = 85 
    success = 1

    while success:
        success, image = vidObj.read()
        if success and count % 15 == 0:
            count1 += 1

            image_path = os.path.join(output_folder, "bottle_new%d.jpg" % count1)
            cv2.imwrite(image_path, image)

        # Display the camera feed
        cv2.imshow("Camera Feed", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        count += 1

    vidObj.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    FrameCapture()

import cv2
import os

def FrameCapture(camera_index=2):
    output_folder = "artag_iter2"
    os.makedirs(output_folder, exist_ok=True)
    
    vidObj = cv2.VideoCapture(camera_index)
    count1 = 571
    success = 1

    while success:
        success, image = vidObj.read()
        if success :
            count1 += 1

            image_path = os.path.join(output_folder, "bottles_neww%d.jpg" % count1)
            cv2.imwrite(image_path, image)

        cv2.imshow("Camera Feed", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        

    vidObj.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    FrameCapture()

import cv2
import os

def capture_frames(video_path, output_folder, frames_per_second=3):
    os.makedirs(output_folder, exist_ok=True)

    vidObj = cv2.VideoCapture(video_path)
    count = 0
    success = 1

    fps = vidObj.get(cv2.CAP_PROP_FPS)  # Get the frames per second from the video

    frame_interval = int(fps / 10)  # Calculate frame interval

    while success:
        success, image = vidObj.read()
        if success and count % frame_interval == 0:
            # Save the frame as an image
            if image is not None:
                image_path = os.path.join(output_folder, "bottlesar%d.jpg" % (count))
                cv2.imwrite(image_path, image)

        count += 1

    vidObj.release()

if __name__ == '__main__':
    video_path = "/home/mustafa/urc/bottle2-2024-02-28_08.07.58.mp4"
    output_folder = "bottleshot"
    capture_frames(video_path, output_folder)

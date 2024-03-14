import cv2
import os

def convert_images_to_bw(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img_path = os.path.join(input_folder, filename)
            img = cv2.imread(img_path)

            if img is not None:
                bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

                output_path = os.path.join(output_folder, f"{filename[:-4]}_bw.jpg")
                cv2.imwrite(output_path, bw_img)

if __name__ == '__main__':
    input_folder = "/home/mustafa/urc/bottle1"
    output_folder = "/home/mustafa/urc/bottles_bw"
    convert_images_to_bw(input_folder, output_folder)

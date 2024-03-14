import cv2 as cv
import numpy as np
from cv2 import aruco
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ArucoDetect:
    calib_data_path = r"/home/mustafa/urc/MultiMatrix.npz"
    calib_data = np.load(calib_data_path)


    cam_mat = np.array([[527.277645, 0.0, 349.755466],
                        [0.0, 530.658217, 233.367262],
                        [0.0, 0.0, 1.0]])

    dist_coef = np.array([[0.236713 ,-0.169058, -0.010459, 0.021462, 0.000000]])
   
#aruco
    # cam_mat = np.array([[820.3589856596768, 0.0, 539.5],
    #                     [0.0, 483.84537647631765, 959.5],
    #                     [0.0, 0.0, 1.0]])

    # dist_coef = np.array([[-1.3142589234883053e-10, -2.615728839048662e-07, -3.778678242834884e-12, -8.159479283769905e-14, 3.458838325714501e-11]])
   
   #chessboard, rospackage
    # cam_mat = np.array([[569.776749, 0.0, 422.286549],
    #                     [0.0, 560.773506, 243.958531],
    #                     [0.0, 0.0, 1.0]])

    # dist_coef = np.array([[0.088685, 0.055558, 0.004746, 0.058562, 0.000000]])    



    marker_size = 0.14
    marker_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
    param_markers = cv.aruco.DetectorParameters_create()

    def __init__(self):
        self.cap = cv.VideoCapture(2) 

        while True:
            ret, frame = self.cap.read() 
            if frame is not None:
                # print(frame.shape)
                frame=cv.resize(frame,(640,480),interpolation= cv.INTER_LINEAR)
                # print(frame.shape)

                self.detect_and_publish(frame)

    def detect_and_publish(self, frame):
        if frame is not None:

            gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            marker_corners, marker_IDs, _ = cv.aruco.detectMarkers(gray_frame, self.marker_dict, parameters=self.param_markers)

            if marker_corners:
                rVec, tVec, _ = aruco.estimatePoseSingleMarkers(marker_corners, self.marker_size, self.cam_mat, self.dist_coef)
                total_markers = range(0, marker_IDs.size)
                for ids, corners, i in zip(marker_IDs, marker_corners, total_markers):
                    cv.polylines(frame, [corners.astype(np.int32)], True, (0, 255, 255), 4, cv.LINE_AA)
                    corners = corners.reshape(4, 2)
                    corners = corners.astype(int)
                    top_right = corners[0].ravel()
                    top_left = corners[1].ravel()
                    bottom_right = corners[2].ravel()
                    bottom_left = corners[3].ravel()
                    print(tVec[i])
                    y_dist = tVec[i][0][1]
                    x_dist = tVec[i][0][0]

                    point = cv.drawFrameAxes(frame, self.cam_mat, self.dist_coef, rVec[i], tVec[i], 4, 4)
                    cv.putText(frame, f"id: {ids[0]} Dist: {round(x_dist, 2)}", tuple(top_right), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv.LINE_AA)
                    cv.putText(frame, f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ", tuple(bottom_right), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv.LINE_AA)

                    # try:
                    #     image_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
                    #     self.image_pub.publish(image_msg)
                    # except CvBridgeError as e:
                    #     print(e)

            display_img = cv.resize(frame, (1920, 1080))
        
            cv.imshow("ArUco Detection", display_img)
            cv.waitKey(1)



    # def run(self):
    #     while True:
    #         cap = cv.VideoCapture(0)
    #         ret, frame = cap.read()
    #         if frame is not None:
    #             self.detect_and_publish(frame)

if __name__ == "__main__":
    aruco_obj = ArucoDetect()
    # aruco_obj.run()

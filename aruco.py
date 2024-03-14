#!/usr/bin/env python3

import cv2 as cv
import numpy as np
from cv2 import aruco
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ArucoDetect:
    def __init__(self):
        self.calib_data_path = r"/home/mustafa/urc/MultiMatrix.npz"
        self.calib_data = np.load(self.calib_data_path)
        self.cam_mat = self.calib_data["camMatrix"]
        print(self.cam_mat)
        self.dist_coef = self.calib_data["distCoef"]
        print(self.dist_coef)
        self.marker_size = 8
        self.marker_dict = cv.aruco.getPredefinedDictionary(cv.aruco.DICT_4X4_50)
        self.param_markers = cv.aruco.DetectorParameters_create()


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

                    y_dist = tVec[i][0][1]
                    x_dist = tVec[i][0][0]

                    point = cv.drawFrameAxes(frame, self.cam_mat, self.dist_coef, rVec[i], tVec[i], 4, 4)
                    cv.putText(frame, f"id: {ids[0]} Dist: {round(x_dist, 2)}", tuple(top_right), cv.FONT_HERSHEY_PLAIN, 1.3, (0, 0, 255), 2, cv.LINE_AA)
                    cv.putText(frame, f"x:{round(tVec[i][0][0],1)} y: {round(tVec[i][0][1],1)} ", tuple(bottom_right), cv.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), 2, cv.LINE_AA)

                    # try:
                    #     image_msg = self.bridge.cv2_to_imgmsg(frame, "bgr8")
                    #     self.image_pub.publish(image_msg)
                    # except CvBridgeError as e:
                    #     print(e)
            cv.imshow("ArUco Detection", frame)
            cv.waitKey(1)



    def run(self):
        while True:
            cap = cv.VideoCapture(2)
            ret, frame = cap.read()
            if frame is not None:
                self.detect_and_publish(frame)

if __name__ == "__main__":
    aruco_obj = ArucoDetect()
    aruco_obj.run()

import cv2
import numpy as np
from World import *
from time import time


class VideoManager:

    def resize(self, H0, Hf):
        factor = Hf/H0
        return cv2.resize(self.frame,None,fx=factor, fy=factor, interpolation = cv2.INTER_CUBIC)

    def __init__(self):
        # Define the camera and configure its parameters
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 800)
        self.cap.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 600)

        # define range of pink color in HSV
        self.lower_pink = np.array([155, 215, 60])
        self.upper_pink = np.array([180, 255, 120])

        # define range of green color in HSV
        self.lower_green = np.array([45, 120, 70])
        self.upper_green = np.array([80, 220, 200])

        # define range of purple color in HSV
        self.lower_brown = np.array([0, 185, 30])
        self.upper_brown = np.array([0, 230, 90])

        # define range of roxo color in HSV
        #self.lower_brown = np.array([130, 200, 0])
        #self.upper_brown = np.array([165, 255, 90])

        # define range of red color in HSV
        #self.lower_brown = np.array([160, 230, 50])
        #self.upper_brown = np.array([180, 255, 85])

        # define range of yellow team color in HSV
        self.lower_team = np.array([12, 115, 110])
        self.upper_team = np.array([35, 255, 180])

        # define range of blue color in HSV
        #self.lower_team = np.array([100, 115, 30])
        #self.upper_team = np.array([150, 250, 100])

        # define range of ball color in HSV
        self.lower_ball_1 = np.array([0, 120, 30])
        self.upper_ball_1 = np.array([12, 255, 255])
        self.lower_ball_2 = np.array([170, 120, 30])
        self.upper_ball_2 = np.array([180, 255, 255])

        self.frame = None
        self.hsv = None

        self.mask_green = None

        # Remember that color is in BGR format

    def draw_circle(self, pos, r, color):
        cv2.circle(self.frame, pos, r, color, -1)

    def get_frame_dimensions(self):
        width = self.cap.get(3)
        height = self.cap.get(4)
        return width, height

    def show(self):
        cv2.imshow('frame', self.frame)

    #Calls the record
    def record(self):
        self.out.write(self.frame)

    #Release capture and record
    def release(self):
        self.cap.release()
        self.out.release()

    def get_element_position(self, color_lower, color_upper):
        # Threshold the HSV image to get only selected colors
        mask = cv2.inRange(self.hsv, color_lower, color_upper)

        # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(self.frame, self.frame, mask, mask)

        # finding team contour with maximum area and store it as best_cnt_team
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # finding team centroids of best_cnt_team and draw a blue circle there
        max_area = 0
        best_cnt = 1
        for cnt in contours:

            if World.is_contour_outside_field(cnt):
                continue

            area = cv2.contourArea(cnt)
            if area > max_area and area > frame_size / 9000:
                max_area = area
                best_cnt = cnt

        M = cv2.moments(best_cnt)
        cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        return cx, cy

    def get_element_position_verde(self, color_lower, color_upper):
        # Threshold the HSV image to get only selected colors

        if self.mask_green == None:
            self.mask_green = cv2.inRange(self.hsv, color_lower, color_upper)
        #cv2.imshow("greenmask",self.mask_green)
        # Bitwise-AND mask and original image
        # res = cv2.bitwise_and(self.frame, self.frame, mask, mask)

        # finding team contour with maximum area and store it as best_cnt_team
        contours, hierarchy = cv2.findContours(self.mask_green, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # finding team centroids of best_cnt_team and draw a blue circle there
        max_area = 0
        best_cnt = 1
        for cnt in contours:

            if World.is_contour_outside_field(cnt):
                continue

            area = cv2.contourArea(cnt)
            if area > max_area and area > frame_size / 9000:
                max_area = area
                best_cnt = cnt

        M = cv2.moments(best_cnt)
        cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        return cx, cy

    def get_ball_position2(self, color_lower_1, color_upper_1):
        # Threshold the HSV image to get only selected colors


        mask1 = cv2.inRange(self.hsv, color_lower_1, color_upper_1)

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(self.frame, self.frame, mask1, mask1)

        #mask2 = cv2.inRange(self.hsv, color_lower_2, color_upper_2)
        #res = cv2.bitwise_and(self.frame, self.frame, mask2, mask2)

        mask = mask1
        #cv2.addWeighted(mask1,1,mask2,1,0,mask)

        kernel = np.ones((5,5),np.float32)/8
        kernel[2][2] = 0
        dst = cv2.filter2D(mask,-1,kernel)

       # cv2.imshow("mask", mask)
#        cv2.imshow("dst", dst)
        cv2.waitKey(1)

        # finding team contour with maximum area and store it as best_cnt_team

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # finding team centroids of best_cnt_team and draw a blue circle there
        i = 0
        vet = np.ones((50,4), np.float32)
        for cnt in contours:

            if World.is_contour_outside_field(cnt):
                continue

            area = cv2.contourArea(cnt)

            if area > 15 and area < 200 and len(cnt) > 4: #and area > frame_size / 9000:
                elipse = cv2.fitEllipse(cnt)
                area_elipse = math.pi*elipse[1][0]*elipse[1][1]/4

                k = area_elipse/area #k eh a razao de area: quanto mais proximo de 1 o contorno aproxima-se de uma circunferencia (no caso, a bola)
                if k > 1:
                    k = 2 - k

                k = 1 - k

                if elipse[1][1] == 0 or elipse[1][0] == 0:
                    f = 1.0
                elif elipse[1][1] > elipse[1][0] :
                    f = (elipse[1][1] - elipse[1][0])/elipse[1][1]
                else:
                    f = (elipse[1][0] - elipse[1][1])/elipse[1][0]

                vet[i][0] = elipse[0][0]
                vet[i][1] = elipse[0][1]
                vet[i][2] = k
                vet[i][3] = f

                i += 1

        valor = 0

        k_min = 10000.0

        i = 0
        for a in vet:
            if a[2] < k_min and a[3] < 0.3:
               # cv2.drawContours(self.frame,[cnt],0,(0,0,255),1)
           #     cv2.circle(self.frame, (a[0],a[1]),5,(0,255,255), 5)
                k_min = a[2]
                valor = i
            i += 1



 #       cv2.circle(self.frame, (vet[valor][0],vet[valor][1]),5,(255,255,0), 2)

        return (vet[valor][0],vet[valor][1])


    def get_ball_position(self, color_lower_1, color_upper_1, color_lower_2, color_upper_2):
        # Threshold the HSV image to get only selected colors
        mask1 = cv2.inRange(self.hsv, color_lower_1, color_upper_1)

        # Bitwise-AND mask and original image
        #res = cv2.bitwise_and(self.frame, self.frame, mask1, mask1)

        mask2 = cv2.inRange(self.hsv, color_lower_2, color_upper_2)
        #res = cv2.bitwise_and(self.frame, self.frame, mask2, mask2)

        mask = mask1
        cv2.addWeighted(mask1,1,mask2,1,0,mask)

        kernel = np.ones((5,5),np.float32)/8
        kernel[2][2] = 0
        dst = cv2.filter2D(mask,-1,kernel)

        cv2.imshow("mask", mask)
#        cv2.imshow("dst", dst)
        cv2.waitKey(1)

        # finding team contour with maximum area and store it as best_cnt_team

        contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # finding team centroids of best_cnt_team and draw a blue circle there
        i = 0
        vet = np.ones((50,4), np.float32)
        for cnt in contours:

            if World.is_contour_outside_field(cnt):
                continue

            area = cv2.contourArea(cnt)

            if area > 15 and area < 200 and len(cnt) > 4: #and area > frame_size / 9000:
                elipse = cv2.fitEllipse(cnt)
                area_elipse = math.pi*elipse[1][0]*elipse[1][1]/4

                k = area_elipse/area #k eh a razao de area: quanto mais proximo de 1 o contorno aproxima-se de uma circunferencia (no caso, a bola)
                if k > 1:
                    k = 2 - k

                k = 1 - k

                if elipse[1][1] == 0 or elipse[1][0] == 0:
                    f = 1.0
                elif elipse[1][1] > elipse[1][0] :
                    f = (elipse[1][1] - elipse[1][0])/elipse[1][1]
                else:
                    f = (elipse[1][0] - elipse[1][1])/elipse[1][0]

                vet[i][0] = elipse[0][0]
                vet[i][1] = elipse[0][1]
                vet[i][2] = k
                vet[i][3] = f

                i += 1

        valor = 0

        k_min = 10000.0

        i = 0
        for a in vet:
            if a[2] < k_min and a[3] < 0.3:
               # cv2.drawContours(self.frame,[cnt],0,(0,0,255),1)
           #     cv2.circle(self.frame, (a[0],a[1]),5,(0,255,255), 5)
                k_min = a[2]
                valor = i
            i += 1



 #       cv2.circle(self.frame, (vet[valor][0],vet[valor][1]),5,(255,255,0), 2)

        return (vet[valor][0],vet[valor][1])


    def get_team_position(self, color_lower, color_upper):
        # Threshold the HSV image to get only selected colors
        mask = cv2.inRange(self.hsv, color_lower, color_upper)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(self.frame, self.frame, mask, mask)

        # finding team contours with maximum areas and store it as best_cnt_team
        contours, hierarchy = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # finding team contour with maximum area and store it as best_cnt_team
        first_max_area_team = 0
        second_max_area_team = 0
        third_max_area_team = 0

        first_best_cnt_team = 1
        second_best_cnt_team = 1
        third_best_cnt_team = 1

        for cnt_team in contours:

            if World.is_contour_outside_field(cnt_team):
                continue

            area_team = cv2.contourArea(cnt_team)
            if area_team > frame_size / 9000:
                if area_team > first_max_area_team:

                    third_max_area_team = second_max_area_team
                    third_best_cnt_team = second_best_cnt_team

                    second_max_area_team = first_max_area_team
                    second_best_cnt_team = first_best_cnt_team

                    first_max_area_team = area_team
                    first_best_cnt_team = cnt_team


                elif area_team > second_max_area_team:

                    third_max_area_team = second_max_area_team
                    third_best_cnt_team = second_best_cnt_team

                    second_max_area_team = area_team
                    second_best_cnt_team = cnt_team

                elif area_team > third_max_area_team:

                    third_max_area_team = area_team
                    third_best_cnt_team = cnt_team

        # finding team centroids of best_cnt_team and draw a blue circle there
        M = cv2.moments(first_best_cnt_team)
        ax_team, ay_team = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
        cv2.circle(self.frame, (ax_team, ay_team), 5, (0, 0, 255), -1)

        N = cv2.moments(second_best_cnt_team)
        bx_team, by_team = int(N['m10'] / N['m00']), int(N['m01'] / N['m00'])
        cv2.circle(self.frame, (bx_team, by_team), 5, (0, 0, 255), -1)

        O = cv2.moments(third_best_cnt_team)
        cx_team, cy_team = int(O['m10'] / O['m00']), int(O['m01'] / O['m00'])
        cv2.circle(self.frame, (cx_team, cy_team), 5, (0, 0, 255), -1)

        return [(ax_team, ay_team), (bx_team, by_team), (cx_team, cy_team)]

    def process_frame(self, world=World()):
        # Take each frame
        _, self.frame = self.cap.read()

        #cv2.flip(self.frame, -1, self.frame)

        # Take frame size
        frame_width, frame_height = self.get_frame_dimensions()
        frame_size = frame_height * frame_width

        # Convert BGR to HSV
        self.hsv = cv2.cvtColor(self.frame, cv2.COLOR_BGR2HSV)

        ls_team = self.get_team_position(self.lower_team, self.upper_team)

        pos_ball = self.get_ball_position(self.lower_ball_1, self.upper_ball_1, self.lower_ball_2, self.upper_ball_2)

        cv2.circle(self.frame, pos_ball, 5, (0, 255, 255), -1)

        # pos_team = self.get_element_position(self.lower_team, self.upper_team)
        # cv2.circle(self.frame, pos_team, 5, (0, 0, 255), -1)

        pos_pink = self.get_element_position(self.lower_pink, self.upper_pink)
        cv2.circle(self.frame, pos_pink, 5, (255, 0, 0), -1)
        pos_green = self.get_element_position(self.lower_green, self.upper_green)
        cv2.circle(self.frame, pos_green, 5, (100, 0, 100), -1)
        pos_brown = self.get_ball_position2(self.lower_green, self.upper_green)
        cv2.circle(self.frame, pos_brown, 5, (50, 100, 50), -1)

        # Goalkeeper
        p0 = world.get_teammate(0)
        p0_front = self.mais_proximo(ls_team, pos_green)
        p0.set_position(p0_front, pos_green)
        cv2.circle(self.frame, p0.getxy(), 5, (255, 255, 255), -1)

        # Player 1
        p1 = world.get_teammate(1)
        p1_front = self.mais_proximo(ls_team, pos_brown)
        p1.set_position(p1_front, pos_brown)
        cv2.circle(self.frame, p1.getxy(), 5, (255, 255, 255), -1)

        # Player 2
        p2 = world.get_teammate(2)
        p2_front = self.mais_proximo(ls_team, pos_pink)
        p2.set_position(p2_front, pos_pink)
        cv2.circle(self.frame, p2.getxy(), 5, (255, 255, 255), -1)

        # TODO: Enemies are not implemented yet

        # Update Ball
        ball = world.get_ball()
        #if ball.distance_to(pos_ball[0], pos_ball[1]) > 60:
        ball.set_position(pos_ball)
        return world

    def dist(self, (xa, ya), (xb, yb)):
        return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

    def mais_proximo(self, ls, p):
        best = None
        for pos in ls:
            if best is None or self.dist(pos, p) < self.dist(best, p):
                best = pos;
        return best


import math
import cv2 as cv
from src.constant.constant import METRIC_TYPE

class Canvas:
    def __init__(self, display_items, gpx_metric, vid_fps, vid_offset):
        self.display_items = display_items
        self.gpx_metric = gpx_metric
        self.vid_fps = vid_fps
        self.vid_offset = vid_offset


    def draw(self, frame, frame_count):
        for item in self.display_items:
            metric = item["metric"]
            frame_in_sec = math.floor(frame_count/self.vid_fps)
            
            if metric == METRIC_TYPE["POWER"]:
                self.draw_power(item, frame, frame_in_sec)

            elif metric == METRIC_TYPE["HEART_RATE"]:
                self.draw_heartrate(item, frame, frame_in_sec)

            elif metric == METRIC_TYPE["CADENCE"]:
                self.draw_cadence(item, frame, frame_in_sec)

            elif metric == METRIC_TYPE["SPEED"]:
                self.draw_speed(item, frame, frame_in_sec)

            elif metric == METRIC_TYPE["DISTANCE"]:
                self.draw_distance(item, frame, frame_in_sec)

            elif metric == METRIC_TYPE["GRADIENT"]:
                self.draw_gradient(item, frame, frame_in_sec)


    def draw_power(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"Power: {self.gpx_metric[frame_in_sec]['power']}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)


    def draw_heartrate(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"BPM: {self.gpx_metric[frame_in_sec]['hr']}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            

    def draw_cadence(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"RPM: {self.gpx_metric[frame_in_sec]['cad']}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            
    
    def draw_speed(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"Speed: N/A", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            


    def draw_distance(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"KM: N/A", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            

    def draw_gradient(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]

        if theme == 0:
            cv.putText(frame, f"M Climb: N/A", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
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
            frame_in_sec = math.floor(frame_count/self.vid_fps) - self.vid_offset
            
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
        power = self.gpx_metric[frame_in_sec]['power'] if self.is_metric_range_valid(frame_in_sec) else 0

        if theme == 0:
            cv.putText(frame, f"Power: {power}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)


    def draw_heartrate(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]
        heartrate = self.gpx_metric[frame_in_sec]['hr'] if self.is_metric_range_valid(frame_in_sec) else 0

        if theme == 0:
            cv.putText(frame, f"BPM: {heartrate}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            

    def draw_cadence(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]
        cadence = self.gpx_metric[frame_in_sec]['cad'] if self.is_metric_range_valid(frame_in_sec) else 0

        if theme == 0:
            cv.putText(frame, f"RPM: {cadence}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            
    
    def draw_speed(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]
        speed = "N/A"

        if theme == 0:
            cv.putText(frame, f"Speed: {speed}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            


    def draw_distance(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]
        distance = "N/A"

        if theme == 0:
            cv.putText(frame, f"KM: {distance}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            

    def draw_gradient(self, item, frame, frame_in_sec):
        theme = item["theme"]
        posx = item["posx"]
        posy = item["posy"]
        gradient = "N/A"

        if theme == 0:
            cv.putText(frame, f"M Climb: {gradient}", (posx, posy), 
                       cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv.LINE_4)
            

    def is_metric_range_valid(self, frame_in_sec):
        return frame_in_sec >= 0 and frame_in_sec <= len(self.gpx_metric) - 1
from typing import Tuple

import cv2
from numpy import ndarray


def get_nu_contours(path: str):
    image: ndarray = cv2.imread(path, 0)
    _, binary = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)
    open_st_elem = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    close_st_elem = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
    opened: ndarray = cv2.morphologyEx(binary, cv2.MORPH_OPEN, open_st_elem)
    closed: ndarray = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, close_st_elem)
    cnt_hei: Tuple[ndarray, ndarray] = cv2.findContours(
        closed, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE
    )
    return len(cnt_hei[0])

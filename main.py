# This code is written authentically and not copied from any external source.
# However, we did refer to several online resources for  understanding purposes.
# Please check out the commit history at https://github.com/deep-1704/camera-calibration-cv

import cv2
import numpy as np
import glob

CHESSBOARD_DIM = (7, 7)

def generate_world_coordinates() -> np.ndarray:
    # Initialise array of shape
    coordinate_set = np.zeros((1, CHESSBOARD_DIM[0]*CHESSBOARD_DIM[1], 3), np.float32)

    # Populate corner coordinates
    for i in range(CHESSBOARD_DIM[0]):
        for j in range(CHESSBOARD_DIM[1]):
            coordinate_set[0][(CHESSBOARD_DIM[1]*i) + j][0] = j
            coordinate_set[0][(CHESSBOARD_DIM[1]*i) + j][1] = i
            
    return coordinate_set


if __name__ == '__main__':
    ans = generate_world_coordinates()
    print(ans)

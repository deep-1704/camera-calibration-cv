# This code is written authentically and not copied from any external source.
# However, we did refer to several online resources for  understanding purposes.
# Please check out the commit history at https://github.com/deep-1704/camera-calibration-cv

import cv2
import numpy as np
import glob

CHESSBOARD_DIM = (7, 7)


def show_corners(img, c):
    img = cv2.drawChessboardCorners(img, CHESSBOARD_DIM, c, True)
    cv2.imshow("img", img)
    cv2.waitKey(0)


def generate_world_coordinates() -> np.ndarray:
    # Initialise array of shape
    coordinate_set = np.zeros((1, CHESSBOARD_DIM[0] * CHESSBOARD_DIM[1], 3), np.float32)

    # Populate corner coordinates
    for i in range(CHESSBOARD_DIM[0]):
        for j in range(CHESSBOARD_DIM[1]):
            coordinate_set[0][(CHESSBOARD_DIM[1] * i) + j][0] = j
            coordinate_set[0][(CHESSBOARD_DIM[1] * i) + j][1] = i

    return coordinate_set


if __name__ == '__main__':
    # 3D coordinates of the corners of chessboard-squares w.r.t. world coordinate system
    coordinates_world = generate_world_coordinates()

    # List of 3D coordinates and corresponding 2D coordinates for calibration function
    coordinates_3D = []
    coordinates_2D = []

    # Variables to store image width and height
    w = 0
    h = 0

    # Analyse the images to get the corresponding image coordinates
    images = glob.glob("./calibration_images/*.jpeg")

    for filename in images:
        image = cv2.imread(filename)

        # Convert into gray scale to work with intensities rather than BGR values
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Image width and height. All images have same resolution
        w = grayscale_image.shape[1]
        h = grayscale_image.shape[0]

        # Find corners
        ret, corners = cv2.findChessboardCorners(grayscale_image, CHESSBOARD_DIM)

        # If corners are found, further refine them
        if ret:
            # Stop refining after 30 iterations or if location improves by <0.001
            criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

            corners_refined = cv2.cornerSubPix(grayscale_image, corners, (11, 11), (-1, -1), criteria)

            coordinates_3D.append(coordinates_world)
            coordinates_2D.append(corners_refined)

            # Uncomment below line to also see the corners detected. Press any key to go on next image
            # show_corners(image, corners_refined)

    ret, matrix, _, r_vecs, t_vecs = cv2.calibrateCamera(coordinates_3D, coordinates_2D,
                                                                  (w, h),
                                                                  None, None)


    # Intrinsic Parameters
    print("\nIntrinsic Parameters:")
    print(f"Focal Length: fx = {matrix[0, 0]}, fy = {matrix[1, 1]}")
    print(f"Principal Point: cx = {matrix[0, 2]}, cy = {matrix[1, 2]}")
    print("Skew parameter: ", matrix[0, 1])

    # Extrinsic Parameters (for each calibration image)
    print("\nExtrinsic Parameters:")
    for i in range(len(r_vecs)):
        print(f"\nImage {i + 1}:")
        # OpenCV outputs the rotation matrix in a compact form called Rodrigues form.
        # To get a 3X3 matrix, it needs to be transformed using cv2.Rodrigues()
        print(f"Rotation matrix:\n{cv2.Rodrigues(r_vecs[i])[0]}\n")
        print(f"Translation Vector: {t_vecs[i].ravel()}")

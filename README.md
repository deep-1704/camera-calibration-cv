# camera-calibration-cv

## Overview

`main.py` is a Python script for camera calibration using OpenCV. The script computes both **intrinsic** (focal lengths, principal points) and **extrinsic** (rotation and translation) parameters of the camera based on images of a chessboard calibration pattern.

-----

## Prerequisites

Before running the script, ensure you have the following installed:

1. **Python** (version 3.12 or later recommended)
2. Required Python packages:
    - `opencv-python`
    - `numpy`
   
### Installation of prerequisites:

You can install the required Python packages using pip:

```bash
pip install numpy opencv-python
```

-----

## Running the Script

1. **Run `main.py`:**
   Execute the script via the command line or your IDE:

   ```bash
   python main.py
   ```
    That's it.

2. **View Results:**
   - The script will output the **intrinsic** and **extrinsic** camera parameters, including:
     - **Focal Length** (`fx` and `fy`)
     - **Principal Point** (`cx` and `cy`)
     - **Skew Parameter** (`S`)
     - **Rotation Matrices** and **Translation Vectors** for each input calibration image.

3. **To view detected corners(Optional):**
   - Uncomment the line within the script to display the detected chessboard corners:
     ```python
     # show_corners(image, corners_refined)
     ```
   - When enabled, a preview window will appear showing the detected corners for each image. Press any key to process the next image.

---

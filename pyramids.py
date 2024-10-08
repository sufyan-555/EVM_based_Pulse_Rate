import cv2
import numpy as np
from constants import LAP_LEVELS

def gaussian_pyramids(image, levels):
    """
    Generate a Gaussian pyramid from the given image.

    Args:
        image (numpy array): The input image.
        levels (int): The number of levels in the pyramid. Defaults to 5.

    Returns:
        A list of numpy arrays representing the Gaussian pyramid.
    """
    float_img = np.ndarray(shape=image.shape, dtype="float")
    float_img[:] = image
    g_pyramids = [float_img]

    # Iterate over the levels and generate the Gaussian pyramid.
    for i in range(levels - 1):
        # Downsample the image using Gaussian blur.
        float_img=cv2.pyrDown(float_img)
        g_pyramids.append(float_img)
    return g_pyramids

def laplacian_pyramids(image,levels):
    """
    Generate a Laplacian pyramid from the given image.

    Args:
        image (numpy array): The input image.
        levels (int): The number of levels in the pyramid. Defaults to 5.

    Returns:
        A list of numpy arrays representing the Laplacian pyramid.
    """
    g_pyramids = gaussian_pyramids(image,levels)
    l_pyramids = []

    # Iterate over the Gaussian pyramid and generate the Laplacian pyramid.
    for i in range(levels - 1):
        # Upsample the next level in the Gaussian pyramid.
        upsampled = cv2.pyrUp(g_pyramids[i + 1])
        
        # Get the dimensions of the upsampled image.
        if len(upsampled.shape) == 3:
            height, width, depth = upsampled.shape
        else:
            height, width = upsampled.shape

        # Resize the current level in the Gaussian pyramid to match the upsampled image.
        g_pyramids[i] = cv2.resize(g_pyramids[i], (width, height))
        
        # Calculate the difference between the two levels, and append to the Laplacian pyramid.
        diff = cv2.subtract(g_pyramids[i], upsampled)
        l_pyramids.append(diff)

    # Append the last level of the Gaussian pyramid to the Laplacian pyramid.
    l_pyramids.append(g_pyramids[-1])
    return l_pyramids

def build_pramaids(frames,levels=LAP_LEVELS):
    """
    Builds a pyramid for a given video.

    Args:
        frames (list of numpy arrays): The input video frames.
        levels (int, optional): The number of levels in the pyramid. Defaults to LAP_LEVELS.

    Returns:
        A list of numpy arrays representing the pyramid for the video.
    """
    # Initialize the pyramid for the video.
    lap_video = []
    for i , frame in enumerate(frames):
        # Generate the pyramid for the current frame.
        pyramid = laplacian_pyramids(frame,levels)
        for j in range(levels):
            # If this is the first frame, initialize the pyramid with zeros.
            if i == 0:
                if len(pyramid[j].shape) == 3:
                    lap_video.append(np.zeros(shape=(
                        len(frames),
                        pyramid[j].shape[0],
                        pyramid[j].shape[1],
                        pyramid[j].shape[2]
                    )))
                else:
                    lap_video.append(np.zeros(shape=(
                        len(frames),
                        pyramid[j].shape[0],
                        pyramid[j].shape[1]
                    )))

            # Add the current frame of the pyramid to the video pyramid.
            lap_video[j][i] = pyramid[j]
    return lap_video

import cv2
import numpy as np

def gaussian_pyramids(image, levels=5):
    """
    Generate a Gaussian pyramid from the given image.

    Args:
        image (numpy array): The input image.
        levels (int): The number of levels in the pyramid. Defaults to 5.

    Returns:
        A list of numpy arrays representing the Gaussian pyramid.
    """
    # Convert the image to a float32 for smoother downsampling
    float_img = np.array(image, dtype=np.float32)

    # The Gaussian pyramid is a list of images, with the original image as the first element
    g_pyramids = [float_img]

    # Iterate over the levels and downsample the image
    for i in range(levels - 1):
        # Downsample the image using OpenCVs pyrDown function
        float_img = cv2.pyrDown(float_img)

        # Add the downsampled image to the list of Gaussian pyramid images
        g_pyramids.append(float_img)

    return g_pyramids


def laplacian_pyramids(image,levels=5):
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
        height, width, depth = upsampled.shape
        
        # Resize the current level in the Gaussian pyramid to match the upsampled image.
        g_pyramids[i] = cv2.resize(g_pyramids[i], (height, width))
        
        # Calculate the difference between the two levels, and append to the Laplacian pyramid.
        diff = cv2.subtract(g_pyramids[i], upsampled)
        l_pyramids.append(diff)

    # Append the last level of the Gaussian pyramid to the Laplacian pyramid.
    l_pyramids.append(g_pyramids[-1])
    return l_pyramids

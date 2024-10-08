# EVM_based_Pulse_Rate

This repository contains the code for a pulse rate detection app using the Eulerian Video Magnification (EVM) technique. The app is designed to detect a user's pulse rate using a video of their face. The program uses the OpenCV library for image processing and the SciPy library for signal processing.

The program works by reading in a video of a user's face, and then using the EVM technique to magnify the subtle changes in the user's skin color caused by their pulse. The resulting video is then processed using a Fast Fourier Transform (FFT) to detect the pulse rate.

The program is designed to be run from the command line, and requires a video file as an argument. The program will then output the detected pulse rate in beats per minute.

The program is written in Python and is designed to be run on a Linux or Windows system with OpenCV and SciPy installed.

## File Structure

The repository contains the following files and directories:

* `pyramids.py`: A module containing functions for generating Gaussian and Laplacian pyramids.
* `processing.py`: A module containing functions for processing the video and detecting the pulse rate.
* `preprocessing.py`: A module containing functions for reading in the video and selecting the region of interest.
* `main.py`: The main program, which reads in the video and calls the functions in the other modules to detect the pulse rate.
* `constants.py`: A module containing constants used by the program.
* `requirements.txt`: A file containing the dependencies required by the program.
* `README.md`: This file, which provides information about the program.

## Running the Program
To run the program, you need to change the video file path in `main.py` and then run it using Python. For example, if you have a video file called `test_video.mov` in the same directory as the program, you can run it using the following command:


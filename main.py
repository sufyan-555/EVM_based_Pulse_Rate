from pyramids import *
from processing import *
from preprocessing import *

video_path="test_video.mov"

video, fps = read_video(video_path)
print("Video loaded from:", video_path)
print("FPS:", fps)

print("Building pyramid levels:")
lap_video = build_pramaids(video)

print("Performing FFT:")
fft_data, freq = perform_fft(lap_video[1],fps)

print("Calculating heart rate:")
rate = get_heart_rate(fft_data, freq)

print("Heart rate:", rate)



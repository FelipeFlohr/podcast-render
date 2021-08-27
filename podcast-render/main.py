from moviepy.editor import *

class ImageAnalyzer():
    def __init__(self, destination_folder_path : str, video_file_path : str):
        self.frame_destination = destination_folder_path
        self.video = video_file_path

    def separate_frames(self):
        video = VideoFileClip(self.video)
        total_amount_of_frames = int(video.fps * video.duration)
        print(f"Total amount of frames: {total_amount_of_frames}")

        # Saving each frame as .png
        for i in range(total_amount_of_frames):
            print(f"Frame: {i / video.fps}")
            video.get_frame(i / video.fps)
            video.save_frame(f"{self.frame_destination}/{i}.png")
            print("Iteration #{} done.".format(i))


image = ImageAnalyzer("C:/Users/Felipe/PycharmProjects/podcastRender/Frames", "video.mp4")
image.separate_frames()

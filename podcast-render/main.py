from moviepy.editor import *
from PIL import Image


class ImageAnalyzer:
    def __init__(self, frames_folder: str, video_file_path: str):
        self.frames_folder = frames_folder
        self.video = video_file_path

    # This method is obsolete. Please use the Java Frame Extractor instead
    def separate_frames(self):
        video = VideoFileClip(self.video)
        total_amount_of_frames = int(video.fps * video.duration)
        print(f"Total amount of frames: {total_amount_of_frames}")

        # Saving each frame as .png
        for i in range(total_amount_of_frames):
            print(f"Frame: {i / video.fps}")
            video.get_frame(i / video.fps)
            video.save_frame(f"{self.frames_folder}/{i}.png")
            print("Iteration #{} done.".format(i))

    def generate_casters_timestamps(self, felipe_pos, gabriel_pos):
        total_files = 0

        # Counting how many files there is on the folder
        for i in os.listdir(self.frames_folder):
            total_files += 1

        print(f'total files {total_files}')

        # Casters' list order: Felipe, Gabriel

        casters = list()

        # This will create a dictionary for Felipe
        felipe = list()
        gabriel = list()

        for i in range(total_files):
            image = Image.open(f"{self.frames_folder}\\{i}.png")
            pixel = image.load()

            if pixel[felipe_pos[0], felipe_pos[1]][0] > 30:
                pixeldict = {"speaking": True}
                felipe.append(pixeldict.copy())
            else:
                pixeldict = {"speaking": False}
                felipe.append(pixeldict.copy())

            # This will create a dictionary for Gabriel
            if pixel[gabriel_pos[0], gabriel_pos[1]][0] > 30:
                pixeldict = {"speaking": True}
                gabriel.append(pixeldict.copy())
            else:
                pixeldict = {"speaking": False}
                gabriel.append(pixeldict.copy())

        # This will add the dictionaries on the list, and thereafter return the same
        casters.append(felipe[:])
        casters.append(gabriel[:])
        return casters


if __name__ == "__main__":
    image_analysis = ImageAnalyzer("C:\\Users\\Felipe\\Desktop\\Frames", "video.mp4")
    # (252, 742), (252, 801)
    timestamps = image_analysis.generate_casters_timestamps((252, 742), (252, 801))

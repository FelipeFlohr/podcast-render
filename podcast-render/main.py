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

    def get_total_amount_of_frames(self):
        total_files = 0

        # Counting how many files there is on the folder
        for i in os.listdir(self.frames_folder):
            total_files += 1

        return total_files

    def generate_casters_timestamps(self, felipe_pos, gabriel_pos):
        total_files = 0

        # Counting how many files there is on the folder
        for i in os.listdir(self.frames_folder):
            total_files += 1

        # Casters' list order: Felipe, Gabriel

        casters = list()

        # This will create a dictionary for Felipe
        felipe = list()
        gabriel = list()

        for i in range(total_files):
            image = Image.open(f"{self.frames_folder}\\{i}.png")
            pixel = image.load()

            if 30 < pixel[felipe_pos[0], felipe_pos[1]][0] < 67:
                pixeldict = {"speaking": True}
                felipe.append(pixeldict.copy())
            else:
                pixeldict = {"speaking": False}
                felipe.append(pixeldict.copy())

            # This will create a dictionary for Gabriel
            if 30 < pixel[gabriel_pos[0], gabriel_pos[1]][0] < 67:
                pixeldict = {"speaking": True}
                gabriel.append(pixeldict.copy())
            else:
                pixeldict = {"speaking": False}
                gabriel.append(pixeldict.copy())

        # This will add the dictionaries on the list, and thereafter return the same
        casters.append(felipe[:])
        casters.append(gabriel[:])
        return casters


class MovieRendering:
    def __init__(self, video_path: str, video_output: str, timestamps, qnt_frames: int):
        self.video_path = video_path
        self.video_output = video_output
        self.timestamps = timestamps
        self.amount_of_frames = qnt_frames

    def generate_frames(self):
        frames = list()

        for i in range(self.amount_of_frames):
            if timestamps[0][i]["speaking"] and timestamps[1][i]["speaking"]:
                frames.append("podcast-render/files/felipegabriel.png")
            elif timestamps[0][i]["speaking"]:
                frames.append("podcast-render/files/felipe.png")
            elif timestamps[1][i]["speaking"]:
                frames.append("podcast-render/files/gabriel.png")
            else:
                frames.append("podcast-render/files/blank.png")

        return frames

    def render_movie(self, frames_stamps):
        video_audio = VideoFileClip(self.video_path)
        video_audio.audio.write_audiofile("temp.mp3")

        clip = ImageSequenceClip(frames_stamps, fps=60)
        clip.set_audio("temp.mp3")
        clip.write_videofile("output.mp4")


if __name__ == "__main__":
    image_analysis = ImageAnalyzer("C:\\Users\\Felipe\\Desktop\\Frames", "video.mp4")
    timestamps = image_analysis.generate_casters_timestamps((252, 742), (252, 801))
    qnt_frames = image_analysis.get_total_amount_of_frames()

    movie_render = MovieRendering("video.mp4", "fodeta/saida.mp4", timestamps, qnt_frames)
    frames = movie_render.generate_frames()
    movie_render.render_movie(frames)

from moviepy.editor import *
from PIL import Image
from ini_parser import Parameters


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
        print("Getting the total amount of frames...")
        total_files = 0

        # Counting how many files there is on the folder
        for i in os.listdir(self.frames_folder):
            total_files += 1

        print(f"Total amount of frames = {total_files}")
        return total_files

    def generate_casters_timestamps(self, felipe_pos, gabriel_pos):
        total_files = 0

        # Counting how many files there is on the folder
        for i in os.listdir(self.frames_folder):
            total_files += 1

        casters = list()

        felipe = list()
        gabriel = list()

        print("Generating timestamps for each casters/guests")
        for i in range(total_files):
            image = Image.open(f"{self.frames_folder}\\{i}.png")
            pixel = image.load()

            # This will create a dictionary for Felipe
            if 60 < pixel[felipe_pos[0], felipe_pos[1]][0] < 75:
                pixel_dict = {"speaking": True}
                felipe.append(pixel_dict.copy())
            else:
                pixel_dict = {"speaking": False}
                felipe.append(pixel_dict.copy())

            # This will create a dictionary for Gabriel
            if 60 < pixel[gabriel_pos[0], gabriel_pos[1]][0] < 75:
                pixel_dict = {"speaking": True}
                gabriel.append(pixel_dict.copy())
            else:
                pixel_dict = {"speaking": False}
                gabriel.append(pixel_dict.copy())

        # This will add the dictionaries on the list, and thereafter return the same
        casters.append(felipe[:])
        casters.append(gabriel[:])
        print("Timestamps generated.")
        return casters


class MovieRendering:
    def __init__(self, video_path: str, video_output: str, timestamps, qnt_frames):
        self.video_path = video_path
        self.video_output = video_output
        self.timestamps = timestamps
        self.amount_of_frames = qnt_frames

    def generate_frames(self):
        print("Generating frames...")
        frames = list()

        for i in range(self.amount_of_frames):
            # Both are speaking
            if timestamps[0][i]["speaking"] and timestamps[1][i]["speaking"]:
                frames.append("podcast-render/files/felipegabriel.png")

            # If just Felipe is speaking
            elif timestamps[0][i]["speaking"]:
                frames.append("podcast-render/files/felipe.png")

            # If just Gabriel is speaking
            elif timestamps[1][i]["speaking"]:
                frames.append("podcast-render/files/gabriel.png")

            # If nobody if speaking
            else:
                frames.append("podcast-render/files/blank.png")

        print("Frames generated...")
        return frames

    def render_movie(self, frames_stamps):
        print("Start video render...")
        video_audio = VideoFileClip(self.video_path)
        audio = video_audio.audio
        video_fps = video_audio.fps

        print("Placing the frames...")
        clip = ImageSequenceClip(frames_stamps, fps=video_fps)
        clip.audio = audio
        print("Frames placed")

        print("Rendering the video...")
        clip.write_videofile(self.video_output)
        print("Video rendered.")


if __name__ == "__main__":
    # Creating the cfg file
    pm = Parameters("config.ini")
    pm.write()

    image_analysis = ImageAnalyzer(pm.frames_folder(), pm.video_path())
    timestamps = image_analysis.generate_casters_timestamps((252, 742), (252, 801))
    qnt_frames = image_analysis.get_total_amount_of_frames()

    movie_render = MovieRendering(pm.video_path(), pm.output_video_name(), timestamps, qnt_frames)
    frames = movie_render.generate_frames()
    movie_render.render_movie(frames)

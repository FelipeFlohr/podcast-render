from moviepy.editor import *
from PIL import Image
from ini_parser import Parameters


class ImageAnalyzer:
    def __init__(self, frames_folder: str, video_file_path: str):
        """
        -> Class for analyzing images
        :param frames_folder: The absolute path to the folder where the frames are located
        :param video_file_path: The absolute path to the video
        """
        self.frames_folder = frames_folder
        self.video = video_file_path

    # This method is obsolete. Please use the Java Frame Extractor instead
    def separate_frames(self):
        """
        -> It will extract every frame of the video and place it on the frames' folder
        :return: no return
        """
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
        """
        -> Will get the total amount of frames
        :return: the total amount of frames as integer
        """
        print("Getting the total amount of frames...")
        total_files = 0

        # Counting how many files there is on the folder
        for _ in os.listdir(self.frames_folder):
            total_files += 1

        print(f"Total amount of frames = {total_files}")
        return total_files

    def generate_casters_timestamps(self, felipe_pos, gabriel_pos):
        """
        -> Will generate timestamps telling who is speaking in the current frame
        :param felipe_pos: The XY position of Felipe's green speaking circle on discord
        :param gabriel_pos: The XY position of Gabriel's green speaking circle on discord
        :return: will return a list containing the timestamps for each member of the podcast
        """
        total_files = self.get_total_amount_of_frames()

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
        """
        -> Class for rendering the video
        :param video_path: the absolute path to the video
        :param video_output: already specified on config.ini
        :param timestamps: the list containing the timestamps for each member of the podcast
        :param qnt_frames: the total amount of frames
        """
        self.video_path = video_path
        self.video_output = video_output
        self.timestamps = timestamps
        self.amount_of_frames = qnt_frames

    def generate_frames(self):
        """
        -> This will generate every frame to be rendered on the final video
        :return: will return a list of frames
        """
        print("Generating frames...")
        frames = list()

        for i in range(self.amount_of_frames):
            # Both are speaking
            if timestamps[0][i]["speaking"] and timestamps[1][i]["speaking"]:
                frames.append("files/felipegabriel.png")

            # If just Felipe is speaking
            elif timestamps[0][i]["speaking"]:
                frames.append("files/felipe.png")

            # If just Gabriel is speaking
            elif timestamps[1][i]["speaking"]:
                frames.append("files/gabriel.png")

            # If nobody is speaking
            else:
                frames.append("files/blank.png")

        print("Frames generated...")
        return frames

    def render_movie(self, frames_stamps):
        """
        -> Method for rendering the movie
        :param frames_stamps: list containing each frame
        :return: no return
        """
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

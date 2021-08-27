package videorelated;

import org.bytedeco.javacv.FFmpegFrameGrabber;

import static labels.SelectVideo.videoPath;

public class ExtractFrames {

    public static int getAmountOfFrames() throws FFmpegFrameGrabber.Exception {
        FFmpegFrameGrabber frameGrabber = new FFmpegFrameGrabber(videoPath);
        frameGrabber.start();

        return frameGrabber.getLengthInVideoFrames();
    }

}

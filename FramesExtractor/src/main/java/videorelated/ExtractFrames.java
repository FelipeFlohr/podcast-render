package videorelated;

import org.bytedeco.copiedstuff.FFmpegFrameGrabber;
import org.bytedeco.copiedstuff.FrameGrabber;
import org.bytedeco.copiedstuff.Java2DFrameConverter;

import javax.imageio.ImageIO;
import javax.swing.*;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import static labels.SelectFolder.folderPath;
import static labels.SelectVideo.videoPath;

public class ExtractFrames {

    /**
     * Gets the total amount of frames of a video
     * @return the lenght of the video in frames as integer
     * @throws FrameGrabber.Exception
     */
    public static int getAmountOfFrames() throws FrameGrabber.Exception {
        FFmpegFrameGrabber frameGrabber = new FFmpegFrameGrabber(videoPath.getAbsolutePath());
        frameGrabber.start();

        return frameGrabber.getLengthInFrames();
    }

    /**
     * Separate each frame using the FFmpegFrameGrabber class. Thereafter, saves it into the user's desired folder
     * @throws FrameGrabber.Exception
     */
    public static void separateFrames() throws FrameGrabber.Exception {
        FFmpegFrameGrabber frameGrabber = new FFmpegFrameGrabber(videoPath.getAbsolutePath());
        frameGrabber.start();
        int frames = getAmountOfFrames();
        int i = 0;

        while(i < frames){
            String path = folderPath.getAbsolutePath()+"\\"+String.valueOf(i)+".png";

            Java2DFrameConverter c = new Java2DFrameConverter();
            BufferedImage bi = c.convert(frameGrabber.grab());

            if(bi != null){
                try {
                    ImageIO.write(bi, "png", new File(path));
                } catch (IOException e) {
                    e.printStackTrace();
                }
                System.out.printf("Iteration #%d completed.\n", i);
                i++;
            }
            if(i == (frames - 1)){
                frameGrabber.close();
                break;
            }

        }
        System.out.println("Task completed.");
        JOptionPane.showMessageDialog(null, "Task completed", "Task completed", JOptionPane.INFORMATION_MESSAGE);
    }

}

package videorelated;

import org.bytedeco.javacv.FFmpegFrameGrabber;
import org.bytedeco.javacv.Java2DFrameConverter;
import progressbars.ProgressBar;

import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import static labels.SelectFolder.folderPath;
import static labels.SelectVideo.videoPath;

public class ThreadExtractFrames implements Runnable {

    @Override
    public void run() {
        FFmpegFrameGrabber grabber = new FFmpegFrameGrabber(videoPath.getAbsolutePath());
        try {
            grabber.start();
        } catch (FFmpegFrameGrabber.Exception e) {
            e.printStackTrace();
        }

        for(int i = 0; i < ProgressBar.totalAmountOfFrames; i++){
            String path = folderPath.getAbsolutePath()+"\\"+String.valueOf(i)+".png";

            Java2DFrameConverter converter = new Java2DFrameConverter();
            try{
                BufferedImage image = converter.getBufferedImage(grabber.grabFrame());
                ImageIO.write(image, "png", new File(path));
            }
            catch(IllegalArgumentException | IOException e){
                //System.out.println(e);
            }

            FrameUI.progress.setProgressValue(i);
            System.out.printf("Iteration #%d completed\n", i);
        }

        JOptionPane.showMessageDialog(null, "Task completed. Frames are located at "+folderPath.getAbsolutePath(), "Task completed", JOptionPane.INFORMATION_MESSAGE);

    }

}

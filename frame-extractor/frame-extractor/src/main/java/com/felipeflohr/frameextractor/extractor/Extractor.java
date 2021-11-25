package com.felipeflohr.frameextractor.extractor;

import com.felipeflohr.frameextractor.swing.progressbar.ProgressBar;
import org.bytedeco.copiedstuff.FFmpegFrameGrabber;
import org.bytedeco.copiedstuff.FrameGrabber;
import org.bytedeco.copiedstuff.Java2DFrameConverter;

import javax.imageio.ImageIO;
import javax.swing.JOptionPane;
import javax.swing.SwingUtilities;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class Extractor implements Runnable {

    final File VIDEO;
    final File FOLDER;
    final ProgressBar PROGRESS_BAR;

    public Extractor(File video, File folder, ProgressBar progressBar) throws FrameGrabber.Exception {
        VIDEO = video;
        FOLDER = folder;
        PROGRESS_BAR = progressBar;

        progressBar.setMaximumBarValue(getAmountOfFrames());
        SwingUtilities.invokeLater(this);
    }

    private int getAmountOfFrames() throws FrameGrabber.Exception {
        FFmpegFrameGrabber frameGrabber = new FFmpegFrameGrabber(VIDEO.getAbsolutePath());
        frameGrabber.start();

        return frameGrabber.getLengthInFrames();
    }

    private void extractFrames() throws FrameGrabber.Exception {
        FFmpegFrameGrabber frameGrabber = new FFmpegFrameGrabber(VIDEO.getAbsolutePath());
        frameGrabber.start();
        int frames = getAmountOfFrames();
        int i = 0;

        while(i < frames){
            String path = FOLDER.getAbsolutePath()+"\\"+ i +".png";

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
                PROGRESS_BAR.setValue(i);
                PROGRESS_BAR.update(PROGRESS_BAR.getGraphics());
            }
            if(i == (frames - 1)){
                frameGrabber.close();
                break;
            }

        }
        JOptionPane.showMessageDialog(null, "Task completed", "Task completed", JOptionPane.INFORMATION_MESSAGE);
    }

    @Override
    public void run() {
        try {
            extractFrames();
        } catch (FrameGrabber.Exception e) {
            e.printStackTrace();
        }
    }
}

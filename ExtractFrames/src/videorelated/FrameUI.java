package videorelated;

import labels.SelectFolder;
import labels.SelectVideo;
import buttons.SeparateFrames;
import progressbars.ProgressBar;

import javax.swing.*;
import java.awt.*;

public class FrameUI extends JFrame {

    public static ProgressBar progress;

    public FrameUI(){
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new GridLayout(4, 1));

        JButton buttonVideo = new JButton("Select video file...");
        JButton buttonFolder = new JButton("Select folder to save video...");

        new SelectVideo(this);
        new SelectFolder(this);
        new SeparateFrames(this);
        progress = new ProgressBar(this, 500);

        this.setSize(500, 200);
        this.setResizable(false);
        this.setTitle("2flps - Frame extractor");
        this.setVisible(true);

    }

}

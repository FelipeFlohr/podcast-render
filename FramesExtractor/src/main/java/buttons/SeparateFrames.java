package buttons;

import org.bytedeco.copiedstuff.FrameGrabber;
import progressbars.ProgressBar;
import videorelated.ExtractFrames;
import videorelated.FrameUI;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.IOException;

import static labels.SelectFolder.folderPath;
import static labels.SelectVideo.videoPath;

public class SeparateFrames extends JButton implements ActionListener {

    public SeparateFrames(JFrame mainFrame) {
        this.setText("Separate frames");
        this.addActionListener(this);

        mainFrame.add(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (videoPath == null || folderPath == null) {
            JOptionPane.showMessageDialog(null, "You need to select both video and folder to save", "Error", JOptionPane.ERROR_MESSAGE);
        }
        else if (videoPath.getAbsolutePath().isEmpty() || folderPath.getAbsolutePath().isEmpty()) {
            JOptionPane.showMessageDialog(null, "You need to select both video and folder to save", "Error", JOptionPane.ERROR_MESSAGE);
        }
        else {
            try {
                FrameUI.progress.setTotalAmountOfFrames(ExtractFrames.getAmountOfFrames());
            } catch (FrameGrabber.Exception ex) {
                ex.printStackTrace();
            }
            System.out.println("Successfully set the total amount of frames: " + ProgressBar.totalAmountOfFrames);

            try {
                ExtractFrames.separateFrames();
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
        }
    }

}

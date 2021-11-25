package com.felipeflohr.frameextractor.swing.buttons;

import com.felipeflohr.frameextractor.extractor.Extractor;
import com.felipeflohr.frameextractor.swing.labels.SelectFolder;
import com.felipeflohr.frameextractor.swing.labels.SelectVideo;
import com.felipeflohr.frameextractor.swing.progressbar.ProgressBar;
import org.bytedeco.copiedstuff.FrameGrabber;

import javax.swing.JButton;
import javax.swing.JOptionPane;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class ExecuteButton extends JButton implements ActionListener {

    final SelectVideo VIDEO;
    final SelectFolder FOLDER;
    final ProgressBar PROGRESS_BAR;

    public ExecuteButton(SelectVideo video, SelectFolder folder, ProgressBar progressBar) {
        this.VIDEO = video;
        this.FOLDER = folder;
        PROGRESS_BAR = progressBar;

        setText("Extract frames");
        setFocusable(false);
        addActionListener(this);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        File videoFile = VIDEO.getVideoFile();
        File folderFile = FOLDER.getFolderFile();

        if (videoFile == null) {
            JOptionPane.showMessageDialog(null, "You need to select both video and folder to save", "Error", JOptionPane.ERROR_MESSAGE);
        }
        else if (videoFile.getAbsolutePath().isEmpty() || folderFile.getAbsolutePath().isEmpty()) {
            JOptionPane.showMessageDialog(null, "You need to select both video and folder to save", "Error", JOptionPane.ERROR_MESSAGE);
        }
        else {
            try {
                new Extractor(videoFile, folderFile, PROGRESS_BAR);
            } catch (FrameGrabber.Exception ex) {
                ex.printStackTrace();
            }
        }
    }
}

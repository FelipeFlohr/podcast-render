package com.felipeflohr.frameextractor.swing.labels;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JTextField;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class SelectVideo extends JLabel implements ActionListener {

    private final JTextField VIDEO_PATH_TXT_FIELD;
    private File file;

    public SelectVideo() {
        setLayout(new FlowLayout());

        JButton selectVideoBtn = new JButton("Select video to open...");
        selectVideoBtn.addActionListener(this);

        VIDEO_PATH_TXT_FIELD = new JTextField("...", 20);
        VIDEO_PATH_TXT_FIELD.setEditable(false);

        add(selectVideoBtn);
        add(VIDEO_PATH_TXT_FIELD);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        FileNameExtensionFilter extensionFilter = new FileNameExtensionFilter("MP4 format", "mp4");
        JFileChooser videoChooser = new JFileChooser();
        videoChooser.setFileFilter(extensionFilter);

        int answer = videoChooser.showOpenDialog(null); // Will open the dialog
        if (answer == JFileChooser.APPROVE_OPTION) {
            File fileSelected = videoChooser.getSelectedFile();

            // If the file exists, then it will be attached to the "file" variable
            if (fileSelected.exists()) {
                file = fileSelected;
                setVideoPathTxtFieldText(file.getAbsolutePath());
            }
        }
    }

    public File getVideoFile() {
        return file;
    }

    private void setVideoPathTxtFieldText(String text) {
        VIDEO_PATH_TXT_FIELD.setText(text);
    }
}

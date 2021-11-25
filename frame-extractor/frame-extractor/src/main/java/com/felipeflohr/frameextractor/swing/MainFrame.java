package com.felipeflohr.frameextractor.swing;

import com.felipeflohr.frameextractor.swing.buttons.ExecuteButton;
import com.felipeflohr.frameextractor.swing.labels.SelectFolder;
import com.felipeflohr.frameextractor.swing.labels.SelectVideo;
import com.felipeflohr.frameextractor.swing.progressbar.ProgressBar;

import javax.swing.JFrame;
import java.awt.GridLayout;

public class MainFrame extends JFrame {

    public MainFrame() {
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLayout(new GridLayout(4, 1));

        SelectVideo selectVideoLabel = new SelectVideo();
        SelectFolder selectFolderLabel = new SelectFolder();
        ProgressBar progressBar = new ProgressBar();
        ExecuteButton executeButton = new ExecuteButton(selectVideoLabel, selectFolderLabel, progressBar);

        add(selectVideoLabel);
        add(selectFolderLabel);
        add(executeButton);
        add(progressBar);

        setSize(500, 200);
        setResizable(false);
        setTitle("2flps' Frame extractor");
        setLocationRelativeTo(null);
        setVisible(true);
    }
}

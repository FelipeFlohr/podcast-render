package com.felipeflohr.frameextractor.swing.labels;

import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JTextField;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class SelectFolder extends JLabel implements ActionListener {

    private final JTextField FOLDER_PATH_TXT_FIELD;
    private File folder;

    public SelectFolder() {
        setLayout(new FlowLayout());

        JButton selectFolderBtn = new JButton("Select folder to save...");
        selectFolderBtn.addActionListener(this);

        FOLDER_PATH_TXT_FIELD = new JTextField("..", 20);
        FOLDER_PATH_TXT_FIELD.setEditable(false);

        add(selectFolderBtn);
        add(FOLDER_PATH_TXT_FIELD);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        JFileChooser folderChooser = new JFileChooser();
        folderChooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

        try {
            folderChooser.showSaveDialog(null);
            folder = folderChooser.getSelectedFile();
            setFolderPathTxtFieldText(folder.getAbsolutePath());
        } catch (NullPointerException ignore) {}
    }

    public File getFolderFile() {
        return folder;
    }

    private void setFolderPathTxtFieldText(String text) {
        FOLDER_PATH_TXT_FIELD.setText(text);
    }
}

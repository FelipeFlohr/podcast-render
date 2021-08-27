package labels;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class SelectFolder extends JLabel implements ActionListener {

    JFrame mainFrame;
    JButton button;
    JTextField text;
    public static File folderPath;

    public SelectFolder(JFrame mainFrame){
        this.mainFrame = mainFrame;
        this.setLayout(new FlowLayout());

        button = new JButton("Select folder to open...");
        button.addActionListener(this);

        text = new JTextField(20);
        text.setEditable(false);

        this.add(button);
        this.add(text);

        mainFrame.add(this);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            JFileChooser chooseFolder = new JFileChooser();
            chooseFolder.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

            // Folder the user wants to save all pictures
            chooseFolder.showSaveDialog(null);
            folderPath = chooseFolder.getSelectedFile();
            text.setText(folderPath.getAbsolutePath());
        }
    }
}



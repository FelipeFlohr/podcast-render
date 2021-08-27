package labels;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;

public class SelectVideo extends JLabel implements ActionListener {

    JFrame mainFrame;
    JButton button;
    JTextField text;
    public static File videoPath;

    public SelectVideo(JFrame mainFrame){
        this.mainFrame = mainFrame;
        this.setLayout(new FlowLayout());

        button = new JButton("Select video to open...");
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
            FileNameExtensionFilter fileFilter = new FileNameExtensionFilter("MP4 format", "mp4");
            JFileChooser chooseVideo = new JFileChooser();
            chooseVideo.setFileFilter(fileFilter);
            int answer = chooseVideo.showOpenDialog(null);
            // Checks to see if file exists
            if(answer == JFileChooser.APPROVE_OPTION){
                File selection = chooseVideo.getSelectedFile();

                // If it exists, then the block will run
                if(selection.exists()){
                    videoPath = selection;
                    text.setText(videoPath.getAbsolutePath());
                }
            }
        }
    }
}

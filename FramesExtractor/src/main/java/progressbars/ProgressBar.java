package progressbars;

import javax.swing.*;

public class ProgressBar extends JProgressBar {

    JFrame mainFrame;
    public static int totalAmountOfFrames;

    public ProgressBar(JFrame mainFrame, int totalAmountOfFrames){
        this.mainFrame = mainFrame;
        this.setMinimum(1);
        this.setMaximum(totalAmountOfFrames);

        mainFrame.add(this);
    }

    public void setTotalAmountOfFrames(int l){
        totalAmountOfFrames = l;
        this.setMaximum(totalAmountOfFrames);
    }

    public void setProgressValue(int value){
        this.setValue(value);
    }

}

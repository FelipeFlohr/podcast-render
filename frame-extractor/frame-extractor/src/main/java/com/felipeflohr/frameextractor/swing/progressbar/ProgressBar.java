package com.felipeflohr.frameextractor.swing.progressbar;

import javax.swing.JProgressBar;
import java.awt.Color;

public class ProgressBar extends JProgressBar {

    public ProgressBar() {
        setMinimum(1);
        setForeground(new Color(66, 157, 39));
    }

    public void setMaximumBarValue(int value) {
        setMaximum(value);
    }
}

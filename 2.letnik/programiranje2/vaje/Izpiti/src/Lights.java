import java.awt.BasicStroke;
import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Lights {
	
	private static Color circleColor1 = new Color(220, 220, 220);
	private static Color circleColor2 = new Color(220, 220, 220);
	private static Color circleColor3 = new Color(220, 220, 220);

	public static void main(String[] args) {
		JFrame frame = new JFrame("Lights");
		frame.setSize(new Dimension(600, 680));
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setLayout(new BorderLayout());
		JPanel panel = new JPanel() {
			@Override
            protected void paintComponent(Graphics gl) {
                super.paintComponent(gl);
                Graphics2D g = (Graphics2D)gl;
                g.setColor(Color.BLACK);
                g.drawRoundRect((int)getWidth()/2 - 50, (int)getHeight()/2 - 200, 100, 300, 40, 40);
                g.fillRoundRect((int)getWidth()/2 - 50, (int)getHeight()/2 - 200, 100, 300, 40, 40);
                g.setColor(new Color(220, 220, 220));
                g.setStroke(new BasicStroke(4.0f));
                g.drawRoundRect((int)getWidth()/2 - 50, (int)getHeight()/2 - 200, 100, 300, 40, 40);
                g.setColor(circleColor1);
                g.drawOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 190, 80, 80);
                g.fillOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 190, 80, 80);
                g.setColor(circleColor2);
                g.drawOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 100, 80, 80);
                g.fillOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 100, 80, 80);
                g.setColor(circleColor3);
                g.drawOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 10, 80, 80);
                g.fillOval((int)getWidth()/2 - 40, (int)getHeight()/2 - 10, 80, 80);
            }
        };
		
		
		panel.setBackground(Color.WHITE);
		frame.add(panel, BorderLayout.CENTER);
		
		JPanel north = new JPanel();
        north.setBackground(new Color(220, 220, 220));
        frame.add(north, BorderLayout.NORTH);

        JButton stop = new JButton("STOP");
        stop.setPreferredSize(new Dimension(96, 30));
        stop.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	circleColor1 = Color.RED;
            	circleColor2 = new Color(220, 220, 220);
            	circleColor3 = new Color(220, 220, 220);
            	panel.repaint();
            	
            }
        });
        north.add(stop);

        JButton ready = new JButton("READY");
        ready.setPreferredSize(new Dimension(96, 30));
        ready.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	circleColor1 = new Color(220, 220, 220);
            	circleColor2 = Color.ORANGE;
            	circleColor3 = new Color(220, 220, 220);
            	panel.repaint();
        
            }
        });
        north.add(ready);
        
        JButton go = new JButton("GO");
        go.setPreferredSize(new Dimension(96, 30));
        go.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	circleColor1 = new Color(220, 220, 220);
            	circleColor3 = Color.GREEN;
            	circleColor2 = new Color(220, 220, 220);
            	panel.repaint();
            }
        });
        north.add(go);
		
		
		frame.setVisible(true);

	}

}

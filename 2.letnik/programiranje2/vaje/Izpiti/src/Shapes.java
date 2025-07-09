import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Shapes {


    public static void main(String[] args) {

    	List<Point> shapes = new ArrayList<Point>();
    	
        JFrame frame = new JFrame("Shapes");
        frame.setSize(new Dimension(1024, 720));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new BorderLayout());

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                for (Point shape: shapes) {
					g.setColor(Math.random() < 0.5? new Color(0.832f, 0.289f, 0.273f): new Color(0.297f, 0.5f, 0.605f));
					g.fillOval((int)shape.getX(), (int)shape.getY(), 32, 32);
					g.setColor(Color.BLACK);
					g.drawOval((int)shape.getX(), (int)shape.getY(), 32, 32);
                }
            }
        };
        panel.setBackground(Color.WHITE);
        frame.add(panel, BorderLayout.CENTER);

        JPanel north = new JPanel();
        north.setBackground(new Color(220, 220, 220));
        frame.add(north, BorderLayout.NORTH);

        JButton button1 = new JButton("Add");
        button1.setPreferredSize(new Dimension(96, 30));
        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	shapes.add(new Point((int)(Math.random() * (panel.getWidth() - 32)), (int)(Math.random() * (panel.getHeight() - 32))));
				frame.repaint();
            }
        });
        north.add(button1);

        JButton delete = new JButton("Delete");
        delete.setPreferredSize(new Dimension(96, 30));
        delete.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
            	shapes.clear();
				frame.repaint();
            }
        });
        north.add(delete);

        frame.setVisible(true);
    }
}

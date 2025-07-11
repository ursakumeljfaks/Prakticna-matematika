import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Polygon;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

public class Poligon {

	static int n = 5;

	public static void main(String[] args) {
		JFrame frame = new JFrame("Polygon");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(new Dimension(800, 800));

		JPanel panel = new JPanel() {
			private static final long serialVersionUID = 1L;
			@Override
			public void paint(Graphics g) {
				super.paint(g);
				
				int r = Math.min(getWidth(), getHeight()) / 3;
				
				Polygon polygon = new Polygon();
				for (int i = 0; i < n; i++) {
					double alpha = -Math.PI / 2 + i * 2 * Math.PI / n;
					polygon.addPoint((int)(getWidth() / 2 + r * Math.cos(alpha)), (int)(getHeight() / 2 + r * Math.sin(alpha)));
				}

				g.drawPolygon(polygon);
			}
		};
		panel.setBackground(Color.WHITE);
		frame.add(panel, BorderLayout.CENTER);

		JPanel controls = new JPanel();
		frame.add(controls, BorderLayout.NORTH);

		JButton decrement = new JButton("n-1"); 
		controls.add(decrement);

		JLabel label = new JLabel("n = " + n);
		label.setFont(new Font(Font.SANS_SERIF, Font.PLAIN, 16));
		controls.add(label);
		
		JButton increment = new JButton("n+1");
		controls.add(increment);

		decrement.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (n > 3) 
					n--;
				
				label.setText("n = " + n);
				panel.repaint();
			}
		});

		increment.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				n++;
				
				label.setText("n = " + n);
				panel.repaint();
			}
		});

		frame.setVisible(true);
	}
}
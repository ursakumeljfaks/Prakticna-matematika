import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Polygon;
import java.awt.event.MouseListener;
import java.awt.event.MouseEvent;


import javax.swing.JFrame;
import javax.swing.JPanel;

public class IceCream {
    public static Flavour flavour = Flavour.NONE;
    private static Color sladoled = new Color(255, 255, 255);

    public static void main(String[] args) {
        JFrame frame = new JFrame("Ice Cream");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(new Dimension(800, 600));
        frame.setResizable(true);
        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics gl) {
                super.paintComponent(gl);
                Graphics2D g = (Graphics2D)gl;
                
                if (flavour == Flavour.NONE) {
                	g.setColor(new Color(84, 62, 12));
                    g.drawRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    g.setColor(new Color(232, 153, 212));
                    g.drawRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    g.setColor(new Color(230, 223, 235));
                    g.drawRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    
                    g.setColor(new Color(207, 184, 130));
                    Polygon kornet = new Polygon();
                    kornet.addPoint((int) getWidth() / 3 + 350, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 450, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 400, (int) getHeight() / 3 + 250);
                    g.drawPolygon(kornet);
                    g.fillPolygon(kornet);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    kornet.addPoint((int) getWidth() / 3 + 350, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 450, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 400, (int) getHeight() / 3 + 250);
                    g.drawPolygon(kornet);
                    
                }
                else {
                	g.setColor(new Color(84, 62, 12));
                    g.drawRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 - 100, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    g.setColor(new Color(232, 153, 212));
                    g.drawRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 + 50, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    g.setColor(new Color(230, 223, 235));
                    g.drawRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.fillRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawRoundRect((int) getWidth() / 3 + 200, (int) getHeight() / 3 + 50, 100, 200, 40, 40);
                    
                    g.setColor(new Color(207, 184, 130));
                    Polygon kornet = new Polygon();
                    kornet.addPoint((int) getWidth() / 3 + 350, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 450, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 400, (int) getHeight() / 3 + 250);
                    g.drawPolygon(kornet);
                    g.fillPolygon(kornet);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    kornet.addPoint((int) getWidth() / 3 + 350, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 450, (int) getHeight() / 3 + 50);
                    kornet.addPoint((int) getWidth() / 3 + 400, (int) getHeight() / 3 + 250);
                    g.drawPolygon(kornet);
                    
                    
                    g.setColor(sladoled);
                    g.drawArc((int) getWidth() / 3 + 350, (int) getHeight() / 3, 100, 100, 0, 180);
                    g.fillArc((int) getWidth() / 3 + 350, (int) getHeight() / 3, 100, 100, 0, 180);
                    g.setColor(Color.BLACK);
                    g.setStroke(new BasicStroke(4.0f));
                    g.drawArc((int) getWidth() / 3 + 350, (int) getHeight() / 3, 100, 100, 0, 180);
                    
                    
                }

            }
        };
        panel.addMouseListener(new MouseListener() {

    		@Override
    		public void mouseClicked(MouseEvent e) {
    			
    			int x = e.getX();
    			int y = e.getY();
    			if (x >= panel.getWidth() / 3 - 100 && x <= panel.getWidth() / 3 && y >= panel.getHeight() / 3 + 50 && y <= panel.getHeight() / 3 + 250) {
    				flavour = Flavour.CHOCOLATE;
    				sladoled = new Color(84, 62, 12);
    				panel.repaint();
    				
    			}
    			else if (x >= panel.getWidth() / 3 + 50 && x <= panel.getWidth() / 3 + 150 && y >= panel.getHeight() / 3 + 50 && y <= panel.getHeight() / 3 + 250) {
    				flavour = Flavour.STRAWBERRY;
    				sladoled = new Color(232, 153, 212);
    				panel.repaint();
    			}
    				
    			else if (x >= panel.getWidth() / 3 + 200 && x <= panel.getWidth() / 3 + 300 && y >= panel.getHeight() / 3 + 50 && y <= panel.getHeight() / 3 + 250) {
    				flavour = Flavour.VANILLA;
    				sladoled = new Color(230, 223, 235);
    				panel.repaint();
    			}
    			else {
    				flavour = Flavour.NONE;
    				panel.repaint();
    			}
    			 
    		}

    		@Override
    		public void mousePressed(MouseEvent e) {}

    		@Override
    		public void mouseReleased(MouseEvent e) {}

    		@Override
    		public void mouseEntered(MouseEvent e) {}

    		@Override
    		public void mouseExited(MouseEvent e) {
    			
    		}});

        panel.setBackground(Color.WHITE);
        frame.add(panel);

        frame.setVisible(true);
    }
}

enum Flavour {
    NONE,
    CHOCOLATE,
    STRAWBERRY,
    VANILLA
}
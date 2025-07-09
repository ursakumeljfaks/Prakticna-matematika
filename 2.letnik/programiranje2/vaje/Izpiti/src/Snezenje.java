import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Snezenje {

   public static boolean sneg[][];

   public static void main(String[] args) throws InterruptedException {

      JFrame okno = new JFrame();
      okno.setTitle("Sneženje");
      okno.setResizable(false);
      okno.setSize(new Dimension(800, 600));
      okno.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

      @SuppressWarnings("serial")
      JPanel platno = new JPanel() {
         @Override
         protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.setColor(new Color(196, 211, 223));

            // izris snežink
            for (int i = 0; i < sneg.length; i++) {
            	for (int j = 0; j < sneg[0].length; j++) {
            		if (sneg[i][j]) {
            			g.fillRect(j, i, 1, 1);
            		}
            	}
            }
            //g.drawLine(0, (int)Math.round(0.5 * getHeight()), getWidth(), (int)Math.round(0.5 * getHeight()));
         }
      };

      platno.setBackground(Color.WHITE);
      okno.add(platno);
      okno.setVisible(true);

      sneg = new boolean[platno.getHeight()][platno.getWidth()];

      while (true) {

         // če sneži, dodamo snežinke na vrhu
         for (int j = 0; j < sneg[0].length; j++){
            sneg[0][j] = Math.random() < 0.25;
         }

         // snežinke, ki so v zraku, premaknemo vrstico nižje
         for (int i = sneg.length - 1; i > 0 ; i--){
            for (int j = 0; j < sneg[i].length - 1; j++){
            	if (!sneg[i][j] && sneg[i-1][j]) {
            		sneg[i][j] = true;
            		sneg[i-1][j] = false;
            	}
            }
         }

         platno.repaint();

         // če je snežna odeja dovolj debela, naj neha snežiti
         int voda = 0;
         for (int j = 0; j < sneg[0].length; j++){
            for (int i = sneg.length - 1; i >= 0; i--){
               if (sneg[i][j]){
                  voda++;
               }
               else{
                  break;
               }
            }
         }

         if (voda >= 0.5 * sneg.length * sneg[0].length){
            break;
         }
         // če se ni nič premaknilo, končaj simulacijo

         Thread.sleep(5);
      }
   }
}
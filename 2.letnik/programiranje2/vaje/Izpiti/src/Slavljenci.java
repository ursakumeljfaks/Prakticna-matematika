import java.io.*;

public class Slavljenci {

   public static void main(String[] args) throws IOException {
      int r = slavljenci("osebe.txt", "slavljenci.txt", 12, 1, 2018);
      System.out.println(r);
   }
   
   public static int slavljenci(String vhodna, String izhodna, int dan, int mesec, int leto) {
	   int steviloSlavljencev = 0;
	   
	   try {
           BufferedReader reader = new BufferedReader(new FileReader(vhodna));
           BufferedWriter writer = new BufferedWriter(new FileWriter(izhodna));
           String line;
           String vr = "";
           String datumRojstva = "";
           
           while ((line = reader.readLine()) != null) {
        	   
        	   if (vr.equals("")) {
                   vr = line;
               } else {
            	   datumRojstva = line;
            	   String[] splitana = line.split(".");
            	   int[] stevila = new int[splitana.length];
            	   for (int j = 0; j < splitana.length; j++) {
            	       stevila[j] = Integer.parseInt(splitana[j]);
            	   }
            	   if (stevila[0] == dan && stevila[1] == mesec) {
            		   int leta = leto - stevila[2];
            		   writer.write(vr + " " + String.format("%d", leto));
                	   writer.newLine();
                	   steviloSlavljencev++;
            	   }
            	   
            	   
               }
        	   
        	   vr = "";
        	   datumRojstva = "";
             
               }
           writer.flush();
           writer.close();
           reader.close();
          
           
           
       } catch (IOException e) {
           e.printStackTrace();
       }
	   
	   return steviloSlavljencev;
   }
}

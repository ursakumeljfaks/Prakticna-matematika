import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;

public class Premesaj {

   public static void main(String[] args) throws IOException {
      premesaj("vhod.txt", "izhod.txt");
   }
   public static void premesaj(String vhodna, String izhodna) {
	   try {
           BufferedReader reader = new BufferedReader(new FileReader(vhodna));
           BufferedWriter writer = new BufferedWriter(new FileWriter(izhodna));
           String line;
           String prejsnja = "";
           boolean aliLiha = true;
           
           
           while ((line = reader.readLine()) != null) {
        	   
        	   if (aliLiha) {
        		   prejsnja = line;
        		   aliLiha = false;
        	   }else {
        		   writer.write(line);
        		   writer.newLine();
        		   writer.write(prejsnja);
        		   writer.newLine();
        		   aliLiha = true;
        	   }

               }
           if (!aliLiha && prejsnja != null) {
               writer.write(prejsnja);
               writer.newLine();
           }
           writer.flush();
           writer.close();
           reader.close();
          
           
           
       } catch (IOException e) {
           e.printStackTrace();
       }
   }
}
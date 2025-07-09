import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;


public class Povprecja {

    public static void main(String[] args) throws IOException {
        povprecja("podatki.txt", "povprecja.txt");
    }

    public static void povprecja(String vhodna, String izhodna) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(vhodna));
            BufferedWriter writer = new BufferedWriter(new FileWriter(izhodna));
            String kraj = "";
            String line;
            while ((line = reader.readLine()) != null) {
                if (line.equals("")) {
                    continue;
                }
                if (kraj.equals("")) {
                    kraj = line;
                } else {
                    String[] meritev = line.split(" ");
                    if (meritev.length > 0) {
                        double vsota = 0;
                        for (String stevilo : meritev) {
                            vsota += Double.parseDouble(stevilo);
                        }
                        double povprecje = vsota / meritev.length;
                        writer.write(kraj + " " + String.format("%.2f", povprecje));
                        writer.newLine();
                    }
                    kraj = "";
                }
            }
            writer.flush();
            writer.close();
            reader.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}

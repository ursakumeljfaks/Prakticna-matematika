import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Locale;

public class Speeding {

	public static void main(String[] args) {
		try {
		    System.out.println(speeding("golovec.txt", "speeding.txt", 622, 80.0));
		} catch (IOException e) {
		e.printStackTrace();
		}
		
	}
	public static int speeding(String in, String out, int distance, double limit) throws IOException{
		int stej = 0;
		try {
		    BufferedReader reader = new BufferedReader(new FileReader(in));
		    BufferedWriter writer = new BufferedWriter(new FileWriter(out));
		    String line;
		    
		    while ((line = reader.readLine()) != null) {
		        String[] podatki = line.split(" ");
		        int zacetek = Integer.parseInt(podatki[0]);
		        int konec = Integer.parseInt(podatki[1]);
		        String registrska = podatki[2];
		        Drive ime = new Drive(zacetek, konec, distance, registrska);  
		        if (ime.getSpeed() > limit){
		        	writer.write(String.format(Locale.US, "%s %.02f\n", registrska, ime.getSpeed()));
		        	stej++;
		        }
		    	
	    }
		    
		    writer.flush(); 
		    writer.close();
		    reader.close();
		} catch (IOException e) {
		    e.printStackTrace();
		}
		return stej;
		
	}
}

class Drive{
	private int start;
	private int finish;
	private int distance;
	private String registration;
	
	public Drive(int start, int finish, int distance, String registration) {
		this.start = start;
		this.finish = finish;
		this.distance = distance;
		this.registration = registration;
		
	}
	
	public int getStart() {
		return start;
	}
	public int getFinish() {
		return finish;
	}
	public int getDistance() {
		return distance;
	}
	public String getRegistration(){
		return registration;
	}
	
	public double getSpeed() {
		return (double) distance / (finish - start) * 3.6;
	}
}
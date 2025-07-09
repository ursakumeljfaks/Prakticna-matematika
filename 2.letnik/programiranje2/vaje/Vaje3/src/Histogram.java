import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

public class Histogram {

	public static void main(String[] args) {
		List<Integer> numbers = null;
        try {
            write("numbers.txt");
            numbers = read("numbers.txt");
        }
        catch (IOException e) {
            e.printStackTrace();
            System.exit(0);
        }
        Histogram histogram = new Histogram(numbers);
        System.out.println(histogram);

	}
	static final int MAXIMUM = 123;
	
	public static void write(String file) throws IOException{
		try {
		    BufferedWriter writer = new BufferedWriter(new FileWriter(file));
		    Random random = new Random();
		    for (int j = 0; j < 1000; j++) {
		    	int nakljucno = random.nextInt(MAXIMUM);
		    	writer.write(String.format("%d", nakljucno));
		    	int stevilo = random.nextInt(4);
		    	for (int i = 0; i < stevilo; i++) {
		    		writer.write(String.format(" %d", nakljucno));
		    	}
		    	writer.write("\n");
		    }
		    writer.flush(); 
		    writer.close();
		} catch (IOException e) {
		    e.printStackTrace();
		}
	}
	public static List<Integer> read(String file) throws IOException {
		List<Integer> stevila = new ArrayList<>();
		try {
			BufferedReader reader = new BufferedReader(new FileReader(file));
		    String line;
		    while ((line = reader.readLine()) != null) {
		    	String[] stevilaString = line.split(" ");
		    	for (String st: stevilaString) {
		    		stevila.add(Integer.valueOf(st));
		    	}
		    }
		    reader.close();
		    
		} catch (IOException e) {
		    e.printStackTrace();
		}
		return stevila;
	}
	
    @Override
    public String toString() {
        String string = "";
        for (int i = 0; i < histogram.length; i++)
            string += (i > 0 ? "\n" : "") + String.format("%10s %3d - %4.1f%%", "[" + i * interval + "," + Math.min(maximum, (i + 1) * interval)+ "):", histogram[i], 100.0 * histogram[i] / size);
        return string;
    }

	private int size;
	private int interval;
	private int maximum;
	private int[] histogram;
	
	public Histogram(List<Integer> numbers, int interval, int maximum) {
        this.size = numbers.size();
        this.interval = interval;
        this.maximum = maximum;
		if ((maximum/interval)*interval != maximum) {
			histogram = new int[maximum/interval+1];
		}
		else {
			histogram = new int[maximum/interval];
		}
		for (int i=1; i < maximum; i++) {
			histogram[i/interval] += Collections.frequency(numbers, i);
		}
    }

	public Histogram(List<Integer> numbers) {
		size = numbers.size();
		interval = 12;
		maximum = MAXIMUM;
		if ((maximum/interval)*interval != maximum) {
			histogram = new int[maximum/interval+1];
		}
		else {
			histogram = new int[maximum/interval];
		}
		for (int i=1; i < maximum; i++) {
			histogram[i/interval] += Collections.frequency(numbers, i);
		}
	}
	
	public int getSize() {
        return size;
    }

    public int getInterval() {
        return interval;
    }

    public int getMaximum() {
        return maximum;
    }

    public int[] getHistogram() {
        return histogram;
    }
    
}


public class Vlak {

	public static void main(String[] args) {
		vlak(10, 35, 14, 5);

	}
	
	public static void vlak(int odhod_h, int odhod_min, int prihod_h, int prihod_min) {
		System.out.format("Odhod: %d:%02d\n", odhod_h, odhod_min);
		System.out.format("Prihod: %d:%02d\n", prihod_h, prihod_min);
		int odhod = 60 * odhod_h + odhod_min;
		int prihod = 60 * prihod_h + prihod_min;
		int trajanje = prihod - odhod;
		int trajanje_h = trajanje / 60;
		int trajanje_min = trajanje % 60;
		System.out.format("Trajanje: %d:%02d", trajanje_h, trajanje_min);
	}
}

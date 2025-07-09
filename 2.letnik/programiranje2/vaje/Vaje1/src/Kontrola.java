
public class Kontrola {
	
	public static void main(String[] args) {
        kontrola(265195368523L);
	}
	public static void kontrola(long stevilo) {
		long koncno = 0;
		long st2 = stevilo;
		for (int i = 0; i < 12; i++) {
			long stevka = (st2 % 10) * (i+2);
			st2 /= 10;			
			koncno += stevka;
		}
		long ostanek = 11 - (koncno % 11);
		long rez = ostanek;
		if (ostanek == 11) {
			rez = 0;
		}
		String sklic = String.valueOf(stevilo) + String.valueOf(rez);
		long sklicC = Long.parseLong(sklic);
		System.out.format("Število %d ima kontrolno števko %d, torej je sklic enak %d", stevilo, rez, sklicC);
	}
}

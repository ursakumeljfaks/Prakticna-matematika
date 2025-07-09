
public class Pretvorba {

	public static void main(String[] args) {
		pretvorba(524.7);

	}
	public static void pretvorba(double yard) {
		double stevila = yard * 0.9144;
		int m = (int) stevila;
		int dm = (int) (stevila * 10 - m*10);
		int cm = (int) (stevila * 100 - m*100 - dm*10);
		System.out.format("%.1f yardov = %d m %d dm %d cm",yard, m, dm, cm);
	}
}

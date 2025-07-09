
public class Kot {

	public static void main(String[] args) {
		kot(7, 5);

	}
	public static void kot(int h, int min) {
		double kot_min = ((360/60) * min);
		double kot_h = ((min/2.0) + (360/12 * h));
		double vmesni_kot = Math.abs(kot_h - kot_min);
		double pravi_kot = Math.min(vmesni_kot, (360-vmesni_kot));
		int stopinje = (int) pravi_kot;
		int minute = (int) ((pravi_kot*10%10)*6);
		System.out.format("Ob %d:%02d je kot med kazalcema enak %d stopinj in %d minut", h, min, stopinje, minute);
	}
}

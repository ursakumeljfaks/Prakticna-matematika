public class Juice extends Drink{
	public Juice() {
		super(1.5, 0);
		
	}
	@Override
	public void print() {
		System.out.println("Juice(" + getVolume() + "L, " + getAlcohol() + "%)");
	}
}
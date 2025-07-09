public class Beer extends Drink{
	public Beer() {
		super(0.5, 5);
	}
	@Override
	public void print() {
		System.out.println("Beer(" + getVolume() + "L, " + getAlcohol() + "%)");
	}
}
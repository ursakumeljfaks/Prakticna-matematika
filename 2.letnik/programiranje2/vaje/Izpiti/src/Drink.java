public class Drink implements Printable {
	
	public static void main(String[] args) {
		Drink beer = new Beer();
		beer.print();
		Drink juice = new Juice();
		juice.print();
		Drink voda = new Drink(0.5,0);
		voda.print();
		
	}

	private double volume;
	private int alcohol;
	
	public Drink(double volume, int alcohol){
		super();
		this.volume = volume;
		this.alcohol = alcohol;	
	}
	public double getVolume() {
		return volume;
	}
	public int getAlcohol() {
		return alcohol;
	}
	public void setVolume(double vr) {
		this.volume = vr;
	}
	public void setAlcohol(int vr) {
		this.alcohol = vr;
	}
	@Override
	public void print() {
		System.out.println("Drink(" + getVolume() + "L, " + getAlcohol() + "%)");
	}
}

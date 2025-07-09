
public class Bicycle extends Vehicle{
	public Bicycle(String owner) {
		super(owner, 1, 20);
		
	}
	@Override
	public void print() {
		System.out.println("Bicycle(" + getOwner() + ", " + getPersons() + " person(s), " +  getSpeed() + "km/h)");
	}	
		
}


public class Car extends Vehicle{
	public Car(String owner) {
		super(owner, 5, 240);
	}
	@Override
	public void print() {
		System.out.println("Car(" + getOwner() + ", " + getPersons() + " person(s), " +  getSpeed() + "km/h)");
	}	
		
}

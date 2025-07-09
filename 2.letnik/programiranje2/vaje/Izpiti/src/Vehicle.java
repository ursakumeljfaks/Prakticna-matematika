
public class Vehicle implements Printable {
	
	public static void main(String[] args) {
		  Vehicle bicycle = new Bicycle("Jaša"); 
		  bicycle.print();
		  Vehicle car = new Car("Janez"); 
		  car.print();
	}
	
	private String owner;
	private int persons;
	private double speed;
	
	public Vehicle(String owner, int persons, double speed) {
		super();
		this.owner = owner;
		this.persons = persons;
		this.speed = speed;
	}
	
	public String getOwner() {
		return owner;
	}
	public int getPersons() {
		return persons;
	}
	public double getSpeed(){
		return speed;
	}
	
	@Override
	public void print() {
		System.out.println("Vehicle(" + getOwner() + ", " + getPersons() + " person(s), " +  getSpeed() + "km/h)");
	}	
		
}

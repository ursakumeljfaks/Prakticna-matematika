
public class Sport {

	public static void main(String[] args) {
		Sport football = new Football();
		System.out.println(football);
		Sport darts = new Darts();
		System.out.println(darts); 
		System.out.println(football.equals(darts));

	}
	
	private String name;
	private int players;
	private boolean ball = true;
	
	public Sport(String name, int players, boolean ball) {
		super();
		this.name = name;
		this.players = players;
		this.ball = ball;
	}
	
	public String getName() {
		return name;
	}
	public int getPlayers() {
		return players;
	}
	public boolean getBall(){
		return ball;
	}
	
	@Override
	  public String toString() {
		if (getBall() == true){
			return getName() + "(" + getPlayers() + " player(s), w/ ball)";
		}
	    return getName() + "(" + getPlayers() + " player(s), w/o ball)";
	  }	
	
	@Override
	  public boolean equals(Object object) {
	    return getPlayers() == ((Sport)object).getPlayers() && getBall() == ((Sport)object).getBall();
	  }

}

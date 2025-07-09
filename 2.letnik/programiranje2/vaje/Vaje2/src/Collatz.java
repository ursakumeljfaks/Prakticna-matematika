
public class Collatz {

	public static void main(String[] args) {
		for (int number: new int[] { 6, 12, 19, 27, 871 }) {
		    System.out.format("Number: %,d\n", number);
		    System.out.format("Length: %,d\n", length(number));
		    System.out.format("Maximum: %,d\n", maximum(number));
		    System.out.print("Sequence: ");
		    sequence(number);
		    System.out.println();
		}

	}
	public static void sequence(int number) {
		System.out.format("%d ", number);
		while (number != 1) {
			if (number % 2 == 0) {
				number = number / 2;
				System.out.format("%d ", number);
			}
			else {
				number = number * 3 + 1;
				System.out.format("%d ", number);
			}
		}
		System.out.println();
	}
	public static int length(int number) {
		int i = 0;
		while (number != 1) {
			if (number % 2 == 0) {
				number = number / 2;
				i += 1;
			}
			else {
				number = number * 3 + 1;
				i += 1;
			}
		}
		return i;
	}
	public static int maximum(int number) {
		int maksimum = number;
		while (number != 1) {
			if (number % 2 == 0) {
				number = number / 2;
				if (number > maksimum) {
					maksimum = number;
				}
			}
			else {
				number = number * 3 + 1;
				if (number > maksimum) {
					maksimum = number;
				}
			}
		}
		return maksimum;
	}
}


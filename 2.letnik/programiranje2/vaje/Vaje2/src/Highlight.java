
public class Highlight {

	public static void main(String[] args) {
		System.out.println(highlight("Poudarjena *beseda* in nepoudarjena beseda."));
		System.out.println(highlight("Poudarjeno *besedilo, ki se nadaljuje..."));
		System.out.println(highlight("Poudarjeno *besedilo*, ki se ne nadaljuje."));
		System.out.println(highlight("*g*it repozitorija *g*ithub in *b*it*b*ucket."));
		final String ALPHABET = "abcčdefghijklmnoprsštuvzž., ";
		String random = "";
		for (int i = 0; i < 40; i++ ) {
			if (Math.random() < 0.1) {
		        random += "*";
			}
			else {
		        random += ALPHABET.charAt((int)(Math.random() * ALPHABET.length()));
			}
		}
		System.out.println(highlight(random));

	}
	
	public static String highlight(String string) {
		String newString = "";
		int zvezdica = 0;
		for (int i = 0; i < string.length(); i++) {
			if (string.charAt(i) == '*'){
				zvezdica += 1;
				continue;
			}
			if (zvezdica % 2 == 1){
				newString += Character.toUpperCase(string.charAt(i));
			}
			else {
				newString += string.charAt(i);
			}
		}
		return newString;
	}
	
}

import java.util.HashMap;
import java.util.Map;

public class Factorization {

	public static void main(String[] args) {
		factorization(5);
		factorization(16);
		factorization(43);
		factorization(99);
		factorization(1025);
		factorization(4382);
		factorization(74438);
		factorization(578298);
		factorization(5761665);

	}

	public static int divisor(int number) {
		int i = 2;
		while (number % i != 0) {
			i += 1;
		}
		return i;
	}
	
	public static Map<Integer, Integer> factorize(int number){
		Map<Integer, Integer> factors = new HashMap<Integer, Integer>();
		while (number > 1){
			int delitelj = divisor(number);
			if (factors.containsKey(delitelj)){
				factors.put(delitelj, factors.get(delitelj)+1);
			}
			else {
				factors.put(delitelj, 1);
			}
			number /= delitelj;
		}
		return factors;
	}
	
	public static void factorization(int number) {
		Map<Integer, Integer> prafaktorji = factorize(number);
		System.out.print(number + " = ");
		StringBuilder niz = new StringBuilder();
		for (int prafaktor: prafaktorji.keySet()) {
			int eksponent = prafaktorji.get(prafaktor);
			if (niz.length() > 0) {
	            niz.append(" * ");
	        }
			if (eksponent == 1) {
				niz.append(prafaktor);
			}
			else {
				niz.append(prafaktor).append("^").append(eksponent);
			}
		}
		System.out.println(niz.toString());
	}
}

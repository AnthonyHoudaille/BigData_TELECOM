import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
/* This comparator permit us to sort the created HashMap by the first letter of the key*/
public class ValueComparator2 implements Comparator<String> {
	
	public int count = 0;
	HashMap<String, Integer> letterMap = new HashMap<String, Integer>();
	HashMap<String, Integer> letterMap2 = new HashMap<String, Integer>();
	Map<String, Integer> base;
	String letter ="a b c d e f g h i j k l m n o p q r s t u v w x y z";
	//Creation of the HashMap for sort the first letter of the key
	public HashMap<String, Integer> letMap(){
		for (String let : letter.split(" ")) {
			count++;
			letterMap.put(let, count);
		}
		return letterMap; // letterMap = (a=1, b=2, c=3, ..., z= 26)
	}
	//Constructor
	public ValueComparator2(Map<String, Integer> base){
		this.base = base;}

	// Method to complete the comparasion 
	public String test(String a, String b) {
		String result = null;
		String atronc = a.substring(0,1);
		String btronc = b.substring(0,1);
		String atronc2 = a.substring(1,1);
		String btronc2 = b.substring(1,1);
		
		int let1 = letterMap.get(atronc);
		int let2 = letterMap.get(btronc);
		int let3 = letterMap.get(atronc2);
		int let4 = letterMap.get(btronc2);
		
		if ( let1 > let2) {		//the problem is that i'm doing a test on Integer !
			result = "up";
		}else if(let1 == let2) {
			if(let3>=let4) {
				result = "up";
			}else {
				result = "down";
			}
		}else {
			result = "down";
		}
		return result;
		
	}
	// Method to compare
	public int compare(String a, String b){
		letterMap2 = letMap();
		String result =null;
		if (base.get(a) > base.get(b)) {
			return -1;
		} else if(base.get(a) == base.get(b)) {
			System.out.println(letterMap);
			result = test(a,b);
			if (result == "up") {
				return 1;
			}else {
				return -1;
			}
		}else {
			return 1;
		}

	}



	
}
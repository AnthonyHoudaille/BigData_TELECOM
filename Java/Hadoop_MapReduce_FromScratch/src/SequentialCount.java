import java.util.Comparator;
import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;



public class SequentialCount {
	
	public static Map<String, Integer> count(String a)
	{
		//Creation of the first countWord HashMap
		HashMap<String, Integer> hMap = new HashMap<String, Integer>();
		ValueComparator comparateur = new ValueComparator(hMap);
		TreeMap<String,Integer> mapSorted = new TreeMap<String,Integer>(comparateur);
		
		for (String word : a.split(" ") ) {
			if (hMap.containsKey(word)) {
				hMap.put(word, hMap.get(word)+1);
				
			} else {
				hMap.put(word,  1);
			}
		}
		//Creation of the sorted HashMap
		mapSorted.putAll(hMap);
		
		
	   
		return (mapSorted);
	}
	
	
	public static class ValueComparator implements Comparator<String> {
		
		public int count = 0;
		HashMap<String, Integer> letterMap = new HashMap<String, Integer>();
		Map<String, Integer> base;
		
		public ValueComparator(Map<String, Integer> base){
			this.base = base;}

		public int compare(String a, String b){
			if (base.get(a) > base.get(b)) {
				return -1;
			} else if(base.get(a) == base.get(b)) {
				String letter ="a b c d e f g h i j k l m n o p q r s t u v w x y z";
				for (String let : letter.split(" ")) {
					count++;
					letterMap.put(let, count);
				}
				int let1 = letterMap.get(a);
				int let2 = letterMap.get(b);
				if ( let1 >= let2) {
					System.out.println(letterMap);
					return 1;
					
				}else {
					return - 1;
				}
			}else {
				return 1;
			}
		
	}
	
		
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String listS = "bear lol hehe jule hehe lol jule lol bear";
        System.out.println(count(listS));
	}
}


import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;



public class SequentialCount {
	
	public static Map<String, Integer> count(String a)
	{
		//Creation of the first countWord HashMap
		HashMap<String, Integer> hMap = new HashMap<String, Integer>();
		ValueComparator comparateur = new ValueComparator(hMap);
		TreeMap<String,Integer> mapSortedbyVal = new TreeMap<String,Integer>(comparateur);
		ValueComparator2 comparateur2 = new ValueComparator2(hMap);
		TreeMap<String,Integer> mapSortedbyLet = new TreeMap<String,Integer>(comparateur2);
		
		for (String word : a.split(" ") ) {
			if (hMap.containsKey(word)) {
				hMap.put(word, hMap.get(word)+1);
				
			} else {
				hMap.put(word,  1);
			}
		}
		//Creation of the sorted HashMap
		mapSortedbyVal.putAll(hMap);
		mapSortedbyLet.putAll(mapSortedbyVal);
		
	   
		return (mapSortedbyVal);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String listS = "bear lol hehe jule hehe lol jule lol bear";
        System.out.println(count(listS));
	}
}

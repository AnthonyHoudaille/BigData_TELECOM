import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;




public class SequentialCount {
	
	public static final Set<String> VALUES = new HashSet<String>();
	
	public static void count(String a) throws IOException 
	{
		
		//Creation of the first countWord HashMap
		HashMap<String, Integer> hMap = new HashMap<String, Integer>();
		
		long startTime = System.currentTimeMillis();
		
		FileReader in = new FileReader(a);
        
        // Reads text from input, buffering characters to provide  efficient reading of characters, arrays, and lines.
        BufferedReader br = new BufferedReader(in);
        String Line;
        while ((Line = br.readLine()) != null) {
			for (String word : Line.replace("\n", " ").split(" ") ) {
				String wordLower= word.toLowerCase();
				boolean contains = VALUES.contains(wordLower);
				
				if (!contains) {
					if(!hMap.containsKey(wordLower)) {
						hMap.put(wordLower,  1);
					} else {
						hMap.put(wordLower, hMap.get(wordLower)+1);
					}
				}
					
			}
        }
        in.close();
        
		//Creation of the sorted HashMap
		
		
		List<Map.Entry<String, Integer>> list = new ArrayList<Map.Entry<String, Integer>>(hMap.entrySet());
		long startTime2 = System.currentTimeMillis();
		// Sort and apply the Double Comparator class above
		Collections.sort(list, new DoubleComparator<String, Integer>());
		long endTime2  = System.currentTimeMillis();
		
		for (int i = 0; i < list.size(); i++){ 
	        System.out.println(list.get(i).getKey() + " " + list.get(i).getValue());
		}
		long endTime   = System.currentTimeMillis();
		long totalTime = endTime - startTime;
		long totalTime2 = endTime2 - startTime2;
		System.out.println(" ");
		System.out.println("Total computation time is " + totalTime + "ms");
		System.out.println("Computation time for sorting is " + totalTime2 + "ms");
		
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String listS = "/home/anthony/Bureau/MS_BIG_DATA/Reste/ArticlePolice.txt";
		count(listS);
		
        
        
	}
}


// Display results
class DoubleComparator<K extends Comparable<? super K>, V extends Comparable<? super V>> implements Comparator<Map.Entry<K, V>> {

// Compare two map entries
public int compare(Map.Entry<K, V> a, Map.Entry<K, V> b) {
      
       // First, we sort by Value
       int cmp1 = b.getValue().compareTo(a.getValue());
       if (cmp1 != 0) {
              return cmp1;
       } else {
              // If values are equal, we sort by keys
              return a.getKey().compareTo(b.getKey());
       }
}
}

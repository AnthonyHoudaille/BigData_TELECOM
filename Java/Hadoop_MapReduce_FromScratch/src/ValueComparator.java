import java.util.Comparator;
import java.util.Map;
/* This comparator permit us to sort the HashMap by decreasing value*/

public class ValueComparator implements Comparator<String> {
			Map<String, Integer> base;
			
			public ValueComparator(Map<String, Integer> base){
				this.base = base;}
	
			public int compare(String a, String b){
				if (base.get(a) >= base.get(b)) {
					return -1;
				}else {
					return 1;
				}
		
	}
			
}


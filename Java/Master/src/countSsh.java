import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;

public class countSsh {
	
	 public static void main(String[] args) throws InterruptedException, IOException{
	        //int a;

	        /*a = 5 + 3;
	        Thread.sleep(10000);
	        System.out.println(a);
	        */
	        HashMap<String, Integer> hMap = new HashMap<String, Integer>();
	        String FiletoRead = "/tmp/AnthoH/Splits/S"+args[0]+".txt";
	        FileReader in = new FileReader(FiletoRead);
	        String FileName = "/tmp/AnthoH/Map/UM"+args[0]+".txt";
	        PrintWriter writer = new PrintWriter(FileName);
	        BufferedReader br = new BufferedReader(in);
	        
	        String Line;
	        while ((Line = br.readLine()) != null) {
				for (String word : Line.replace("\n", " ").split(" ") ) {
					String wordLower= word.toLowerCase();
					hMap.put(wordLower,  1);
					writer.println(wordLower+ " 1");
				}
	        }
	        writer.close();
	        in.close();
	       
	    }
}

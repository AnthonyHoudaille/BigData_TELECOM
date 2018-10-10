import java.io.*;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.concurrent.TimeUnit;

public class master {
	
	private static void readOutput(Process p) throws IOException, InterruptedException{
		// TODO Auto-generated method stub
		InputStream is = p.getInputStream();
		InputStream is2 = p.getErrorStream();
		
		InputStreamReader isr = new InputStreamReader(is , StandardCharsets.UTF_8);
		InputStreamReader isr2 = new InputStreamReader(is2);
		
		BufferedReader br2 = new BufferedReader(isr2);
		BufferedReader br = new BufferedReader(isr);
		
		String line;
		
		boolean b = p.waitFor(3, TimeUnit.SECONDS);
		
		while (((line = br.readLine()) != null)){
			System.out.println(line);
		
		}
	}
	
	
	public static void main(String[] args) throws IOException, InterruptedException {

		ProcessBuilder pb = new ProcessBuilder("java","-jar","/tmp/AnthoH/Slave.jar");
		ProcessBuilder pb2 = new ProcessBuilder("ls", "/jesuisunhero");
        
		Process p = pb.start();
		Process p2 = pb2.start();
		
		
		
		
		readOutput(p);
		
	}
	
}

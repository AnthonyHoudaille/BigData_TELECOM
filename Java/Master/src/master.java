import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.List;
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
		
		if (b==false) {
	
			while (((line = br.readLine()) != null)){
				System.out.println(line);
			}
			while (((line = br2.readLine()) != null)){
				System.out.println(line);
			}
		}
	}
	
	
	public static void main(String[] args) throws IOException, InterruptedException {
		String path = "Computer.txt";
		FileReader computers = new FileReader(path);
		BufferedReader br = new BufferedReader(computers);
		
		String computer;
		
		while ((computer = br.readLine()) != null){
			//ProcessBuilder pb = new ProcessBuilder("ssh", "ahoudaille@"+computer, "java","-jar","/tmp/AnthoH/Slave.jar");
			ProcessBuilder pb2 = new ProcessBuilder("ssh", "ahoudaille@" + computer, "mkdir -p /tmp/AnthoH/Splits");
			Process p2 = pb2.start();
			ProcessBuilder pb6 = new ProcessBuilder("ssh", "ahoudaille@" + computer, "mkdir -p /tmp/AnthoH/Map");
			Process p6 = pb6.start();
			Thread.sleep(3000);
			
			ProcessBuilder pb3 = new ProcessBuilder("scp", "/tmp/AnthoH/Splits/S0.txt" , "ahoudaille@"+computer+":/tmp/AnthoH/Splits/S0.txt");
			Process p3 = pb3.start();
			ProcessBuilder pb4 = new ProcessBuilder("scp", "/tmp/AnthoH/Splits/S1.txt" , "ahoudaille@"+computer+":/tmp/AnthoH/Splits/S1.txt");
			Process p4 = pb4.start();
			ProcessBuilder pb5 = new ProcessBuilder("scp", "/tmp/AnthoH/Splits/S2.txt" , "ahoudaille@"+computer+":/tmp/AnthoH/Splits/S2.txt");
			Process p5 = pb5.start();
			Thread.sleep(3000);
			
			ProcessBuilder pb7 = new ProcessBuilder("ssh", "ahoudaille@"+computer, "java","-jar","/tmp/AnthoH/Slave.jar 0");
			Process p7 = pb7.start();
			ProcessBuilder pb8 = new ProcessBuilder("ssh", "ahoudaille@"+computer, "java","-jar","/tmp/AnthoH/Slave.jar 1");
			Process p8 = pb8.start();
			ProcessBuilder pb9 = new ProcessBuilder("ssh", "ahoudaille@"+computer, "java","-jar","/tmp/AnthoH/Slave.jar 2");
			Process p9 = pb9.start();
			Thread.sleep(3000);
			
			//Process p = pb.start();
			ProcessBuilder pb = new ProcessBuilder("ssh", "ahoudaille@" + computer, "hostname");
			Process p = pb.start();
			readOutput(p);
			readOutput(p7);
			readOutput(p8);
		}
		
		
		
		
		
		
	}
	
}

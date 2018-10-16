import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;


public class deploy {
	
		private static void testSSH(String a) throws IOException, InterruptedException {
			// TODO Auto-generated method stub
			FileReader computers = new FileReader(a);
			BufferedReader br = new BufferedReader(computers);
			
			String computer;
			
			while ((computer = br.readLine()) != null){
				ProcessBuilder pb = new ProcessBuilder("ssh", "ahoudaille@" + computer, "hostname");
				Process p = pb.start();
				
				List<BufferedReader> ISR = Buffering(p);
				
				
				String line;
				while (((line = ISR.get(0).readLine()) != null)){
					ProcessBuilder pb2 = new ProcessBuilder("ssh", "ahoudaille@" + computer, "mkdir -p /tmp/AnthoH");
					Process p2 = pb2.start();
					List<BufferedReader> ISR2 = Buffering(p2);
					Thread.sleep(3000);
					ProcessBuilder pb3 = new ProcessBuilder("scp -r", "/tmp/AnthoH/Slave.jar" , "ahoudaille@"+computer+":/tmp/AnthoH/");
					Process p3 = pb2.start();
					
					System.out.println(line);
				}
				while (((line = ISR.get(1).readLine()) != null)){
					System.out.println(line);
					
				}
			
			}
		}
		
		private static List<BufferedReader> Buffering(Process p) {
			
			InputStream is = p.getInputStream();
			InputStream is2 = p.getErrorStream();
			
			InputStreamReader isr = new InputStreamReader(is , StandardCharsets.UTF_8);
			InputStreamReader isr2 = new InputStreamReader(is2, StandardCharsets.UTF_8);
			
			BufferedReader br2 = new BufferedReader(isr2);
			BufferedReader br1 = new BufferedReader(isr);
			List l = new ArrayList();
			l.add(br1);
			l.add(br2);

			// TODO Auto-generated method stub
			return l;
		}
		
		public static void main(String[] args) throws IOException, InterruptedException {
			//String path = "/tmp/AnthoH/Computer.txt"; // pour pc linux TPT
			String path = "Computer.txt"; // Sur mon mac
			testSSH(path);
		}
}

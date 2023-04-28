package arduinodata;
import java.security.Timestamp;
import java.util.*;
public class ArduinoData {
    
    String arduinoName = "noname";
    String MACAddress = "nomac";
    boolean isShutdown = false;
    int[] energyData = new int[100];
    // Map <String,Integer> energyData = new HashMap<String, Integer>();

   public ArduinoData(String name,String mac, boolean shutdown, int energyData){
        this.arduinoName = name;
        this.MACAddress = mac;
        this.isShutdown = shutdown;
        // Date date = new Date();
        this.energyData[0] = energyData;
        // Timestamp time = new Timestamp(date, null);
        // this.energyData.put(time.toString(), energyData);
    }

    public void addData(int energyData){
        this.energyData[0] = energyData;
        // Date date = new Date();
        // Timestamp time = new Timestamp(date, null);
        // this.energyData.put(time.toString(), energyData);
    }
    public String getArduinoName(){
        return this.arduinoName;
    }
}


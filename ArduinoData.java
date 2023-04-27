import java.io.*;
import java.security.Timestamp;
import java.util.*;
public class ArduinoData {
    
    String arduinoName = "";
    String MACAddress = "";
    boolean isShutdown = false;
    Map <String,Integer> energyData = new HashMap<String, Integer>();

   public ArduinoData(String name,String mac, boolean shutdown, int energyData){
        this.arduinoName = name;
        this.MACAddress = mac;
        this.isShutdown = shutdown;
        Timestamp time = new Timestamp(null, null);
        this.energyData.put(time.toString(), energyData);
    }

    public void addData(int energyData){
        Timestamp time = new Timestamp(null, null);
        this.energyData.put(time.toString(), energyData);
    }
}

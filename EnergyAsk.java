import java.net.*;
import java.nio.charset.Charset;

import javax.xml.catalog.Catalog;

import java.io.*;
import java.nio.charset.*;

import arduinodata.ArduinoData;



// import tcpclient.TCPClient;
public class EnergyAsk {

    ArduinoData[] arduinos = new ArduinoData[10];
    int arduinoCount = 0;
    public static void main( String[] args) throws Exception{
        EnergyAsk server = new EnergyAsk();

        int port = Integer.parseInt(args[0]);
        // System.out.println(args[0]);
        
        ServerSocket askServerSocket = new ServerSocket(port);
        // 

        int bufferSize = 1024;
        
        int readByte = 0;  
        
        ArduinoData myArduino;

        ByteArrayOutputStream recvData;
        ByteArrayInputStream outData;
        String clientRecv;
        while(true){
            Socket connectionAsk = askServerSocket.accept();
            connectionAsk.setTrafficClass(0x04);
            connectionAsk.setTcpNoDelay(false);
            System.out.println("Socket accept: " + String.valueOf(connectionAsk.getTrafficClass()));
         

            recvData = new ByteArrayOutputStream();
            byte[] readSomeBytes = new byte[bufferSize];

            // while(readByte != -1){
                readByte = connectionAsk.getInputStream().read(readSomeBytes);
                System.out.println(readByte);
                if(readByte != -1 ){
                    recvData.write(readSomeBytes, 0, readByte);
                }
                connectionAsk.shutdownInput();
                // }
                String serverInput = new String(readSomeBytes);
                System.out.println(readSomeBytes.toString());
             
                // String[] clientData = datasplit(recvData.toString());
                // String serverInput = recvData.toString();
                // for(int i = 0; i < clientData.length; i++){
                //     System.out.println(clientData[i]);
                //     if(server.getArduinoCount() > 0){
                        
                //         for(int j = 0; j < server.arduinos.length; j++){
                //             if(server.arduinos[i].getArduinoName() == clientData[0]){
                //                 server.arduinos[i].addData(1);
                //             }
                            
                //         }
                //     }
                //     else
                //     server.arduinos[0] = new ArduinoData(clientData[0], clientData[1], false, 10);
                // }

                // recvData.flush();
                // recvData.close();
                // connectionAsk.setKeepAlive(true);
                // System.out.println(serverInput);
                // connectionAsk.shutdownInput();
                Charset charset = Charset.forName("UTF-8");
                // Socket returnData = new Socket(connectionAsk.getInetAddress(), connectionAsk.getPort());
                // returnData.getOutputStream().write("hello".getBytes());
                
                for(int i = 0; i < readSomeBytes.length; i++){
                }
                    // connectionAsk.getOutputStream().wait(100);
                    connectionAsk.getOutputStream().write("hello".getBytes(charset));
                
                readByte = 0;
                Boolean badResponse = false;
                
                
                byte[] clientResponse;


            // returnData.close();
                
            connectionAsk.getOutputStream().flush();
            connectionAsk.close();

        }//end while
        // askServerSocket.close();
    } //main
    public int getArduinoCount(){
        return this.arduinoCount;
    }
    public static String[] datasplit(String clientData)
    {
        String[] Data;
        Data = clientData.split("\\?");

        return Data;
    }

} 
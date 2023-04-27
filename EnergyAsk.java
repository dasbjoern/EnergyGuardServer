import java.net.*;

import javax.xml.catalog.Catalog;

import java.io.*;




// import tcpclient.TCPClient;
public class EnergyAsk {
    public static void main( String[] args) throws Exception{
        int port = Integer.parseInt(args[0]);
        // System.out.println(args[0]);

        ServerSocket askServerSocket = new ServerSocket(port);
        // 

        int bufferSize = 1024;
        
        int readByte = 0;    
        ByteArrayOutputStream recvData;
        String clientRecv;
        while(true){
            Socket connectionAsk = askServerSocket.accept();
            System.out.println("Socket accept");
         

            recvData = new ByteArrayOutputStream();
            byte[] readSomeBytes = new byte[bufferSize];

            // while(readByte != -1){
                readByte = connectionAsk.getInputStream().read(readSomeBytes);
                if(readByte != -1 ){
                    recvData.write(readSomeBytes, 0, readByte);
                }
                // }
                String[] clientData = datasplit(recvData.toString());
                String serverInput = recvData.toString();
                for(int i = 0; i < clientData.length; i++)
                System.out.println(clientData[i]);
                // System.out.println(serverInput);

                connectionAsk.getOutputStream().write(recvData.toByteArray());
                readByte = 0;
                Boolean badResponse = false;
                
                
                byte[] clientResponse;


                
            // connectionAsk.getOutputStream().flush();
            connectionAsk.close();

        }//end while
        // askServerSocket.close();
    } //main
    public static String[] datasplit(String clientData)
    {
        String[] Data;
        Data = clientData.split("?");

        return Data;
    }

} 
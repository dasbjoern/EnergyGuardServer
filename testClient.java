import java.net.*;

import javax.xml.catalog.Catalog;

import java.io.*;

public class testClient {
    public static void main( String[] args) throws Exception{
        String data = args[0];
        // System.out.println(args[0]);

        Socket clientSocket = new Socket("192.168.137.200", 8888);
        // 
        
        int bufferSize = 1024;
        
        int readByte = 0;    
        
        clientSocket.getOutputStream().write(data.getBytes());

            System.out.println("Socket accept");
            ByteArrayOutputStream recvData = new ByteArrayOutputStream();
            byte[] readSomeBytes = new byte[bufferSize];

            while(readByte != -1){

                readByte = clientSocket.getInputStream().read(readSomeBytes);
                if(readByte != -1 ){
                    recvData.write(readSomeBytes, 0, readByte);
                }

            }

                String serverInput = new String(readSomeBytes);
                System.out.println(serverInput);
                // System.out.println(serverInput);

               
                readByte = 0;
                Boolean badResponse = false;
                
                
                byte[] clientResponse;


        
                // clientSocket.getOutputStream().flush();
                clientSocket.close();

        }//e
        //
    } //


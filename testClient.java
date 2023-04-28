import java.net.*;

import java.io.*;
import javax.xml.catalog.Catalog;

import java.nio.charset.*;
public class testClient {
    public static void main( String[] args) throws Exception{
        // System.out.println(args[0]);
        int count = 0;
        String data = args[0]+"\0";
        while(true){
            Thread.sleep(1000);
        Socket clientSocket = new Socket("192.168.137.165", 8888);
        // 
        
        int bufferSize = 1024;

            int readByte = 0;    
        Charset charset = Charset.forName("UTF-8");
        clientSocket.getOutputStream().write((String.valueOf(count) + ":".concat(data)).getBytes(charset));
        count++;
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

            }
        }//e
        //
    } //


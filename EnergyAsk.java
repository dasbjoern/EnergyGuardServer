import java.net.*;

import javax.xml.catalog.Catalog;

import java.io.*;
import tcpclient.TCPClient;
public class EnergyAsk {
    public static void main( String[] args) throws Exception{
        int port = Integer.parseInt(args[0]);
        // System.out.println(args[0]);

        ServerSocket askServerSocket = new ServerSocket(port);
        // 
        
        int bufferSize = 1024;
        
        int readByte = 0;
        String response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n";
        String htmlS = "<html>\r\n<body>\r\n<h1>\r\n";
        String htmlE = "</h1>\r\n</body>\r\n</html>\r\n\r\n";
      
        

        while(true){
            Socket connectionAsk = askServerSocket.accept();
            System.out.println("Socket accept");
            ByteArrayOutputStream recvData = new ByteArrayOutputStream();
            byte[] readSomeBytes = new byte[bufferSize];

                readByte = connectionAsk.getInputStream().read(readSomeBytes);
                if(readByte != -1 ){
                    recvData.write(readSomeBytes, 0, readByte);
                }

                String serverInput = new String(readSomeBytes);
                System.out.println(serverInput);
                // System.out.println(serverInput);

                connectionAsk.getOutputStream().write("hello".getBytes());
                readByte = 0;
                Boolean badResponse = false;
                
                
                byte[] clientResponse;
                // try{
                // if(gotString)
                //         clientResponse = tcpclient.askServer(hostnameTCP, portTCP, aString.getBytes());
                // else 
                //     clientResponse = tcpclient.askServer(hostnameTCP, portTCP);
                    
                //     String serverOutput = new String(clientResponse);
                //     String fullRespone = response + htmlS + serverOutput + htmlE;
                //     byte[] responeInByte = fullRespone.getBytes();
                //     connectionAsk.getOutputStream().write(responeInByte);
                    
                // } catch(java.net.ConnectException e){
                //     String errorResponse = response + htmlS + "java.net.ConnectException: " + e.getMessage() + htmlE;
                //     connectionAsk.getOutputStream().write(errorResponse.getBytes());
                    
                //     }
                // catch(java.net.UnknownHostException d){
                //     String errorResponse = response + htmlS + "java.net.UnknownHostException: " + d.getMessage() + htmlE;
                //     connectionAsk.getOutputStream().write(errorResponse.getBytes());
                // } 
         

        
            connectionAsk.getOutputStream().flush();
            connectionAsk.close();

        }//end while
        // askServerSocket.close();
    } //main
} //class

  // String fullRespone = response + htmlS + htmlE;
        // byte[] responeInByte = fullRespone.getBytes();

        // string parsing
        // String testURL = "http://hostname.domain/ask?hostname=time.nist.gov&limit=1200&port=13";
        // URL parse = new URL(testURL);
        // System.out.println(parse.getProtocol()); //http
        // System.out.println(parse.getHost()); //hostname.domain
        // System.out.println(parse.getFile()); //  /ask?hostname=time.nist.gov&limit=1200&port=13
        // System.out.println(parse.getQuery()); //hostname=time.nist.gov&limit=1200&port=13
        // System.out.println(parse.getPath()); // /ask
        // String[] queryURI = parse.getQuery().split("&");
        // for(int i = 0; i < queryURI.length; i++){
        //     System.out.println(queryURI[i]); //e.g port=13
        //     System.out.println(queryURI[i].split("=")[0]); // e.g port
        //     System.out.println(queryURI[i].split("=")[1]); // e.g 13

        // }
        // System.out.println(splitIt[1]);
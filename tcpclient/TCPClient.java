package tcpclient;
import java.net.*;
import java.io.*;

public class TCPClient {
    static boolean shutdownTCPAsk = false;             // True if client should shutdown connection
	static Integer timeoutTCPAsk = null;			     // Max time to wait for data from server (null if no limit)
	static Integer limitTCPAsk = null;			     // Max no. of bytes to receive from server (null if no limit)

    public TCPClient(boolean shutdown, Integer timeout, Integer limit) {
          shutdownTCPAsk =  shutdown;
          timeoutTCPAsk = timeout;
          limitTCPAsk = limit;
    }

    /*
    
    Timeout. When askServer has not received any data from the server during a period of time, 
             it closes the connection and returns.
    
     Data limit. When askServer has received a certain amount of bytes from the server, 
                 it closes the connection and returns.
    
    Furthermore, we will add the possibility for TCPClient to close the connection first.
    */
    public byte[] askServer(String hostname, int port, byte [] toServerBytes) throws IOException {
        
            /*
         open socket connection, save data and return
         socket->connect->send->recv->close
        */
        int bufferSize = 64;
        ByteArrayOutputStream recvData = new ByteArrayOutputStream();
        byte[] readSomeBytes = new byte[bufferSize];
        /*creating a socket without connecting. If timeout is not null, set timeout Socket.CONNECT(ADDPORT,TIMEOUT) */
        Socket tcpClientSocket = new Socket(hostname, port); //creates and connects
        // SocketAddress addressAndPort = new InetSocketAddress(hostname, port);

        
        // tcpClientSocket.connect(addressAndPort);
        if(timeoutTCPAsk != null)
        tcpClientSocket.setSoTimeout(timeoutTCPAsk);
        
        
        tcpClientSocket.getOutputStream().write(toServerBytes);
        if(shutdownTCPAsk) //shutdown tag -> shutdown outgoing 
            tcpClientSocket.shutdownOutput();
        
        int readByte = 0;
        boolean limitReached = false;
        int byteLimitCounter = -1;  
        
        if(limitTCPAsk != null)
            byteLimitCounter = limitTCPAsk;

      

        while(readByte != -1 && !limitReached){

        
        try{ //If it is not possible to read, catch error and shutdown.
            if(limitTCPAsk != null){
                //bufferSize = 64
                if(bufferSize > byteLimitCounter){  //if the buffer wants to read more than limit, set read length
                    readByte = tcpClientSocket.getInputStream().read(readSomeBytes, 0, byteLimitCounter);
                    if(readByte != -1)
                        recvData.write(readSomeBytes, 0, readByte);
                    // readByte = -1;
                    limitReached = true;
                }
                else{
                    readByte = tcpClientSocket.getInputStream().read(readSomeBytes);
                    if(readByte != -1 ){
                        byteLimitCounter = byteLimitCounter - readByte;
                        recvData.write(readSomeBytes, 0, readByte);
                    }
                }
            }
            else{
                readByte = tcpClientSocket.getInputStream().read(readSomeBytes);
                if(readByte != -1){

                    recvData.write(readSomeBytes, 0, readByte);
                    
                }
            }
            
            // recvData.write(readSomeBytes, 0, readByte);
            
        }// try
        catch(java.net.SocketTimeoutException e){
            limitReached = true;
        }
        
     }
        tcpClientSocket.close();

        return recvData.toByteArray();
    }// END Function 1

    public byte[] askServer(String hostname, int port) throws IOException {
    /* Same but no write. */
    int bufferSize = 64;
    ByteArrayOutputStream recvData = new ByteArrayOutputStream();
    byte[] readSomeBytes = new byte[bufferSize];
    Socket tcpClientSocket = new Socket(hostname, port); //creates and connects
    // SocketAddress addressAndPort = new InetSocketAddress(hostname, port);

    // tcpClientSocket.connect(addressAndPort);
        if(timeoutTCPAsk != null)
            tcpClientSocket.setSoTimeout(timeoutTCPAsk);

         int readByte = 0;
         boolean limitReached = false;
         int byteLimitCounter = -1;  
         
         if(limitTCPAsk != null)
             byteLimitCounter = limitTCPAsk;
        
        if(shutdownTCPAsk) //shutdown tag -> shutdown outgoing 
             tcpClientSocket.shutdownOutput();
        
        while(readByte != -1 && !limitReached){
         
         try{ //If it is not possible to read, catch error and shutdown.
             if(limitTCPAsk != null){
                 //bufferSize = 64
                 if(bufferSize > byteLimitCounter){  //if the buffer wants to read more than limit, set read length
                     readByte = tcpClientSocket.getInputStream().read(readSomeBytes, 0, byteLimitCounter);
                     if(readByte != -1)
                         recvData.write(readSomeBytes, 0, readByte);
                     // readByte = -1;
                     limitReached = true;
                 }
                 else{
                     readByte = tcpClientSocket.getInputStream().read(readSomeBytes);
                     if(readByte != -1 ){
                         byteLimitCounter = byteLimitCounter - readByte;
                         recvData.write(readSomeBytes, 0, readByte);
                     }
                 }
             }
             else{
                 readByte = tcpClientSocket.getInputStream().read(readSomeBytes);
                 if(readByte != -1){
 
                     recvData.write(readSomeBytes, 0, readByte);
                     
                 }
             }
             
         }// try
         catch(java.net.SocketTimeoutException e){
             limitReached = true;
         }
         
     }

    tcpClientSocket.close();

    return recvData.toByteArray();
    }


}// end class


# import TCPClient
import time

def timerStatus(timer ,starttime):
    timerReached = False
    print("TIMER: ", round(time.time() - starttime))
    if(timer <= round(time.time() - starttime)):
        timerReached = True
    return timerReached



# Hostname = "127.0.0.1"
# Port = 8888
# shutdownFlag = 1
# timerSet = False
# timer = 10
# starttime = time.time()

# timer = 10
# while True:
#     time.sleep(1)
    
#     sendData = "OK?"
#     print(round(time.time() - starttime))
#     if(timerStatus(timer ,starttime)):
#         print("TIMER REACHED")
#         shutdownFlag = 1
#     flag = str(shutdownFlag)
#     sendData = sendData + flag
#     sendData = sendData + "?.\n"
#     # print(sendData)
#     TCPClient.tcpClient(Hostname, Port, sendData)




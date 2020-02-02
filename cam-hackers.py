import requests, re
import sys

print("""

\033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
\033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
\033[1;31m                                                                        ANGELSECURITYTEAM 
""")

try:
    cc = input("ISO ALPHA-2 COUNTRY CODE (OR - FOR EXTRA): ")
    pages = int(input("MAX PAGES TO CHECK: "))
    print("\n")		
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}
        
        for page in range(0, pages):
            url = ("https://www.insecam.org/en/bycountry/"+cc+"/?page="+str(page))
        
            res = requests.get(url, headers=headers)
            findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                            
            for ip in findip:
                 print ("\033[1;31m", ip)
        
    except:
        print(" ")
except KeyboardInterrupt:
    print(" ")

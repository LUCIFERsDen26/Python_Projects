import os
import requests
from proxy_checker import ProxyChecker
import time 

main_path = os.getcwd() #main path
type_proxy=0
url = ' '
down_dir_path = main_path+'/'+'downloaded_proxies/'
working_dir_path = main_path+'/'+'working_proxies/'
comm_url='https://api.proxyscrape.com/v2/?request=getproxies&protocol='
opt1=''
opt2=''

def cls():
	os.system('cls' if os.name=='nt' else 'clear')
	
def grab_save_txt(fin_url,type_proxy,timout):

	url = fin_url
	
	r = requests.get(url, allow_redirects=True)
	
	if(type_proxy == 'Http'):
		open(down_dir_path+'/'+'Http'+'/'+timout+'(ms)_http'+'.txt','wb').write(r.content)
		print("\n" + "Downloaded and saved for proxy type ", type_proxy)
	elif(type_proxy == 'Socks4'):
		open(down_dir_path+'/'+'Socks4'+'/'+timout+'(ms)_socks4'+'.txt', 'wb').write(r.content)
		print("\n" + "Downloaded and saved for proxy type ", type_proxy)
	else:
		open(down_dir_path+'/'+'Socks5'+'/'+timout+'(ms)_socks5'+'.txt', 'wb').write(r.content)
		print("\n" + "Downloaded and saved for proxy type ", type_proxy)
def url_maker(timout,type_proxy):

	if(type_proxy == 'Https'):
		url_maker.fin_url = comm_url+"http&timeout="+timout+"&country=all&ssl=all&anonymity=all"
			
	elif(type_proxy == 'Socks4'):
		url_maker.fin_url = comm_url+"socks4&timeout="+timout+"&country=all"
	else:
		url_maker.fin_url = comm_url+"socks5&timeout="+timout+"&country=all"
		
cls()#clear screen

print(" Which type of proxy you want to Download '(option available -:)' ")

proxy_list=['Http', 'Socks4' , 'Socks5' ]
no=0

print("\n")

for lst in (proxy_list):
	print(no,") ",lst)
	no+=1

print("\n")

ans = True
while (ans):
	opt = input("Choose the no from ' 0 - 2 ' -: ")
	if(opt < '4'):
		ans = False
	else:
		print("\n" + "Wrong input, try again"+"\n")
print("\n" + "You have choosen to download this proxy "+"'",proxy_list[int(opt)],"'")

ms=True
while (ms):
	timout=input("\n" + "Enter 'time out' from proxies (50 - 10000) -: ")
	if(int(timout) > 50 and int(timout) < 10000):
		ms = False
	else:
		print("\n" + " Wrong input , proxies avaiable from 50 to 10000"+"\n")

print("\n" + "Downloading proxy for ",proxy_list[int(opt)]," With timeout ",timout)

url_maker(timout,proxy_list[int(opt)])

grab_save_txt(url_maker.fin_url,proxy_list[int(opt)],timout)
time.sleep(3)
print("\nNow starting checking working proxies in 5 seconds")
time.sleep(4)

cls()

print(" Which type of proxy you want to check '(option available -:)' ")
print("\n")
no=0
for lst in (proxy_list):
	print(no,") ",lst)
	no+=1
ans1 = True
while (ans1):
	opt1 = input("Choose the no from ' 0 - 2 ' -: ")
	if(int(opt1) < 3):
		ans1 = False
	else:
		print("\n" + "Wrong input, try again"+"\n")

print("\n" + "You have choosen to check this proxy folder"+"'",proxy_list[int(opt1)],"'")

list_txt=down_dir_path+proxy_list[int(opt1)]+'/'	
look_sub_dir = os.listdir(list_txt)

if(len(look_sub_dir)==0):
	print("No files here\nFirst Download some proxies !")
else:
	print("\nFiles available here!\n")
	txt_no=0
	for chk_txt in look_sub_dir:
		print(txt_no,")" , chk_txt)
		txt_no+=1
	ans2 = True
	
	while (ans2):
		opt2 = input("Choose the no from above no -: ")
		if(int(opt2) <= len(look_sub_dir)-1):
			ans2 = False
		else:
			print("\n" + "Wrong input, try again"+"\n")	

down_proxy_path = list_txt+look_sub_dir[int(opt2)]
work_proxy_path = working_dir_path+proxy_list[int(opt1)]+'/'+look_sub_dir[int(opt2)]
cls()
#print(down_proxy_path)
#print(work_proxy_path)

file_down = open(down_proxy_path, "r")
gp = file_down.read().splitlines()

file_up = open(work_proxy_path, 'w+')
checker = ProxyChecker()
count=1
for i in range(len(gp)):

		pull = checker.check_proxy(gp[i])
		print(count,'>',gp[i] + ":\n " + str(pull))
		count+=1
		if pull != False:
			result = gp[i] + " " + str(pull)
			file_up.write(result)
			file_up.write("\n")
file_down.close()
file_up.close()
print("Task failed Sucessfully!")
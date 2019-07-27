import dns.resolver
import pyfiglet
import terminal_banner

print("\033[1;34;48m* LINUX BASED TOOL V1.0 \033[1;32;48mDeveloped By @Aman Gondaliya\033[1;31;48m")
the_banner = pyfiglet.figlet_format("Sub-Bromain!")
print(the_banner)
print("\033[1;32;48m")
banner_text = "[+]It is a linux based tool.\n[+]It search subdomains for the domain you wants."
my_banner = terminal_banner.Banner(banner_text)
print(my_banner)


## PREPARATION ##

print("\033[1;31;48mEnter the subdomain name!\033[1;32;48m")


## taking files ##
try:
	domain = input()

except:
	print("Need more arguments")

print("\033[1;31;48mEnter the file name!\033[1;32;48m")

try:
	list_path = input()
except:
	print("Need more arguments")



## open wordlist ##
try:
	list_file = open(list_path)
	lines = list_file.read().splitlines()
except:
	print("File {} not found".format(list_path))



## BRUTE FORCE ##


for line in lines:
	subdomain = line + "." + domain
	try:
		answers = dns.resolver.query(subdomain, 'a')
		for result in answers:
			print ("[+] {} {}".format(subdomain,result))
	except:
		pass

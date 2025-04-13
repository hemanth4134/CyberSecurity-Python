from scapy.all import  *
interface = 'wlan0'
probReqs = []

def snifProves(p):

     if p.haslayer(Dot11ProbeReq):
        netName = p.getlayer(Dot11ProbeReq).info
        if netname not in probReqs:
            probReqs.append(netname)
            print{'[+] Detected New Probe Request: ' + nteName)

sniff(iface=interface, prn=sniffproves)


commands to run in kali linux
-->ifconfig
-->ifconfig wlan0 down
-->ifconfig (to check wlano was not appear)
--> iwconfig wlan0 mode monitor
ifconfig wlan0 up
ifconfig
ls
cd (to the sinffer.py file)
python sniffer.py

-----------------------------------

main.py

import tldextract
import Levenshtein as lv

legitimate_domains = ['example.com', 'google.com', 'facebook.com']

test_urls = [
       'http://example.co',
        'http://example.com',
        'https://www.google.security-update.com',
         'http://faceb00k.com/login',
         'https://google.com
]

def extract_domin_parts(urls):
       extracted = tldextract.extract(url)
       return extracted.subdomin, extracted.domin, extracted.suffix

def is_misspelled_domain(domain, legiimate_domain, threshold=0.9):
  for legit_domain in legitimate_domains:
            similarity = lv.ratio(domain, legit_domain)
             if similarity >= threshold:
                      return False # It's a legitimate domain
               return True

def is_phishing_url(url, legitimate_domains):
           subdomain, domain, suffix = etarct_domain_parts(url)

if f"{domain}.{suffix}" in legitimate_domains:
        return False


if is_misspelled_domain(domain, legitimate_domains):
print(f"Potential phishing detected: {url}")
return True

return False

if __name__ == '__main__':
   for url in test_urls:
             is_phishing_url(url, legitimate_domains)

below ss 


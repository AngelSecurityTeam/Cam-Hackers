#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers

import os, re, sys

mainurl = "https://www.insecam.org/en/bycountry/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"
}

def banner():
    print("""

        \033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
        ██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
        ██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
        ██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
        ╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
        \033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
        \033[1;31m                                                                        ANGELSECURITYTEAM 

        \033[1;31m1)\033[1;37mUnited States                \033[1;31m31)\033[1;37mMexico                \033[1;31m61)\033[1;37mMoldova
        \033[1;31m2)\033[1;37mJapan                        \033[1;31m32)\033[1;37mFinland               \033[1;31m62)\033[1;37mNicaragua
        \033[1;31m3)\033[1;37mItaly                        \033[1;31m33)\033[1;37mChina                 \033[1;31m63)\033[1;37mMalta
        \033[1;31m4)\033[1;37mKorea                        \033[1;31m34)\033[1;37mChile                 \033[1;31m64)\033[1;37mTrinidad And Tobago
        \033[1;31m5)\033[1;37mFrance                       \033[1;31m35)\033[1;37mSouth Africa          \033[1;31m65)\033[1;37mSoudi Arabia
        \033[1;31m6)\033[1;37mGermany                      \033[1;31m36)\033[1;37mSlovakia              \033[1;31m66)\033[1;37mCroatia
        \033[1;31m7)\033[1;37mTaiwan                       \033[1;31m37)\033[1;37mHungary               \033[1;31m67)\033[1;37mCyprus
        \033[1;31m8)\033[1;37mRussian Federation           \033[1;31m38)\033[1;37mIreland               \033[1;31m68)\033[1;37mPakistan
        \033[1;31m9)\033[1;37mUnited Kingdom               \033[1;31m39)\033[1;37mEgypt                 \033[1;31m69)\033[1;37mUnited Arab Emirates
        \033[1;31m10)\033[1;37mNetherlands                 \033[1;31m40)\033[1;37mThailand              \033[1;31m70)\033[1;37mKazakhstan
        \033[1;31m11)\033[1;37mCzech Republic              \033[1;31m41)\033[1;37mUkraine               \033[1;31m71)\033[1;37mKuwait
        \033[1;31m12)\033[1;37mTurkey                      \033[1;31m42)\033[1;37mSerbia                \033[1;31m72)\033[1;37mVenezuela
        \033[1;31m13)\033[1;37mAustria                     \033[1;31m43)\033[1;37mHong Kong             \033[1;31m73)\033[1;37mGeorgia
        \033[1;31m14)\033[1;37mSwitzerland                 \033[1;31m44)\033[1;37mGreece                \033[1;31m74)\033[1;37mMontenegro
        \033[1;31m15)\033[1;37mSpain                       \033[1;31m45)\033[1;37mPortugal              \033[1;31m75)\033[1;37mEl Salvador
        \033[1;31m16)\033[1;37mCanada                      \033[1;31m46)\033[1;37mLatvia                \033[1;31m76)\033[1;37mLuxembourg
        \033[1;31m17)\033[1;37mSweden                      \033[1;31m47)\033[1;37mSingapore             \033[1;31m77)\033[1;37mCuracao
        \033[1;31m18)\033[1;37mIsrael                      \033[1;31m48)\033[1;37mIceland               \033[1;31m78)\033[1;37mPuerto Rico
        \033[1;31m19)\033[1;37mIran                        \033[1;31m49)\033[1;37mMalaysia              \033[1;31m79)\033[1;37mCosta Rica
        \033[1;31m20)\033[1;37mPoland                      \033[1;31m50)\033[1;37mColombia              \033[1;31m80)\033[1;37mBelarus
        \033[1;31m21)\033[1;37mIndia                       \033[1;31m51)\033[1;37mTunisia               \033[1;31m81)\033[1;37mAlbania
        \033[1;31m22)\033[1;37mNorway                      \033[1;31m52)\033[1;37mEstonia               \033[1;31m82)\033[1;37mLiechtenstein
        \033[1;31m23)\033[1;37mRomania                     \033[1;31m53)\033[1;37mDominican Republic    \033[1;31m83)\033[1;37mBosnia And Herzegovia
        \033[1;31m24)\033[1;37mViet Nam                    \033[1;31m54)\033[1;37mSloveania             \033[1;31m84)\033[1;37mParaguay
        \033[1;31m25)\033[1;37mBelgium                     \033[1;31m55)\033[1;37mEcuador               \033[1;31m85)\033[1;37mPhilippines
        \033[1;31m26)\033[1;37mBrazil                      \033[1;31m56)\033[1;37mLithuania             \033[1;31m86)\033[1;37mFaroe Islands
        \033[1;31m27)\033[1;37mBulgaria                    \033[1;31m57)\033[1;37mPalestinian           \033[1;31m87)\033[1;37mGuatemala
        \033[1;31m28)\033[1;37mIndonesia                   \033[1;31m58)\033[1;37mNew Zealand           \033[1;31m88)\033[1;37mNepal
        \033[1;31m29)\033[1;37mDenmark                     \033[1;31m59)\033[1;37mBangladeh             \033[1;31m89)\033[1;37mPeru
        \033[1;31m30)\033[1;37mArgentina                   \033[1;31m60)\033[1;37mPanama                \033[1;31m90)\033[1;37mUruguay
        \033[1;31m91)\033[1;37mExtra
    """)
    pass

def requirements():
    # maybe need installation ?
    try:
        global requests
        import requests
    except ImportError:
        print("[!] Warning: request module not found !")
        print("[+] Hint: install it by executing pip install requests")
        sys.exit(os.EX_SOFTWARE)
    pass

def is_alive(url):
    try:
        req = requests.get(url, headers=headers)
        # print(req.ok)
        if req.status_code == 200:
            return True
        else:
            return False
    except IOError as err:
        print("[!] Your internet connection may be lost ?")
        print("[+] Error Detail:")
        print("[-] ", err)
        sys.exit(os.EX_NOHOST)

def main():
    countries = [
        "US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
        "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
        "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
        "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
        "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
        "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
        "MD", "NI", "MT", "IT", "SA", "HR", "CY", "PK", "AE", "KZ",
        "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
        "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
        "-"
    ]

    try:
        code = int(input("OPTION (1-91): "))
        while code not in range(1, 92):
            print("[!] The option you entered is not available (1-91)")
            code = int(input("OPTION (1-91): "))

        country = countries[code-1]
        request = requests.get(
            f"{mainurl}{country}", headers=headers
        )

        last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', request.text)[0]
        for page in range(int(last_page)):
            request = requests.get(
                f"{mainurl}{country}?page={page}", headers=headers
            )
            find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", request.text)
            for ip in find_ip:
                if is_alive(ip):
                    print("\033[1;32m[+] (alive) => ", ip, "\033[0;m")
                else:
                    print("\033[1;31m[+] (maybe lost) => ", ip, "\033[0;m")
        print()
        print("[------------------------- DONE -------------------------]")
        sys.exit(os.EX_OK)
    except ValueError:
        print("[!] Please enter only a number !")
        sys.exit(os.EX_DATAERR)

if __name__ == '__main__':
    try:
        os.system('clear || cls')
        requirements()
        # if is_active(mainurl) == False:
        #   print("\033[1;31m[!] At this time the server cannot be reached\033[0;m")
        #   sys.exit(os.EX_NOHOST)
        banner()
        try:
            main()
        except IOError as RunErr:
            print("[!] Your internet connection may be lost ?")
            print("[+] Error Detail:")
            print("[-] ", err)
            sys.exit(os.EX_NOHOST)
    except (KeyboardInterrupt, EOFError) as UserExc:
        print()
        print("[!] Exit command detected")
        print("[+] GoodByee :)")
        sys.exit(os.EX_OK)
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# github.com/AngelSecurityTeam/Cam-Hackers

import colorama
import re
import requests
import html

colorama.init()
print("""
\033[1;31m\033[1;37m ██████╗ █████╗ ███╗   ███╗      ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ███████╗
██╔════╝██╔══██╗████╗ ████║      ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗██╔════╝
██║     ███████║██╔████╔██║█████╗███████║███████║██║     █████╔╝ █████╗  ██████╔╝███████╗
██║     ██╔══██║██║╚██╔╝██║╚════╝██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗╚════██║
╚██████╗██║  ██║██║ ╚═╝ ██║      ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║███████║
\033[1;31m ╚═════╝╚═╝  ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝
\033[1;31m                                                                        ANGELSECURITYTEAM 
\033[1;31m1) \033[1;37mUnited States                \033[1;31m31) \033[1;37mMexico                \033[1;31m61) \033[1;37mMoldova
\033[1;31m2) \033[1;37mJapan                        \033[1;31m32) \033[1;37mFinland               \033[1;31m62) \033[1;37mNicaragua
\033[1;31m3) \033[1;37mItaly                        \033[1;31m33) \033[1;37mChina                 \033[1;31m63) \033[1;37mMalta
\033[1;31m4) \033[1;37mKorea                        \033[1;31m34) \033[1;37mChile                 \033[1;31m64) \033[1;37mTrinidad And Tobago
\033[1;31m5) \033[1;37mFrance                       \033[1;31m35) \033[1;37mSouth Africa          \033[1;31m65) \033[1;37mSoudi Arabia
\033[1;31m6) \033[1;37mGermany                      \033[1;31m36) \033[1;37mSlovakia              \033[1;31m66) \033[1;37mCroatia
\033[1;31m7) \033[1;37mTaiwan                       \033[1;31m37) \033[1;37mHungary               \033[1;31m67) \033[1;37mCyprus
\033[1;31m8) \033[1;37mRussian Federation           \033[1;31m38) \033[1;37mIreland               \033[1;31m68) \033[1;37mPakistan
\033[1;31m9) \033[1;37mUnited Kingdom               \033[1;31m39) \033[1;37mEgypt                 \033[1;31m69) \033[1;37mUnited Arab Emirates
\033[1;31m10) \033[1;37mNetherlands                 \033[1;31m40) \033[1;37mThailand              \033[1;31m70) \033[1;37mKazakhstan
\033[1;31m11) \033[1;37mCzech Republic              \033[1;31m41) \033[1;37mUkraine               \033[1;31m71) \033[1;37mKuwait
\033[1;31m12) \033[1;37mTurkey                      \033[1;31m42) \033[1;37mSerbia                \033[1;31m72) \033[1;37mVenezuela
\033[1;31m13) \033[1;37mAustria                     \033[1;31m43) \033[1;37mHong Kong             \033[1;31m73) \033[1;37mGeorgia
\033[1;31m14) \033[1;37mSwitzerland                 \033[1;31m44) \033[1;37mGreece                \033[1;31m74) \033[1;37mMontenegro
\033[1;31m15) \033[1;37mSpain                       \033[1;31m45) \033[1;37mPortugal              \033[1;31m75) \033[1;37mEl Salvador
\033[1;31m16) \033[1;37mCanada                      \033[1;31m46) \033[1;37mLatvia                \033[1;31m76) \033[1;37mLuxembourg
\033[1;31m17) \033[1;37mSweden                      \033[1;31m47) \033[1;37mSingapore             \033[1;31m77) \033[1;37mCuracao
\033[1;31m18) \033[1;37mIsrael                      \033[1;31m48) \033[1;37mIceland               \033[1;31m78) \033[1;37mPuerto Rico
\033[1;31m19) \033[1;37mIran                        \033[1;31m49) \033[1;37mMalaysia              \033[1;31m79) \033[1;37mCosta Rica
\033[1;31m20) \033[1;37mPoland                      \033[1;31m50) \033[1;37mColombia              \033[1;31m80) \033[1;37mBelarus
\033[1;31m21) \033[1;37mIndia                       \033[1;31m51) \033[1;37mTunisia               \033[1;31m81) \033[1;37mAlbania
\033[1;31m22) \033[1;37mNorway                      \033[1;31m52) \033[1;37mEstonia               \033[1;31m82) \033[1;37mLiechtenstein
\033[1;31m23) \033[1;37mRomania                     \033[1;31m53) \033[1;37mDominican Republic    \033[1;31m83) \033[1;37mBosnia And Herzegovia
\033[1;31m24) \033[1;37mViet Nam                    \033[1;31m54) \033[1;37mSloveania             \033[1;31m84) \033[1;37mParaguay
\033[1;31m25) \033[1;37mBelgium                     \033[1;31m55) \033[1;37mEcuador               \033[1;31m85) \033[1;37mPhilippines
\033[1;31m26) \033[1;37mBrazil                      \033[1;31m56) \033[1;37mLithuania             \033[1;31m86) \033[1;37mFaroe Islands
\033[1;31m27) \033[1;37mBulgaria                    \033[1;31m57) \033[1;37mPalestinian           \033[1;31m87) \033[1;37mGuatemala
\033[1;31m28) \033[1;37mIndonesia                   \033[1;31m58) \033[1;37mNew Zealand           \033[1;31m88) \033[1;37mNepal
\033[1;31m29) \033[1;37mDenmark                     \033[1;31m59) \033[1;37mBangladeh             \033[1;31m89) \033[1;37mPeru
\033[1;31m30) \033[1;37mArgentina                   \033[1;31m60) \033[1;37mPanama                \033[1;31m90) \033[1;37mUruguay
                                                          \033[1;31m91) \033[1;37mExtra
""")
data_to_extract = []


def extract_data(data):
    extracted_data = []
    for camera in data:
        ip = camera.split("src=\"")[1].split("\"")[0]
        camera_type = camera.split("title=\"View ")[1].split(" CCTV")[0]
        city = camera.split("title=\"")[1].split(", ")[1].split("\"")[0]
        extracted_data.append({'ip': ip, 'type': camera_type, 'city': city})
    return extracted_data


def unique(obj):
    unique_city = []

    for camera in obj:
        if camera['city'] not in unique_city:
            unique_city.append(camera['city'])
    return unique_city


def print_cameras(cts, cams, index):

    if len(cts) != index:
        cam_to_show = list(filter(lambda x: x['city'] == cts[index], cams))
    else:
        cam_to_show = list(cams)
    for i, c in enumerate(cam_to_show):
        txt = """\033[1;31m""" + str(i) + """) \033[1;37m""" + """\033[1;31mUrl:\033[1;37m """ + c['ip'] + \
              """ | \033[1;31mType:\033[1;37m """ + c['type'] + \
              """ | \033[1;31mCity:\033[1;37m """ + c['city']
        print(txt)


try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "IR", "PL",
                 "IN", "NO", "RO", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-"]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 91 + 1):
        raise IndexError

    country = countries[num - 1]
    res = requests.get(
        f"https://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"https://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        # find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)^.*token.*$
        relevant_lines = re.findall(r"^.*http://\d+.\d+.\d+.\d+:\d+.*$", res.text, re.MULTILINE)

        for line in relevant_lines:
            data_to_extract.append(line)
            # print("\033[1;31m", ip)
    cameras = extract_data(data_to_extract)
    print()
    print('\033[1;31mTotal found cameras: ', str(len(cameras)))
    print('\033[1;31mChoose city:')
    cities = unique(cameras)
    cities = sorted(cities)
    cities_to_print = ""
    count = 0
    for idx, ct in enumerate(cities):
        max_chars = 29

        if "&#" in ct:
            cities[idx] = html.unescape(ct)
            ct = html.unescape(ct)

        if count == 3:
            cities_to_print += '\n'
            count = 0

        if idx >= 10 or (idx >= 10 and idx == 0):
            max_chars -= 1

        if len(ct) < max_chars:
            spaces = max_chars - len(ct)

        cities_to_print += """\033[1;31m""" + str(idx) + """) \033[1;37m""" + ct + (" " * spaces)
        if idx == len(cities) - 1:
            print(cities_to_print + """\033[1;31m""" + str(len(cities)) + """) \033[1;37m""" + "All Cameras")

        count += 1

    num = int(input("OPTIONS : "))
    if num not in range(0, len(cities)+1):
        raise IndexError
    print()
    print_cameras(cities, cameras, num)

except Exception as e:
    print(e)
finally:
    print("\033[1;37m")
    exit()

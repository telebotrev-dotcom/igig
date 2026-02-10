import requests
from user_agent import *
import time
import os
import webbrowser
webbrowser.open('https://t.me/tols_python')
username = input('ENTER YOUR USERNAME => ')

pa = input('ENTER YOUR PASSWORD => ')

os.system('clear')

print('''
محتوى غير مهم أو احتيالي -1 
لا يعجبني فحسب -2 
مضايقة أو تواصل غير مرغوب فيه 3- 
الانتحار أو إيذاء الذات أو اضطرابات الأكل
عنف أو كراهية أو استغلال 4- 
بيع أو ترويج عناصر محظورة 5- 
عُري أو نشاط جنسي 6- 
خداع أو احتيال 7- 
معلومات زائفة 8- 


''')
h = input('ENTER YOUR NUMPER =>')


tr = input('ENTER YOUR USERNAME the account => ')


cookies = {
    'datr': 'OqhFaSvz3896RM699JeDRERS',
    'ig_did': '24E8448B-DA5C-4392-A68C-6F71FA8DD8FE',
    'mid': 'aUWoPwAEAAHn-v0cDfeyq7L3OXrg',
    'ig_nrcb': '1',
    'ps_l': '1',
    'ps_n': '1',
    'csrftoken': 'a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa',
    'dpr': '3.0234789848327637',
    'wd': '891x1671',
}

headers = {
    'authority': 'www.instagram.com',
    'accept': '*/*',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=OqhFaSvz3896RM699JeDRERS; ig_did=24E8448B-DA5C-4392-A68C-6F71FA8DD8FE; mid=aUWoPwAEAAHn-v0cDfeyq7L3OXrg; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa; dpr=3.0234789848327637; wd=891x1671',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': str(generate_user_agent()),
    'x-asbd-id': '359341',
    'x-csrftoken': 'a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa',
    'x-ig-app-id': '936619743392459',
    'x-ig-www-claim': '0',
    'x-instagram-ajax': '1031623017',
    'x-requested-with': 'XMLHttpRequest',
    'x-web-session-id': 'xm1wtf:t1yo2p:xxabri',
}
ti = str(time.time()).split(".")[0]
data = {
    'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{ti}:{pa}',
    'caaF2DebugGroup': '0',
    'isPrivacyPortalReq': 'false',
    'loginAttemptSubmissionCount': '0',
    'optIntoOneTap': 'false',
    'queryParams': '{}',
    'trustedDeviceRecords': '{}',
    'username': username,
    'jazoest': '22669',
}

response = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', cookies=cookies, headers=headers, data=data)

if '"user":true' in response.text and '"authenticated":true' in response.text:
	print(f'GOOD LOGIN : {username} : {pa}')
	
	ses = response.cookies.get_dict()
	
	csr = ses['csrftoken']
	
	ds_user_id = ses['ds_user_id']
	
	sessionid = ses["sessionid"]
	
	while True:
	
		cookies = {
		    'datr': 'OqhFaSvz3896RM699JeDRERS',
		    'ig_did': '24E8448B-DA5C-4392-A68C-6F71FA8DD8FE',
		    'mid': 'aUWoPwAEAAHn-v0cDfeyq7L3OXrg',
		    'ig_nrcb': '1',
		    'ps_l': '1',
		    'ps_n': '1',
		    'csrftoken': 'a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa',
		    'dpr': '3.0234789848327637',
		    'wd': '891x1671',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    # 'cookie': 'datr=OqhFaSvz3896RM699JeDRERS; ig_did=24E8448B-DA5C-4392-A68C-6F71FA8DD8FE; mid=aUWoPwAEAAHn-v0cDfeyq7L3OXrg; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa; dpr=3.0234789848327637; wd=891x1671',
		    'referer': 'https://www.instagram.com/dfff/?_a=1',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': 'a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa',
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': '0',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': '5jn0mu:d8l08w:n70p96',
		}
		
		params = {
		    'username': tr,
		}
		
		response = requests.get(
		    'https://www.instagram.com/api/v1/users/web_profile_info/',
		    params=params,
		    cookies=cookies,
		    headers=headers,
		).json()
		
		t = response['data']['user']['id']
		
	
	
		cookies = {
		    'datr': 'OqhFaSvz3896RM699JeDRERS',
		    'ig_did': '24E8448B-DA5C-4392-A68C-6F71FA8DD8FE',
		    'mid': 'aUWoPwAEAAHn-v0cDfeyq7L3OXrg',
		    'ig_nrcb': '1',
		    'ps_l': '1',
		    'ps_n': '1',
		    'csrftoken': csr,
		    'dpr': '3.0234789848327637',
		    'wd': '891x1671',
		    'sessionid': sessionid,
		    'ds_user_id': ds_user_id,
		    'rur': '"RVA\\05476303971746\\0541799156624:01fe55ca021385cee550e685e869107224dbfbf9995deb0e4d913dce331eac6f50fd8466"',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'datr=OqhFaSvz3896RM699JeDRERS; ig_did=24E8448B-DA5C-4392-A68C-6F71FA8DD8FE; mid=aUWoPwAEAAHn-v0cDfeyq7L3OXrg; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa; dpr=3.0234789848327637; wd=891x1671; sessionid=76303971746%3AjkJYBsxA1J3Fzd%3A28%3AAYgKHdLQCM0LgwRbOMhIlBiTthnb5uMc9uogM_WhNQ; ds_user_id=76303971746; rur="RVA\\05476303971746\\0541799156624:01fe55ca021385cee550e685e869107224dbfbf9995deb0e4d913dce331eac6f50fd8466"',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/royacomedy/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': csr,
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR2ZebPnMV8oF_FGwsM0MVblQPCh470v2aqmAowZOV6WChcz',
		    'x-instagram-ajax': '1031623017',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': '9lsu2o:mc585y:3b197s',
		}
		
		data = {
		    'container_module': 'profilePage',
		    'entry_point': '1',
		    'location': '2',
		    'object_id': id,
		    'object_type': '5',
		    'context': '{"tags":["ig_report_account"],"ixt_context_from_www":"QVFZbTRhZUFMVHY4UGpQTXRBZmR0UHNvUFR1UU9QZThXRUZZZ29uOEN6YzZidklNYnNkTmVmQS1hSXZWTzdtbzNzX3BNc3plTUpJek5qOUR0OTIyMVVVMUo5a2wtb3ZrTUF5MGtWV2FNV1BVYk1sNzc0VDk2bmtfcUlqT2pRSkZiSmpnWUdjTENaOFJxXzM0aDgxVnBWdzlMRzU3NlVWNThqb1pRNzVleUowVUxtUG5EdEZzLXFiYWZqbkI4Z25WRjQtc2dnVHZpVXNtLVp4d3I0NFlfZ2pzOXg3Y1IzeEpQcy1KWFZ2Mlh1VC1yb3liN1pKd1lhU19GRWZpNk4wWWJLU0EyZ1Fxclpac3E0ZHptRkJGc1pBR3BPNnYtdDl2aE85bV9mNnNWVWd3Q3d6bDN4RFVqUFRvVDNiX1dGWlJpcS1JQVJzelFraEJqNlJDMElCRTdTS1ZqbWxZMEpqaVZ4Y2FwMTNMWkJWQXhUWFNqTTdETFpzbkhPOHBtSVVYMTk2dHphT0FZU0xockFVR0h2cHdvZVZfUTdJWXdNU3JnWkYteWh5cWZ1c0lJQk9XR1BzOENXeTk0WWdQZURjQUNzbHk3STRuNUlrMnc2cUt5QVdBeEQzcURSV29wN3NUOVVvdFV4enBGNkdVWTluZmVBdThaOEVZa3dQS3FhcnBFOUV6aXo0MnMxUVZJVmpPTmcyVjAzZlNkVXZuWWRJR1ZXbVk5bFNMT0N0d2xwVDI1RlFmVWJqY0hnZ0JpRGItRW1xVWRRN1AyN1BMb3phYXk3UWNLZnNtcjNqYW5EenUwMXJTNE50bGNzUFRDTHNzdklaMW5aQWY3d2xwOWhwNWQ3bXliYzdVbnFBX2M5X0RRU0JXT21pMzBCU2pvbTRWdERwcWxmVE11cE14QS1KN19adzMxbEJLN3V2aHVvZlg3Q1VGOUZjYlJ1V3ZvT0NXRi1paXZ6NU9WS183TXRjM3dVUUNKTmZRZVN0MFgzQjNRaXJUNy1aX1BpUHhMOFpwNzNHWElPbjJablhHaDFIc2x6cnFaM1RfUXRTbkYxMUdrVENJXzV6UkROQmNwWFBVYVdyVjQzUzAzRUdVVkZkVnctVTk5TlgyUWNvSF9WVjlIVzVtVnRmQXJBUzNnY0dhOGlZUHF3ZzlGY3hRMWFRazBELXZRcVVLT3VuWnJfN3B4TVR2dW84OVpyQTNIdTJuaHRpX1d2WXAtQzR4MlZVR1BUS09uWHJaRFRNc2Zaa3QxZG9weEd6UzB6U2x1MUFBdFhIWHFjZjRyYjk0MzIxYUZySUllMlFKVkJiODRKWTcyVnY4ZmNPUER0S0JXcE1YdVpfcE5xX3NmbTlsTVBQMEYyRzB5UGpPbjlwSkE2VUZ0ckduZk1vcVdrSTNzREFJaUo0THo0SFFoRFZrVENiSWtRYVVJS280UFU2aDB0dkhmZGtJX3RHeFM5eUx0WXBURmRkTTVzY3I4aFpVa3ZXNVdJb0VRWVVhSktRT0E2OFdjeU1pclFuaGJWM3NmcGExV0h6ei1aYkZ1OURMQUFHWVVRZUYtUWxHQnptQy1kMENaclBjOXB4Y3BKMDRVY2lYWHU0U05NZEEwcGFrOVJpR01KZHFfdTlKN3pxbDloTVdLOXBaMmRMbkFNQ3dfTDRseXZYTnB6RTUwbWhtcUwyTHIyLTNmTEViM2dHbWdlY043NW5Xa0ZLUGp1eXBMc1BWVHNZbDB5amlZZTB4ZGd1STN2THo4WHNaclNIblg5ZjhBRWxCOEhZYXFoTEhKaTNXMkJCOVJBOHJjQWkzbW1MVXdYWkdmQnk5b3NhOHVBemFWaHlCaktjS1puUXplcTdwR2pSdDExRXA3Ym9IOXV2VE5Fb0JCbkNEX180amE5LXhQOGJQRlBZOGVOVFN4QVY4ZTNhOGNJdmYwcThQcFVMeXY1U3V3NnJLdG1HU2o2MWJ6TDZnOEhSQXN1THNVbEtkMlUxelBkTWhlSVZaUGNLY0Y0RnNGakpydklMOUM3cUQ4eW9MMzhGaVg0SjNPUFFRV2RVOGE0SWo2RmlzaGV0VHZBaUhYZUZkWW0teGlfWVJ3T1ZsQk10U0NZUmJfcUhoa2NKd2FnakpFUnF2MEJ4cDdJTXpObC1MdVZHZHVreGNoTllOWG84Y1ZkNl9Tc21DNzVjVGdRUkJ6N0I2dkd5RnpXUkdIMF9FZjU2d09KQ19hME8xSFVtcm96NTBqN3h2NzZ3d0lONDVsVjM0V21tWkZDVURsY1prWnVaV2Vtd003S1FOMWJ2c0Fobm1GaE5vbUV2amhtMV9iQnJnVEx6UVlxNS1kLU1pTjdVQkhuTjlnUmdGejZVSmMwNUhXYlpEcXRjWVUzYy1EV3h4RDY2dFpINDZoSW5WX045NFo0bW1tdmRXaXVDbXplOU05WGtFR3ByQThHZ294RUtmMUtiZnZoNDBnY2dmTHJNbE9Vdm5PQlF3amFobnV5dUJJV0xRNkhCSE55RW95akM5RW9yUzBVUVJxc1JIbC03N05BSTg3QmJPeTQzcmEtRTVBV3RsckJTY3FQYjJKaUQwN1QwTEkwM3JCRmtQMXU5N0s5eUNmY05uYmlHcVYtaS1hYThhSmZ2djZpZ2xnaGR6Zjk4TThPX05mWkd0R2ZsQVl5S201QmhZbWhWbTVQYmZ4Y3ZoVWNxb1pvalFmN0lIa01sbE1DVmJxcEdyQjBFRXFRTmhrMGs2R1VIMG1FMWQtVWVnRDlPS1ZldmNRdzVhbFBUSjJUYjhVMDMwU0M4OUJRY3ZvQjlOa3lpa01NRG0xMWlMLVZUTjZYQlc0VUdpUU9BQXNhSmFhVlpVcFN4MzFzU3R4RmhtRXJsbUtVQmpOQWVfd1NfYVlqX2pVWjBsOWlCZkF1LUdTaDdlcnZUTFNoV3dhc1NhVENUTTUwR0pDRUJObW1YdFcwWllKdjkxVFhIM01MclRxNjlhRnFYbGFGaWJ4TXhKZmxSZ2dWeVctbnNYNnBFMGVjMzNtWDhKaVdVTVpyMW1PUks5U0pzSG9zcmM4Z3M1SlJLV2ZiMjhBRVZYYzI4TS1PSTM3amZtT1NyWUkzUk1GM0JBYzBydGRxQi1IbUh4bDNFNFh4WWVfaERkc0tMdXNycTFyc3VYTThGVU1LdUlkQ09ucEItNHRQVWV6Y3l4WklHMmZFRlVTQWxVMEdHcjRERHV2aFdtS2dXMlFqN1lqUWJzTy1RbG9UVU4yVGgxenkzLXhBWnI4SlozSy03UW12OW43NTlHOGxEWXZNYThTakhZR1VETjZob3k2ekIzOVhMdmVNdkc1aXF3VnhmTlc4a0ZsZGV4c3Fva19kenZkcTJUR3JPOVNIMFZ4bnpSdjh3R0c4OThPNzBjaFZFaktCaG9EWUJ1MF83cGFlZ1FtMWhzZFhFdkY2ekYxclVPYmZNX21VcW5mWFI1NDZET1V2Y3I4aFNnQ2w3aDc5dmgwLWlnR1M0Y3FUREozc0ZRRWRmYXpPNzNJRXVXbmltUExCVlVMd19oZnYtVnZSVnhmTkNFTEFjcURlSWVvWno1dlNOMDJ2eVQ0VjFnVENmNHZBakQyTENIcGVKazVKT1Z4RXdzT1c0NTZoNVZ4VzNwX196elFPZ0NBaGhGZDU3ZGdkaGtLbjZnMDRDRG9HeGZmeG9YMHdzaDdrZ0xXcEhXVWQxUE8xLWpZbmRIQjkzZElIWXN5cWw0RWQ5MlJaZUtkdGhGODE3a2dkZENzSWRyRDdJTjFXTGdvbDdvU19mV29kZGdHQzlIZlI3cjAwU1AzM1JpZ2FDWTJkUFVYQ2xNYlpkdXFybDVVMnFxT1BLNE5uTHR5UzBJQXM1OGRMemZzQ0RRWm5hOEhRdEJtcEotbGZweWNhT3Bsd0ZlSG5ubWloMGlLcW84bzhqenV0Y3ROM3VzNXg1VjJ4ZjNER1h1N1BZeHpraGtNTGR5QkI2RkdyT2dpMDUxM0pDZWd2NnY1N3FhTnVRRHFIS0N4SVByTUxDQVhRUWJkSDhVeTE1T3dMVnhIX0xGX2Y2NFJUU2hGaWZEWEFIV3JCQnJUQW9JX3pSY3djc2lFbXR5alRhTUZZcmNHOFZOcWZfcmh1cVZFZjkwck45M3d5UkNpM28yQy1SNTFZVlV0NVgtWWxnTGI2bzRkMXN3YnJRZmM3WmlZY3U4bTNScVF1MlA4QjdZZ29RTHVuajd2Z1VSRDZsajRsOTR2VGtOMEU1Z0tXelZLNU5jNDQ4dHNFbmpVVUlaZ2VVZlBONVcwYTAtTEFHbUlDZ1RidnRXbmJhaE1YeWRZdFJwbkhVdXc3YXVGR0JJRWV6Ny00bWFNS1o5dzJsdWZBYnp5bzBlYlJycGpCUzlhQW0xY081dmdra2M1R1h5elA5aFZ2VDZXX1B2WjVxY3ItbHZ1b19mWnhCUXpsSVE3UXlvZWNYV3VJbDNzSkUtVzBsMlo1TGkzTkJVYWVJOG9nbVdfbzFxVDhyczNxdkFLcDliR0toY2RvYVFJWFlzcHBBOEY0OU5DaHM=","frx_context_from_www":"{\\"location\\":\\"ig_profile\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"88c773b5-fe49-46d7-a2a9-cefdf82e3369\\",\\"tags\\":[\\"ig_report_account\\"],\\"object\\":\\"{\\\\\\"user_id\\\\\\":\\\\\\"11414701372\\\\\\"}\\",\\"reporter_id\\":17841476192407996,\\"responsible_id\\":17841411441176837,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"profilePage\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"JsTWkcG4BBgNMzcuMjM3LjEzNi4xNRhlTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM3LjAuMC4wIFNhZmFyaS81MzcuMzYYBWFyX0FSHBggZjdiN2ZlYmYyNzY0YTllNmYwN2ZmMTM4Yjg0Y2ZmNGIYABggMWUwNTA2ZTgxYWYzZjQzZmRiMTM2MGJlYzcwNGQwM2EYJHF1aWM1ZTlkOTI4YjEyZmMzNGE2ZTYzOWY3MjgzNjI0YjdjMhWc5xgoIDQzOWFlOTM1NTUxMzNlOTU0YjY3NDE1MjhhNzc5Zjg1GCRxMTNkMDMxMWgzXzU1YjM3NWM1ZDIyZV81YTFmMzIzZWY1NmQAPCwYHGFVV29Qd0FFQUFIbi12MGNEZmV5cTdMM09YcmcWsNjJgedmABwVCCsBiAJvcwNYMTEAIjwYJDI0RTg0NDhCLURBNUMtNDM5Mi1BNjhDLTZGNzFGQThERDhGRSkVFhkVADkVAAAYIGFhNTU2YTBjMjMzZDRmZDQ4OWVjYTFiMGZjMDlmMzRlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaItv+WzbCyPxhAYTdlNjhkY2M0NzBlYjEwNTFhMjIwNzE3ZDQyNTJmMWFhZjg0Yjg5NTRjMWIyZmJmODM5YThhODY3ZGQ4MzA5ZBgZNzYzMDM5NzE3NDY6Mjg6MTc2NzYyMDUwNwAcFQQAEiglaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9yb3lhY29tZWR5LxgOWE1MSHR0cFJlcXVlc3QAFvjGvKvMrrE\\\\\\/KCMvYXBpL3YxL3dlYi9yZXBvcnRzL2dldF9mcnhfcHJvbXB0LxY4Frb+3ZUNWAE0GAVWQUxJRAA=\\",\\"shopping_session_id\\":null,\\"logging_extra\\":\\"{\\\\\\"navigation_chain\\\\\\":\\\\\\"PolarisFeedRoot:feedPage:1:via_cold_start,PolarisProfilePostsTabRoot:profilePage:2:unexpected\\\\\\"}\\",\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-b6016bf5-c136-4c70-945f-f825dec5bef8\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IGEntUser\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_tag_selection_screen\\",\\"ent_has_music\\":false,\\"evidence_selections\\":[],\\"is_full_screen\\":false}"}',
		    'selected_tag_types': '["ig_its_inappropriate"]',
		    'frx_prompt_request_type': '2',
		    'logging_extra': '{"navigation_chain":"PolarisFeedRoot:feedPage:1:via_cold_start,PolarisProfilePostsTabRoot:profilePage:2:unexpected"}',
		    'jazoest': '22669',
		}
		
		response = requests.post(
		    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
		    cookies=cookies,
		    headers=headers,
		    data=data,
		).json()
		
		rep = response['response']["report_tags"][h]["tag_type"]
		
		
	
		cookies = {
		    'datr': 'OqhFaSvz3896RM699JeDRERS',
		    'ig_did': '24E8448B-DA5C-4392-A68C-6F71FA8DD8FE',
		    'mid': 'aUWoPwAEAAHn-v0cDfeyq7L3OXrg',
		    'ig_nrcb': '1',
		    'ps_l': '1',
		    'ps_n': '1',
		    'csrftoken': csr,
		    'dpr': '3.0234789848327637',
		    'wd': '891x1671',
		    'sessionid': sessionid,
		    'ds_user_id': ds_user_id,
		    'rur': '"RVA\\05476303971746\\0541799156630:01fe56ede324b21cde6ea4ccb8eb1a56a2b2a3b84706172d2293905276995aa570e80e65"',
		}
		
		headers = {
		    'authority': 'www.instagram.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'content-type': 'application/x-www-form-urlencoded',
		    # 'cookie': 'datr=OqhFaSvz3896RM699JeDRERS; ig_did=24E8448B-DA5C-4392-A68C-6F71FA8DD8FE; mid=aUWoPwAEAAHn-v0cDfeyq7L3OXrg; ig_nrcb=1; ps_l=1; ps_n=1; csrftoken=a23WoaP6T9yoOfR5b2UpEZkMNTDSx6Qa; dpr=3.0234789848327637; wd=891x1671; sessionid=76303971746%3AjkJYBsxA1J3Fzd%3A28%3AAYgKHdLQCM0LgwRbOMhIlBiTthnb5uMc9uogM_WhNQ; ds_user_id=76303971746; rur="RVA\\05476303971746\\0541799156630:01fe56ede324b21cde6ea4ccb8eb1a56a2b2a3b84706172d2293905276995aa570e80e65"',
		    'origin': 'https://www.instagram.com',
		    'referer': 'https://www.instagram.com/royacomedy/',
		    'sec-ch-prefers-color-scheme': 'dark',
		    'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
		    'sec-ch-ua-full-version-list': '"Chromium";v="137.0.7337.0", "Not/A)Brand";v="24.0.0.0"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-model': '""',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-ch-ua-platform-version': '""',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': str(generate_user_agent()),
		    'x-asbd-id': '359341',
		    'x-csrftoken': csr,
		    'x-ig-app-id': '936619743392459',
		    'x-ig-www-claim': 'hmac.AR2ZebPnMV8oF_FGwsM0MVblQPCh470v2aqmAowZOV6WChcz',
		    'x-instagram-ajax': '1031623017',
		    'x-requested-with': 'XMLHttpRequest',
		    'x-web-session-id': '9lsu2o:mc585y:3b197s',
		}
		
		data = {
		    'container_module': 'profilePage',
		    'entry_point': '1',
		    'location': '2',
		    'object_id': id,
		    'object_type': '5',
		    'context': '{"tags":["ig_report_account","ig_its_inappropriate","suicide_or_self_harm_or_eating_disorder_concern"],"ixt_context_from_www":"QVFiZktfTzFoajAtZEhEQ0hNQkQ3c2djeDZmR0FKZ09vbUxvMldfN01MSUdtYlNWWVp2NFZ4WGZhM1ptYzhPeTBWWVF0aEt5ZEFFT0VGbnh2cTE0YXFvdFk1RDBoLWIwM21teGtrTk9HZmluaVVaTE8waFE0TUtfXzhNZVd2RXd5eW5QelM3YjZFdkpPYlFFT013bE52bTZoTHpzbkZram9OMDVnUmx4RC01Q0V6M3lGWnlnRWV4X1lnd2FleHFlR1VLMnRKY0o0MHl3SFV3ZUkzbEdmcjBpLVM4UVRkNmRKeE1vcm1WczJibVJ3SGFWR1VNbVR6WFNYYW9heEc1dUR4U3AtXzM2bmhITkRTbC1CcW13dTdGRkZ3OXFMWmtqelVyelJWTHN3RlBIV2JnOGhYTnlmUnFLOFBHTi12bzJ2SGJtNUdTTEFZNkdIcXpuWjFCdUtmUUZpcWw4ZERXaGRwVm9rN1pQR05ZY2xDdWVUaEpKZjBWRURFR3Q3TGh2MlNiRjBpV1FVUm1oa2lfdUtqZ2U2SzVtVHJpNjRud0tjVmtwWlNTUGkzWE8wd3NCRVd0YWNVWnhwT0ZvYTd2ci1YVkYybFJSRWV2d1RfMEtmMTBjeGVpS2YyY29uY3RlMURRYkI3Qm5Ua1V3eXN2dl9fM245dlFWZkthNWFBUWlWWkdnVE9oTU1XckYzbEppdjFsZEFQM0FkMlM4VkVqbFg2LWpJNkNrelFWb3V4Sy1BQVBEWXZMb3Q5N1dLQ2twSV9ibmFDVUxHYklpUjNOdWRqWUt6N3VvR052cEl4VVBZVDhWRjhIaWxHSXc2bzlYd0NBMXpTRHlzUFRiY0pyN1JyVmJ3ZnBZaHU3QVNHQnFzZGhpd0w3dE1hcnlDallYY096QktOV2VvY2JWTnlBVU9XQWI5bE02b0JKelh1aW1Rak04ZTQ2THJ5eEQ5Qnd5a2d5MTJ2aC0wMjRBeDZrS1lHdFJ3c212ODFfWER1VUota0lGbm9fZEpDSjkwdllpNnVCMEtPWk1fSkpobFYwTzJSWldreFFSNk0wWmRRc2FhQ3ZDWmM3WXBoOTNheHprSWlUbWhzdE45TjRwa1NUSmx4VWxfNjhzcUYyc0NHd0dfTzRlWkFXVHFGZ2piZWw5TU4tZjZFLTlUNWszYjgyQmIxdXc3RnRvcG0ydlZLV242TGRZTnQ5UmxCbGRLTi1UOEVrdTVKRHNTa1BXbUNDalgyVklyQUxVVUJ0aWhscy1SU0lGaUoydW84MlRrQnl1VG14cGN1d3FpOGUzdi1QeENWcTExbG1JSlhCV09QaWpGNDlwdjdaeHFwbDNSMzRQZTltMnprWDNaWDd1dHl2aWNlQ3ZyTjBlMXg2OWs1WW13ZnQ2eHMtVW1TOWtsZkZXRU5ydEdSZFlmMWtFOHBON1dfRnhGQms0SXNBZXc0SXFuQWpEV0MzWk9XXzFFQlg2WXJveDhOMV92QUFrN1J0d3JWOTh2Mk9UQ3pGNG5JOEZxZnBYZUhnUXFfQ0FkMDVCRHNBTktQT2dralU0cFlzR1BhdElfQ2t6eG1qVnlQQldCX016TUFKVXFwM0pSUnl5OTI0RlFuS0VjSGJDSTdkdmY0WUR2X09WMTNrR1YyYk5hbUV2UmZSZC0wZHFLZThTa2hkRnhFdjdTRFdkZjRkVXNINFdYZjRsSlRIaUNYdi1GY25PTTdLQjVMLVlJbFZIa0xJLVFfTk9FcVZBQ1JVUkxESmgzNGRMZGsxOXBIU2Zsb1MtRmg2NTVlQXB0dnJOUDNia0hrN2ljOXlla3N2ajFpVFNhNzFHSE51b05DT0NMaVNPb2pMWVhPOTdYVTdWMXdVME1QUTRZOXhkUldidS01bDBZTEJQajc1SDdPYmNMMy0zTDBmaU1oUW14THhsSDhEeUE0STdQZjFXdnFVYjlZam44SHZtcVpGZE9WWEwzNmphUkl6UVdqR2VoblctU2VyYXA5cUJWTDFBOVl6Smk0dVVFNm9seWxtWEtkd1Rfa2dJQ0xqNWNQUlYtclM4MGJmWlFUMUpfMkdDc0QzcW1qZmxGNWJhQTVWajJOOGVEckZ3STBjSWNmLU04ckFjVDFtTGNYbndkZXRDTGdTRlhBcVRmUUN2ajJlYlMzN2lFTWRYS2JoOER6SHJHb1FOZ1NrQ0FielhiekRENEJBUkp1ZFlCOUJBUm5yOXB1N3NRTDhlbkFZQzljN0t3clZQQzBQVWF5cGdfTXJ3NEQ0cEFobmNVa2hlRXprbjQxU1hVNEtTZkdadk93bEFQZmp5b21valFJSzNEWTJFblh5Mml2SUIyN24xOGJWdHN4MW95OVNSMXlJSjhMcmo3UnpkOTl3TGg3dlZVdzFGanZTaDBkV2k1TFdKQmFFYm41bm5jSWRBMXl3TmdmWWN0OG94c29naWkxYndXc2FVbG1ON1JqbE1jXzVXNTVjUWNrWWNrNjJLcWwxQXRLSWx1TXlXU2ctMHg0QTVhSXppdlY3Ni1ObkZObG5sblR5WGJIOEYySHFpZmo2a0E0TW9GZDMyR0s1dERDallvWXVudElzUFhwSGt2RmpkazdYWWZrMngzTHZobEdKalZrNzdtdlhDTlJRUjdQVkc3THQtSE9xakQ4emRhamdyMzJRVHV4ak5HWl9fRm51WjZTTHdGaXF5UWVNQnJ4SjdIdE9FNFA3X25Sam1hcnBKLU5FRG5qMVZRSGhOS29sei03MEI5akRMbVhJUk1Ga3llQUItcGNEU1ZVOTQ0ZUNqZGx6MEZCVFJlalllRTdqV3RBNzJDM2xyOHNzYmFyeWg3QVpYTEoyTExmX0tnMWNtLUQ2TVBpWkFUdkl6VHJXRkQzaDhkb0MwWmlhMGxTaV8xdHVrQm1kU1lKT09mV3FWWUtsVXk1RXJ5b1VXcVFieThqNE1SRGlmeTRiUjN4MTgzeWpSZS1Dd1pSQ0FSLWJZWGV0cUpjcnEzMm1iQm8zR3BNLU9ydTRuU29EZ1NqdGpNY2N4aF9vbW5ZQTVHNHhsdWZvSjlLVEwwSnhiVUhIRGE1S2c5RTlSblJvaE45LWhUUmVZYUQxY1oxd3ltZWdZZ1lwRjg3eXlYOWMzZEdnLU96bUpQSUlIVXZRZjBodzNjSmZPWG8xMjBBdmREdlZmX0RxR0U1Qnl3WE5YdWVveHNyaUlqU0k3NjNvbHQxMTZfLS1KZGVVQkliUG9hT2VreGJqUzFsTlZHZjVKQjc4ZjNjZ0E5dmhaN29xS1JURmNwTkM1TEFxeUNGUWg5Nl9RaFBrSDlrQlZDY1QwWk8wUkhKYkpRNktHT05hMEJhaEU5djVITk4zYUFCSHBjRDRlcVRBOHh0RjkyRGtKVlhvV294T2ljM2FJTTFTRmwtZWRZSXNKRWhoclg0RWVKc3U0Q1ZWYVdWb093ZXlNbGVFTFU5WVh0bU5tX2pHWnJJazZsdmp4QnNNa1BvYm9xcDZQZHF1Zm9kMUkyZFl1eGRFanJmNzBMOFlhWkh3cE1ZYVM5V2h6QndDZFI4Wm5rRVBFZ2RGVk5ienVWT281VEJaT2ZUdFhaYkhneHkxRGUwc0RFcVpMcU9TV3pZZjNlMzg5cVlIRmc4LXUwU3l3NmEyM05BS3h2aHFGVDZEQlgxYmtzaVhvM3ZRMGJMcEZYSEhNYU13a0toQ1l3eXlkeWpMYlIxYVh5OTZMVXh5bHNQRFAxY3ltc1NUMXdEaDJkNzVjUGg0XzZKR3NzNjJzZzZUcktUNURXQ3VkRE1yZnNJb01ORmxXbkZuY1BkSERpd0VFbjJlczdSWlFlXzMwUXdYQzVQTFNRT3pjWWxVV0std3dCcTBQZGc1akxXbG92N1NCMUhoS3JWREhrWE0tR3pTZTBxdnMwSFp5eUw5WkIxTXdlZF9vZF8wT3hMWG1HdUtrdUltYk45UEhJdm14bkZ0bE1EeHczSGlfNjhLallQZjV0aEtWaVdZSHpoeXZNQU5YT05BS2RoVDhXc2RTNzc3OHFsWFFIazVGQ3lUeGQxRDJfQXZIWThSRjhKbzlLYktHZTJMVHlWLTByVEVUMzZ1X0V0aVMyZWhITzR0RmZTbkxXRG9XODVyMEpsUkkwV2hhYnVtaFFhRU5UNlR5bzhtNzlFRWk1dGVwWkU4cUtCZzNlNk1ma0tGYWphcGpaNGs1VnNpak5sSGtNQTI0Y2Nib0ZUYXZ2VzlBaV9kcW1rd2hmWHRIOW5lUXdhR3YzWFhlZlBob0xDanJEeGFsdTV5LUhKWW5NcVZQWGFCWGhlZW5oS1JfcHNRVnpBZWkyYzY4M1JTMGtMZGZzaUpMUVIzcElJdmpKR21CY3dSVUI2bzhFa3NlVkwxLVM3NVdGOEZtZE83VEV1aVlTcXFFaExxelZ4ZG5jY0NjUjQ4YWkyYWFkaS1GUDVCZ3VYZzhyZHRzeEpUQjlIbldrTW1lX1dsSU1WRU5Zd1o2cjdfLWNtOVVRUVgxTXk4Y0ZUMy1QTXFUbzBtMzJlYzdiSDJtUmx6czdybzNZdTkzYWltYWNSUGQxV0tUb29vMzc0dC04TlJlbEhDODZqLWoycU9iVWIwVTBqSHotZHhPU1Y1T1NyeUN3UjN1NkxFTXY5QjE4d2E5d0FqOC1hdlVBQ0paZTF2dWlHR080QTVoR01GZE5B","frx_context_from_www":"{\\"location\\":\\"ig_profile\\",\\"entry_point\\":\\"chevron_button\\",\\"session_id\\":\\"88c773b5-fe49-46d7-a2a9-cefdf82e3369\\",\\"tags\\":[\\"ig_report_account\\",\\"ig_its_inappropriate\\",\\"suicide_or_self_harm_or_eating_disorder_concern\\"],\\"object\\":\\"{\\\\\\"user_id\\\\\\":\\\\\\"11414701372\\\\\\"}\\",\\"reporter_id\\":17841476192407996,\\"responsible_id\\":17841411441176837,\\"locale\\":\\"ar_AR\\",\\"app_platform\\":4,\\"extra_data\\":{\\"container_module\\":\\"profilePage\\",\\"app_version\\":\\"None\\",\\"is_dark_mode\\":null,\\"app_id\\":936619743392459,\\"sentry_feature_map\\":\\"JsTWkcG4BBgNMzcuMjM3LjEzNi4xNRhlTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTM3LjAuMC4wIFNhZmFyaS81MzcuMzYYBWFyX0FSHBggZjdiN2ZlYmYyNzY0YTllNmYwN2ZmMTM4Yjg0Y2ZmNGIYABggMWUwNTA2ZTgxYWYzZjQzZmRiMTM2MGJlYzcwNGQwM2EYJHF1aWM1ZTlkOTI4YjEyZmMzNGE2ZTYzOWY3MjgzNjI0YjdjMhWc5xgoIDQzOWFlOTM1NTUxMzNlOTU0YjY3NDE1MjhhNzc5Zjg1GCRxMTNkMDMxMWgzXzU1YjM3NWM1ZDIyZV81YTFmMzIzZWY1NmQAPCwYHGFVV29Qd0FFQUFIbi12MGNEZmV5cTdMM09YcmcWsNjJgedmABwVCCsBiAJvcwNYMTEAIjwYJDI0RTg0NDhCLURBNUMtNDM5Mi1BNjhDLTZGNzFGQThERDhGRSkVFhkVADkVAAAYIGFhNTU2YTBjMjMzZDRmZDQ4OWVjYTFiMGZjMDlmMzRlFQIREhgPOTM2NjE5NzQzMzkyNDU5HBaItv+WzbCyPxhAYTdlNjhkY2M0NzBlYjEwNTFhMjIwNzE3ZDQyNTJmMWFhZjg0Yjg5NTRjMWIyZmJmODM5YThhODY3ZGQ4MzA5ZBgZNzYzMDM5NzE3NDY6Mjg6MTc2NzYyMDUwNwAcFQQAEiglaHR0cHM6Ly93d3cuaW5zdGFncmFtLmNvbS9yb3lhY29tZWR5LxgOWE1MSHR0cFJlcXVlc3QAFvjGvKvMrrE\\\\\\/KCMvYXBpL3YxL3dlYi9yZXBvcnRzL2dldF9mcnhfcHJvbXB0LxY4Frb+3ZUNWAE0GAVWQUxJRAA=\\",\\"shopping_session_id\\":null,\\"logging_extra\\":\\"{\\\\\\"navigation_chain\\\\\\":\\\\\\"PolarisFeedRoot:feedPage:1:via_cold_start,PolarisProfilePostsTabRoot:profilePage:2:unexpected\\\\\\"}\\",\\"is_in_holdout\\":null,\\"preloading_enabled\\":null},\\"frx_feedback_submitted\\":false,\\"ufo_key\\":\\"ufo-b6016bf5-c136-4c70-945f-f825dec5bef8\\",\\"additional_data\\":{\\"is_ixt_session\\":true,\\"frx_validation_ent\\":\\"IGEntUser\\"},\\"profile_search\\":false,\\"screen_type\\":\\"frx_tag_selection_screen\\",\\"ent_has_music\\":false,\\"evidence_selections\\":[],\\"is_full_screen\\":false}"}',
		    'selected_tag_types': f'["{rep}"]',
		    'frx_prompt_request_type': '2',
		    'logging_extra': '{"navigation_chain":"PolarisFeedRoot:feedPage:1:via_cold_start,PolarisProfilePostsTabRoot:profilePage:2:unexpected"}',
		    'jazoest': '22669',
		}
		
		response = requests.post(
		    'https://www.instagram.com/api/v1/web/reports/get_frx_prompt/',
		    cookies=cookies,
		    headers=headers,
		    data=data,
		).text
		if '"text":"تم"' in response:
			print(f'DONE Report : {tr}')
		else:
			print(f'BAD Report : {tr}')
		
	
else:
	print(f'BAD LOGIN : {username} : {pa}')
	 
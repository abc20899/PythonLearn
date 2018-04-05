# https://leohxj.gitbooks.io/a-programmer-prepares/software/mac/softwares/iTerm2.html
# encoding=utf8
import requests
import time

import sys
import urllib3

urllib3.disable_warnings()

id = '5a53526f959d690db50001f7'
api_token = '8d8d49154ade65589b1802fc458c4e06'


def get_upload_info():
    minlen = 6
    syslen = len(sys.argv)  # 获取输入参数
    # 检查输入参数
    if syslen < minlen:
        print('input params error')
        return
    else:
        appname = sys.argv[1]  # app name
        appversion = sys.argv[2]  # app version
        buildnum = sys.argv[3]  # build
        iconpath = sys.argv[4]  # 图标路径
        apkpath = sys.argv[5]  # apk路径
    url = 'http://api.fir.im/apps'
    type = 'android'
    bundle_id = 'cn.ikicker.ikickerlottery'
    params = {'type': type, 'bundle_id': bundle_id, 'api_token': api_token}
    response_data = requests.post(url, data=params)
    resjson = response_data.json()
    print(resjson['cert']['icon'])  # icon字典
    print(resjson['cert']['binary'])  # 二进制文件上传字典

    upload_iocn(resjson['cert']['icon'], iconpath)
    upload_apk(resjson['cert']['binary'], appname, appversion, buildnum, apkpath)
    '''
    {
	'id': '5a53526f959d690db50001f7',
	'short': 'qbm7',
	'form_method': 'POST',
	'storage': 'qiniu',
	'type': 'android',
	'cert': {
		'icon': {
			'custom_headers': {},
			'upload_url': 'https://upload.qbox.me',
			'custom_callback_data': {
				'original_key': '82b31c3e84c685aaae58aa2b7e1531bb7aad3660'
			},
			'key': '4a91349573a27d0aac38b6f3f2922a70e126d1e8',
			'token': 'LOvmia8oXF4xnLh0IdH05XMYpH6ENHNpARlmPc-T:GyHt9vtu7eKcF-Kh-sCLC_o9VFw=:eyJzY29wZSI6ImZpcmljb246NGE5MTM0OTU3M2EyN2QwYWFjMzhiNmYzZjI5MjJhNzBlMTI2ZDFlOCIsImNhbGxiYWNrVXJsIjoiaHR0cDovL2FwaS5maXIuaW0vYXV0aC9xaW5pdS9jYWxsYmFjaz9wYXJlbnRfaWQ9NWE1MzUyNmY5NTlkNjkwZGI1MDAwMWY3XHUwMDI2dGltZXN0YW1wPTE1MTY3NzY4OTFcdTAwMjZzaWduPWZmZjI2XHUwMDI2b3JpZ2luYWxfa2V5PTgyYjMxYzNlODRjNjg1YWFhZTU4YWEyYjdlMTUzMWJiN2FhZDM2NjAiLCJjYWxsYmFja0JvZHkiOiJrZXk9JChrZXkpXHUwMDI2ZXRhZz0kKGV0YWcpXHUwMDI2ZnNpemU9JChmc2l6ZSlcdTAwMjZmbmFtZT0kKGZuYW1lKVx1MDAyNm9yaWdpbj0kKHg6b3JpZ2luKVx1MDAyNmlzX2NvbnZlcnRlZD0kKHg6aXNfY29udmVydGVkKSIsImRlYWRsaW5lIjoxNTE2Nzc3NDkxLCJ1cGhvc3RzIjpbImh0dHA6Ly91cC5xaW5pdS5jb20iLCJodHRwOi8vdXBsb2FkLnFpbml1LmNvbSIsIi1IIHVwLnFpbml1LmNvbSBodHRwOi8vMTgzLjEzMS43LjE4Il0sImdsb2JhbCI6ZmFsc2V9'
		},
		'support': 'qiniu',
		'binary': {
			'custom_headers': {},
			'upload_url': 'https://upload.qbox.me',
			'key': '5792e867f6b834d1f67c2a9a6d50f047bb3da642.apk',
			'token': 'LOvmia8oXF4xnLh0IdH05XMYpH6ENHNpARlmPc-T:eYCMy0Eb6iOsKmC7_8jd0Z6zke4=:eyJzY29wZSI6InByby1hcHA6NTc5MmU4NjdmNmI4MzRkMWY2N2MyYTlhNmQ1MGYwNDdiYjNkYTY0Mi5hcGsiLCJjYWxsYmFja1VybCI6Imh0dHA6Ly9hcGkuZmlyLmltL2F1dGgvcWluaXUvY2FsbGJhY2s_cGFyZW50X2lkPTVhNTM1MjZmOTU5ZDY5MGRiNTAwMDFmN1x1MDAyNnRpbWVzdGFtcD0xNTE2Nzc2ODkxXHUwMDI2c2lnbj1mZmYyNlx1MDAyNnVzZXJfaWQ9NTc5OWNhMmE5NTlkNjk2MGI5MDAwZDMyIiwiY2FsbGJhY2tCb2R5Ijoia2V5PSQoa2V5KVx1MDAyNmV0YWc9JChldGFnKVx1MDAyNmZzaXplPSQoZnNpemUpXHUwMDI2Zm5hbWU9JChmbmFtZSlcdTAwMjZvcmlnaW49JCh4Om9yaWdpbilcdTAwMjZuYW1lPSQoeDpuYW1lKVx1MDAyNmJ1aWxkPSQoeDpidWlsZClcdTAwMjZ2ZXJzaW9uPSQoeDp2ZXJzaW9uKVx1MDAyNmlzX3VzZV9tcWM9JCh4OmlzX3VzZV9tcWMpXHUwMDI2Y2hhbmdlbG9nPSQoeDpjaGFuZ2Vsb2cpXHUwMDI2cmVsZWFzZV90eXBlPSQoeDpyZWxlYXNlX3R5cGUpXHUwMDI2ZGlzdHJpYnV0aW9uX25hbWU9JCh4OmRpc3RyaWJ1dGlvbl9uYW1lKVx1MDAyNnN1cHBvcnRlZF9wbGF0Zm9ybT0kKHg6c3VwcG9ydGVkX3BsYXRmb3JtKVx1MDAyNm1pbmltdW1fb3NfdmVyc2lvbj0kKHg6bWluaW11bV9vc192ZXJzaW9uKVx1MDAyNnVpX3JlcXVpcmVkX2RldmljZV9jYXBhYmlsaXRpZXM9JCh4OnVpX3JlcXVpcmVkX2RldmljZV9jYXBhYmlsaXRpZXMpXHUwMDI2dWlfZGV2aWNlX2ZhbWlseT0kKHg6dWlfZGV2aWNlX2ZhbWlseSkiLCJkZWFkbGluZSI6MTUxNjc4MDQ5MSwidXBob3N0cyI6WyJodHRwOi8vdXAucWluaXUuY29tIiwiaHR0cDovL3VwbG9hZC5xaW5pdS5jb20iLCItSCB1cC5xaW5pdS5jb20gaHR0cDovLzE4My4xMzEuNy4xOCJdLCJnbG9iYWwiOmZhbHNlfQ=='
		},
		'mqc': {
			'used': 0,
			'is_mqc_availabled': True,
			'total': 5
		},
		'prefix': 'x:'
	}
    '''


def upload_iocn(icondict, iconpath):
    try:
        print("start upload icon")
        url = icondict['upload_url']
        key = icondict['key']
        token = icondict['token']
        paramdata = {'key': key, "token": token}
        iconfile = {'file': open(iconpath, 'rb')}
        # 上传icon
        res = requests.post(url, files=iconfile, data=paramdata, verify=False)
        print(res.text)
    except BaseException as e:
        print(e)
    finally:
        print('iocn finally')


def upload_apk(binarydict, appname, appversion, buildnum, apkpath):
    try:
        print("start upload apk")
        url = binarydict["upload_url"]
        key = binarydict["key"]
        token = binarydict["token"]
        changelog = str('time :' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        paramdata = {
            'key': key,
            'token': token,
            'name': appname,  # '必赢'
            'version': appversion,  # '1.0.0'
            'build': buildnum,  # 11
            'changelog': changelog  # 日志
        }
        apkfile = {'file': open(apkpath, 'rb')}
        res = requests.post(url, files=apkfile, data=paramdata, verify=False)
        print(res.text)
        print("upload success")
    except BaseException as e:
        print(str(e))
    finally:
        print('apk finally')


def test_print():
    minlen = 5
    syslen = len(sys.argv)  # 获取输入参数
    appname = sys.argv[1]  #
    appversion = sys.argv[2]
    iconpath = sys.argv[3]
    apkpath = sys.argv[4]
    print(apkpath)


if __name__ == '__main__':
    get_upload_info()

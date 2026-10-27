import time
import requests
import urllib3
import traceback

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "http://up.smf24.cx:8088/hr.php"

params = {
    'SzRZSFBiRS9wSDZkUVk4TmhBUU13d1VnNjZibW9DVE9kWERpc3ZkQUhXWWVPaW94ZGkvN3hMbndna3V6OWZsNwo': ""
}

headers = {
    'Host': "up.smf24.cx:8088",
    'User-Agent': "84388B2359531",
    'Connection': "Keep-Alive"
}

print("[*] تم بدء تشغيل نظام الإنعاش السريع جداً بنسخته المحسنة...")

counter = 1
while True:
    try:
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=15)
        print(f"[{counter}] - الرد: {response.status_code} - {response.text[:30]}")
        counter += 1
    except requests.exceptions.RequestException as e:
        print(f"[-] خطأ في الشبكة أو الاتصال: {e}")
    except Exception as e:
        print(f"[-] خطأ غير متوقع: {e}")
        traceback.print_exc()
        
    # الانتظار 3 ثوانٍ قبل الطلب التالي
    time.sleep(3)

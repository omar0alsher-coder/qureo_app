import threading
import time
import webbrowser
from app import app

def start_server():
    app.run(host="127.0.0.1", port=8080, threaded=True, use_reloader=False)

if __name__ == "__main__":
    # تشغيل السيرفر في الخلفية
    threading.Thread(target=start_server, daemon=True).start()
    time.sleep(1.5) # انتظار ثانية ونصف لتجهيز السيرفر
    
    # فتح الواجهة داخل التطبيق
    # ملاحظة: p4a webview بيعترض الأمر ده ويفتح شاشة ويب فيو أصلية
    webbrowser.open("http://127.0.0.1:8080")
    
    # إبقاء التطبيق شغال
    while True:
        time.sleep(1)

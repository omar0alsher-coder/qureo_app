import threading
import time
from app import app
from android import mActivity
from android.content import Intent
from android.net import Uri

def run_server():
    app.run(host="127.0.0.1", port=5000, threaded=True, use_reloader=False)

if __name__ == "__main__":
    t = threading.Thread(target=run_server, daemon=True)
    t.start()
    time.sleep(2)
    intent = Intent(Intent.ACTION_VIEW)
    intent.setData(Uri.parse("http://127.0.0.1:5000"))
    mActivity.startActivity(intent)
    while True:
        time.sleep(1)

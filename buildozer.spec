[app]
title = Qureo Premium
package.name = qureopremium
package.domain = org.qureo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css
version = 1.0
requirements = python3,kivy,flask,requests,urllib3,android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.archs = arm64-v8a
p4a.bootstrap = webview
p4a.port = 8080
p4a.branch = master
android.accept_sdk_license = True

# هنا المسارات بتاعتك اللي إنت نزلتها في التيرموكس
android.sdk_path = /data/data/com.termux/files/home/android-sdk
android.ndk_path = /data/data/com.termux/files/usr/opt/android-ndk

[buildozer]
log_level = 2
warn_on_root = 0

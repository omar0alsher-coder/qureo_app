[app]
title = Qureo Premium
package.name = qureopremium
package.domain = org.qureo
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css
version = 1.0
requirements = python3,flask,requests,urllib3,android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
p4a.bootstrap = webview
p4a.port = 8080
p4a.branch = master
android.ndk = 25b
android.ndk_api = 23

[buildozer]
log_level = 2
warn_on_root = 0

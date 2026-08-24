[app]
title = Sismos Venezuela & Frontera
package.name = sismosvzla
package.domain = org.sismos
source.dir = .
source.exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,urllib3,certifi
orientation = portrait
android.permissions = INTERNET
android.ndk = 25b
android.api = 33
android.archs = arm64-v8a
android.accept-sdk-license = True

[buildozer]
log_level = 2
warn_on_root = 1
# Incrementa el nivel de paralelismo para aprovechar los núcleos del servidor de GitHub
# y terminar más rápido antes de que se agote el tiempo:
build_mode = debug

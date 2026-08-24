[app]

# (str) Title of your application
title = Sismos Venezuela & Frontera

# (str) Package name
package.name = sismosvzla

# (str) Package domain (needed for android packaging)
package.domain = org.sismos

# (str) Source files where the let's go (relative to directory of spec)
source.dir = .

# (str) List of inclusions/exclusions
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning (method 1)
version = 1.0

# (list) Application requirements
requirements = python3,kivy,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (str) Android NDK version to use
android.ndk = 25b

# (int) Target Android API
android.api = 33

# (str) Supported architectures
android.archs = arm64-v8a

# (bool) Automatically accept SDK license
android.accept-sdk-license = True

[buildozer]
log_level = 2
warn_on_root = 1

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
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy,urllib3,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (list) Target Android API, should be as high as possible.
android.api = 33

# (str) Supported architectures (arm64-v8a is required for modern phones)
android.archs = arm64-v8a

# (bool) Automatically accept SDK license
android.accept-sdk-license = True

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

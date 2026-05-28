[app]
# Application title
title = Joker

# Package name
package.name = joker

# Package domain
package.domain = org.joker

# Source code directory
source.dir = .

# Source code inclusions
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 1.0.0

# Requirements
requirements = python3,kivy,pillow

# Orientation
orientation = portrait

# Fullscreen
fullscreen = 0

# Icon and presplash
icon.filename = %(source.dir)s/assets/icon.png
presplash.filename = %(source.dir)s/assets/presplash.png

# Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Features
android.features = android.hardware.touchscreen

# API levels
android.api = 31
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# Google Play specific
android.release_artifact = aab

# Gradle options
android.gradle_dependencies = 

# Meta-data
android.meta_data = com.google.android.gms.version=@integer/google_play_services_version

[buildozer]
# Log level
log_level = 2

# Display warning on buildozer run
warn_on_root = 1

name: Joker Build System

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout Code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    - name: Install Dependencies
      run: |
        python -m pip install --upgrade pip
        pip install kivy buildozer cython

    - name: Build Android APK (Joker)
      run: |
        # هذا الأمر يبدأ عملية تحويل مشروعك إلى تطبيق للهاتف
        # تأكد من وجود ملف buildozer.spec في مشروعك
        buildozer android debug

# 🎭 تطبيق الجوكر الذكي - Joker Smart App

تطبيق ويب ذكي متطور يجمع بين الذكاء الاصطناعي والتطبيقات المحمولة. يدعم اللغة العربية بلهجات مختلفة.

## ✨ المميزات

- 🤖 دعم الذكاء الاصطناعي (Google Gemini API)
- 📱 تطبيق ويب تقدمي (PWA) - يمكن تثبيته على الهاتف
- 🌍 دعم كامل للغة العربية واللهجات المصرية
- 🎨 واجهة مستخدم جميلة وحديثة
- ⚡ أداء سريع وموثوقية عالية

## 🚀 البدء السريع

### المتطلبات
- Node.js و npm
- Python 3.9+
- Git

### التثبيت

```bash
# استنساخ المستودع
git clone https://github.com/wd9412136-netizen/Joker-Assets.git
cd Joker-Assets

# تثبيت المتعلقات
npm install

# تثبيت متعلقات Python
pip install -r requirements.txt
```

### التشغيل

```bash
# تشغيل خادم الويب
npm start

# أو في نافذة أخرى، تشغيل الخادم الخلفي (Flask)
python Al-Joker.py
```

ثم افتح المتصفح على `http://localhost:8000`

## 📁 هيكل المشروع

```
Joker-Assets/
├── index.html              # الصفحة الرئيسية
├── qrcode.html            # صفحة QR Code
├��─ Al-Joker.py            # الخادم الخلفي (Flask)
├── package.json           # متعلقات Node.js
├── requirements.txt       # متعلقات Python
├── manifest.json          # ملف PWA
├── config.xml             # إعدادات Cordova
└── capacitor.config.json  # إعدادات Capacitor
```

## 🔧 المتغيرات البيئية

انسخ `.env.example` إلى `.env` وأضف مفاتيحك:

```env
GOOGLE_GEMINI_API_KEY=your_api_key_here
PORT=5000
```

## 📖 التوثيق

اطلع على `SETUP_AND_DEPLOYMENT.md` للحصول على تعليمات التثبيت والنشر التفصيلية.

## 🛠️ البناء والنشر

### بناء تطبيق Android

```bash
npm run build
```

### خدمة الملفات الثابتة

```bash
npm run serve
```

## 📝 الترخيص

هذا المشروع مرخص تحت ترخيص MIT - اطلع على ملف `LICENSE` للتفاصيل.

## 👨‍💻 المطور

**wd9412136-netizen**

## 📧 التواصل والدعم

إذا واجهت أي مشاكل أو لديك اقتراحات، يرجى فتح issue على GitHub.

---

**آخر تحديث:** 27 مايو 2026

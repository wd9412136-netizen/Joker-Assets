# دليل نشر التطبيق على Google Play

## الخطوة 1: إعداد حساب Google Play Developer

### 1.1 إنشاء الحساب
- اذهب إلى [Google Play Console](https://play.google.com/console)
- انقر على "إنشاء حساب"
- ادفع رسم التسجيل ($25)
- أكمل الملف الشخصي للمطور

### 1.2 إعدادات الحساب
- أضف بيانات الدفع
- اقبل اتفاقية Google Play
- ملء معلومات الاتصال

---

## الخطوة 2: إعداد التطبيق في Google Play Console

### 2.1 إنشاء تطبيق جديد
1. افتح [Google Play Console](https://play.google.com/console)
2. انقر على "إنشاء تطبيق"
3. أدخل اسم التطبيق: **Joker**
4. اختر الفئة (مثلاً: Games, Productivity, etc.)

### 2.2 إعدادات الحزمة
1. في القائمة اليسرى، اذهب إلى **All apps**
2. اختر تطبيقك
3. انقر على **Setup** → **App bundles and APKs**
4. تأكد من تفعيل App Bundle (AAB)

### 2.3 إنشاء مفتاح خاص (Service Account)
1. اذهب إلى **Setup** → **API and services**
2. انقر على **Create Service Account**
3. ستُعاد توجيهك إلى Google Cloud Console
4. انقر على **Create Service Account**
5. ملء البيانات:
   - Service account name: `joker-uploader`
   - Description: `GitHub Actions Uploader for Joker App`
6. انقر على **Create and Continue**
7. منح الدور: اختر **Editor** من القائمة المنسدلة
8. انقر على **Continue**
9. انقر على **Create Key** → **JSON** → **Create**
10. سيتم تحميل ملف JSON - احفظه بأمان

### 2.4 إضافة صلاحيات Service Account
1. العودة إلى Google Play Console
2. اذهب إلى **Setup** → **API and services** → **Users and permissions**
3. انقر على **Invite user**
4. أدخل بريد Service Account (من ملف JSON)
5. امنح الدور: **Admin (all permissions)**
6. انقر على **Send invite**

---

## الخطوة 3: إعداد GitHub Secrets

### 3.1 إضافة Service Account JSON إلى GitHub
1. اذهب إلى مستودعك على GitHub
2. انقر على **Settings** → **Secrets and variables** → **Actions**
3. انقر على **New repository secret**
4. اسم السر: `PLAY_STORE_SERVICE_ACCOUNT_JSON`
5. القيمة: انسخ محتوى ملف JSON الذي حصلت عليه
6. انقر على **Add secret**

### 3.2 التحقق من السر
```bash
# تحقق من أن السر مضاف بنجاح في GitHub
# (لا تعرض محتوى السر لأسباب أمان)
```

---

## الخطوة 4: تحضير بيانات التطبيق

### 4.1 صور الأيقونة
- حجم: 512×512 بكسل
- الصيغة: PNG
- الموقع: `assets/icon.png`

### 4.2 الصورة الافتتاحية (Presplash)
- الأبعاد: توصى 1080×1920 بكسل
- الصيغة: PNG
- الموقع: `assets/presplash.png`

### 4.3 لقطات الشاشة
في Google Play Console:
1. اذهب إلى **Main store listing**
2. أضف 2-8 لقطات شاشة
- الحجم الموصى به: 1080×1920 بكسل
- بصيغة PNG أو JPG

### 4.4 البيانات الوصفية
```
العنوان: Joker
الوصف القصير: وصف التطبيق بـ 80 حرف
الوصف الكامل: وصف مفصل بـ 4000 حرف
الفئة: Games / Productivity
المحتوى: اختر المناسب
السعر: مجاني أو مدفوع
```

---

## الخطوة 5: بناء وتحميل التطبيق

### 5.1 بناء محلي
```bash
# تثبيت المتطلبات
pip install kivy buildozer cython

# بناء Release AAB
buildozer android release
```

### 5.2 التحميل اليدوي
1. في Google Play Console
2. اذهب إلى **Testing** → **Internal testing**
3. انقر على **Upload new release**
4. اختر ملف AAB من `bin/` folder

### 5.3 التحميل التلقائي (GitHub Actions)
```bash
# ما عليك سوى عمل push tag:
git tag v1.0.0
git push origin v1.0.0

# سيتم البناء والتحميل تلقائياً
```

---

## الخطوة 6: الاختبار والنشر

### 6.1 اختبار داخلي (Internal Testing)
- حمّل AAB
- أضف المختبرين
- اختبر التطبيق

### 6.2 اختبار الإغلاق (Closed Testing)
- اختبار مع مجموعة محدودة

### 6.3 النشر العام (Production)
- بعد التأكد من عدم وجود مشاكل
- انقر على **Release to Production**

---

## الخطوة 7: البيانات الوصفية الكاملة

أكمل جميع الأقسام:
- **Main store listing**: العنوان، الوصف، الصور
- **Categorization**: الفئة والمحتوى
- **Pricing**: السعر والتوفر الجغرافي
- **App content**: تقييم المحتوى
- **Permissions**: صرح بالأذونات المطلوبة

---

## المشاكل الشائعة والحلول

### مشكلة: خطأ في التوقيع الرقمي
**الحل**: تأكد من وجود `key.jks` في المجلد الصحيح

### مشكلة: فشل بناء AAB
**الحل**: تحقق من:
- إصدار Android SDK
- إصدار Java (يجب أن يكون 11+)
- المتطلبات في `buildozer.spec`

### مشكلة: رفضت Google Play التطبيق
**الحل**: تحقق من:
- سياسة الخصوصية
- عدم انتهاك حقوق النشر
- المحتوى المناسب للعمر

---

## روابط مفيدة
- [Google Play Console](https://play.google.com/console)
- [Kivy Documentation](https://kivy.org/doc/stable/guide/packaging-android.html)
- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Android App Bundle](https://developer.android.com/guide/app-bundle)

# Joker-Assetsimport os
import subprocess
import sys

def install_requirements():
    # قائمة المكتبات التي يحتاجها تطبيقك (يمكنك تغييرها لاحقاً)
    libraries = ["requests", "colorama"] 
    
    print("جاري فحص وتثبيت المكتبات اللازمة...")
    
    for lib in libraries:
        try:
            # محاولة استيراد المكتبة للتأكد من وجودها
            __import__(lib)
            print(f"✅ {lib} مثبتة بالفعل.")
        except ImportError:
            # إذا لم تكن موجودة، يتم تثبيتها
            print(f"📥 جاري تثبيت {lib}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

    print("\n✨ تم التثبيت بنجاح! يمكنك الآن تشغيل التطبيق.")

if __name__ == "__main__":
    install_requirements()

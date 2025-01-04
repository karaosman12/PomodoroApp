import PyInstaller.__main__
import os
import shutil
import sys

def build_app():
    try:
        print("=== Pomodoro App Build Başlıyor ===")
        print(f"Python versiyonu: {sys.version}")
        
        # Ana klasöre git
        os.chdir('..')
        current_dir = os.getcwd()
        print(f"Çalışma klasörü: {current_dir}")
        
        # Masaüstü yolunu al
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        output_dir = os.path.join(desktop, 'PomodoroApp')
        
        print(f"\nÇıktı klasörü: {output_dir}")
        
        # Klasörleri temizle
        if os.path.exists(output_dir):
            print("Eski klasör temizleniyor...")
            shutil.rmtree(output_dir)
        
        # Template ve static klasörlerinin tam yolları
        templates_dir = os.path.join(current_dir, 'templates')
        static_dir = os.path.join(current_dir, 'static')
        icon_path = os.path.join(current_dir, 'build', 'app_icon.ico')
        
        print("\nKlasör yolları:")
        print(f"Templates: {templates_dir}")
        print(f"Static: {static_dir}")
        print(f"Icon: {icon_path}")
        
        # Dosyaların varlığını kontrol et
        required_files = {
            'run.py': os.path.exists('run.py'),
            'templates': os.path.exists(templates_dir),
            'static': os.path.exists(static_dir),
            'icon': os.path.exists(icon_path),
            'error.html': os.path.exists(os.path.join(templates_dir, 'error.html'))
        }
        
        print("\nDosya kontrolleri:")
        for file, exists in required_files.items():
            print(f"- {file}: {'✓' if exists else 'X'}")
        
        if not all(required_files.values()):
            raise Exception("Bazı gerekli dosyalar bulunamadı!")

        print("\nPyInstaller başlatılıyor...")
        PyInstaller.__main__.run([
            'run.py',
            '--name=PomodoroApp',
            '--onefile',
            '--windowed',
            f'--icon={icon_path}',
            f'--add-data={templates_dir};templates',  # Ana templates
            f'--add-data={os.path.join(templates_dir, "games")};templates/games',  # Oyunlar templates
            f'--add-data={static_dir};static',
            '--hidden-import=flask',
            '--hidden-import=werkzeug',
            '--hidden-import=jinja2',
            '--collect-all=flask',
            '--clean',
            f'--distpath={output_dir}'
        ])
        
        # README dosyasını kopyala
        readme_path = os.path.join(current_dir, 'build', 'README.txt')
        if os.path.exists(readme_path):
            shutil.copy(readme_path, output_dir)
            print("README dosyası kopyalandı")
        
        print("\n=== Build Tamamlandı! ===")
        print(f"Exe dosyası masaüstündeki PomodoroApp klasöründe:")
        print(output_dir)
        
    except Exception as e:
        print("\n!!! HATA !!!")
        print(str(e))
        raise e

if __name__ == "__main__":
    build_app()
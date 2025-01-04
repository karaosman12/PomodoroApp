=== POMODORO APP AÇIKLAMALAR ===

== DOSYA VE KLASÖR YAPISI ==

1. ANA KLASÖR (pomodoro_app)
   • app.py
     - Uygulamanın ana dosyası
     - Tüm sayfaların yönlendirmeleri burada
     - Flask uygulamasının temel ayarları

   • run.py
     - Uygulamayı başlatan dosya
     - Tarayıcıyı otomatik açar
     - Çevrimdışı çalışmayı sağlar

2. TEMPLATES KLASÖRÜ
   • base.html
     - Tüm sayfaların ortak şablonu
     - Menü ve footer burada
     - Bootstrap bağlantıları

   • index.html
     - Ana sayfa
     - Karşılama ekranı
     - Hızlı başlangıç butonları

   • timer.html
     - Pomodoro zamanlayıcısı
     - Çalışma ve mola süreleri
     - Sesli uyarılar

   • tasks.html
     - Görev listesi
     - Yapılacaklar yönetimi
     - İlerleme takibi

   • games/
     - index.html: Oyunlar ana sayfası
     - memory.html: Hafıza oyunu
     - minesweeper.html: Mayın tarlası

3. STATIC KLASÖRÜ
   • css/
     - style.css: Ana stil dosyası
     - games.css: Oyunlar için stiller

   • js/
     - timer.js: Zamanlayıcı kodları
     - tasks.js: Görev yönetimi
     - games/: Oyun kodları

   • img/
     - Resimler ve ikonlar
     - Arka plan görselleri

4. BUILD KLASÖRÜ
   • build.py
     - Exe oluşturma kodları
     - PyInstaller ayarları

   • build.bat
     - Windows için derleme başlatıcı
     - Tek tıkla build alma

   • app_icon.ico
     - Uygulama ikonu
     - Windows görev çubuğu ikonu

== NASIL ÇALIŞIR? ==

1. Uygulama Başlatma
   • PomodoroApp.exe'yi çalıştırın
   • Tarayıcı otomatik açılır
   • Localhost üzerinde çalışır

2. Zamanlayıcı Kullanımı
   • 25 dakika çalışma
   • 5 dakika kısa mola
   • 15 dakika uzun mola
   • Özelleştirilebilir süreler

3. Görev Yönetimi
   • Yeni görev ekle
   • Tamamlananları işaretle
   • İlerlemeyi takip et

4. Oyunlar
   • Mola zamanında eğlence
   • Zihin egzersizleri
   • Stres atma aktiviteleri

== ÖNEMLİ NOTLAR ==

1. Güvenlik
   • %100 çevrimdışı çalışır
   • Veri toplamaz
   • İnternet bağlantısı gerekmez

2. Kapatma
   • Görev çubuğunda simge var
   • Sağ tık > Çıkış
   • Görev yöneticisinden kapatılabilir

3. Bilinen Durumlar
   • İlk açılış 15-20 saniye sürebilir
   • Windows güvenlik uyarısı normal
   • Arka planda çalışmaya devam eder
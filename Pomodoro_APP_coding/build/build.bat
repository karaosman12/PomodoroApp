@echo off
echo === Pomodoro App Build Basliyor ===

:: Gerekli kütüphaneleri yükle
echo Gerekli kutuphaneler yukleniyor...
pip install -r build_requirements.txt

:: Build işlemini başlat
echo.
echo Build islemi basliyor...
python build.py

IF %ERRORLEVEL% NEQ 0 (
    echo.
    echo !!! Build sirasinda hata olustu !!!
    echo Hatayi gorebilmek icin bir tusa basin...
    pause
    exit /b 1
)

echo.
echo Build islemi tamamlandi!
echo Exe dosyasini masaustundeki PomodoroApp klasorunde bulabilirsiniz.
echo Cikmak icin bir tusa basin...
pause
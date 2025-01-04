from flask import Flask, render_template, request, jsonify
import webbrowser
import threading
import time
import os
import sys

def create_app():
    if getattr(sys, 'frozen', False):
        # Exe olarak çalışıyorsa
        template_folder = os.path.join(sys._MEIPASS, 'templates')
        static_folder = os.path.join(sys._MEIPASS, 'static')
        app = Flask(__name__, 
                   template_folder=template_folder,
                   static_folder=static_folder)
    else:
        # Normal Python olarak çalışıyorsa
        app = Flask(__name__)
    
    # Route'ları direkt burada tanımlayalım
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/timer')
    def timer():
        return render_template('timer.html')

    @app.route('/tasks')
    def tasks():
        return render_template('tasks.html')

    @app.route('/games')
    def games():
        try:
            return render_template('games/index.html')
        except Exception as e:
            print("Oyunlar sayfası hatası:", str(e))
            return f"Hata: {str(e)}", 500

    @app.route('/games/memory')
    def memory_game():
        try:
            return render_template('games/memory.html')
        except Exception as e:
            print("Hafıza oyunu hatası:", str(e))
            return f"Hata: {str(e)}", 500

    @app.route('/games/minesweeper')
    def minesweeper():
        try:
            return render_template('games/minesweeper.html')
        except Exception as e:
            print("Mayın tarlası hatası:", str(e))
            return f"Hata: {str(e)}", 500

    @app.route('/settings')
    def settings():
        return render_template('settings.html')

    # Hata sayfaları
    @app.errorhandler(500)
    def internal_error(error):
        return render_template('error.html', error=error), 500

    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('error.html', error=error), 404
    
    return app

def open_browser():
    """Tarayıcıyı 1.5 saniye sonra aç"""
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5000/')
    print("Tarayıcı açılıyor...")

def main():
    print("Uygulama başlatılıyor...")
    app = create_app()
    
    # Tarayıcıyı ayrı bir thread'de aç
    threading.Thread(target=open_browser).start()
    
    # Uygulamayı başlat
    app.run(host='127.0.0.1', port=5000, debug=False)

if __name__ == '__main__':
    main()
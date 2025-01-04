from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

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
    return render_template('games/index.html')

@app.route('/games/memory')
def memory_game():
    return render_template('games/memory.html')

@app.route('/games/minesweeper')
def minesweeper():
    return render_template('games/minesweeper.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    import webbrowser
    import threading
    import time
    
    def open_browser():
        """Tarayıcıyı 1.5 saniye sonra aç"""
        time.sleep(1.5)
        webbrowser.open('http://127.0.0.1:5000/')
        print("Tarayıcı açılıyor...")
    
    # Tarayıcıyı ayrı bir thread'de aç
    threading.Thread(target=open_browser).start()
    
    # Uygulamayı başlat
    print("Flask uygulaması başlatılıyor...")
    app.run(host='0.0.0.0', port=5000, debug=True)
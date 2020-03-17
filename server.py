import os
from flask import Flask, send_from_directory

app = Flask("SISL GUI", static_folder='build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')


if True:
    import webbrowser

    host = "0.0.0.0"
    port = 7001
    webbrowser.open(f'http://{host}:{port}', new=2)
    app.run(host=host, use_reloader=True, port=port, threaded=True)
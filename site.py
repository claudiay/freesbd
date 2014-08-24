import os

from flask import Flask, render_template, abort
from distros_installs import distros_installs


app = Flask(__name__)
app._static_folder = os.getcwd() + '/static'

@app.route('/')
def index():
    from placeholders import news, events, press, security
    return render_template('index.html',
            news=news,
            events=events,
            press=press,
            security=security
    )

@app.route('/about')
def about():
    return render_template('about/index.html')

@app.route('/docs')
def docs():
    return render_template('docs/index.html')

@app.route('/community')
def community():
    return render_template('community/index.html')

@app.route('/developers')
def developers():
    return render_template('developers/index.html')

@app.route('/support')
def support():
    return render_template('support/index.html')

@app.route('/download/<distro>')
def simple_install(distro=None):
    distro = distros_installs.get(distro)
    if not distro: abort(404)
    return render_template('simple_install.html', distro=distro)


if __name__ == '__main__':
    app.run(debug=True)


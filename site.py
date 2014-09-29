import os

from flask import Flask, render_template, abort, g, request
from distros_installs import distros_installs

from flask.ext.babel import Babel

app = Flask(__name__)
app._static_folder = os.getcwd() + '/static'
if app.debug:
    from flaskext.lesscss import lesscss
    lesscss(app)
#app.config.from_pyfile('mysettings.cfg')
babel = Babel(app)

@babel.localeselector
def get_locale():
    languages = ["en_US.ISO8859-1", "bn_BD.UTF-8", "da_DK.ISO8859-1", "de_DE.ISO8859-1",
        "el_GR.ISO8859-7", "es_ES.ISO8859-1", "fr_FR.ISO8859-1", "hu_HU.ISO8859-2",
        "it_IT.ISO8859-15", "ja_JP.eucJP", "mn_MN.UTF-8", "nl_NL.ISO8859-1", "pl_PL.ISO8859-2",
        "pt_BR.ISO8859-1", "ru_RU.KOI8-R", "sr_YU.ISO8859-2", "tr_TR.ISO8859-9", "zh_CN.UTF-8",
        " zh_TW.UTF-8"]
    return request.accept_languages.best_match(languages)

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


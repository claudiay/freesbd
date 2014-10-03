Redesign
============

To Run:
```bash
git clone https://github.com/claudiay/freesbd.git
cd freebsdorg/
bash setup.sh
```

Translations:

To compile for use (for new git clones, or after changes):
```bash
pybabel compile -d website/translations
```

If text changes in templates, to get new strings:
```bash
pybabel update -i messages.pot -d website/translations
```

To Do:
* new logo
* new install guide
* finish css compiler setup (adding bootstrap stuff?)
* summarize base text for rest of website
* add extras to setup script, including easy builds, pip/virtual including, dev/live mode
* easier way for people to get involved translating? including in dev mode only
* copying static files into static www/ dir for live mode


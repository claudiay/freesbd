Redesign
============

To Run:
```bash
# while in /var/www/
# make sure virtualenv is installed and working
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
* generate events and news
* new install guide
* finish css compiler setup (adding bootstrap stuff?)
* summarize base text for rest of website


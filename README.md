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

To extract strings for translation:
```bash
pybabel extract -F babel.cfg -o messages.pot website/
```

For new language (ex: 'de'),
```bash
pybabel init -i messages.pot -d website/translations -l de
```

After editing changes, to compile for use:
```bash
pybabel compile -d website/translations
```

If text changes, to get new strings:
```bash
pybabel update -i messages.pot -d website/translations
```


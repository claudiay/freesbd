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

For new language (ex: 'de'),
```bash
pybabel init -i messages.pot -d translations -l de
```

After editing changes, to compile for use:
```bash
pybabel compile -d translations
```

If text changes, to get new strings:
```bash
pybabel update -i messages.pot -d translations
```


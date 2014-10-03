#!/bin/sh
# Bash script to set up virtualenv and run dev server.
cwd=$(pwd)

echo "Setting up..."

# Set up virtual environment.
if [ ! -d $cwd/env ]; then
    echo "Creating virtualenv..."
    virtualenv --no-site-packages env
else
    echo "Virtualenv already exists."
    echo "If you want to set up a new one, please remove the env directory."
fi

# Install all dependencies in the virtual environment.
source env/bin/activate && pip install -r $cwd/requirements.txt

# Set up database.
#if [ ! -f "$cwd/something.db" ]; then
#    echo "Creating Database."
#    source env/bin/activate && python createdbs.py
#else
#    echo "Database already exists."
#    echo "To recreate database, delete current one and rerun script."
#fi

echo "Setup is done!"
echo "Starting up..."
source env/bin/activate && python website/site.py


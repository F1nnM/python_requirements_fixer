#!/bin/bash

python3 -m venv $2
. $2/bin/activate

pip install -r $1
pip freeze > $3
# Remove pkg-resources as it can cause problems on dockerbuild
#(see https://stackoverflow.com/questions/40670602/could-not-find-a-version-that-satisfies-the-requirement-pkg-resources-0-0-0)
sed -i '/pkg-resources/d' $3
deactivate
rm -r $2
exit 0
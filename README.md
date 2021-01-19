# opencv-basic

Collection of basic OpenCV applications.

## main.py
The simplest opencv application, it captures video from th camera and displays it.

## mog2.py
Uses a background subtraction technique to detect moving objects.

## haar.py
Uses the haar cascade algorythm to detect faces.

### To clear the pylint errors:
Run this command at the terminal:

> pylint --generate-rcfile > .pylintrc

At the beginning of the generated .pylintrc file you will see:

> \# A comma-separated list of package or module names from where C extensions may
> \# be loaded. Extensions are loading into the active Python interpreter and may
> \# run arbitrary code.
> extension-pkg-whitelist=

Add cv2 so you end up with:

> \# A comma-separated list of package or module names from where C extensions may
> \# be loaded. Extensions are loading into the active Python interpreter and may
> \# run arbitrary code.
> extension-pkg-whitelist=cv2

And add this setting to the error messages:
> [MASTER]
> disable=
>     C0114, # missing-module-docstring

Save the file. The lint errors should disappear.
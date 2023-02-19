# photo_rename

Go through a given directory and its subdirectories, copy all (image) files (with their metatdata) into a new "renamed" directory and rename the (image) files with a timestamp + the original filename, while keeping the directory structure. This will not rename the original files. If the renamed directory does not exist, it will be created. 

For the timestamp it will try to read the creation time from the exif data, or the creation date from the file itelf and if that does not work it will use the last modified timestamp. The Tkinter filedialog.askdirectory function is used to present a file dialog for the user to choose a photo directory.

Requires tkinter and Pillow.

Use at you own risk.
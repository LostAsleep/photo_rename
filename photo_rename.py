"""
Go through a given directory and its subdirectories, copy all (image) files (with their metatdata) into a new "renamed" directory and rename the (image) files with a timestamp + the original filename, while keeping the directory structure. This will not rename the original files. If the renamed directory does not exist, it will be created. 

For the timestamp it will try to read the creation time from the exif data, or the creation date from the file itelf and if that does not work it will use the last modified timestamp. The Tkinter filedialog.askdirectory function is used to present a file dialog for the user to choose a photo directory.

Use at you own risk.
"""


import os
import tkinter as tk
from tkinter import filedialog
import datetime
import shutil
from PIL import Image


def choose_directory():
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    return directory


def rename_photos(directory):
    image_types = ["TIFF", "JPEG", "JPG", "PNG", "Webp", "HEIC", "PNG"]
    renamed_directory = os.path.join(directory, "renamed")
    if not os.path.exists(renamed_directory):
        os.makedirs(renamed_directory)
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(subdir, file)
            file_type = ""
            try:
                with Image.open(full_path) as img:
                    file_type = img.format
            except:
                pass
            if file_type in image_types:
                try:
                    date = img._getexif()[36867]
                    date = datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S")
                except:
                    date = os.path.getctime(full_path)
                    date = datetime.datetime.fromtimestamp(date)
                new_file_name = (
                    date.strftime("%Y-%m-%d_%H-%M-%S") + "_" + file.replace(" ", "-")
                )
            else:
                date = os.path.getctime(full_path)
                date = datetime.datetime.fromtimestamp(date)
                new_file_name = (
                    date.strftime("%Y-%m-%d_%H-%M-%S") + "_" + file.replace(" ", "-")
                )
            subdir_split = subdir.split(directory)[-1].lstrip(os.path.sep)
            new_directory = os.path.join(renamed_directory, subdir_split)
            if not os.path.exists(new_directory):
                os.makedirs(new_directory)
            new_full_path = os.path.join(new_directory, new_file_name)
            shutil.copy2(full_path, new_full_path)


directory = choose_directory()
rename_photos(directory)

import os
import shutil

file_exts = [
    ["Audio", ".aif", ".cda", ".mid", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"],
    ["Compressed", ".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"],
    ["Executable", ".apk", ".exe"],
    ["Image", ".ai", ".bmp", ".gif", ".ico", ".jpeg", ".jpg", ".png", ".ps", ".psd", ".svg", ".tif"],
    ["Video", ".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", ".mpg", ".mpeg", ".rm", ".swf",
     ".vob", ".wmv"],
    ["Text", ".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wks", ".wpd"]
]

download_path = os.path.expanduser("~") + "/Downloads/"
audio_path = os.path.expanduser("~") + "/Music/"
image_path = os.path.expanduser("~") + "/Pictures/"
video_path = os.path.expanduser("~") + "/Videos/"
documents_path = os.path.expanduser("~") + "/Documents/"


def change_dir(file_type, file_name, file_ext):
    if file_type == 'Audio':
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{audio_path}/{file_name}{file_ext}")
    elif file_type == "Video":
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{video_path}/{file_name}{file_ext}")
    elif file_type == "Image":
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{image_path}/{file_name}{file_ext}")
    elif file_type == "Text":
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{documents_path}/{file_name}{file_ext}")
    elif file_type == "Executables":
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{documents_path}/Programs/{file_name}{file_ext}")
    elif  file_type == "Compressed":
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{documents_path}/Compressed Files/{file_name}{file_ext}")


isext = True
for i in os.listdir(download_path):
    file_name, file_ext = os.path.splitext(i)
    for j in file_exts:
        if file_ext in j:
            change_dir(j[0], file_name, file_ext)
            isext = False
    if isext:
        shutil.move(f"{download_path}/{file_name}{file_ext}", f"{documents_path}/Unknown Files/{file_name}{file_ext}")
    isext = True

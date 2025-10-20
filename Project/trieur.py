#Project Udemy

#trier les fichiers selon leur extensions

from pathlib import Path

data = {
    ".mp3" : "Musique",
    ".wav" : "Musique",
    ".flac" : "Musique",
    ".avi" : "Videos",
    ".mp4" : "Videos",
    ".gif" : "Videos",
    ".bmp" : "Images",
    ".png" : "Images",
    ".jpg" : "Images",
    ".txt" : "Documents",
    ".pptx" : "Documents",
    ".csv" : "Documents",
    ".xls" : "Documents",
    ".odp" : "Documents",
    ".pages" : "Documents"}

dir = Path.cwd() / "data"
files = [f for f in dir.iterdir() if f.is_file()]
for g in files:
    out = dir / data.get(g.suffix, "Divers")
    out.mkdir(exist_ok=True)
    g.rename(out / g.name)

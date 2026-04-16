import os
import shutil
from app.config import config

def save_uploaded_file(file_content, filename):
    os.makedirs(config.UPLOAD_DIR, exist_ok=True)
    path = os.path.join(config.UPLOAD_DIR, filename)
    with open(path, "wb") as f:
        f.write(file_content)
    return path

def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)
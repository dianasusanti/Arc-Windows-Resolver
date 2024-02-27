import os
import subprocess
import time
import shutil

subprocess.run(["taskkill", "/IM", "Arc.exe", "/F"])

time.sleep(3)

local_appdata = os.environ.get('LOCALAPPDATA')
dir_to_remove = os.path.join(local_appdata, r'Packages\TheBrowserCompany.Arc_ttt1ap7aakyb4\LocalCache\Local\firestore\Arc\bcny-arc-server\main')

print(f"Menghapus direktori '{dir_to_remove}'...")
shutil.rmtree(dir_to_remove)

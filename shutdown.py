import os
import time

while os.listdir(' *your steam downloading directory here* ') != []:
  print('Download in progress..')
  time.sleep(5)

print('Folder empty. Downloads complete')
os.system("Shutdown /s /t 1")

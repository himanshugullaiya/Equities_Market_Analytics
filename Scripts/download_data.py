import pandas as pd
import requests
import os
import zipfile
from datetime import date, timedelta


def format_date(the_date):
    day = str(the_date.day).zfill(2)       #..format dates...#
    month = str(the_date.month).zfill(2)
    year = str(the_date.year)[-2:]
    date_formatted = f'{day}{month}{year}'
    return date_formatted
    
latest_zipfile_name = ''
latest_date = ''

def download_files(starting_date, ending_date):
    global latest_zipfile_name
    
    #....Bhavcopy....#

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Referer": "https://www.nseindia.com/",
    "Accept": "*/*",
    }
    
    curr_date = starting_date
    delta = timedelta(days = 1)
    
    while curr_date < ending_date:
        curr_date += delta
        if curr_date.weekday() >= 5:    #..skip weekends..#
            continue
        
        date_formatted = format_date(curr_date)
        
        bhav_url = f"https://nsearchives.nseindia.com/archives/equities/bhavcopy/pr/PR{date_formatted}.zip"
        print(f'Downloading File : PR{date_formatted}.zip\n')
        bhav_response = requests.get(url = bhav_url, headers = headers)
    
        if bhav_response.status_code != 200:  #..market_holiday
            print(f'Skipped : {date_formatted} - Holiday/Not Avail')
            continue
        
        #.. Zip file...#
        
        zip_folder = '../Data/Stock_Data/Zips'
        os.makedirs(zip_folder, exist_ok = True)     #.. if zip path folder not avail make it
        
        zip_path = f'../Data/Stock_Data/Zips/PR{date_formatted}.zip'
        with open(zip_path,'wb') as f:
            f.write(bhav_response.content)
        print(f'Saved {date_formatted} Zip')
        
        latest_zipfile_name = zip_path
        latest_date = date_formatted
        
    
    #... Market Report Download....#
    
    
    mr_path = f'../Data/Other_Csvs/MA{latest_date}.csv'
    mr_url = f'https://nsearchives.nseindia.com/archives/equities/mkt/MA{latest_date}.csv'
    mr_response = requests.get(url = mr_url, headers = headers)

    if mr_response.status_code == 200:
        with open(mr_path, 'wb') as f:
            f.write(mr_response.content)
        print(f'Saved {date_formatted} MR File')
    else:
        print('Error in MR')
        
        
    #.. PE Ratio ...#
        
    pe_path = f'../Data/Other_Csvs/PE_{latest_date}.csv'
    pe_url = f'https://nsearchives.nseindia.com/content/equities/peDetail/PE_{latest_date}.csv'
    pe_response = requests.get(pe_url, headers = headers)
    
    if pe_response.status_code == 200:
        with open(pe_path, 'wb') as f:
            f.write(pe_response.content)
        print(f'Saved {latest_date} PE File')
        
        
    #.. 52 Week HL ...#
    
    second_date_formatted = latest_date[:-2] + '20' + latest_date[-2:]
    
    wk_path = f'../Data/Other_Csvs/CM_52_wk_High_low_{second_date_formatted}.csv'
    wk_52_hl_url = f'https://nsearchives.nseindia.com/content/CM_52_wk_High_low_{second_date_formatted}.csv'
    wk_response = requests.get(wk_52_hl_url, headers = headers)
    
    if wk_response.status_code == 200:     
        with open(wk_path, 'wb') as f:
            f.write(wk_response.content)
        print(f'Saved 52 Week High Low File')
           


def extract_bhavcopy():
    global latest_zipfile_name
    #...Extract Csvs..#
    
    Other_csvs  = '../Data/Other_csvs'
    zips_folder = '../Data/Stock_Data/Zips'
    csvs_folder = '../Data/Stock_Data/Csvs'
    os.makedirs(csvs_folder, exist_ok = True)
    
    
    for zip_filename in os.listdir(zips_folder):
        if not zip_filename.endswith('.zip'):       #make sure the filename ends with zip, else skip this iteration
            continue
        zip_path = os.path.join(zips_folder, zip_filename)
    
        with zipfile.ZipFile(zip_path, 'r') as z:
            for file in z.namelist():
                if file.lower().startswith('pd'):
                    new_name = file.capitalize()
                    if len(file) > 12:
                        new_name = new_name[:6]+new_name[8:]
                    with z.open(file) as source:
                        with open(os.path.join(csvs_folder, new_name), 'wb') as target:
                            target.write(source.read())
                        
                    #z.extract(file, csvs_folder)
                    print(f'Extracted as : {new_name}')
                                   
    
    #........Extracting Other files of latest_date...#
    print(f'The lastest File : {latest_zipfile_name}')
    
    if latest_zipfile_name.endswith('.zip'):       #make sure the filename ends with zip, else skip this iteration
        with zipfile.ZipFile(latest_zipfile_name, 'r') as z:
            for file in z.namelist():
                if file.lower()[:2] in ('gl', 'hl', 'mc') :
                    z.extract(file, Other_csvs)
                    print(f'Extracted: {file}')
    
    

def master_func():
    starting_date = date(2025,4,15)
    ending_date = date.today()
    download_files(starting_date, ending_date)
    extract_bhavcopy()
    
master_func()

    
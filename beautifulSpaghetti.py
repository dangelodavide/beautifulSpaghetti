#%% Install
import subprocess
import sys
def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
install_dependencies()
#%% Libraries
from termcolor import colored
import time
from bs4 import BeautifulSoup
import requests
import os
import csv
from urllib.parse import urljoin
from pathlib import Path
#%% ASCII 
def print_ascii_art():
    title = "beautifulSpaghetti_v1.0.0"
    ascii_art = """
    _____________________$$$
    ____________________$___$
    ____________________$$$
    ___________________$_$
    ___________________$_$
    __________________$$$_$$$
    ________________$$__$$$__$$$
    ______________$$__$$$$$$$___$
    _____________$_______________$
    ____________$_________________$
    ____________$_________________$
    ____________$_____$$$$$$$$$$$$$$$
    ____________$____$_______________$
    ____________$____$___$$$$$$$$$$$$$
    ____________$___$___$___________$$$
    ____________$___$___$_$$$___$$$__$$
    ____________$___$___$_$$$___$$$__$$
    ____________$___$___$___________$$$
    ____________$____$___$$$$$$$$$$$$$
    ____________$_____$$$$$$$$$$$$$$
    ____________$_________________$
    ____________$____$$$$$$$$$$$$$$
    ____________$___$__$__$__$__$__$
    ____________$__$$$$$$$$$$$$$$
    ____________$__$___$__$__$__$__$
    ____________$___$$$$$$$$$$$$$$$
    ____________$$$_________________$$$
    ________$$___$$$_________$$$$$___$$
    _____$$________$$$$$$$$$__________$$$
    ____$__$$_____________________$$$$___$$
    __$$$$$___$$$$$$$$______$$$$$$$_______$_$
    $__$$____________________________$$$$___$$
    $_____$_____________________$$$$$$$_______$$
    $$$____$___$$$$$$$$$$$$__________$_______$_$
    $___$$$_____$____________________________$_$_$
    $_____$___$______________$$$$$$$$$$$___$_$_$$
    $___$__$__$$__$________________________$__$_$$
    $_____$$_$$____$_______________$$$____$__$_$__$"""
    
    max_line_length = max(len(line) for line in ascii_art.split('\n'))
    title_length = len(title)
    padding = (max_line_length - title_length) // 2

    print(colored(" " * padding + title, 'green'))
    print(colored(ascii_art, 'green'))
print_ascii_art()
#%% Authorization
def continue_program():
    user_input = input("Are you authorized to use the program? (Y/N): ")
    return user_input.upper() == 'Y'
#%% Fake Loading
def fake_loading():
    print(colored("Loading...", 'white'))
    for i in range(1, 11):
        time.sleep(0.3)  
        sys.stdout.write(colored("\r[" + "=" * i + " " * (10 - i) + "] " + str(i * 10) + "%", 'white'))
        sys.stdout.flush()
    print(colored("\nLoading complete!", 'white'))
#%% User Input (Website Link)
def get_user_input():
    return input(colored("Enter the link of the website you want to scrape: ", 'white'))
#%% Create a beautifulSpaghetti Folder
def create_beautiful_spaghetti_folder():
    documents_folder = Path.home() / "Documents"
    beautiful_spaghetti_folder = documents_folder / "beautifulSpaghetti"
    
    # Create a beautifulSpaghetti's folder
    beautiful_spaghetti_folder.mkdir(parents=True, exist_ok=True)
    
    # Create folders for HTML, Img & Tabs
    html_folder = beautiful_spaghetti_folder / "html"
    images_folder = beautiful_spaghetti_folder / "images"
    tables_folder = beautiful_spaghetti_folder / "tables"
    
    html_folder.mkdir(exist_ok=True)
    images_folder.mkdir(exist_ok=True)
    tables_folder.mkdir(exist_ok=True)
    
    return html_folder, images_folder, tables_folder
#%% Web Scraping Logic
def scrape_website(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # !!! Restart Check !!!
        restart_program = False
        # User Input
        save_html = input(colored("Do you want to save the HTML file? (Y/N): ", 'white')).upper() == 'Y'
        time.sleep(0.3)  
        save_images = input(colored("Do you want to save images from the website? (Y/N): ", 'white')).upper() == 'Y'
        time.sleep(0.3)  
        save_tables = input(colored("Do you want to save tables from the website? (Y/N): ", 'white')).upper() == 'Y'
        # If not 
        if not (save_html or save_images or save_tables):
            print("Restarting the process.")
            restart_program = True  # !!! Variable Check !!!
        # HTML
        if save_html:
            html_folder, _, _ = create_beautiful_spaghetti_folder()
            html_file_path = html_folder / 'beautifulSpaghetti.html'
            with open(html_file_path, 'w', encoding='utf-8') as html_file:
                html_file.write(response.text)
            print(colored(f"HTML file saved at: {html_file_path}", 'white'))
        # IMG
        if save_images:
            _, images_folder, _ = create_beautiful_spaghetti_folder()
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                img_url = img_tag.get('src')
                img_url = urljoin(url, img_url)
                img_data = requests.get(img_url).content
                img_name = images_folder / os.path.basename(img_url)
                with open(img_name, 'wb') as img_file:
                    img_file.write(img_data)
            print(colored(f"Images saved in the 'images' folder at: {images_folder}", 'white'))
        # Tabs
        if save_tables:
            _, _, tables_folder = create_beautiful_spaghetti_folder()
            table_tags = soup.find_all('table')
            for idx, table_tag in enumerate(table_tags):
                table_name = tables_folder / f'table_{idx + 1}.csv'
                with open(table_name, 'w', newline='', encoding='utf-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    for row in table_tag.find_all('tr'):
                        csv_writer.writerow([col.get_text(strip=True) for col in row.find_all(['th', 'td'])])
            print(colored(f"Tables saved in the 'tables' folder at: {tables_folder}", 'white'))

        return restart_program  # !!! TRUE IF WE NEED A RESTART !!!

    except Exception as e:
        print(colored("An error occurred during scraping:", e, 'white'))
        return False
#%% Run
if continue_program():
    fake_loading()
    
    while True:
        url = get_user_input()
        restart_program = scrape_website(url)
        
        if not restart_program:
            break  # Break loop

        restart = input("Do you want to scrape another website? (Y/N): ").upper()
        if restart != 'Y':
            break  # Break loop
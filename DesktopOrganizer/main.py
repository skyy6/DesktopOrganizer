## Fredrik Jacobsson 2023 ##

import os.path
import shutil

##Bara att lägga till filformat nedan om behovet finns. Värdet för nycklarna är den mapp som filerna ska tillhöra
extension_folders = {
    '.png' : 'Bilder', 
    '.jpeg' : 'Bilder',
    '.webp' : 'Bilder', 
    '.jpg'  : 'Bilder', 
    '.mp3' : 'Audio',
    '.wav' : 'Audio',
    '.mp4' : 'Videos',
    '.txt' : 'Textfiler',
    '.doc' : 'Textfiler', 
    '.docx' : 'Textfiler',
    '.zip' : 'Zip',
    '.rar' : 'Zip',
    '.lnk' : 'Shortcuts',
    '' : 'Folders',
    'MISC' : 'Misc'
}



desktop_path = 'C:/Users/skyy6/Desktop'

misc_path = 'Misc'

def create_directories():
    
    for val in extension_folders.values():
        
        desktop_folder = desktop_path + '/' + val
        isExist = os.path.exists(desktop_folder) # Kan hanteras bättre utan att hårdkoda in slash på samtliga ställen
        if not(isExist):
            os.mkdir(desktop_folder)
    

def organize_files(file, path): 
    
    source_path =  desktop_path + '/' + file
    dest_path = desktop_path + '/' + path + '/' + file
     
    shutil.move(source_path, dest_path)
        
def find_file_extension():    
    for file_name in os.listdir(desktop_path):
        dummy_name, extension = os.path.splitext(file_name)
        
        if(file_name in extension_folders.values()):
            continue        
        
        if(extension in extension_folders):
            path = extension_folders[extension]
            organize_files(file_name, path)
        
        else:
            organize_files(file_name, misc_path)
            
          
create_directories()
find_file_extension()
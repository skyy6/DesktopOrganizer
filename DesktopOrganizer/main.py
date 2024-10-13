import os.path
import shutil

extension_folders = {
    '.png' : 'Bilder', 
    '.jpeg' : 'Bilder',
    '.webp' : 'Bilder', 
    '.jpg'  : 'Bilder', 
    '.mp3' : 'Audio',
    '.wav' : 'Audio',
    '.mp4' : 'Video',
    '.txt' : 'Textfiler',
    '.doc' : 'Textfiler', 
    '.docx' : 'Textfiler',
    '.zip' : 'Zip',
    '.rar' : 'Zip',
    '.lnk' : 'Shortcuts',
    '' : 'Folders'
}

deskPath = 'C:/Users/skyy6/Desktop'

miscPath = 'Misc'

def OrganizeFiles(file, path):
    isExist = os.path.exists(deskPath + '/' + path)
    if not(isExist):
        os.mkdir(deskPath + '/' + path)
        
    shutil.move(deskPath + '/' + file, deskPath + '/' + path + '/' + file)
        
def FindFileExt():    
    for file in os.listdir(deskPath):
        if(file not in extension_folders.values() and file != miscPath):
            filename, extension = os.path.splitext(file)
            if(extension in extension_folders):
                path = extension_folders[extension]
                OrganizeFiles(file, path)
            else:
                OrganizeFiles(file, miscPath)
                     
FindFileExt()
import os, shutil 

path = r"C:/Users/user/Desktop/Test/"
file_name = os.listdir(path)

#List of the folders that will create and store it in folder_names variable
folder_names = ['Pdf Files', 'Word Files', 'Excel Files', 'Video Files', 'Picture Files','PPT Files']

#Iterates over the list of the folder names and creates each folder if it does not already exist within the directory specified by the path variable.
for i in folder_names:
  if not os.path.exists(os.path.join(path, i)):
    os.makedirs(os.path.join(path, i))

#Dictionary that maps file extensions to corresponding folder names where files with those extensions should be organized.
folder_mapping = {
    '.pdf': 'Pdf Files',
    '.xlsx': 'Excel Files',
    '.png': 'Picture Files',
    '.mp4': 'Video Files',
    '.docx': 'Word Files',
    '.pptx':  'PPT Files'
}

#Iterates over each file name in the file_name list, extracts the file extension using the os.path.splitext() function, and assigns it to the variable extension. 
for file in file_name:
  _, extension = os.path.splitext(file)

#Checks the contents in extension in the folder_mapping
  if extension in folder_mapping:
    source_file = os.path.join(path, file) 
    destination_file = os.path.join(path, folder_mapping[extension], file)
    if not os.path.exists(destination_file):
      shutil.move(source_file, destination_file)

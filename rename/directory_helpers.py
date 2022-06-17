from file_helpers import get_files, multi_generate,multi_generate
def get_directories(directory_string):
   return directory_string.split(',')

def wordrename_directory(directory_name,replaced,replaced_with,output):
  directories  = get_directories(directory_name)
  for directory in directories:
    files = get_files(directory)
    for file in files:
      multi_generate(f"{directory}/{file}",replaced,replaced_with,output)
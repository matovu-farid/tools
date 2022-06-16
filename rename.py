import sys
import getopt

import os


def get_files(directory):
  obj = os.scandir(directory)
  entrylist = list(filter(lambda x: x.is_file,obj))
  return list(map(lambda x: x.name,entrylist))

def generate_files(input_name,replaced,replaced_with,output_name):

    file = open(input_name,"r")
    input_name
    extension = os.path.splitext(input_name)[1]
    print(extension)
    created_name = f"{input_name}_output{extension}"
    print(created_name)

    output = open(output_name or created_name,"w")

    lines= file.readlines()

    output_array = []
    for line in lines:
      sanitized = line.replace(replaced,replaced_with)
      output_array.append(sanitized)


    output.writelines(output_array)  

    file.close()
    output.close()
    print("Rename succesfull 😀")

def multi_generate(input_name,replaced,replaced_with,output_name):

  replaced_array = replaced.split(',')
  with_array = replaced_with.split(',')
  if len(replaced_array) != len(with_array):
    print("The input replaced anguments must match those they are replaced with")
    sys.exit(5)
  for i in range(len(replaced_array)):
    generate_files(input_name,replaced_array[i],with_array[i],output_name)

  


def main(argv):
    arg_input = ""
    arg_output = ""
    arg_replaced = ""
    arg_directory = ""
    arg_with=""
    arg_help = f"{argv[0]} -[i <input>| -d <directory>] -o <output> -r <replaced>  -w <with> "
    
    try:
        opts, _ = getopt.getopt(argv[1:], "hd:i:r:w:o:", ["help", "directory=","input=", 
        "replaced=","with=", "output="])

        

    except:
        print(arg_help)
        sys.exit(2)
    for opt,arg in opts:
      if opt in ("-i","--input"):
        arg_input = arg
      elif opt in ("-o","--output"):
        arg_output = arg
      elif opt in ("-r","--replaced"):
        arg_replaced = arg
      elif opt in ("-w","--with"):
        arg_with = arg
      elif opt in ("-d","--directory"):
        arg_directory = arg
    if(arg_replaced == ''):
      print("Please insert the word replaced")
      sys.exit(3)
    if(arg_with == ''):
      print("Please insert the word that is replpaceing it")
      sys.exit(4)

    if(arg_input != ''):  
      multi_generate(arg_input,arg_replaced,arg_with,arg_output)
    if arg_directory!= '':
      files = get_files(arg_directory)
      for file in files:
        multi_generate(f"{arg_directory}/{file}",arg_replaced,arg_with,arg_output)


if __name__ == "__main__":
    main(sys.argv)

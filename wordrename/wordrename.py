import sys
import getopt
from help_string import help_string
from file_helpers import wordrename_file
from directory_helpers import wordrename_directory

def main(argv):
    arg_input = ""
    arg_output = ""
    arg_replaced = ""
    arg_directory = ""
    arg_with=""
    arg_help = help_string
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
      elif opt in ("-h","--help"):
        print(arg_help)
        sys.exit(2)
  
    if(arg_input == "" and arg_directory == ""):
      print("Please provide the input file or a directory 🧐")
      sys.exit(6)
    if(arg_replaced == ''):
      print("Please insert the word replaced 🧐")
      sys.exit(3)
    if(arg_with == ''):
      print("Please insert the word that is replpaceing it 🧐")
      sys.exit(4)

    if(arg_input != ''):  
      wordrename_file(arg_input,arg_replaced,arg_with,arg_output)
    if arg_directory!= '':
      wordrename_directory(arg_directory,arg_replaced,arg_with,arg_output)








if __name__ == "__main__":
    main(sys.argv)


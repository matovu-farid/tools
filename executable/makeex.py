import os
import sys
import getopt
import errno
from help_string import help_string
def main(argv):
    arg_input = ""
    arg_output = ""

    arg_help = help_string
    try:
        arg_input = argv[1]
        opts, _ = getopt.getopt(argv[2:], "ho:", ["help", "output="])

    except:
        print(arg_help)
        sys.exit(2)
    for opt,arg in opts:
      if opt in ("-o","--output"):
        arg_output = arg

      elif opt in ("-h","--help"):
        print(arg_help)
        sys.exit(2)
  
    if(arg_input == ""):
      print("Please provide the input file or a directory 🧐")
      sys.exit(3)
    create_executable(arg_input,arg_output)

   
def create_executable(input_name,output_name):

    file = open(input_name,"r")
    created_name = os.path.splitext(input_name)[0]
    final_output_name = output_name or created_name

    output = open(final_output_name,"w")
    lines= file.readlines()
    lines.insert(0,"#!/usr/bin/env python3\n")
    output.writelines(lines)  

    file.close()
    output.close()
    os.chmod(final_output_name,0o755)
    
    
    print("Created executable succesfull 😀")

    try:
      output = os.path.basename(final_output_name)
      os.symlink(os.path.join(os.path.abspath(final_output_name)), os.path.join('/usr/bin/',output))
      print("Successfully added a symlink 😀")
    except OSError as e:
      if e.errno != errno.EEXIST:
            raise  
   
   

if __name__ == "__main__":
    main(sys.argv)

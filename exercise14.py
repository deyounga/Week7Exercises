#exercise 14.1

import os
import string


def sed(pstring, rstring, file1, file2):

    if os.path.isfile(file1):
        ofile = open(file1)
    else:
        print("not a valid file")

    wfile = open(file2, "w")

    for line in ofile:
        line = (line.strip(string.punctuation + "\n" + ".")).lower()
        print(line)
        print(pstring in line)
        
        if pstring in line:
            line = line.replace(pstring, rstring)
            print(line)

        wfile.write(line + "\n")

    wfile.close()
    ofile.close()



    

    

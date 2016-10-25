#!/usr/bin/env python
import os, datetime, time, sys 
from cgi import logfile
def main(argv):
    try:
        for argcheck in argv:
            if os.path.exists(argcheck):
                print(argcheck + ": Path Available")
            else:
                print(argcheck + ": Path Not Available")
                
        if argv != []:
            for arg in argv:
                if os.path.exists(arg):
                    folder = arg
                    folder_size = 0
                    no_files = 0
                    no_dirs = 0
                    curr_time = time.strftime('%Y-%m-%d-%H:%M:%S')
                    curr_date = time.strftime('%Y-%m-%d')
                    logfile = "/tmp/FolderStats-" + str(curr_date)
                    
                    for (path, dirs, files) in os.walk(folder):
                        for d in dirs:
                            no_dirs += 1
                            d_name = os.path.join(path, d)
                            d_size = os.path.getsize(d_name)
                            d_size_mb = "%0.1f MB" % (d_size/(1024*1024.0))
                            
                        for f in files:
                            filename = os.path.join(path, f)
                            folder_size += os.path.getsize(filename)
                            no_files += 1
                            
                    mod_time = os.path.getmtime(folder)
                    print("Folder Name: " + str(folder))
                    print("No of Sub Dirs: " + str(no_dirs))
                    print "Folder = %0.1f MB" % (folder_size/(1024*1024.0))
                    foldersize = "%0.1f MB" % (folder_size/(1024*1024.0))
                    print "Folder Modification Time: " + datetime.datetime.fromtimestamp(int(mod_time)).strftime('%Y-%m-%d %H:%M:%S')
                    foldermtime = datetime.datetime.fromtimestamp(int(mod_time)).strftime('%Y-%m-%d-%H:%M:%S') 
                    print "Total Number of Files: " + str(no_files)
                    
                    with open(logfile, 'a') as w2f:
                        w2f.write(str(curr_time) + " " + str(folder) + " " + str(foldermtime) + " " + str(foldersize) + " " + str(no_files) + "\n")
                else:
                    pass
        else:
            print("Pass folder names as command line arguments")
            print("Usage: ./FolderSize Folder1 Folder2 Folder3 Folder4")                
                    
    except IndexError:
        print "list index out of range"
    except OSError:
        print(sys.exc_info())
    except:
        print(sys.exc_info())

if __name__ == "__main__":
    main(sys.argv[1:])
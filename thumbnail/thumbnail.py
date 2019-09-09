import os
import cv2

home = os.getcwd()
print(home)

folder = os.listdir(home)
print(folder)

image_folder_path = os.chdir(home+"/upload_images")
new_folder_path = os.getcwd()
image_folder = os.listdir(new_folder_path)
print(new_folder_path)
print(image_folder)

def check_folder(path,list):
    #print path, list
    for i in list:
        newpath = os.path.join(path,i)
        #print newpath
        if os.path.isdir(newpath):
            print "checking directory"
            newlist = os.listdir(newpath)
            check_folder(newpath,newlist)
        else:
            filetype = i.split(".")[-1].upper()
            is_thumbnail = i.split("-")[1]
            if filetype == "PDF" or filetype == "TXT" or filetype == "XLS" or filetype == "XLSX":
                print "this is not a picture", i
            elif is_thumbnail == "thumb":
                print "already have thumbnail", i
            else:
                print "let's edit this picture", i
                img = cv2.imread(os.path.join(path,i))
                large_height, large_width, channels = img.shape
                # print height, width, channels
                ratio = float(large_width) / float(large_height)
                max_height = 208*3
                max_width = 180*3
                # print(ratio)
                if ratio > 1.15:
                    width = float(max_width)
                    height = float(large_height)*(float(max_width)/float(large_width))
                    dim = (int(width), int(height))
                    resized = cv2.resize(img, dim, interpolation= cv2.INTER_AREA )
                else:
                    width = float(large_width)*(float(max_height)/float(large_height))
                    height = float(max_height)
                    dim = (int(width), int(height))
                    resized = cv2.resize(img, dim, interpolation= cv2.INTER_AREA )
                
                new_name = i.split("-")
                new_name.insert(1, "thumb")
                new_thumb = '-'.join(new_name)
                cv2.imwrite(os.path.join(path,new_thumb), resized)

check_folder(new_folder_path, image_folder)


from downloadFIlesFromS3 import downloadFile
import uploadFilesToS3
import tkinter
from tkinter import filedialog
import config
import boto3
from tkinter import *

s3 = boto3.client("s3", aws_access_key_id=config.access_key,
                  aws_secret_access_key=config.secret_access_key)
top = tkinter.Tk()
top.geometry("750x500")

# Create a canvas object
# canvas = tkinter.Canvas(top, width=500, height=200,)

Lb1 = Listbox(top, width=100)


def browseFiles():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      ".txt"), ("PDF Files", ".pdf"),
                                                     ("all files",
                                                      ".\*")))
    filename = filename.replace('/', '\\')
    print(filename)

    uploadFilesToS3.upload_file(filename)
    # exit()


def downloadFiles():
    #text.insert(END, content)
    FileToDownload = textbox.get(1.0, END)
    FileToDownload = FileToDownload.strip()
    # print(len(FileToDownload))
    downloadFile(FileToDownload)
    # exit()


button = tkinter.Button(top, text='UPLOAD', command=browseFiles)
textbox = tkinter.Text(top, width=50, height=1)
button2 = tkinter.Button(top, text='DOWNLOAD', command=downloadFiles)
files = 'Files available in the bucket:\r\n'
s3_matadata = s3.list_objects(Bucket=config.bucket_name)
if 'Contents' in s3_matadata:
    i = 1
    for key in s3.list_objects(Bucket=config.bucket_name)['Contents']:
        # files += key['Key'] + '\r\n'
        Lb1.insert(i, key['Key'])
        i += 1
else:
    files += 'No Files in S3'

# Add a text in Canvas
# canvas.create_text(250, 150, text=files, fill="black",
#                    font=('Helvetica 15 bold'))
# canvas.pack()

Lb1.pack()
button.pack()
textbox.pack()
button2.pack()
top.mainloop()

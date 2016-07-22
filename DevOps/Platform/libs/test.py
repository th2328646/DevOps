import time
import os


def handle_uploaded_file(f):
    file_name = ""
    try:
        path = "F:\\bak\\" + time.strftime('%Y%m%d\\')
        if not os.path.exists(path):
            os.makedirs(path)
        file_name = path + f.name
        destination = open(file_name, 'wb+')
        for chunk in f.chunks():
            destination.write(chunk)
        destination.close()
    except Exception, e:
        print e
    return file_name

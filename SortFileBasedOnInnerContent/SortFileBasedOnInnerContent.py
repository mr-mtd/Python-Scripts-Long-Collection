import os
import shutil
import time
import calendar


if __name__ == '__main__':
   # path = r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/edi210_unorganized/file_from_jacob'


    path = r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/invoicesByCarrier/CHR_1-22-20/1_by_1'


    car_TQYL = "TQYL"
    car_CHRB = "RBTWTEST"
    car_PRIM = "PRIM"
    car_MTEN = "MTEN"

    path_TQYL=r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/edi210_test_files/TQYL/'
    path_CHRB=r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/edi210_test_files/RBTWTEST/'
    path_PRIM=r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/edi210_test_files/PRIM/'
    path_MTEN=r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210-docs/edi210_test_files/MTEN/'



    print('file path is: ' + path)

    # Create an array for storing files
    files = []

    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            # place all file names in a list
            files.append(os.path.join(r, file))

    for index,fname in enumerate(files):
            with open(fname) as f:
                if '10007058' in f.read():
                    print(fname)




                    #ts = calendar.timegm(time.gmtime())
                    # destFileName = path_TQYL + "TQYL." + str(ts) + "." + str(index) + ".xml"
                    # shutil.copy(fname, destFileName)

            # with open(fname) as f:
            #     if car_CHRB in f.read():
            #         ts = calendar.timegm(time.gmtime())
            #         destFileName = path_CHRB + "CHR." + str(ts) + "." + str(index) + ".xml"
            #         shutil.copy(fname, destFileName)
            #
            # with open(fname) as f:
            #     if car_PRIM in f.read():
            #         ts = calendar.timegm(time.gmtime())
            #         destFileName = path_PRIM + "PRIM." + str(ts) + "." + str(index) + ".xml"
            #         shutil.copy(fname, destFileName)
            #
            # with open(fname) as f:
            #     if car_MTEN in f.read():
            #         ts = calendar.timegm(time.gmtime())
            #         destFileName = path_MTEN + "MTEN." + str(ts) + "." + str(index) + ".xml"
            #         shutil.copy(fname, destFileName)


    # print file names
    # for f in files:
    #     print(f)

    # Rename file names
    # for f in files:
    #     os.rename(f, f + '.xml')
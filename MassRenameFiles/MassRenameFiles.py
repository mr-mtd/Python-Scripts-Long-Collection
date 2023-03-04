import os


if __name__ == '__main__':
    path = r'/Users/m0d00v4/Documents/FREIGHT_PAY/Application_Docs/tms-fp-edi-210 docs/edi210_unorganized'
    print('file path is: ' + path)

    # Gather file names
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(path):
        for file in f:
            if '.xml' not in file:
                files.append(os.path.join(r, file))

    # print file names
    for f in files:
        print(f)

    # Rename file names
    for f in files:
        os.rename(f, f + '.xml')
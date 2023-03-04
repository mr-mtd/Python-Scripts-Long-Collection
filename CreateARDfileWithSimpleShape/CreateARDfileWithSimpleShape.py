def create_simple_ard(filename):
    with open(filename, 'w') as f:
        f.write("CIRCLE,50,50,25")  # write a circle with center at (50, 50) and radius of 25 to the file

if __name__ == '__main__':
    create_simple_ard('simple_shape.ard')

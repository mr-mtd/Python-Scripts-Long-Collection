import ezdxf

def create_basic_model(filename):
    doc = ezdxf.new(dxfversion='R2010')  # create a new DXF document with version R2010
    msp = doc.modelspace()  # get the modelspace for the document

    # add a line to the modelspace
    msp.add_line((0, 0), (5, 0))

    # add a circle to the modelspace
    msp.add_circle(center=(2.5, 2.5), radius=2)

    # save the DXF document to the specified filename
    doc.saveas(filename)

if __name__ == '__main__':
    create_basic_model('basic_model.dxf')

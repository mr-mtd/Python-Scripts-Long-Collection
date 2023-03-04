import ezdxf

def convert_dxf_to_ard(dxf_path, ard_path):
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()

    with open(ard_path, 'w') as f:
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start_point = entity.dxf.start
                end_point = entity.dxf.end
                f.write("LINE,{start_point[0]},{start_point[1]},{end_point[0]},{end_point[1]}\n")
            elif entity.dxftype() == 'CIRCLE':
                center = entity.dxf.center
                radius = entity.dxf.radius
                f.write("CIRCLE,{center[0]},{center[1]},{radius}\n")

if __name__ == '__main__':
    dxf_path = 'example.dxf'
    ard_path = 'example.ard'
    convert_dxf_to_ard(dxf_path, ard_path)

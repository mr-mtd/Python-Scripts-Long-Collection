import os
import ezdxf
import struct

class ARD_to_DXF_Converter:
    def __init__(self):
        self.input_file = None
        self.output_file = None

    def select_input_file(self):
        self.input_file = input("Enter path to ARD input file: ")
        print("Selected input file: {self.input_file}")

    def select_output_file(self):
        self.output_file = input("Enter path to DXF output file: ")
        print("Selected output file: {self.output_file}")

    def convert(self):
        if self.input_file is None:
            print("No input file selected.")
            return
        if self.output_file is None:
            print("No output file selected.")
            return

        # Open the input ARD file in binary mode
        with open(self.input_file, 'rb') as f:
            data = f.read()

        # Extract the points from the ARD data
        points = []
        for i in range(0, len(data), 4):
            x, y = struct.unpack('<hh', data[i:i+4])
            points.append((x, y))

        # Create a new DXF document
        doc = ezdxf.new()

        # Add a new LINE entity to the DXF document for each pair of points
        msp = doc.modelspace()
        for i in range(len(points)-1):
            start = points[i]
            end = points[i+1]
            msp.add_line(start, end)

        # Save the DXF document to the output file
        doc.saveas(self.output_file)
        print("Conversion complete: {self.input_file} -> {self.output_file}")

# Create a new converter instance
converter = ARD_to_DXF_Converter()

# Prompt the user for the input and output files
converter.select_input_file()
converter.select_output_file()

# Convert the file
converter.convert()

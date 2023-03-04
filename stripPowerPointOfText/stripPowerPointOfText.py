import pptx

def strip_ppt(ppt_filename, stripped_filename):
    # Load the PowerPoint presentation
    prs = pptx.Presentation(ppt_filename)

    # Loop through all slides in the presentation
    for slide in prs.slides:

        # Loop through all shapes in the slide
        for shape in slide.shapes:

            # Check if the shape is a text box
            if shape.has_text_frame:

                # Remove the text from the text box
                shape.text_frame.text = ''

    # Save the modified presentation with a different name
    prs.save(stripped_filename)

if __name__ == '__main__':
    # Replace example.pptx and example_stripped.pptx with your own file names
    strip_ppt('C:\Users\mason\Downloads\Unit_1.pptx', 'C:\Users\mason\Downloads\example_stripped.pptx')

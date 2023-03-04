from pptx import Presentation
from pptx.util import Inches

# Create a new PowerPoint presentation
prs = Presentation()

# Add a new slide to the presentation
slide = prs.slides.add_slide(prs.slide_layouts[0])

# Add a title to the slide
title = slide.shapes.title
title.text = "Title of the Slide"

# Add a subtitle to the slide
subtitle = slide.placeholders[1]
subtitle.text = "Subtitle of the Slide"

# Add an image to the slide
img_path = 'path/to/image.jpg'
pic = slide.shapes.add_picture(img_path, Inches(1), Inches(3))

# Save the presentation
prs.save('example.pptx')

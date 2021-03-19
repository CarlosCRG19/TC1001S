# TC1001S Project: Awesome Image Filters
This is the repository for the project "Awesome Image Filters", made by José Naime, Carlos Rodríguez, Mauricio Cantú and Francisco Ramírez for the class TC1001S. The aforementioned project consists of a program in which the user uploads images, applies filters to it as desired and either saves or resets the image. This is explained in further detail below.

### Features
* Sharpen filter: Increases the sharpness of the image.
* Blur filter: Applies a 5x5 Gaussian blur to the image.
* Show edges: Highlights the edges of the deatures inside the image.
* Vignette: Creates a black, vignette-type gradient along the edges and corners of the image.
* **Epic filter**: Applies a _cinematic_ fringe filter to the image, giving it a retro look.
* RGB filter: Applies a tint to the image, according to the color and saturation selected.

### Usage
To open the main gui, simply run the file named "main.py". After that, select your image file, and apply the desired filters by either selecting them from the "Basic Filters" menu (Sharpen, Blur, Show Edges, Vignette, Epic Filter) or modifying the RGB and saturation sliders and clicking "Apply" to apply a tint with the desired color. The filters can be used on the same image one after the other, and when an undesired change is made, the image can be reset by clicking on the "Reset Image" button. Finally, you can save the image by clicking on "Save Image", which stores the modified image in the project directory.

### Dependencies
This project uses OpenCV and NumPy for the filters themselves, TkInter for the GUI and its elements, and PIL for the processing of image files.

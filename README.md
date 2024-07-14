# ASCII Art Generator

This Python script converts images into ASCII art using OpenCV, leveraging the varying intensities of ASCII characters to represent different shades and details of the image.

## Overview

ASCII art is a technique that uses printable characters from the ASCII standard to create images. Each character in the ASCII set has a different intensity, allowing them to be used like pixels to represent variations in brightness and contrast within an image.

This script takes an input image (`image.jpg`), converts it to grayscale, and then maps each pixel's intensity to an ASCII character from a predefined set (`ASCII_CHARS`). The resulting ASCII representation provides a stylized, text-based version of the original image.

## Usage

1. **Clone the repository:**
   ```
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```

2. **Install Python dependencies:**
   ```
   pip install opencv-python
   ```

3. **Download an image:**
   Place your image file (`image.jpg`) in the project directory.

4. **Run the script:**
   ```
   python ascii_generator.py
   ```

5. **Customize ASCII characters:**
   - Modify the `ASCII_CHARS` list in the script to include characters that best represent the intensity levels you desire.
   - The characters can be adjusted based on their visual weight, such as using lighter characters (e.g., `.`) for darker areas and heavier characters (e.g., `M`) for lighter areas.

6. **Adjust parameters:**
   - Modify the `rescaleFrame` function parameters (`scale1` and `scale2`) to adjust the size of the output ASCII art.

## Dependencies

- Python 3.x
- OpenCV
- NumPy

### Notes:

- **Images:** Replace `example.jpg` with an example of the original image used and `ascii_output.png` with a screenshot or saved output of the generated ASCII art.
- **Customization:** Explain how users can customize the `ASCII_CHARS` list to create different artistic effects and representations of their images.

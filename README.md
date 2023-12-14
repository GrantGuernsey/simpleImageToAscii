# Image to ASCII Art Converter
This script converts an image into ASCII art using the Python Imaging Library (PIL). The ASCII characters are chosen based on pixel intensity, creating a visual representation of the image in a text format.

# How to Use

## Install PIL:
Make sure you have the Pillow library installed. If not, install it using:

```
pip install Pillow
```
## Modify Image Path:
In the main method, change the image_path variable to the path of the image you want to convert. For example:

```python
image_path = r'path_to_your_image.jpg'
```

## Run the Script:
Execute the script in a terminal or command prompt:

```
python ascii.py
```
## Review Output:
The script will generate ASCII art based on the image and save it to a text file. The file path is specified by the output_path variable in the main method.

## Customization
### ASCII Characters:
You can modify the ASCII_CHARS variable to use different characters for representing different pixel intensities. Ensure the characters are arranged from dark to light.

### Output Size:
Adjust the new_width parameter in the resize_image function to control the width of the output ASCII art.

Example
Here is an example of how to use the script:

```python
# Example usage
image_path = r'path_to_your_image.jpg'
output_path = r'path_to_save_ascii.txt'

# Open the image file
try:
    image = Image.open(f'{image_path}', 'r')
except Exception as e:
    print(f"Error: {e}")
    return

# Create ASCII art representation
ascii_art = create_ascii_image(image)

# Save the ASCII art to a text file
try:
    with open(output_path, 'w') as output_file:
        output_file.write(ascii_art)
    print(f"ASCII art saved to {output_path}")
except Exception as e:
    print(f"Error: {e}")
```
Feel free to experiment with different images and adjust the parameters to achieve the desired ASCII art output.

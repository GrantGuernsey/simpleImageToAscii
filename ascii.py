from PIL import Image

# Define ASCII characters to represent the image
ASCII_CHARS = '@%#*+=-:. '

def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def convert_grayscale(image):
    return image.convert('L')

def map_pixels_to_ascii(image, range_width=25):
    pixels = image.getdata()
    ascii_str = ''
    for pixel_value in pixels:
        ascii_str += ASCII_CHARS[pixel_value // range_width]
    return ascii_str

def create_ascii_image(image):
    image = resize_image(image)
    image = convert_grayscale(image)
    ascii_str = map_pixels_to_ascii(image)
    
    img_width = image.width
    ascii_str_len = len(ascii_str)
    ascii_img = ''
    
    for i in range(0, ascii_str_len, img_width):
        ascii_img += ascii_str[i:i+img_width] + '\n'
        
    return ascii_img

def main():
    # Example usage
    image_path = r'test.jpg'
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
        
if __name__ == "__main__":
    main()

from PIL import Image

def change_lsb(original_image_path, output_image_path, message):
    img = Image.open(original_image_path)

    binary_message = ''.join(format(ord(char), '08b') for char in message)

    data_index = 0
    img = img.convert('RGB')
    pixels = img.getdata()

    new_pixels = []

    for pixel in pixels:
        red, green, blue = pixel

        # Encodes in the least significant bit
        if data_index < len(binary_message):
            red = (red & ~1) | int(binary_message[data_index])
            data_index += 1

        if data_index < len(binary_message):
            green = (green & ~1) | int(binary_message[data_index])
            data_index += 1

        if data_index < len(binary_message):
            blue = (blue & ~1) | int(binary_message[data_index])
            data_index += 1

        new_pixels.append((red, green, blue))

    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)

    # Specify the file format when saving
    new_img.save(output_image_path, format="PNG")
    print("Message encoded successfully!")

def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.getdata()

    binary_data = ""
    for pixel in pixels:
        for color in pixel:
            binary_data += str(color & 1)

    # Convert binary data to ASCII
    message = ''.join(chr(int(binary_data[i:i + 8], 2)) for i in range(0, len(binary_data), 8))
    return message

# Example usage
original_image_path = 'C:/Users/soudi/Downloads/sou.jpg'
output_image_path = 'C:/Users/soudi/Downloads/sou1.jpg'
message = 'Hello, this is a secret message!'
change_lsb(original_image_path, output_image_path, message)

# Decode the message
decoded_message = decode_lsb(output_image_path)
print(f"Decoded Message: {decoded_message}")



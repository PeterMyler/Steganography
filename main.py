from PIL import Image
DATA_END = "!EOF!"  # special characters that signify the end of the message


def decodeData(img_path):
    img = Image.open(img_path, 'r')  # load image from filename
    pixel_values = list(img.getdata())  # get flattened list of all rgb values

    full_bin = ""
    for pixel in pixel_values:
        # get binary string for each colour value and combine last bit of each value
        full_bin += sum(bin(p)[-1] for p in pixel)

    output = ""
    # go through full binary string in groups of 8 bits
    for i in range(0, len(full_bin), 8):
        # get the 8 bits and convert them to decimal
        ascii_value = int(full_bin[i:i + 8], 2)

        # make sure the ascii value is valid
        # if it's not -> append "?" instead
        if (ascii_value == 10) or (32 <= ascii_value <= 126):
            output += chr(num)
        else:
            output += "?"

        # if the last characters equal the special ending characters
        # return the message (without those characters)
        if output[-len(DATA_END):] == DATA_END:
            return output[:-len(DATA_END)]

    return output


def encodeData(img_path, message_str):
    message_str += DATA_END
    img = Image.open(img_path)  # load image from filename
    width, height = img.size

    bin_str = "".join([format(ord(c), '08b') for c in message_str])
    # convert message into sets of 3 bits
    bits = [bin_str[i:i + 3] for i in range(0, len(bin_str), 3)]

    pixel_count = 0
    for y in range(height):
        for x in range(width):

            pixel_count += 1
            if pixel_count > len(bits):
                img.save(img_path)
                return

            pos = (x, y)
            rgb_bin = [*map(bin, img.getpixel(pos))]
            for i in range(len(bits[pixel_count - 1])): rgb_bin[i] = rgb_bin[i][:-1] + bits[pixel_count - 1][i]
            rgb = tuple(int(i[2:], 2) for i in rgb_bin)
            img.putpixel(pos, rgb)


def main():
    inp = input("Do you want to encode or decode your image (e/d)? ").lower()

    if inp == "e":  # encode into image
        data = input("Enter the message you want to encode: ")
        path = input("Enter the image filename: ")
        if "." not in path: path += ".png"

        encodeData(path, data)
        print("Encoding completed!")

    elif inp == "d":  # decode from image
        path = input("Enter the image filename: ")
        if "." not in path: path += ".png"

        result = decodeData(path)
        if result: print("Result:\n" + result)

    else:
        print("Error! Invalid input.")


if __name__ == "__main__":
    main()


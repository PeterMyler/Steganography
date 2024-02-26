from PIL import Image
DATA_END = "!EOF"


def decodeData(img_path):
    img = Image.open(img_path, 'r')  # load image from filename
    pixel_values = list(img.getdata())  # get flattened list of all rgb values

    full_bin = ""
    # go through each pixel
    for pixel in pixel_values:
        # get binary string for each colour value
        # add last bit of each value to the full string
        full_bin += sum(bin(p)[-1] for p in pixel)

    output = ""
    # go through full binary string in groups of 8
    for i in range(0, len(full_bin), 8):
        byte = full_bin[i:i + 8]  # get 8 bits
        num = int(byte, 2)
        if 32 <= num <= 126 or num == 10:
            output += chr(num)
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


# writeImageData("img2.png", "Hi Jamie! I love coding, but really I don\'t.")
# print(readImageData("img2.png"))

inp = input("Do you want to encode or decode your image (e/d)? ").lower()
if inp == "e":
    # encode
    data = input("Enter the data you want to encode: ")
    path = input("Enter the image name (without extension): ") + ".png"
    encodeData(path, data)
    print("Done!")
elif inp == "d":
    # decode
    path = input("Enter the image name (without extension): ") + ".png"
    result = decodeData(path)
    print("Result:\n" + result)
else:
    # invalid input
    print("Error! Invalid input.")


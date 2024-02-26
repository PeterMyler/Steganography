# Steganography

Steganography is the technique of hiding data within an ordinary, nonsecret file or message to avoid detection. 
The hidden data is then extracted at its destination.

Basically, it is a way of encoding data into a file (and being able to decode that data back) without visibly changing that file.\
Here I implemented a solution that encodes a string into an image and decodes a string from an image.

I used the LSB (Least Significant Bit) of each individual RGB value of each pixel to map a series of 1s and 0s to. This way each pixel can store 3 bits.
This does change the actual colour of the pixel but the difference is so small it isn't visible at all.

## Requirements
Uses PIL (pillow)
```
pip install pillow
```

## Encoding
First the user specifies a message they want to encode and the image file to use. The program then:
1. Adds a special set of characters ("!EOF!") to the end of the message so the it knows where to stop when it's decoding the image.
2. Converts each character in the message to an 8 bit number (using ASCII) and joins them all together into one long string of 1s and 0s.
3. Goes through each colour component of each pixel in the image (left-to-right, top-to-bottom) and change the LSB to match the binary message.

## Decoding
Decoding is as simple as going through each colour component of each pixel and getting its LSB. 
Every 8 bits can be converted back into a character. Once the special end-signifying charcters are reached the program stops decoding and outputs the result.


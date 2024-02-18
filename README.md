# Steganography

Steganography is the technique of hiding data within an ordinary, nonsecret file or message to avoid detection. 
The hidden data is then extracted at its destination.

Basically, it is a way of encoding data into an image without visibly changing the image. 
It is then possible to decode that data from the image, if the specific encoding techique is known.

Here I used the LSB (Least Significant Bit) of each RGB component of each pixel to map a series of 1s and 0s to. So each pixel can store 3 bits.
This does change the actual colour of the pixel but the difference is so small it isn't visible to us.

## Encoding
This is what the code would do if I wanted to encode the message "Hello" into an image:
1. Add "!EOF" to the end of the message so that when the program decodes the message it knows where to stop.
2. Convert each character in the message to an 8 bit number (using ASCII) and join them all together into one long string of 1s and 0s.
3. Go through each colour component of each pixel in the image (left-to-right, top-to-bottom) and change the LSB of that colour to match the binary message.

## Decoding
Decoding is as simple as going through each colour component of each pixel and noting down its LSB. Every 8 bits can be converted back into a character. Once the characters "!EOF" are reached the program stops decoding and outputs the result.


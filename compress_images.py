from PIL import Image
import sys
import os

def compress_image(input_path, output_path, quality):
    try:
        with Image.open(input_path) as img:
            if(img.format =='PNG'):
                #pngs are lossless
                print("Since you have a png file it wont compress that much")
            img.save(output_path, quality=quality)
            print(f"\nImage saved to {output_path} with quality={1-quality}%")
    except Exception as e:
        print(f"Failed to compress image: {e}")

def main():
    input_path = input("Input path: ")
    output_path = input("output_path: (press enter if its the same): ")
    quality = input("whats the compression % (press enter if you wnat the default. default 15%): ")
    #checking if the quality is blank otherwise set it to 15
    quality = quality if quality.isspace() else 15
    #check if the output path is empty then set it to the input's path parent other wise set it to the user input
    output_path = output_path if output_path.isspace() else os.path.dirname(input_path)+"/compressed_image_"+os.path.split(input_path)[-1]
    print(output_path)
    compress_image(input_path, output_path, quality)


if __name__ == '__main__':
    main()
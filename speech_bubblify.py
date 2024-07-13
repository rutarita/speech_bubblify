import os
import sys
from PIL import Image, ImageDraw

# List of supported image formats
image_formats = [".jpg", ".jpeg", ".png", ".webp", ".gif"]

# Get the current directory
current_directory = os.getcwd()

# Get a list of all files in the current directory
files_in_directory = os.listdir(current_directory)

# Filter out only the image files with supported formats
image_files = [file for file in files_in_directory if os.path.splitext(file)[1].lower() in image_formats]

finish_setup = 0

# Sets the default value for if the program should remove the original image_files
delete_original_files = "false"

print("Hello and welcome to speech_bubblifier! (CLI method)")
while finish_setup == 0:
    print("current modes are:")
    print("1 - automatically speech bubblify all the supported images")
    print("2 - convert a single supported image")
    print("3 - enter micro bash mode to chose the directory")
    print("4 - exit the program")
    mode = input("Choose the mode: ")
    if mode == '2':
        print("Image files in the current directory and are available to convert:")
        for image_file in image_files:
            print(image_file)
        chosen_file = input("What file(s) do you want to convert?: ")
        filtered_array = [entry for entry in image_files if chosen_file in entry]
        print(filtered_array)
        if len(filtered_array) > 1:
            mode = input("There are more than 1 file that match this, convert all of them(n) or search again(y)?: ")
            if mode == 'n':
                finish_setup = 1
                image_files = filtered_array
        elif len(filtered_array) == 1:
            finish_setup = 1
            image_files = filtered_array
        else:
            print("There are no images matching this string, perhaps, try again?")
    if mode == '1':
        finish_setup = 1
    if mode == '3':
        print("Welcome to the shell mode!")
        print("Supported commands are: pwd, ls, cd. they work almost like in sh shell script, except stripped down")
        print("Once you find and enter the folder you need, just exit")
        bash_mode = 1

        def cd(directory):
            try:
                os.chdir(directory)
            except FileNotFoundError:
                print("No such file or directory: {}".format(directory))

        def ls():
            for item in os.listdir():
                if os.path.isdir(item):
                    print("\033[92m{}\033[0m".format(item))  # Print directories in green
                else:
                    print(item)
        def pwd():
            print(os.getcwd())
        while bash_mode:
            command = input("$ ")

            if command.startswith("cd"):
                _, directory = command.split(" ", 1)
                cd(directory)
            elif command == "ls":
                ls()
            elif command == "pwd":
                pwd()
            elif command == "exit":
                current_directory = os.getcwd()
                files_in_directory = os.listdir(current_directory)
                image_files = [file for file in files_in_directory if os.path.splitext(file)[1].lower() in image_formats]
                bash_mode = 0
            else:
                print("Unknown command: {}".format(command))
    if mode == '4':
        sys.exit()
if input("Do you wish to remove the original images after the operation finishes? (y/n)") == "y":
    if input(f"Are you sure? The deletion can not be reverted resulting in {len(image_files)} images getting removed.") == "y":
        # Set the the condition of deleting the files to true
        delete_original_files = "true"
for image_file in image_files:
    image_name = image_file
    # Open the image
    image = Image.open(image_name)

    # Create a new image with an alpha channel
    new_image = Image.new("RGBA", image.size, (0, 0, 0, 0))

    # Paste the original image onto the new image
    new_image.paste(image, (0, 0))

    # Draw an ellipse to erase a portion from the top of the image
    draw = ImageDraw.Draw(new_image)

    image_width, image_height = new_image.size
    ellipse_width = image_width
    ellipse_height = image_height / 10

    left = (0 - image_width / 10)
    top = ellipse_height * -1
    right = image_width + image_width / 10
    bottom = ellipse_height

    draw.ellipse((left, top, right, bottom), fill=(0, 0, 0, 0))

    triangle_points = [(image_width - (image_width / 20), 0), (image_width, image_height / 20), ((image_width / 4) * 3, (image_height / 4))]
    draw.polygon(triangle_points, fill=(0, 0, 0, 0))

    # Create a subfolder for output
    output_folder = "converted_output"
    os.makedirs(output_folder, exist_ok=True)

    filename_without_extension = os.path.splitext(image_name)[0]

    # Save the edited image as a GIF with a custom filename
    output_filename = f"speech_bubblified_{filename_without_extension}.gif"
    output_path = os.path.join(output_folder, output_filename)
    new_image.save(output_path, save_all=True, append_images=[new_image], duration=100, loop=0)
    print(f"{filename_without_extension} converted to speech_bubblified_{filename_without_extension}.gif")
    if delete_original_files == "true":
        os.remove(image_name)
print(f"The files were saved in {current_directory}/converted_output")
print(f"Done! {len(image_files)} file(s) were converted")

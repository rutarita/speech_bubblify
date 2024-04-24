# speech_bubblify
A python script made in python using pillow to generate speech bubble images for funnies
# What is it for?
This is a program to make speech bubbles for discord and soon will be for telegram. Currently it can mass convert and convert single files and ones that match a string of characters *(not RegEx though)*
# How to use it?
## Windows
Install pillow somehow and run it (not documented yet)
## Linux
Install pillow via
```
pip install pillow
```
or using your systems package manager by installing a package `python-pillow`
## Android
Install [Termux](https://f-droid.org/packages/com.termux/) (or any alternative) from f-droid (reccomended source) and then after installing, grant it full file control and after that run run
```
apt install python-pillow
```
to install pillow and then
```
python3 /storage/emulated/0/Downloads/speech_bubblify.py
```
or move to that directory with `cd`
# Usage
On the start of the program in the terminal you will be prompted to chose one of the modes that are avaliable:
1. Convert all - converts all the images in the current directory
2. Conver one/multiple - converts one or multiple image based on the input of the string that will be compared with the array of supported images.
3. Bash mode - a mode to move to the directory where you need to convert. Work with basic sh commands such as ls, cd, pwd and exit
4. Exit - self explanatory, halts the program.
# How does it work?
For now it simply draws an elipse madde of alpha channel and a triangle.

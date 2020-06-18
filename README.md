# DOTGOM
***
### About the program:
The genres of music that the program can identify:
- rock 
- hip-hop 
- jazz 
- electronics

The program has a fairly simple and intuitive interface. The full address for the .wav or .flac file is entered into the line and the "Define Genre" button is pressed. The program displays in the line under the input field what kind of music it is.

The library is at the development stage, so in the future it is possible to increase the number of genres that the program can recognize. The quality of recognition will also increase.
***
### Use exe:
1. Download the repository and unzip it in any directory convenient for you. The exe file is in the "/ DOTGOM-exe" folder.
2. Next to the program there is a folder "/ music", it is necessary to copy tracks to it, the genre of which you want to know.
3. Try the program;)
***
### Development:
#### You need a PIP program, if it is not, then do.
- #### If Windows: 

1. Download the install script get-pip.py (https://bootstrap.pypa.io/get-pip.py). If you have Python 3.2, the version of get-pip.py should be the same. In any case, right-click on the link and click “Save As ...” and save the script to any safe folder, for example, in “Downloads”.

2. Open a command prompt and browse to the directory with the get-pip.py file.

3. Run the following command: 
> python get-pip.py
- #### If Linux:
> apt install python3-pip
#### Installing the necessary libraries:
To run the program, execute the following commands in the terminal:
> pip install numpy scikit-learn soundfile tkinter

If the Pandas library you have has a version greater than 1.0.1, then delete it:
> pip uninstall pandas

And install version 1.0.1 (If you did not have this library installed, then run only this command):
> pip install pandas==1.0.1

after installing the libraries, you can run the program.

#### Attention!!! Please prepare files in the format .wav or .flac before using the program. To format a file in these formats, you can use the Audacity (You can download it here: https://audacity-free.ru/) program or any other program that can format files in these formats.

It is enough for the program to submit only the name of the file that you want to use. (Input example: "Grand Massive - Recurrence.wav")
#### Attention!!! Be sure to place the file in the directory with the program.
*** 
### If you have problems installing, please write to me in VK or by mail:

Mail: evgenii.salaurov@gmail.com

VК: https://vk.com/streetread

# Pixelated
## Description
I have these 2 images, can you make a flag out of them? scrambled1.png scrambled2.png
## Solution
Scrambled1.png
![scrambled1](https://github.com/Selwynuy/PicoCTF/assets/107299589/3ca90eaf-3ec6-4e66-8c05-c82615f9f6b0)
Scrambled2.png
![scrambled2](https://github.com/Selwynuy/PicoCTF/assets/107299589/0e14da2b-5fb7-4f99-b81c-a20d20136f42)


installed stegsolver to solve the problem
```
$ wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
$ chmod +x stegsolve.jar
$ mkdir bin
$ mv stegsolve.jar bin/
```

Usage:
```
$ java -jar stegsolve.jar
```
Steps:

Step 1: Open the first image Scrambled1.png

Step 2: Use Analyse Tool and use image combiner

** A new window pops up **

Step 3: Click next until you get the expected output

![image](https://github.com/Selwynuy/PicoCTF/assets/107299589/9a61302a-4e2e-449d-893e-ea0d5a214e0c)

FLAG: picoCTF{d562333d}

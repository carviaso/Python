# How to Convert Base64 Image To Png in Python

  In this python tutorial we will learn about how to convert base64 image to png in python. We will look at an example of how to convert base64 to png image in python. you will learn how to convert base64 string to png in python. we will help you to give an example of how to decode base64 string to png in python. Alright, let us dive into the details.

  If you are looking to convert base64 string to an png image in python then I will help you with that. I will give you a very simple example, we will take one variable "imageData" with base64 string and then convert it into the png image. we will use base64 library. So, without further ado, let's see simple examples: You can use these examples with python3 (Python 3) version.

### Example:

```
main.py

# Import base64 Module
import base64
   
# Image Base64 String
imageData = "iVBORw0KGgoAAAANSUhEUgAAAZAAAAGQCAIAAAAP3...";
    
# Decode base64 String Data
decodedData = base64.b64decode((imageData))
  
# Write Image from Base64 File
imgFile = open('image.png', 'wb')
imgFile.write(decodedData)
imgFile.close()
```

Output:

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

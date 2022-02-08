# -*- coding: utf-8 -*-
"""


@author: sara
"""

import numpy as np
import math
from PIL import Image
from IPython.display import display




#open the imge
im=Image.open(r'C:\Users\sara\Desktop\aruba.jpg').convert('L')
im.save('grey.jpg') #convert from RGB to greyscale (dim3 to dim2)
#display(im)





#convert image to numpy array 
a=np.array(im)
a=a.astype(np.uint8)
print(a.ndim)    #2
print(a.shape)   #(667,667)
print(a)     #[[253 253 253 ... 254 254 254]
             #[254 254 254 ... 254 254 254]
             #[251 252 252 ... 248 248 248]
             #...
             #[246 246 247 ... 242 242 242]
             #[246 246 247 ... 242 242 242]
             #[245 246 247 ... 242 242 242]]



#numpy to an object (jupiter can render)
#b=Image.fromarray(a)
#display(b)
reshaped=np.reshape(a, (400000,44889))
print(reshaped)
display(Image.fromarry(reshaped))



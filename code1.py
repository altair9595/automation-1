import os
import shutil
os.chdir('Data')

    
for file in os.listdir('.'):
     filename = os.fsdecode(file)
     if filename.endswith(".png",".jpg",) : 
      if not os.path.exists('images'):
        os.mknod('images')
      
     shutil.copy(filename,'images')
     os.remove(filename)
      
      
      
      
      
      
      
     print ('done')

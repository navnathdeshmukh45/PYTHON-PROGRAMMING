import qrcode
import image 
qr = qrcode.QRCode (
    version = 15,  #15 means  the version of the  qr code  high  the number bigger  the code  image  and complicated picture
    box_size = 10 ,#size of  the box where qr code  will be display 
    border = 5 #it  is the  white  part  of image  --border in  all 4  side with white  colour 
    
)
data =" https://www.youtube.com/watch?v=tWXpzQbjBFk&list=PLqPqNkq_yO50c_4vqU8Pg_983EBvYmNro"
#as  i have  given  the path  of my  channel  like  the same  way  can givn  anything 
#if you  don't want  to regirect and create  for  normal  text that write  text  in  quotes

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill ="black",back_color="white")
img.save("test.png")
import cv2


with open("test.csv") as iostream:
    content = iostream.read()

for line in content.split("\n"):
	image, image_path, xmin, ymin, xmax, ymax, label, conf, scalex, scaley= line.split(",")
	image_name = image
	image_w = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

	scalemtplx =1.25 #width
	scalemtply =3 #height
	sizex = round ((int(xmax)-int(xmin)))
	sizey = round ((int(ymax)-int(ymin)))
	avrgx = int(xmin) + round(sizex/2)
	avrgy = int(ymin) + round(sizey/2)
	
	
	if sizex >= sizey:
		outimage = image_w[max (1,avrgy - round(scalemtply * sizex/2)) : max (1,avrgy + round(scalemtply * sizex/2)) , max (1,avrgx - round(scalemtplx * sizex/2)) : max (1,avrgx + round(scalemtplx * sizex/2))]
	else:
		outimage = image_w[max (1,avrgy - round(scalemtply * sizey/2)) : max (1,avrgy + round(scalemtply * sizey/2)) , max (1,avrgx - round(scalemtplx * sizey/2)) : max (1,avrgx + round(scalemtplx * sizey/2))]

	
	cv2.imwrite("D:\\Work\\cropped\\mask\\" + image_name[:-4] + " 0" + label + "_bbox" + str(avrgx+avrgy) +".png", outimage)
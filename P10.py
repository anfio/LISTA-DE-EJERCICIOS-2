#10.)Realizar un programa que realice las siguientes funciones de string al texto.
#-split
#-count
#-find
#-uppercase
#-lowercase
#texto=”Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto.
#Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
#impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y
#los mezcló de tal manera que logró hacer un libro de textos especimen.”

my_string = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen."
print(my_string.split(sep=" "))
print(my_string.count("el"))
print(my_string.find("simplemente"))
print(my_string.upper())
print(my_string.lower())

import json,os,time
import funciones as fn

opciones=0
categoriaopciones=0
while True:
    print("************************************")
    print("*            MUNDO LIBRO           *")
    print("************************************")
    print("1- Mantenedor de categorias")
    print("2- Reportes")
    print("3- Salir")
    opciones=int(input("Seleccione su opcion:"))
    if opciones==1:
        while True:
            print("************************************")
            print("*       MANTENEDOR CATEGORIAS      *")
            print("************************************")
            print("1- Agregar Categoria")
            print("2- Editar Categoria")
            print("3- Eliminar Categoria")
            print("4- Listado Categorias")
            print("5- Volver")
            categoriaopciones=int(input("Seleccione su opcion:"))
            if categoriaopciones==1:
                nombre=str(input("Que Categoria quiere agregar:"))
                fn.agregarcategoria(nombre)
                time.sleep(1)
                print("Categoria Agregada")
                time.sleep(1)
                os.system("cls")
            elif categoriaopciones==2:
                id=int(input("Dame la ID de la categoria para cambiar el nombre:"))
                nombrecat=str(input("Dame el nuevo nombre de la categoria:"))
                fn.editarcategoria(nombrecat,id)
                time.sleep(1)
                print("Cambio de nombre de Categoria hecho")
                time.sleep(1)
                os.system("cls")
            elif categoriaopciones==3:
                idelim=int(input("Dame la id de la categoria que quieres eliminar:"))
                fn.eliminarcat(idelim)
                time.sleep(1)
                print("Eliminacion de Categoria hecha")
                time.sleep(1)
                os.system("cls")
            elif categoriaopciones==4:
                with open("biblioteca.json","r") as listado:
                    leerlistado=json.load(listado)
                for i in leerlistado["Categoria"]:
                    print("CategoriaID:",i["CategoriaID"],)
                    print("Nombre:",i["Nombre"])
                time.sleep(5)
                os.system("cls")
            elif categoriaopciones==5:
                os.system("cls")
                break
    elif opciones==2:
        libro1=0
        libro2=0
        libro3=0
        libro4=0
        libro5=0
        libro6=0
        libro7=0
        libro8=0
        libro9=0
        libro10=0
        libro11=0
        libro12=0
        libro13=0
        libro14=0
        libro15=0
        libro16=0
        libro17=0
        libro18=0
        libro19=0
        libro20=0
        print("****************************************************************************")
        print("*       Libros                             Cantidad de veces prestado      *")
        print("****************************************************************************")
        with open("biblioteca.json","r") as reportes:
            leerreportes=json.load(reportes)
        for i in leerreportes["Prestamo"]:
            if i["LibroID"] ==1:
                libro1+=1
            elif i["LibroID"]==2:
                libro2+=1
            elif i["LibroID"]==3:
                libro3+=1
            elif i["LibroID"]==4:
                libro4+=1
            elif i["LibroID"]==5:
                libro5+=1
            elif i["LibroID"]==6:
                libro6+=1
            elif i["LibroID"]==7:
                libro7+=1
            elif i["LibroID"]==8:
                libro8+=1
            elif i["LibroID"]==9:
                libro9+=1
            elif i["LibroID"]==10:
                libro10+=1
            elif i["LibroID"]==11:
                libro11+=1
            elif i["LibroID"]==12:
                libro12+=1
            elif i["LibroID"]==13:
                libro13+=1
            elif i["LibroID"]==14:
                libro14+=1
            elif i["LibroID"]==15:
                libro15+=1
            elif i["LibroID"]==16:
                libro16+=1
            elif i["LibroID"]==17:
                libro17+=1
            elif i["LibroID"]==18:
                libro18+=1
            elif i["LibroID"]==19:
                libro19+=1
            elif i["LibroID"]==20:
                libro20+=1
            print(f"""Cien Años de Soledad:{libro1},
        La Casa de los Espíritus:{libro2},
        Rayuela:{libro3},
        La Ciudad y los Perros:{libro4},
        La Sombra del Viento:{libro5},
        Ficciones:{libro6},
        Don Quijote de la Mancha:{libro7},
        Veinte Poemas de Amor y una Canción Desesperada:{libro8},
        Bodas de Sangre:{libro9},
        El Laberinto de la Soledad:{libro10},
        El Amor en los Tiempos del Cólera:{libro11},
        Eva Luna:{libro12},
        Bestiario:{libro13},
        La Fiesta del Chivo:{libro14},
        El Juego del Ángel:{libro15},
        El Aleph:{libro16},
        Novelas Ejemplares:{libro17},
        Residencia en la Tierra:{libro18},
        La Casa de Bernarda Alba:{libro19},
        Piedra de Sol:{libro20}""")
                          
        reportelibros={
        "Cien Años de Soledad":libro1,
        "La Casa de los Espíritus":libro2,
        "Rayuela":libro3,
        "La Ciudad y los Perros":libro4,
        "La Sombra del Viento":libro5,
        "Ficciones":libro6,
        "Don Quijote de la Mancha":libro7,
        "Veinte Poemas de Amor y una Canción Desesperada":libro8,
        "Bodas de Sangre":libro9,
        "El Laberinto de la Soledad":libro10,
        "El Amor en los Tiempos del Cólera":libro11,
        "Eva Luna":libro12,
        "Bestiario":libro13,
        "La Fiesta del Chivo":libro14,
        "El Juego del Ángel":libro15,
        "El Aleph":libro16,
        "Novelas Ejemplares":libro17,
        "Residencia en la Tierra":libro18,
        "La Casa de Bernarda Alba":libro19,
        "Piedra de Sol":libro20
        }   
        with open("Reporte_biblioteca_mundo_libro.json","w") as reportejson:
            json.dump(reportelibros,reportejson,indent=4)
    elif opciones==3:
        print("Hasta la proxima!!!!")
        break










    

















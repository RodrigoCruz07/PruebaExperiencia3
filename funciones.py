import json


def agregarcategoria(nombre:str):
    with open("biblioteca.json","r") as agregar:
        leercatg=json.load(agregar)
        categoria={
            "CategoriaID":len(leercatg["Categoria"])+1,
            "Nombre":nombre
        }
        leercatg["Categoria"].append(categoria)
    with open("biblioteca.json","w") as agregar:
        json.dump(leercatg,agregar,indent=4)

def editarcategoria(nombrecat:str,id:int):
    with open("biblioteca.json","r") as editar:
        leereditar=json.load(editar)
        contador=0
        for i in leereditar["Categoria"]:
            if i["CategoriaID"]==id:
                print("Categoria encontrada.")
                print("Cambiando el Nombre a la Categoria")
                break
            contador+=1
    leereditar["Categoria"][contador]["Nombre"]=nombrecat
    with open("biblioteca.json","w") as agregar:
        json.dump(leereditar,agregar,indent=4)


def eliminarcat(idelim:int):
    with open("biblioteca.json","r")as eliminar:
        leereliminar=json.load(eliminar)
        contador=0

        for i in leereliminar["Categoria"]:
            if i["CategoriaID"] == idelim:
                del leereliminar["Categoria"][contador]
                break
            contador+=1
        
    with open("biblioteca.json","w") as eliminar:
        json.dump(leereliminar,eliminar,indent=4)




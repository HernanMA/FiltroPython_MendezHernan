import json

with open("usuario.json", "r") as i:
    user = json.load(i)
    with open("servicios.json", "r") as i:
        servicios = json.load(i)

def users():
    print("""
        1: registrar usuario
        2: registrar servicio
        """)
    decision = str("¿Que desea hacer?" )

    if decision == "1":
        nuevo_usuario={
        "Documento" : str(input("documento")),
        "nombre" : str(input("nombre completo")),
        "email" : str(input("email")),
        "servicios" : ""
        }
        users["movistar"]["users"].append(nuevo_usuario)
        with open("usuario.json","r") as i:
            json.dump(users,i,indent=4)

    if decision=="2":
        data=users["movistar"]["users"]
        servicioss=servicios["movistar"]["servicios"]
        
        print("-nuevo servicio")
        for i in data:
            print(i["nombre"], " ID: ", i["Documento"]) 
        print("")  
        id_usuario=str(input("Ingrese el id del usuario a agregar un servicio: "))
        for i in data:
            if id_usuario==i["Documento"]:
                for j in servicioss:
                    print("Nombre: ", j["Nombre_servicio"]) 
                    print("Precio: ", j["Precio"])
                    print("cualidades: ", j["cualidades"])
                name_servicio=str(input("Nombre del servicio:"))
                for j in servicioss:
                    print("hola")
                    for p in servicioss:
                        if name_servicio==p["Nombre_servicio"]:
                            for x in data:
                                if id_usuario==x["Documento"]:
                                    print("perro")
                                    x["servicios"]= name_servicio
                                    print("¡Ingreso exitoso!")



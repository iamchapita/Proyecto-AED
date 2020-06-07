from Información_Pélicula import Info_Pelicula
from LinkedList import LinkedList

ll = LinkedList()

obj = Info_Pelicula("Nombre", "Duración", "Descripción", "Director", "Género")
obj1 = Info_Pelicula("Nombre1", "Duración1", "Descripción1", "Director1", "Género1")
obj2 = Info_Pelicula("Nombre2", "Duración2", "Descripción2", "Director2", "Género2")
obj3 = Info_Pelicula("Nombre3", "Duración3", "Descripción3", "Director3", "Género3")

ll.push(obj)
ll.push(obj1)
ll.push(obj2)
ll.push(obj3)

current = ll.first

json = '{"root":{\n'
contador = 0
while(current):
    
    indice_str = "%s" %(str(contador))
    json += '\t\t"%s":{\n' %(indice_str)
    json += '\t\t\t"nombre":"%s",\n'%(current.value.nombre)
    json += '\t\t\t"duracion":"%s",\n'%(current.value.duracion)
    json += '\t\t\t"descripcion":"%s",\n'%(current.value.descripcion)
    json += '\t\t\t"director":"%s",\n'%(current.value.director)
    json += '\t\t\t"genero":"%s"\n'%(current.value.genero)
    
    if(current.next):
        
        json += '\t\t},\n'
    
    else:
        json += '\t\t}\n'
        json += '\t}\n'
        json += '}'


    current = current.next
    contador += 1


print(json)

    

    






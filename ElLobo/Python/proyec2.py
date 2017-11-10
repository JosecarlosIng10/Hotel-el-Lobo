import bisect, os
outputdebug = False 

def debug(msg):
    if outputdebug:
        print msg

class Node():
    def __init__(self, cuenta, costo):
        self.cuenta = cuenta
        self.costo= costo
      
        self.left = None 
        self.right = None 

class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, cuenta,costo):
        tree = self.node
        
        newnode = Node(cuenta,costo)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(cuenta) + "]")
        
        elif cuenta <= tree.cuenta: 
            self.node.left.insert(cuenta,costo)
            
        elif cuenta >= tree.cuenta: 
            self.node.right.insert(cuenta,costo)
        
        else: 
            debug("Key [" + str(newnode.cuenta) + "] already in tree.")
            
        self.rebalance() 


        
    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()


            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.cuenta) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.cuenta) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def delete(self, cuenta):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.cuenta == cuenta: 
                debug("Deleting ... " + str(cuenta))  
                if self.node.left.node == None and self.node.right.node == None:
                    self.node = None # leaves can be killed at will 
                # if only one subtree, take that 
                elif self.node.left.node == None: 
                    self.node = self.node.right.node
                elif self.node.right.node == None: 
                    self.node = self.node.left.node
                
                # worst-case: both children present. Find logical successor
                else:  
                    replacement = self.logical_successor(self.node)
                    if replacement != None: # sanity check 
                        debug("Found replacement for " + str(cuenta) + " -> " + str(replacement.cuenta))  
                        self.node.cuenta = replacement.cuenta 
                        
                        # replaced. Now delete the key from right child 
                        self.node.right.delete(replacement.cuenta)
                    
                self.rebalance()
                return  
            elif cuenta < self.node.cuenta: 
                self.node.left.delete(cuenta)  
            elif cuenta > self.node.cuenta: 
                self.node.right.delete(cuenta)
                        
            self.rebalance()
        else: 
            return 
    def Modificar(self, cuenta,nuevacuenta,nuevocosto):
        # debug("Trying to delete at node: " + str(self.node.key))
        if self.node != None: 
            if self.node.cuenta == cuenta:
                
                self.node.cuenta=nuevacuenta
                self.node.costo = nuevocosto           
                #self.node.nombre=nuevo
                print (str(self.node.cuenta))
                return  
            elif cuenta < self.node.cuenta: 
                self.node.left.Modificar(cuenta,nuevacuenta,nuevocosto)
            elif cuenta > self.node.cuenta: 
                self.node.right.Modificar(cuenta,nuevacuenta,nuevocosto)
                        
            self.rebalance()
        else: 
            return         

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.cuenta))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.cuenta)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist 

    def display(self, level, pref,archivo,labels,cadena):
        '''
        Display the whole tree. Uses recursive def.
        TODO: create a better display using breadth-first search
        '''
             
        self.update_heights()  # Must update heights before balances 
        self.update_balances()
        if(self.node != None): 
            padre=  self.node.cuenta 
            labels+= str(self.node.cuenta)+"[label= \"" +  str(self.node.cuenta)+ "--" + str(self.node.costo) +"\"];\n"
            if pref != '':
                
                #cadena =str(self.node.cuenta)+"[label= \"" +  str(self.node.cuenta)+ "--" + str(self.node.costo) +"\"];\n"
                archivo.writelines(labels)
                archivo.writelines(str(pref)+ str(self.node.cuenta)+ ";") 
            #print pref, str(self.node.key) + ";"    
            if self.node.left != None: 
                self.node.left.display(level + 1, str(padre)+"->",archivo,labels,cadena)
            if self.node.left != None:
                self.node.right.display(level + 1, str(padre)+"->",archivo,labels,cadena)
        
                   
               
    

    def dibujarAvl(self):
        archivo=open('avl.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("node [fontname=\"Arial\"];\n");
        #archivo.write("rankdir = TD;\n");
        self.display(0,'', archivo,"","")
        archivo.write('}')
        archivo.close() 
        os.system('dot avl.dot -o avl.png -Tpng ')

class Nodo:
    def __init__(self,usuario, contra,direccion,telefono,edad):
        self.usuario=usuario
        self.contra=contra
        self.direccion= direccion
        self.telefono = telefono
        self.edad= edad
        
        self.siguiente= None
        self.anterior = None
class ListaDobleEnlazada:
    def __init__(self):
        self.primero=None
        self.ultimo= None
        
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_final(self,usuario, contra, direccion,telefono,edad):
        if self.vacia():
            self.primero = self.ultimo = Nodo(usuario,contra,direccion,telefono,edad)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(usuario,contra,direccion,telefono,edad)
            self.ultimo.anterior = aux
        
    def recorrer_inicio_fin(self):
        cadena=""
        aux= self.primero
        r= True
        while aux!=None:
            cadena +=str(aux.usuario)
            aux =aux.siguiente
            if aux != None:
                 cadena+="->"    
        aux=self.ultimo
        while aux!= None:
            if r!=True:
                cadena +=str(aux.usuario)
            r=False
            aux = aux.anterior   
            if aux != None:
                 cadena+="->"     
                
        archivo=open('users.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("node [fontname=\"Arial\"];\n");
        
        archivo.write(cadena)
        archivo.write('}')
        archivo.close() 
        os.system('dot users.dot -o users.png -Tpng -Grankdir=LR')        
    def recorrer_fin_inicio(self):
        aux=self.ultimo
        while aux:
            print (str(aux.usuario) + "--" + str(aux.contra))
            aux = aux.anterior
            if aux ==  self.ultimo:
                break
    def buscar(self, user, passw):
        aux= self.primero
        check= False
       
        while aux:
            if aux.usuario == user and aux.contra == passw:
                check=True
                break
            aux = aux.siguiente
            if aux == self.primero:
                break
        if check ==  True:
            return "Si"
        else:
            return "No"
    def eliminar(self, user, passw):
        aux= self.primero
        check= False
       
        while aux:
            if aux.usuario == user and aux.contra == passw:
                aux1=aux
                aux.anterior.siguiente= aux1.siguiente
                aux1.anterior=aux.anterior
                check=True
                break
            aux = aux.siguiente
            if aux == self.primero:
                break
        if check ==  True:
            return "Si"
        else:
            return "No"
    def modificar(self, user, passw,usuario, contra, direccion,telefono,edad):
        aux= self.primero
        check= False
       
        while aux:
            if aux.usuario == user and aux.contra == passw:
                aux.usuario= usuario
                aux.contra= contra
                aux.direccion= direccion
                aux.telefono=telefono
                aux.edad=edad
                check=True
                break
            aux = aux.siguiente
            if aux == self.primero:
                break
        if check ==  True:
            return "Si"
        else:
            return "No"                

class Nodosimple:
    def __init__(self):
        self.nivel = None
        self.numero= None
        self.idd= None
        
        self.siguiente=None
         
class Lista:

    def __init__(self):
        self.raiz = Nodosimple()
        self.primero=None
        self.ultimo=None
        
    def vacia(self):
        if self.primero == None:
            return True
        else:
            return False    
    
    def insertar(self,nodo):
        if self.vacia():
            self.primero = self.ultimo = nodo
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo
            self.ultimo.anterior = aux
        self.__unir_nodos()
    def __unir_nodos(self):
        self.primero.anterior = self.ultimo
        self.ultimo.siguiente = self.primero
                           
    def imprimir(self):
        cadena=""
        labels=""
        aux= self.primero
        while aux!=None:

            labels +=  str(aux.idd)+ "[label= \"Nivel " + str(aux.nivel)+ "--Numero "+ str(aux.numero) + "--"+ str(aux.idd) +"\"];\n"
            cadena+= str(aux.idd)+ "->"
            aux =aux.siguiente
            if aux == self.primero:
                cadena += str(aux.idd)
                break
                
        archivo=open('habitaciones.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("node [fontname=\"Arial\"];\n");
        archivo.write(labels)
        archivo.write(cadena)
        archivo.write('}')
        archivo.close() 
        os.system('dot habitaciones.dot -o habitaciones.png -Tpng -Grankdir=LR') 

class NodoB(object):
    def __init__(self, usuario=None, cuenta=None, costo=None, habitacion=None, fechai=None,fechaf=None):
        self.usuario = usuario
        self.cuenta= cuenta
        self.costo= costo
        self.habitacion = habitacion
        self.fechai=fechai
        self.fechaf=fechaf

class Pagina(object): 
    def __init__(self, ramas=[0,0,0,0,0], claves=[0,0,0,0], cuentas=0):     
        self.ramas = ramas
        self.claves = claves
        self.cuentas = cuentas

class ArbolB(object):
    def __init__(self):
        self.inicio = Pagina()
        self.inicio2 = Pagina()
        self.inserta = NodoB()
        
        self.enlace = Pagina()
        self.pivote = False
        self.existe = False
        self.existe2 = False
    
    
              
        
        
    #Crea el Nodo del Arbol B
    def crearNodoInsertar(self, usuario, cuenta, costo, habitacion, fechai,fechaf):
        nodob = NodoB(usuario, cuenta, costo, habitacion, fechai,fechaf)
        self.InsertarArbolB(nodob, self.inicio)
    def avlre(self):
        nodo = self.inserta

        return nodo.nodoAVL
        
   
    #Inserta el nodo al Arbol B La clave es el Nodo y la raiz la Pagina
    def InsertarArbolB(self, clave, raiz):
        self.agregar(clave, raiz)
        if(self.pivote == True):
            self.inicio = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
            self.inicio.cuentas = 1
            self.inicio.claves[0] = self.inserta
            self.inicio.ramas[0] = raiz
            self.inicio.ramas[1] = self.enlace
            
            
    #Agregar al Arbol, Balanceando el arbol por Id
    def agregar(self, clave, raiz):
        pos = 0              
        self.pivote = False; 
        
        vacioBol = self.vacio(raiz)
        
        if(vacioBol == True):
            self.pivote = True
            self.inserta = clave
            self.enlace = None
        else:
            pos = self.existeNodo(clave, raiz)
            
            if(self.existe == True):
                self.pivote = False
            else:
                self.agregar(clave, raiz.ramas[pos])
                
                if(self.pivote == True):
                    
                    if(raiz.cuentas < 4):
                        self.pivote = False;
                        self.insertarClave(self.inserta, raiz, pos)
                    else:
                        self.pivote = True
                        self.dividirPagina(self.inserta, raiz, pos)
                        print("Inserto")
            
            
    #Verificar si la raiz no Existe
    def vacio(self, raiz):
        if(raiz == None or raiz.cuentas == 0):
            return True
        else:
            return False
        
    
    #Insertar Claves en Pagina
    def insertarClave(self, clave, raiz, posicion):
        i = raiz.cuentas
        
        while i != posicion:
            raiz.claves[i] = raiz.claves[i - 1]
            raiz.ramas[i + 1] = raiz.ramas[i]
            i-=1
        
        raiz.claves[posicion] = clave
        raiz.ramas[posicion + 1] = self.enlace
        val = raiz.cuentas+1
        raiz.cuentas = val
        print("Inserto Valor")
        
        
    #Dividir Pagina
    def dividirPagina(self, clave, raiz, posicion):
        pos = 0
        Posmda = 0
        if(posicion <= 2):
            Posmda = 2
        else:
            Posmda = 3
        
        Mder = Pagina(ramas=[None,None,None,None,None], claves=[None,None,None,None], cuentas=0)
        pos = Posmda + 1
        
        while pos != 5:
            i = ((pos - Posmda) - 1)
            j = (pos - 1)
            Mder.claves[i] = raiz.claves[j]
            Mder.ramas[pos - Posmda] = raiz.ramas[pos]
            pos+=1
        
        Mder.cuentas = 4 - Posmda
        raiz.cuentas = Posmda
        
        if(posicion <= 2):
            self.insertarClave(clave, raiz, posicion)
        else:
            self.insertarClave(clave, Mder, (posicion - Posmda))
            
        self.inserta = raiz.claves[raiz.cuentas - 1]
        Mder.ramas[0] = raiz.ramas[raiz.cuentas]
        val = raiz.cuentas - 1
        raiz.cuentas = val
        self.enlace = Mder
        
    
    #Virificar si Existe el Nodo    
    def existeNodo(self, clave, raiz):
        valor =0
        if(clave.fechai < raiz.claves[0].fechai):
            self.existe2 = False
            valor = 0
        else:
            valor = raiz.cuentas
            while (clave.fechai < raiz.claves[valor - 1].fechai and valor > 1):
                valor-=1
            
            if (clave.fechai < raiz.claves[valor - 1].fechai):
                self.existe = True
            else:
                self.existe = False
            
            if (clave.fechai == raiz.claves[valor - 1].fechai):
                self.existe2 = True
            else:
                self.existe2 = False            
            
        
        return valor
    
    #Crear Archivo
    def dibujarArbol(self):
        archivo=open('arbolB.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("node [shape = record];\n");
        archivo.write("rankdir = TD;\n");
        self.grabarArchivo(self.inicio , archivo)
        archivo.write('}')
        archivo.close()
        os.system('dot arbolB.dot -o arbolB.png -Tpng ')

   
    #Escribir Contenido del Archivo
    def grabarArchivo(self, raiz, archivo):
        nodo = raiz             
        if(nodo == None):
            a=""
        else:
            if (nodo.cuentas != 0):
                archivo.writelines("activo_" + str(nodo.claves[0].usuario) + " [label= \"")
                k=1
                while k <= nodo.cuentas:
                    archivo.writelines("<r" + str(k - 1) + ">" + " | " + "<cl" + str(k) + ">"  + str(nodo.claves[k - 1].usuario) +" / "+str(nodo.claves[k - 1].cuenta)+" / "+ str(nodo.claves[k - 1].fechai)+ " &#92;" + " | ")
                    k+=1
                
                
                archivo.writelines("<r" + str(k - 1) + "> \"];\n")
                i=0
                while i <= nodo.cuentas:
                    if (nodo.ramas[i] != None):
                        if (nodo.ramas[i].cuentas != 0):
                            archivo.writelines("activo_" + str(nodo.claves[0].usuario) + ":r" + str(i) + " -> activo_" + str(nodo.ramas[i].claves[0].usuario) + ";\n")                          
                        
                    i+=1
                    
                j=0
                while j <= nodo.cuentas:
                    self.grabarArchivo(nodo.ramas[j],archivo)
                    j+=1

                
class Nodocontenido:
    def __init__(self):
        self.upheader=None
        self.leftheader=None
        self.dia=None
        self.tablahash= TablaHash()
        self.arriba=None
        self.abajo=None
        self.derecha=None
        self.izquierda=None
        self.enfrente=None
        self.atras=None
class matriz:
    def __init__(self):
        self.mes=None
        self.year=None
        self.dia=None
        self.tablahash = TablaHash()
        self.siguiente=None
        self.anterior=None
        self.first=None

class listaencabezados:

    def __init__(self):

        self.izquierda=None
        self.ultimoizquierda=None
        self.abajo=None
        self.ultimoabajo=None
        
    def recibir(self,nodo):
        
        nodoaux= matriz()
        nodoaux.mes= nodo.mes
        nodoaux.year= nodo.year
        nodoaux.dia=nodo.dia
        nodoaux.tablahash = nodo.tablahash

        self.agregarmes(nodo)

        #self.agregaryear(nodoaux)
          
    def vaciames(self):
        if self.izquierda == None:
            return True
        else:
            return False
    def vaciayear(self):
        if self.abajo == None:
            return True
        else:
            return False        
    def agregarmes(self,nodo):
        cont = Nodocontenido()
        cont.tablahash = nodo.tablahash
        nodoaux= matriz()
        nodoaux.mes= nodo.mes
        nodoaux.year= nodo.year
        nodoaux.dia=nodo.dia
        if self.vaciames():
            cont.upheader= nodo.mes
            
            cont.dia= nodo.dia
            
            self.izquierda=self.ultimoizquierda =  nodo
            self.izquierda.first= self.ultimoizquierda.first=cont
            self.agregaryear(nodoaux,cont)
        else:
            aux= self.izquierda
            g= False
            exist=False
            while aux != None:
                if aux.mes == nodo.mes:
                    contaux=Nodocontenido() 
                    contaux=aux.first
                    cont.dia= nodo.dia
                    yearigual = Nodocontenido()
                    yearigual = aux.first
                    while yearigual !=None:
                        if yearigual.leftheader == nodo.year:
                            exist=True
                            faux= Nodocontenido()
                            if yearigual.enfrente == None:
                                    yearigual.enfrente=cont
                                    cont.atras = yearigual
                            else:
                                faux = yearigual.enfrente          
                                while  faux!=None:
                                    if faux.enfrente == None:
                                        faux.enfrente=cont
                                        cont.atras = faux
                                        break 
                                    else:
                                        faux= faux.enfrente
                            break            
                        yearigual= yearigual.abajo 

                    if contaux.leftheader< nodo.year  and exist == False:
                        abaux= Nodocontenido()
                        abaux= contaux.abajo
                        
                        if contaux.abajo == None:
                            
                            contaux.abajo=cont
                            cont.arriba= contaux

                            self.agregaryear(nodoaux,cont)
                        else:
                            
                            aux3 = Nodocontenido()
                         
                            while abaux != None:
                                
                                if abaux.leftheader> nodo.year:
                                    
                                    aux3= abaux
                                    cont.arriba = abaux.arriba
                                    abaux.arriba.abajo= cont
                                    cont.abajo= aux3
                                    aux3.arriba= cont
                                    self.agregaryear(nodoaux,cont)
                                   
                                    break
                                if abaux.abajo == None:
                                    abaux.abajo= cont
                                    cont.arriba = abaux
                                    self.agregaryear(nodoaux,cont)
                                    break    
                                abaux= abaux.abajo     
                    elif contaux.leftheader > nodo.year and exist == False:
                        faux= Nodocontenido()
                        faux= aux.first
                        cont.upheader=nodo.mes
                        aux.first=cont
                        faux.upheader=None
                        faux.arriba=cont
                        cont.abajo= faux
                        self.agregaryear(nodoaux,cont)        
                           
                                    
                                    
                                    




                       
                    g=True
                    break        
                   
                                         
                            
                    

                elif nodo.mes< aux.mes:
                    cont.upheader= nodo.mes
                    
                    cont.dia= nodo.dia
                    if aux.anterior==None:
                        aux2=self.izquierda
                        self.izquierda= nodo
                        self.izquierda.siguiente=aux2
                        aux2.anterior = self.izquierda
                        self.izquierda.first= cont
                        self.agregaryear(nodoaux,cont)

                    else:   
                        aux2= aux.anterior
                        aux2.siguiente=nodo
                        aux.anterior= nodo
                        aux.anterior.first= cont
                        self.agregaryear(nodoaux,cont)
                        nodo.anterior= aux2
                        nodo.siguiente= aux
                    g=True    
                    break    

                        
                aux= aux.siguiente          

                    
            if (g==False):
                cont.upheader= nodo.mes
                
                cont.dia= nodo.dia
                aux2 = self.ultimoizquierda
                self.ultimoizquierda = aux2.siguiente = nodo
                self.ultimoizquierda.first= cont
                self.agregaryear(nodoaux,cont)
                self.ultimoizquierda.anterior = aux2

    def agregaryear(self,nodo, cont):
        
        if self.vaciayear():
            
            cont.leftheader= nodo.year
            
            self.abajo=self.ultimoabajo= nodo
            self.abajo.first=self.ultimoabajo.first= cont
        else:
            aux= self.abajo
            g= False
            while aux != None:
                if aux.year == nodo.year:
                    contaux=Nodocontenido() 
                    contaux=aux.first
                    upaux = Nodocontenido()
                    auxcont = Nodocontenido()
                    auxcont= cont

                    while auxcont.upheader == None:
                        auxcont= auxcont.arriba
                    
                    if contaux.derecha==None:
                        upaux= contaux
                        while upaux.upheader == None:
                            upaux= upaux.arriba
                        if upaux.upheader< auxcont.upheader:
                            contaux.derecha= cont
                            cont.izquierda = contaux
                        else:
                            aux5=Nodocontenido()
                            aux5= contaux
                            aux.first = cont
                            cont.leftheader= nodo.year
                            cont.derecha= contaux
                            contaux.izquierda= cont
                            contaux.leftheader=None

                         
                    else:

                        y=False
                        if contaux.upheader > auxcont.upheader:
                            aux6=Nodocontenido()
                            aux6= contaux
                            aux.first = cont
                            cont.leftheader= nodo.year
                            cont.derecha= contaux
                            contaux.izquierda= cont
                            cont.leftheader=None
                            y=True
                        while contaux.derecha!=None and y==False:
                        
                            upaux= contaux.derecha
                        
                            while upaux.upheader == None:
                                upaux= upaux.arriba
                        
                            if upaux.upheader > auxcont.upheader:
                                aux4=Nodocontenido()
                                aux4 = contaux.derecha
                                contaux.derecha=cont
                                cont.izquierda= contaux
                                cont.derecha= aux4
                                aux4.izquierda= cont
                                break 
                            contaux= contaux.derecha 
                                
                            if contaux.derecha==None:
                                contaux.derecha=cont
                                cont.izquierda= contaux
                                break
                                           

                            
                    g= True               
                    break
                       
                elif nodo.year< aux.year:
                    
                    cont.leftheader= nodo.year
                    
                    if aux.anterior==None:
                        aux2=self.abajo
                        self.abajo= nodo
                        self.abajo.siguiente=aux2
                        aux2.anterior = self.abajo
                        self.abajo.first=cont
                        
                    else:   
                        aux2= aux.anterior
                        aux2.siguiente=nodo
                        aux.anterior= nodo
                        aux.anterior.first=cont
                        nodo.anterior= aux2
                        nodo.siguiente= aux

                    g=True    
                    break    

                        
                aux= aux.siguiente          

                    
            if (g==False):
                
                cont.leftheader= nodo.year
                
                aux2 = self.ultimoabajo
                self.ultimoabajo = aux2.siguiente = nodo
                self.ultimoabajo.first=cont
                self.ultimoabajo.anterior = aux2            

    def dibujardispersa(self):
        archivo=open('dispersa.dot', 'w')
        archivo.write('digraph structs {\n')
        archivo.write("autosize=false;size=\"10,10!\"")
        archivo.write("rankdir=R; \ngraph [splines = ortho];\n");
        archivo.write("node [shape = box];\n");
        archivo.write("edge [dir = none];\n");
        archivo.write("{rank=same \n");
        archivo.write("matriz[label=\"Matriz\"]; \n");
        self.grabarmes(archivo)
        archivo.writelines("{ \n rankdir=LR;\n")
        self.grabaryear(archivo)
        self.grabarfilas(archivo)
        self.grabarcolumnas(archivo)
        archivo.write('}')
        archivo.close()
        os.system('dot dispersa.dot -o dispersa.png -Tpng -Kdot')            
    def grabarmes(self,archivo):
        aux= self.izquierda
        rel="";
        relinv="matriz"; 
        while aux!=None:

            archivo.writelines(str(aux.mes)+"[label=\"" + str(aux.mes)+"\"];\n")
            if (aux.siguiente!=None):
                rel+= str(aux.mes) +"->"
                auxcad= relinv
                relinv = str(aux.mes)+"->"+ auxcad  
            else:
                rel+=str(aux.mes);
                auxcad=relinv
                relinv = str(aux.mes)+"->"+ auxcad

            aux = aux.siguiente
        archivo.writelines("matriz->"+rel+ "[dir=R];\n " ) 
        archivo.writelines(relinv+"[dir=R];\n}");  
    def grabaryear(self,archivo):
        aux= self.abajo
        rel="";
        relinv="matriz"; 
        while aux!=None:

            archivo.writelines(str(aux.year)+"[label=\"" + str(aux.year)+"\"];\n")
            if (aux.siguiente!=None):
                rel+= str(aux.year) +"->"
                auxcad= relinv
                relinv = str(aux.year)+"->"+ auxcad  
            else:
                rel+=str(aux.year);
                auxcad=relinv
                relinv = str(aux.year)+"->"+ auxcad    
            aux = aux.siguiente
        archivo.writelines("matriz->"+rel+ "[dir=LR];\n " ) 
        archivo.writelines(relinv+"[dir=LR];\n}");             
    def mestonum(self,mes):
        if (mes=="enero"):
            return 1
        
        elif (mes=="febrero"):
            return 2    
        elif (mes=="marzo"):
            return 3
        elif (mes=="abril"):
            return 4 
        elif (mes=="mayo"):
            return 5      
        elif (mes=="junio"):
            return 6 
        elif (mes=="julio"):
            return 7 
        elif (mes=="agosto"):
            return 8 
        elif (mes=="septiembre"):
            return 9 
        elif (mes=="octubre"):
            return 10
        elif (mes=="noviembre"):
            return 11 
        elif (mes=="diciembre"):
            return 12     
                                                         
    def grabarfilas(self, archivo):
        aux= self.abajo
        
        
        relfondo=""
        fondolabel=""
        cont=0
        while aux != None:
            archivo.writelines("{\nrank=same\n");
            rel=aux.year+"->"
            relinv=aux.year
           
            aux1= Nodocontenido()
            aux1=aux.first
            
            arriba=""
            if aux1.upheader ==None:
                arriba=str(aux1.arriba.dia)
            else:
                arriba=str(self.mestonum(str(aux1.upheader)))

            label=aux.year+arriba+str(aux1.dia)

            archivo.writelines(label+"[label=\""+str(aux1.dia)+"\"];\n")
            
            if aux1.derecha!=None:
                rel+= label+"->"
                auxcad= relinv
                relinv= label+"->"+ relinv
            else:
                rel+= label
                auxcad= relinv
                relinv= label+"->"+ relinv
            aux2= aux1.derecha    
            
            auxfondo= aux1.enfrente
            relfondoaux=""
            if auxfondo==None:
                relfondoaux=""
            else:
                
                relfondoaux= label+"->" 
                while auxfondo!=None:
                    if auxfondo.enfrente!=None:
                        label1=str(aux1.dia)+str(cont);
                        fondolabel+=label1+"[label=\""+ str(auxfondo.dia)+"\"];\n"
                        cont= cont+1
                        relfondoaux+= label1+"->"
                    else:
                        label1=str(aux1.dia)+str(cont);
                        fondolabel+=label1+"[label=\""+ str(auxfondo.dia)+"\"];\n"
                        cont= cont+1
                        relfondoaux+= label1  
                    auxfondo= auxfondo.enfrente
                relfondo+= relfondoaux+";\n"     
                    



            while aux2!=None:
                arriba=""
                n= Nodocontenido()
                if aux2.upheader ==None:
                    n = aux2.arriba
                    arriba=str(n.dia)
                else:
                    arriba=str(self.mestonum(str(aux2.upheader)))
                i = Nodocontenido()
                i = aux2.izquierda    
                label= str(i.dia)+arriba+str(aux2.dia)
                archivo.writelines(label+"[label=\""+str(aux2.dia)+"\"];\n")
                if aux2.derecha!=None:
                    rel+= label+"->"
                    auxcad= relinv
                    relinv= label+"->"+ relinv
                else:
                    rel+= label
                    auxcad= relinv
                    relinv= label+"->"+ relinv

                
                auxfondo= aux2.enfrente
                relfondoaux=""
                if auxfondo==None:
                    relfondoaux=""
                else:
                    relfondoaux= label+"->"
                    while auxfondo!=None:
                        if auxfondo.enfrente!=None:
                            label1=str(auxfondo.dia)+str(cont);
                            fondolabel+=label1+"[label=\""+ str(auxfondo.dia)+"\"];\n"
                            cont= cont+1
                            relfondoaux+= label1+"->"
                        else:
                            label1=str(auxfondo.dia)+str(cont);
                            fondolabel+=label1+"[label=\""+ str(auxfondo.dia)+"\"];\n"
                            cont= cont+1
                            relfondoaux+= label1  
                        auxfondo= auxfondo.enfrente
                    relfondo+= relfondoaux+";\n"     
                    

                aux2= aux2.derecha 
            archivo.writelines(rel + "[dir=R];\n") 
            archivo.writelines(relinv + "[dir=R];\n}")            
            aux=aux.siguiente
        archivo.writelines("\n { \n"+ fondolabel+"\n")    
        archivo.writelines(relfondo+"\n}")    

    def grabarcolumnas(self, archivo):
        aux= self.izquierda
        
        
        
        while aux != None:
            archivo.writelines("{\nrankdir=LR\n");
            rel=aux.mes+"->"
            relinv=aux.mes
            aux1= Nodocontenido()
            aux1=aux.first
            
            izquierda=""
            if aux1.leftheader ==None:
                izquierda=str(aux1.izquierda.dia)
            else:
                izquierda=str(aux1.leftheader)

            label=izquierda+str(self.mestonum(str(aux.mes)))+str(aux1.dia)

            archivo.writelines(label+"[label=\""+str(aux1.dia)+"\"];\n")
            
            if aux1.abajo!=None:
                rel+= label+"->"
                auxcad= relinv
                relinv= label+"->"+ relinv
            else:
                rel+= label
                auxcad= relinv
                relinv= label+"->"+ relinv
            aux2= aux1.abajo    
            
            while aux2!=None:
                izquierda=""
                n= Nodocontenido()
                if aux2.leftheader ==None:
                    n = aux2.izquierda
                    izquierda=str(n.dia)
                else:
                    izquierda=str(aux2.leftheader)
                i = Nodocontenido()
                i = aux2.arriba    
                label= izquierda+str(i.dia)+str(aux2.dia)
                archivo.writelines(label+"[label=\""+str(aux2.dia)+"\"];\n")
                if aux2.abajo!=None:
                    rel+= label+"->"
                    auxcad= relinv
                    relinv= label+"->"+ relinv
                else:
                    rel+= label
                    auxcad= relinv
                    relinv= label+"->"+ relinv
                aux2= aux2.abajo 
            archivo.writelines(rel + "[dir=LR];\n") 
            archivo.writelines(relinv + "[dir=LR];\n}")            
            aux=aux.siguiente        
               






    def imprimir(self):
        aux= self.izquierda
        print("Imprimir desde cabecera mes")
        while aux!= None:
            print (str(aux.mes) + "->"+ str(aux.first.dia) + "->" + str(aux.first.leftheader))
            cadena=""
            
            aux2= aux.first
            while aux2!= None:
                cad=""
                
                enfre= aux.first.enfrente
                while enfre !=None:
                    cad+= str(enfre.dia)+"->"
                    enfre= enfre.enfrente

                         
                

                cadena+=  str(aux2.leftheader)+"->"+ str(aux2.dia) + ":" + cad +"\n"
                
                aux2= aux2.abajo
            print cadena    
            aux = aux.siguiente  
    def imprimiryear(self):
        aux= self.abajo
        print("Imprimir desde cabecera year")
        while aux!= None:

            auxfila= Nodocontenido()
            auxfila= aux.first
            cadena=""

            while auxfila!=None:
                cadena+= str(auxfila.dia) + "->"
                auxfila=auxfila.derecha

            print (str(aux.year) + ":"+ cadena)
            
            aux = aux.siguiente   
    def existedia(self,nodo):
        aux= self.izquierda
        tabla = TablaHash()
        check= False;
        while aux != None:
                if aux.mes == nodo.mes:
                    yearigual = Nodocontenido()
                    yearigual = aux.first
                    while yearigual !=None:
                        if yearigual.leftheader == nodo.year:
                            if yearigual.dia== nodo.dia:
                                tabla = yearigual.tablahash
                                check= True
                                break
                            else:    

                                enfre= yearigual.enfrente
                                while enfre !=None:
                                    if enfre.dia == nodo.dia:
                                        tabla = enfre.tablahash
                                        check= True
                                        break
                                    enfre= enfre.enfrente


                        yearigual= yearigual.abajo    
                aux = aux.siguiente
        if check==True:
                
            return tabla
        else:
            return False                                 

class NodoHash:
    def __init__(self):
        self.habitacion=None
        self.user= None
        self.tarjeta=None
        self.siguiente=None
class TablaHash:
    def __init__(self):
        self.size=47
        self.datos=0
        self._keys = []
        self.tabla =  [ 0 for _ in range(int(self.size))]

    def agregar(self, elemento):
        
        aux = NodoHash()
        aux= elemento

        x=int(self.getkey(aux.habitacion))
        #print (x)
        #print ("tama-> " + str(int(self.size)))
        if self.tabla[x] == 0:
            self.tabla[x]= aux;
            self.datos= self.datos+1
            self.rehashing()
        else:
            aux2= self.tabla[x]
            while aux2.siguiente != None:
                aux2=aux2.siguiente
            aux2.siguiente= aux 
            
            self.datos= self.datos+1
            self.rehashing() 

    def agregaraux(self, elemento):
        
        aux = NodoHash()
        aux= elemento

        x=int(self.getkey(aux.habitacion))
        
        if self.tabla[x] == 0:
            self.tabla[x]= aux;
            self.datos= self.datos+1
            
        else:
            aux2= self.tabla[x]
            while aux2.siguiente != None:
                aux2=aux2.siguiente
            aux2.siguiente= aux 
            
            self.datos= self.datos+1
                  
            
    def rehashing(self):

        factor = (float(self.datos)/ float(self.size)) *100
        
        if (int(factor)<30) :
            
            self.size = (float(self.size)/float(2)) + float(1)

            
            aux= self.tabla
            self.tabla =  [ 0 for _ in range(int(self.size)+1)]
            self.datos=0
            for item in aux:
                if item != 0:
                    aux2=item
                    while aux2!= None:
                        nodo = NodoHash()
                        nodo.habitacion=aux2.habitacion
                        self.agregaraux(nodo)
                        aux2=aux2.siguiente
            self.rehashing()        
            
        elif (int(factor)>60):
           
            self.size = float(self.size)*float(2) 
            
            aux1= self.tabla
            self.tabla =  [ 0 for _ in range(int(self.size)+1)]
           
            self.size= int(self.size)+1
            
            self.datos=0
            print("Cambio")
            for item1 in aux1:

                if item1 != 0:
                    aux22=item1
                    while aux22!= None:
                        nodo = NodoHash()
                        nodo.habitacion=aux22.habitacion
                        self.agregaraux(nodo)
                        aux22=aux22.siguiente
            self.rehashing()      
            





                

    def getkey(self,habitacion):
        
        d = float(0.6180334) * float(habitacion)  
        b= str(d).split(".")
        c= float(d)- float(b[0])   

        index = float(c) * float(self.size)

        return int(index)
    def imprimirhash(self):
        archivo=open('Hash.dot', 'w')
        archivo.write('digraph G{\n')
        archivo.write("nodesep=.05;\n");
        archivo.write("rankdir = LR;\n");
        archivo.write("node [shape=record,width=.1,height=.1];\n");
        archivo.write("node [width = 1.5];\n");

        cadena=""
        i=0
        for item in self.tabla:
            if item==0:
                
                archivo.write( "node"+str(i) + "[label = \"0\"]; \n")
            else:
                aux=item
                relaciones=""
                while aux!=None:
                    archivo.write( "node"+str(i) + "[label = \" " +aux.habitacion+ "\"]; \n")
                    if aux.siguiente != None:
                        relaciones+= "node"+str(i)+"->"
                        i=i+1
                    else: 
                        if relaciones != "":  
                            relaciones+= "node"+str(i)    
                    aux= aux.siguiente  
                    
                if relaciones != "":
                    relaciones+=";"
                archivo.write(relaciones)      
            i=i+1    







        archivo.write("}");
        
        
        archivo.close()
        os.system('dot Hash.dot -o Hash.png -Tpng')    



from flask import Flask, request


app = Flask(__name__)

ListaUsuarios = ListaDobleEnlazada()
lista = Lista()
avl= AVLTree()

arbolb = ArbolB()
listaencabezados = listaencabezados()




@app.route('/Hola')
def hello_world():
    return 'Hello from Flask sale!'

@app.route('/Usuario', methods=['POST'])
def h1():
    
    usuario = request.form['usuario']
    contra = request.form['contra']
    direccion= request.form['direccion']
    telefono = request.form['telefono']
    edad= request.form['edad']
    ListaUsuarios.agregar_final(usuario,contra,direccion, telefono, edad)
    ListaUsuarios.recorrer_inicio_fin()
    
    return "True"
@app.route('/Check', methods = ['POST'])
def h2():
    usuario = request.form['usuario']
    contra = request.form['contra']
    verificar =ListaUsuarios.buscar(usuario,contra)
    print (verificar)
    return verificar  
@app.route('/Habitacion', methods = ['POST'])
def h3():
    nivel = request.form['nivel']
    numero = request.form['numero']
    idd = str(nivel)+str(numero)
    nodo= Nodosimple()
    nodo.nivel = nivel
    nodo.numero=numero
    nodo.idd = idd
    lista.insertar(nodo)
    lista.imprimir()

    return "True"

@app.route('/Costo', methods = ['POST'])
def h4():
    cuenta = request.form['cuenta']
    costo = request.form['costo']

    avl.insert(cuenta,costo) 
    avl.dibujarAvl()
    return "True"

@app.route('/EliminarCosto', methods = ['POST'])
def h40():
    cuenta = request.form['cuenta']
    

    avl.delete(cuenta) 
    avl.dibujarAvl()
    return "True"

@app.route('/ModificarCosto', methods = ['POST'])
def h41():
    cuenta = request.form['cuenta']
    nuevacuenta=request.form['nuevacuenta']
    nuevocosto= request.form['nuevocosto']
    

    avl.Modificar(cuenta,nuevacuenta,nuevocosto) 
    avl.dibujarAvl()
    return "True"        

@app.route('/Bitacora', methods = ['POST'])
def h5():
    usuario= request.form['usuario']
    cuenta = request.form['cuenta']
    costo = request.form['costo']
    habitacion= request.form['habitacion']
    fechai= request.form['fechai']
    fechaf= request.form['fechaf']



    arbolb.crearNodoInsertar(usuario,cuenta,costo,habitacion,fechai,fechaf)
    arbolb.dibujarArbol()

    return "True" 
@app.route('/Hash', methods = ['POST'])
def h7():
    mes = request.form['mes']
    year= request.form['year']
    dia = request.form['dia']
    if mes=="01":
            mes="enero"
    elif mes=="02":
            mes="febrero" 
    elif mes=="03":
            mes="marzo" 
    elif mes=="04":
            mes="abril"                            
    elif mes=="05":
            mes="mayo" 
    elif mes=="06":
            mes="junio" 
    elif mes=="07":
            mes="julio" 
    elif mes=="08":
            mes="agosto" 
    elif mes=="09":
            mes="septiembre" 
    elif mes=="10":
            mes="octubre" 
    elif mes=="11":
            mes="noviembre" 
    elif mes=="12":
            mes="diciembre"                                                         
    nodo = matriz()
    nodo.mes= str(mes)
    nodo.year= str(year)
    nodo.dia= str(dia)

    t=""
    if listaencabezados.existedia(nodo) != False:
        tabla= TablaHash()
        tabla = listaencabezados.existedia(nodo)
        tabla.imprimirhash()
        t="True"
        
    else:
        t="False"

    return t    
        

@app.route('/Dispersa', methods = ['POST'])
def h6():
    mes = request.form['mes']
    year= request.form['year']
    dia = request.form['dia']
    usuario = request.form['usuario']
    habitacion= request.form['habitacion']
    tarjeta = request.form['tarjeta']             

    if mes=="01":
            mes="enero"
    elif mes=="02":
            mes="febrero" 
    elif mes=="03":
            mes="marzo" 
    elif mes=="04":
            mes="abril"                            
    elif mes=="05":
            mes="mayo" 
    elif mes=="06":
            mes="junio" 
    elif mes=="07":
            mes="julio" 
    elif mes=="08":
            mes="agosto" 
    elif mes=="09":
            mes="septiembre" 
    elif mes=="10":
            mes="octubre" 
    elif mes=="11":
            mes="noviembre" 
    elif mes=="12":
            mes="diciembre"                                                         
    nodo = matriz()
    nodo.mes= str(mes)
    nodo.year= str(year)
    nodo.dia= str(dia)

    print (dia +"/" + mes + "/"+ year)
    if listaencabezados.existedia(nodo) == False:
        nodohash= NodoHash()
        nodohash.habitacion= habitacion
        nodohash.user= usuario
        nodohash.tarjeta= tarjeta
        tabla= TablaHash()
        tabla.agregar(nodohash)
        tabla.imprimirhash()
        
        nodo.tablahash= tabla


        listaencabezados.recibir(nodo)
        print("entro no existe")
    else:
        tabla= TablaHash()
        tabla = listaencabezados.existedia(nodo)
        nodohash= NodoHash()
        nodohash.habitacion= habitacion
        nodohash.user= usuario
        nodohash.tarjeta= tarjeta

        tabla.agregar(nodohash)
        print("entro existe")
        tabla.imprimirhash()


    listaencabezados.imprimir()
    listaencabezados.imprimiryear()
    listaencabezados.dibujardispersa()  
    return "True"   


            



    
    




if __name__ == "__main__":
 

 app.run(debug=True, host='192.168.1.7')                
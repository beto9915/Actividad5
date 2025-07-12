class Program:
    opcion=0
    nuevoEstudiante=[]
    while opcion!=0:
        print("""1. Ingresar estudiante
            2. Mostrar estudiantes agregados
            3. Buscar estudiante
            4. Calcular promedio de todos los estudiantes""")
        opcion = int(input("Seleccione una opcion: "))
        try:
            if opcion==1:
                nombre=input("Ingrese nombre: ")
                carnet=int(input("Ingrese numero de carne"))
                carrera=input("Ingrese carrera que cursa")
                notaFinal=int(input("Ingrese nota final: "))
                estudiante=Estudiante(nombre, carnet, carrera, notaFinal)
                nuevoEstudiante.__add__(estudiante)
                print("\nEstudiante ingresado con exito...")
                print("presione ENTER para continuar...")
                input()
            if opcion==2:
class Estudiante:
    def __init__(self, nombre, carnet, carrera, notaFinal):
        self.nombre=nombre
        self.carnet=carnet
        self.carrera=carrera
        self.notaFinal=notaFinal
    def MostrarEstudiante(self):
        print(f"Nombre: {self.nombre}, Carnet: {self.carnet}, Carrera: {self.carrera}, Nota Final: {self.notaFinal}")

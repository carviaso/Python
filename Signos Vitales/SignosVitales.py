
#consultas = []
pacientes = [
    ["12345678", "Ana Pérez", "8888-8888", "ana@mail.com"],
    ["87654321", "Carlos Gómez", "7777-7777", "carlos@mail.com"]
]

doctores = [
    ["55566677", "Dra. María Ruiz", "Cardiología"],
    ["44455566", "Dr. Juan Rojas", "Pediatría"]
]

consultas = [
    ["12345678", "55566677", "2025-03-104",
     [
         ["Presión Arterial", "120/80"],
         ["Frecuencia Cardíaca", "72 bpm"],
         ["Temperatura", "36.5°C"]
     ]
     ],
    ["12345678", "55566677", "2025-03-104",
     [
         ["Presión Arterial", "140/80"],
         ["Frecuencia Cardíaca", "72 bpm"],
         ["Temperatura", "36.5°C"]
     ]
     ],
    ["12345678", "55566677", "2025-03-104",
     [
         ["Presión Arterial", "160/80"],
         ["Frecuencia Cardíaca", "72 bpm"],
         ["Temperatura", "36.5°C"]
     ]
     ]
]



def registrar_paciente():
    print("\nRegistro de Paciente")
    cedula = input("Ingrese la cédula: ")
    for paciente in pacientes:
        if paciente[0] == cedula:
            print("Error: La cedula ya esta registrada.")
            return
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo electrónico: ")
    pacientes.append([cedula, nombre, telefono, correo, []])
    print("Paciente registrado con éxito.")
    
def ver_paciente():
    for paciente in pacientes:
        print(f"cedula:{paciente[0]} \t nombre:{paciente[1]} \t telefono:{paciente[2]} \t correo:{paciente[3]}")
        
def ver_doctor():
    for doctor in doctores:
        print(f"cedula:{doctor[0]} \t nombre:{doctor[1]} \t especialidad:{doctor[2]}")
def registrar_doctor():
    print("\nRegistro de Doctor")
    cedula = input("Ingrese la cédula: ")
    for doctor in doctores:
        if doctor[0] == cedula:
            print("Error: La cédula ya está registrada.")
            return
    nombre = input("Ingrese el nombre: ")
    especialidad = input("Ingrese la especialidad: ")
    doctores.append([cedula, nombre, especialidad])
    print("Doctor registrado con éxito.")

def registrar_control_signos():
    print("\nRegistro de Control de Signos Vitales")
    cedula_paciente = input("Ingrese la cédula del paciente: ")
    cedula_doctor = input("Ingrese la cédula del doctor: ")
    fecha = input("Ingrese la fecha de la consulta: ")
    
    if not any(paciente[0] == cedula_paciente for paciente in pacientes):
        print("Error: El Paciente no se encontro.")
        return
    if not any(doctor[0] == cedula_doctor for doctor in doctores):
        print("Error: El Doctor no se encontro.")
        return
    
    presion_arterial = input("Ingrese la presión arterial: ")
    frecuencia_cardiaca = input("Ingrese la frecuencia cardíaca: ")
    temperatura = input("Ingrese la temperatura: ")
    frecuencia_respiratoria = input("Ingrese la frecuencia respiratoria: ")
    saturacion_oxigeno = input("Ingrese la saturación de oxígeno: ")
    
    signos_vitales = [["Presión Arterial", presion_arterial],
                      ["Frecuencia Cardíaca", frecuencia_cardiaca],
                      ["Temperatura", temperatura],
                      ["Frecuencia Respiratoria", frecuencia_respiratoria],
                      ["Saturación de Oxígeno", saturacion_oxigeno]]
    
    consultas.append([cedula_paciente, cedula_doctor, fecha, signos_vitales])
    print("Consulta registrada con éxito.")

def ver_historial_paciente():
    print("\nHistorial de Signos Vitales")
    cedula = input("Ingrese la cédula del paciente: ")
    encontrado = False
    for consulta in consultas:
        if consulta[0] == cedula:
            encontrado = True
            print(f"Fecha: {consulta[2]}, Doctor: {consulta[1]}")
            print("Signos Vitales:")
            for signo in consulta[3]:
                print(f" - {signo[0]}: {signo[1]}")
    if not encontrado:
        print("No se encontraron consultas para este paciente.")

def menu():
    while True:
        print("\nMenú de Opciones")
        print("1. Registrar Paciente")
        print("2. Registrar Doctor")
        print("3. Registrar Control de Signos Vitales")
        print("4. Ver Historial de Signos Vitales de un Paciente")
        print("5. Ver Pacientes")
        print("6. Ver Doctores")
        print("8. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_doctor()
        elif opcion == "3":
            registrar_control_signos()
        elif opcion == "4":
            ver_historial_paciente()
        elif opcion == "5":
            ver_paciente()
        elif opcion == "6":
            ver_doctor()
        elif opcion == "8":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

menu()

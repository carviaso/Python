# -*- coding: utf-8 -*-
"""
Sistema de Seguimiento de Signos Vitales en Pacientes
"""

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


def ver_pacientes():
    print(f"Cédula: \t - nombre: - teléfono: - correo:")
    for paciente in pacientes:
        # print(f"\tCédula: {paciente[0]} - nombre: {paciente[1]} - teléfono: {paciente[2]} - correo: {paciente[3]}")
        print(f"{paciente[0]} - \t {paciente[1]} - \t {paciente[2]} - \t {paciente[3]}")

def registrar_paciente():
    cedula = input("Ingrese la cédula del paciente: ")
    for paciente in pacientes:
        if paciente[0] == cedula:
            print("⚠️ Error: La cédula ya está registrada.")
            return
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    correo = input("Ingrese el correo: ")
    pacientes.append([cedula, nombre, telefono, correo])
    print("✅ Paciente registrado con éxito.")


def registrar_doctor():
    cedula = input("Ingrese la cédula del doctor: ")
    for doctor in doctores:
        if doctor[0] == cedula:
            print("⚠️ Error: La cédula ya está registrada.")
            return
    nombre = input("Ingrese el nombre: ")
    especialidad = input("Ingrese la especialidad: ")
    doctores.append([cedula, nombre, especialidad])
    print("✅ Doctor registrado con éxito.")


def registrar_signos_vitales():
    cedula_paciente = input("Ingrese la cédula del paciente: ")
    cedula_doctor = input("Ingrese la cédula del doctor: ")

    paciente_existe = any(p[0] == cedula_paciente for p in pacientes)
    doctor_existe = any(d[0] == cedula_doctor for d in doctores)

    if not paciente_existe or not doctor_existe:
        print("⚠️ Error: Paciente o doctor no encontrado.")
        return

    fecha = input("Ingrese la fecha de la consulta (YYYY-MM-DD): ")
    presion = input("Ingrese la presión arterial (Ejemplo: 120/80 mmHg): ")
    frecuencia = int(
        input("Ingrese la frecuencia cardíaca (Ejemplo: 72 bpm): "))
    temperatura = float(input("Ingrese la temperatura (Ejemplo: 36.5°C): "))

    # Validaciones de rango
    if frecuencia < 60 or frecuencia > 100:
        print("⚠️ Advertencia: Frecuencia cardíaca fuera de rango.")

    if temperatura < 36.0 or temperatura > 37.5:
        print("⚠️ Advertencia: Temperatura fuera de rango.")

    consultas.append([cedula_paciente, cedula_doctor, fecha, [["Presión Arterial", presion], [
                     "Frecuencia Cardíaca", str(frecuencia) + " bpm"], ["Temperatura", str(temperatura) + "°C"]]])
    print("✅ Signos vitales registrados con éxito.")


def ver_historial():
    cedula = input("Ingrese la cédula del paciente: ")
    encontrado = False
    for consulta in consultas:
        if consulta[0] == cedula:
            print(f"\n📅 Fecha: {consulta[2]}")
            for signo in consulta[3]:
                print(f"{signo[0]}: {signo[1]}  mmHg")
            encontrado = True
    if not encontrado:
        print("❌ No se encontraron registros para este paciente.")


def reporte_hipertension():
    print("\n📢 Reporte de Pacientes con Hipertensión:")
    for consulta in consultas:
        for signo in consulta[3]:
            if signo[0] == "Presión Arterial":
                valores = signo[1].split('/')
                if int(valores[0]) > 130 or int(valores[1]) > 80:
                    print(
                        f"- {consulta[0]} tiene presión arterial alta: {signo[1]}")
                elif int(valores[0]) < 130 or int(valores[1]) > 80:
                    print(
                        f"- {consulta[0]} tiene presión arterial normal: {signo[1]}")


def calcular_promedio():
    cedula = input("Ingrese la cédula del paciente: ")
    suma_frecuencia = 0
    suma_temperatura = 0
    conteo = 0

    for consulta in consultas:
        if consulta[0] == cedula:
            for signo in consulta[3]:
                if signo[0] == "Frecuencia Cardíaca":
                    suma_frecuencia += int(signo[1].split()[0])
                if signo[0] == "Temperatura":
                    suma_temperatura += float(signo[1].split("°")[0])
            conteo += 1

    if conteo == 0:
        print("❌ No hay datos suficientes.")
        return

    print(f"\nPromedio Frecuencia: {suma_frecuencia/conteo:.2f} bpm")
    print(f"Promedio Temperatura: {suma_temperatura/conteo:.2f}°C")


while True:
    print("\n--- Menú del Sistema ---")
    print("1. Registrar Paciente")
    print("8. Ver Paciente")
    print("2. Registrar Doctor")
    print("3. Registrar Signos Vitales")
    print("4. Ver Historial")
    print("5. Reporte de Hipertensión")
    print("6. Calcular Promedio")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        registrar_doctor()
    elif opcion == "3":
        registrar_signos_vitales()
    elif opcion == "4":
        ver_historial()
    elif opcion == "5":
        reporte_hipertension()
    elif opcion == "6":
        calcular_promedio()
    elif opcion == "8":
        ver_pacientes()
    elif opcion == "7":
        break

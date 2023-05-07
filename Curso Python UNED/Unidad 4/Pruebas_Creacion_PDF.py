from fpdf import FPDF

# Creacion del Objeto FPDF
pdf = FPDF()

# Agragando Pagina
pdf.add_page()

# Establece fuentes negrita
pdf.set_font("Helvetica", 'B', size=15)

# Establece fuentes Italica
pdf.set_font("Helvetica", 'I', size=12)

# Establece fuentes
pdf.set_font("Helvetica", size=8)

# Agregando Contenido
# -------------------------------------------
# Establece fuentes negrita
pdf.set_font("Helvetica", 'B', size=15)
# Texto Centrado
pdf.cell(200, 10, txt="Nocturna sin Patria", ln=1, align='C')

# Establece fuentes italica
pdf.set_font("Helvetica", 'I', size=12)

# Texto Centrado
pdf.cell(200, 10, txt="Yo no quiero un cuchillo en manos de la patría.", ln=2, align='C')
pdf.cell(200, 10, txt="Ni un cuchilo ni un rifle para nadie", ln=4, align='C')
pdf.cell(200, 10, txt="la tierra es para todos,", ln=6, align='C')
pdf.cell(200, 10, txt="como el aire", ln=8, align='C')
pdf.cell(200, 10, txt="Me Gustaría tener manos enormes,", ln=10, align='C')
pdf.cell(200, 10, txt="violentas y salvajes,", ln=12, align='C')
pdf.cell(200, 10, txt="para arrancar fronteras una a una", ln=14, align='C')
pdf.cell(200, 10, txt="y dejar de frontera solo el aire.", ln=16, align='C')
pdf.cell(200, 10, txt="Que nadie tenga tierra", ln=18, align='C')
pdf.cell(200, 10, txt="como tiene tierra:", ln=20, align='C')
pdf.cell(200, 10, txt="que todos tengan tierra ", ln=22, align='C')
pdf.cell(200, 10, txt="como tienen el aire.", ln=24, align='C')

# Guardando el PDF
pdf.output("Prueba.pdf")


# try:
#   Código susceptible a lanzar error
# except PosibleErrorLanzado:
#   Código para manejar el error
# Else:
#   Código complementario si no se lanzó el error

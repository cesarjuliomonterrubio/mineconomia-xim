from flask import Flask, render_template, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def inicio():
    fecha_actual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    return render_template('index.html', 
                         titulo="Economía Mineconómica", 
                         fecha_actual=fecha_actual)

# NUEVA RUTA PARA AGRADECIMIENTOS
@app.route('/agradecimientos')
def agradecimientos():
    return render_template('agradecimientos.html', 
                         titulo="Agradecimientos",
                         seccion="agradecimientos")

# RUTAS PARA CADA SECCIÓN
@app.route('/carrera')
def carrera():
    return render_template('carrera.html', 
                         titulo="Mi Carrera en Economía",
                         seccion="carrera")

@app.route('/economia-minecraft')
def economia_minecraft():
    return render_template('economia_minecraft.html', 
                         titulo="Economía en Minecraft",
                         seccion="economia-minecraft")

@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html', 
                         titulo="Mis Proyectos",
                         seccion="proyectos")

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', 
                         titulo="Contacto",
                         seccion="contacto")

# RUTAS PARA RECURSOS ECONÓMICOS
@app.route('/capital-humano')
def capital_humano():
    return render_template('recursos/capital_humano.html', 
                         titulo="Capital Humano",
                         seccion="recursos")

@app.route('/capital-fisico')
def capital_fisico():
    return render_template('recursos/capital_fisico.html', 
                         titulo="Capital Físico",
                         seccion="recursos")

@app.route('/innovacion')
def innovacion():
    return render_template('recursos/innovacion.html', 
                         titulo="Innovación Tecnológica",
                         seccion="recursos")

@app.route('/instituciones')
def instituciones():
    return render_template('recursos/instituciones.html', 
                         titulo="Instituciones Económicas",
                         seccion="recursos")

@app.route('/globalizacion')
def globalizacion():
    return render_template('recursos/globalizacion.html', 
                         titulo="Globalización Económica",
                         seccion="recursos")

@app.route('/crecimiento')
def crecimiento():
    return render_template('recursos/crecimiento.html', 
                         titulo="Crecimiento Económico",
                         seccion="recursos")

# NUEVAS RUTAS PARA LOGROS ACADÉMICOS INTERACTIVOS
@app.route('/licenciatura-economia')
def licenciatura_economia():
    return render_template('logros/licenciatura.html', 
                         titulo="Licenciatura en Economía",
                         seccion="logros")

@app.route('/econometria-aplicada')
def econometria_aplicada():
    return render_template('logros/econometria.html', 
                         titulo="Econometría Aplicada",
                         seccion="logros")

@app.route('/finanzas-corporativas')
def finanzas_corporativas():
    return render_template('logros/finanzas.html', 
                         titulo="Finanzas Corporativas",
                         seccion="logros")

@app.route('/economia-internacional')
def economia_internacional():
    return render_template('logros/economia_internacional.html', 
                         titulo="Economía Internacional",
                         seccion="logros")

@app.route('/analisis-datos')
def analisis_datos():
    return render_template('logros/analisis_datos.html', 
                         titulo="Análisis de Datos",
                         seccion="logros")

@app.route('/economia-digital')
def economia_digital():
    return render_template('logros/economia_digital.html', 
                         titulo="Economía Digital",
                         seccion="logros")

# NUEVAS RUTAS PARA CONCEPTOS ECONÓMICOS
@app.route('/oferta')
def oferta():
    return render_template('conceptos/oferta.html', 
                         titulo="Oferta - Concepto Completo",
                         seccion="conceptos")

@app.route('/demanda')
def demanda():
    return render_template('conceptos/demanda.html', 
                         titulo="Demanda - Concepto Completo",
                         seccion="conceptos")

@app.route('/is-lm')
def is_lm():
    return render_template('conceptos/is_lm.html', 
                         titulo="Modelo IS-LM - Concepto Completo",
                         seccion="conceptos")

@app.route('/descargar-cv')
def descargar_cv():
    return "Descarga de CV - Próximamente"

@app.route('/linkedin')
def linkedin():
    return redirect("https://linkedin.com")


# NUEVAS RUTAS PARA TIPOS DE MERCADO
@app.route('/tipos-mercado')
def tipos_mercado():
    return render_template('conceptos/tipos_mercado.html', 
                         titulo="Tipos de Mercado",
                         seccion="conceptos")

@app.route('/competencia-perfecta')
def competencia_perfecta():
    return render_template('conceptos/competencia_perfecta.html', 
                         titulo="Competencia Perfecta",
                         seccion="conceptos")

@app.route('/oligopolio')
def oligopolio():
    return render_template('conceptos/oligopolio.html', 
                         titulo="Oligopolio",
                         seccion="conceptos")

@app.route('/competencia-monopolistica')
def competencia_monopolistica():
    return render_template('conceptos/competencia_monopolistica.html', 
                         titulo="Competencia Monopolística",
                         seccion="conceptos")

@app.route('/monopolio')
def monopolio():
    return render_template('conceptos/monopolio.html', 
                         titulo="Monopolio",
                         seccion="conceptos")

@app.route('/regresion-lineal')
def regresion_lineal():
    return render_template('recursos/regresion_lineal.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
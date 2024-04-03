import tkinter as tk
from tkinter import filedialog
import pandas as pd
from tkinter import filedialog


reglas = [
   {
  "sintomas_presentes": ["mancha_marron", "lesiones"],
  "diagnostico": "La planta sufre de marchitez angular",
  "explicacion": "Presencia de mancha marrón o amarilla y tiene lesiones."
},
{"sintomas_presentes": ["manchas_oscuras_fruto", "pudricion_acuosa"],
     "diagnostico": "La planta podría tener podredumbre negra",
     "explicacion": "Presencia de manchas oscuras en el fruto y pudrición acuosa."},

{"sintomas_presentes": ["manchas_oscuras_fruto", "pudricion"],
    "diagnostico": "Antracnosis",
    "explicacion": "Presencia de manchas oscuras en el fruto y pudrición."},
{
  "sintomas_presentes": ["manchas_negras_hojas", "caida_prematura_hojas"],
  "diagnostico": "La planta sufre de mancha negra",
  "explicacion": "Presencia de manchas negras en las hojas y caída prematura en hojas."
}
,
{
  "sintomas_presentes": ["manchas_negras_alargadas", "reduccion_area_foliar"],
  "diagnostico": "La planta sufre de sigatoka negra",
  "explicacion": "Presencia de manchas negras alargadas y reducción del área foliar."
}
,
{
  "sintomas_presentes": ["manchas_negras_circulares_hojas_frutos", "caida_hojas"],
  "diagnostico": "La planta sufre de mancha de asfalto",
  "explicacion": "Presencia de manchas negras circulares en hojas y frutos y caída de hojas."
}
,{
  "sintomas_presentes": ["marchitez", "decoloracion_tallo_raices", "perdida_vigor"],
  "diagnostico": "La planta sufre de marchitez por Fusarium",
  "explicacion": "Presencia de marchitez, decoloración del tallo y raíces, y pérdida de vigor."
},
{
  "sintomas_presentes": ["marchitez", "necrosis_cogollo", "hojas_no_abren"],
  "diagnostico": "La planta sufre de pudrición del cogollo",
  "explicacion": "Presencia de marchitez y necrosis del cogollo, y las hojas no abren."
}
,
{
  "sintomas_presentes": ["pustulas_naranja_parte_inferior_hojas"],
  "diagnostico": "La planta sufre de roya de café",
  "explicacion": "Presencia de pústulas del color naranja en la parte inferior de las hojas."
}
,
{
  "sintomas_presentes": ["polvo_blanco_gris_hojas", "tallo_deforme"],
  "diagnostico": "La planta sufre de oídio",
  "explicacion": "Presencia de polvo blanco y gris en las hojas y tiene tallo deforme."
}
,
{
  "sintomas_presentes": ["mosaico_hojas", "deformacion_hojas_fruto"],
  "diagnostico": "La planta sufre de virosis",
  "explicacion": "Presencia de mosaico en las hojas y deformación de hojas y fruto."
}
]

# Función para cargar los síntomas desde un archivo Excel
def cargar_sintomas():
    # Abrir el cuadro de diálogo para seleccionar el archivo
    archivo = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
    if archivo:
        # Leer el archivo Excel en un DataFrame de pandas
        df = pd.read_excel(archivo)
        # Extraer las columnas relevantes del DataFrame
        columnas_relevantes = [
            'manchas_oscuras_fruto',
            'pudricion_acuosa',
            'pudricion',
            'manchas_oscuras_hojas_frutos',
            'manchas_negras_hojas',
            'caida_prematura_hojas',
            'manchas_negras_alargadas',
            'reduccion_area_foliar',
            'manchas_negras_circulares_hojas_frutos',
            'marchitez',
            'decoloracion_tallo_raices',
            'perdida_vigor',
            'necrosis_cogollo',
            'hojas_no_abren',
            'pustulas_naranja_parte_inferior_hojas',
            'polvo_blanco_gris_hojas',
            'tallo_deforme',
            'mosaico_hojas',
            'deformacion_hojas_fruto',
            'mancha_marron',
            'lesiones'
        ]
        datos_filtrados = df[columnas_relevantes].to_dict(orient='records')
        return datos_filtrados
    else:
        return None

def evaluar_reglas(sintomas_entrada, reglas):
    diagnosticos = []
    explicaciones = []
    for sintomas in sintomas_entrada:
        rule_found = False
        for regla in reglas:
            sint_presentes = all(sintomas.get(s, False) for s in regla["sintomas_presentes"])
            if sint_presentes:
                diagnosticos.append(regla["diagnostico"])
                explicaciones.append(regla["explicacion"])
                rule_found = True
                break
        if not rule_found:
            diagnosticos.append("Diagnóstico genérico")
            explicaciones.append("No se encontró una regla específica para estos síntomas.")
    return diagnosticos, explicaciones

# Función para evaluar síntomas y obtener diagnósticos y explicaciones
def evaluar_sintomas():
    datos_filtrados=cargar_sintomas()
    # Limpiar el widget de texto de entrada de síntomas
    entrada_sintomas.delete(1.0, tk.END)

    # Contador para enumerar las salidas de síntomas
    numero_salida = 1

    # Filtrar y mostrar solo los síntomas en True
    for objeto in datos_filtrados:
        sintomas_true = [k.replace('_', ' ') for k, v in objeto.items() if v is True]
        entrada_sintomas.insert(tk.END, f"Síntomas {numero_salida}: {', '.join(sintomas_true)}\n")
        numero_salida += 1
      
    # Llamar a la función evaluar_reglas para obtener diagnósticos y explicaciones
    diagnosticos, explicaciones = evaluar_reglas(datos_filtrados, reglas)

    # Mostrar los resultados en el widget de texto de resultados
    if diagnosticos:
        numero_salida_diagnostico = 1
        texto_resultados.delete(1.0, tk.END)  # Limpiar el widget de texto
        for diagnostico, explicacion in zip(diagnosticos, explicaciones):
            texto_resultados.insert(tk.END, f"{numero_salida_diagnostico}:{diagnostico} Razón: {explicacion}\n")
            numero_salida_diagnostico+=1
    else:
        texto_resultados.delete(1.0, tk.END)  # Limpiar el widget de texto
        texto_resultados.insert(tk.END, "No se encontraron enfermedades basadas en los síntomas dados.")

    # Evaluación de síntomas y obtención de diagnósticos y explicaciones
        diagnosticos, explicaciones = evaluar_reglas(datos_filtrados, reglas)

# Impresión de resultados
        if diagnosticos:
            for diagnostico, explicacion in zip(diagnosticos, explicaciones):
              print(f"{diagnostico} Razón: {explicacion}")
        else:
            print("No se encontraron enfermedades basadas en los síntomas dados.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Evaluación de Síntomas y Diagnósticos")

# Crear un marco para organizar los elementos de la interfaz
marco = tk.Frame(ventana, padx=10, pady=10)
marco.pack()

# Etiqueta para el título 
etiqueta_sintomas = tk.Label(marco, text="Cuestionario de enfermedades Lab Jafeth C04657", font=("Arial", 14, "bold"))
etiqueta_sintomas.pack()


# Etiqueta para el título "Síntomas"
etiqueta_sintomas = tk.Label(marco, text="Síntomas", font=("Arial", 14, "bold"))
etiqueta_sintomas.pack()

# Widget de texto para ingresar los síntomas
entrada_sintomas = tk.Text(marco, height=10, width=50, font=("Arial", 12))
entrada_sintomas.pack()


# Separador entre la entrada de síntomas y el botón
separador = tk.Frame(marco, height=2, bd=1, relief=tk.SUNKEN)
separador.pack(fill=tk.X, padx=5, pady=5)

# Botón para evaluar síntomas
boton_evaluar = tk.Button(marco, text="Evaluar Síntomas", command=evaluar_sintomas, font=("Arial", 12, "bold"))
boton_evaluar.pack()

# Etiqueta para el título "Diagnósticos"
etiqueta_diagnosticos = tk.Label(marco, text="Diagnósticos", font=("Arial", 14, "bold"))
etiqueta_diagnosticos.pack()

# Widget de texto para mostrar los resultados
texto_resultados = tk.Text(marco, height=10, width=50, font=("Arial", 12))
texto_resultados.pack()

ventana.mainloop()
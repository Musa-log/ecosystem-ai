from transformers import AutoModelForCausalLM, AutoTokenizer
import json
import os
from datetime import datetime

print("🚀 Iniciando Ecosystem AI Employee...")

print("📚 Cargando modelo Qwen (100% libre)...")
modelo = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2-0.5B-Instruct",
    device_map="cpu",
    torch_dtype="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2-0.5B-Instruct")
print("✅ Modelo listo!")

archivo_memoria = "conversaciones.json"
if os.path.exists(archivo_memoria):
    with open(archivo_memoria, 'r') as f:
        memoria = json.load(f)
    print(f"📝 Recuerdo {len(memoria)} conversaciones")
else:
    memoria = []
    print("📝 Memoria nueva")

print("\n" + "="*50)
print("🤖 ECOSYSTEM AI EMPLOYEE")
print("="*50)
print("Empresas del holding:")
print("  1. Finanzas")
print("  2. Retail")
print("  3. Logística")
print("  4. General")
print("="*50)

empresa = input("¿Qué empresa? (1-4): ")

if empresa == "1":
    nombre_empresa = "Finanzas"
    personalidad = "Eres experto financiero. Hablas de números, inversiones, ahorro."
elif empresa == "2":
    nombre_empresa = "Retail"
    personalidad = "Eres vendedor experto. Conoces productos, precios, promociones."
elif empresa == "3":
    nombre_empresa = "Logística"
    personalidad = "Eres especialista en envíos, rutas, tiempos de entrega."
else:
    nombre_empresa = "General"
    personalidad = "Eres asistente amable y servicial."

print(f"\n✅ Empleado asignado a: {nombre_empresa}")
print("💬 Escribe 'salir' para terminar, 'memoria' para ver historial\n")

while True:
    pregunta = input("\n👤 Tú: ")
    
    if pregunta.lower() == 'salir':
        with open(archivo_memoria, 'w') as f:
            json.dump(memoria, f)
        print("👋 Memoria guardada. ¡Hasta luego!")
        break
    
    if pregunta.lower() == 'memoria':
        print("\n📖 Últimas conversaciones:")
        for i, conv in enumerate(memoria[-5:]):
            print(f"  {i+1}. {conv['pregunta'][:50]}...")
        continue
    
    # Formato de chat para Qwen
    contexto = f"<|im_start|>system\n{personalidad}<|im_end|>\n<|im_start|>user\n{pregunta}<|im_end|>\n<|im_start|>assistant\n"
    
    inputs = tokenizer(contexto, return_tensors="pt", max_length=800, truncation=True)
    outputs = modelo.generate(**inputs, max_new_tokens=150, temperature=0.7)
    respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    # Limpiar la respuesta
    respuesta = respuesta.split("<|im_start|>assistant\n")[-1].strip()
    
    print(f"🤖 {nombre_empresa}: {respuesta}")
    
    memoria.append({
        "pregunta": pregunta,
        "respuesta": respuesta,
        "empresa": nombre_empresa,
        "fecha": str(datetime.now())
    })

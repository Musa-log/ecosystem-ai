from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

print("Cargando Llama 3.2... esto toma 1-2 minutos")

modelo = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.2-1B-Instruct",
    device_map="cpu",
    load_in_4bit=True,
    torch_dtype=torch.float16
)

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")

print("¡Modelo listo! Pregúntame algo:")
while True:
    pregunta = input("Tú: ")
    if pregunta == "salir":
        break
    
    inputs = tokenizer(pregunta, return_tensors="pt")
    outputs = modelo.generate(**inputs, max_new_tokens=100)
    respuesta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(f"AI: {respuesta}")

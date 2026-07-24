def extract_total(text: str):

    for line in text.splitlines():
        if "total" in line.lower():
            parts = line.split()
            value=(parts[-1].replace("$", "").replace(".", ""))
            return float(value)
        
    return "No se encontró el total en el texto proporcionado."

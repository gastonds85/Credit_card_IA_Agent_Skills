from skills.read_text import read_text
from skills.extract_total import extract_total

class CreditCardAgent:

    def __init__(self):
        self.summary = ""

    def say_hello(self):
        return "¡Hola! Soy tu agente de tarjeta de crédito. ¿En qué puedo ayudarte hoy?"

    def load_summary(self, file_path: str) -> None:
        self.summary = read_text(file_path)

    def get_summary(self):
        return self.summary

    def get_total(self)-> float:
        return extract_total(self.summary)

    def answer_question(self, question: str):
        if "total" in question.lower():
            return self.get_total()
        elif "minimo" in question.lower() or "minimum" in question.lower():
            return "La consulta del pago mínimo todavía no está implementada."
        else:
            return "No entendí la pregunta."

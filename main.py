from skills.hello import say_hello
from skills.read_text import read_text
from skills.extract_total import extract_total




def main():
    content = read_text("data/invoice.txt")
    total = extract_total(content)
    print(f"El total de la tarjeta es: {total}")








if __name__ == "__main__":
    main()
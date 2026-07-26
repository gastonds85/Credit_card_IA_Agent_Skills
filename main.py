from agent import CreditCardAgent

def main():
    agent = CreditCardAgent()
    agent.load_summary("data/invoice.txt")
    print(agent.get_summary())
    print(f"Total: ${agent.get_total():.2f}")
    print(f"El total a pagar es: ${agent.answer_question('What is the total amount?')}")


if __name__ == "__main__":
    main()
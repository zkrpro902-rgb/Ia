def chatbot_reponse(question):
    # Ici, tu remplaceras par l'appel à ton API
    return f"[IA] Tu as dit : '{question}'. (Réponse simulée - ajoute ton API ici !)"

# Boucle de conversation
print("🤖 IA Demo - Tape 'quit' pour arrêter.")
while True:
    user_input = input("Toi : ")
    if user_input.lower() == "quit":
        break
    print(chatbot_reponse(user_input))

for i in range(5):
    meme_dict = {
        "CRINGE": "Algo excepcionalmente raro o embarazoso",
        "LOL": "Una respuesta común a algo gracioso",
        "RED FLAG": "Una mala señal de alguna cosa o persona",
        "AURA": "Descripcion de alguien o algo que se define en increible o epico",
        "GOD": "Algo bueno, bonito, divertido, o en general positivo"
    }
    print()
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Palabra no agregada al diccionario")

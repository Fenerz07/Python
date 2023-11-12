def hangman_game(word):
    """
    The hangman game works with the parameter word which is the one we are looking for and the trials parameter which corresponds to the letters to form this word.
    Settings:
        :param word string: character string corresponding to a vocabulary word.
        :param l string: character string containing only one letter and it cannot be reused several times during a single execution.
    """
    print("Welcome to the Hangman Game !")
    print(" ==========Y= ")
    print(" ||/          ")  
    print(" ||           ")
    print(" ||           ")  
    print(" ||           ")  
    print("/||           ") 
    print("==============")
    e=8
    t=0
    a=0
    dt=""
    while e != 0:
        e=e-1
        b=0
        l=input("Choose your letter : ")
        for i in word:
            if l == i :
                b=1
                a=a+1
                e=e+1
                print("Found !")
                if a==len(word) :
                    print("Victory !")
                    return "p"
        if b==0:
            print("Not Found !")
            t=t+1    
            print(" ==========Y= ")
            if t>=1 :
                print(" ||/       |  ")
            if t>=2 :
                print(" ||        0  ")
            if t==3 :
                print(" ||        |  ") 
            if t==4 :
                print(" ||       /|  ")
            if t>=5 :
                print(" ||       /|\ ")
            if t==6 :
                print(" ||        |  ") 
            if t==7 :
                print(" ||       /|  ") 
            if t==8 :
                print(" ||       /|\ ") 
    print("It's Loose !")

searching_word=input("What is your word ? ")
hangman_game(searching_word)
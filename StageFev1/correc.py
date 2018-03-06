def une_suite(L):
    # astuce, on transforme L en chaine de caractère
    # pour utiliser les méthodes .find et .replace qui vont
    # faire le taf pour nous
    L_str = "".join(map(str,L))# transforme [1,1,0] en "110"
    
    max_len_ones = -1
    where = -1
    for len_ones in range(1,len(L_str)):
        new_where = L_str.find("1"*len_ones)# on teste si "1..1" (len_ones fois) est dans la chaine
        if new_where == -1:# si find renvoie -1, ca n'y est pas pour cette taille, pas la peine de continuer
            break
            
        max_len_ones = len_ones
        where = new_where
    
    if where == -1: # si pas de 1 du tout
        return L
    
    L_str = L_str.replace("1"*max_len_ones,"2"*max_len_ones,1) # remplacer 1 fois "1...1" par "2...2"
    return list(map(int,list(L_str))) # transformation inverse

def look_and_say(L):
    '''
        Implémente un pas de la procédure "look and say", cf: https://en.wikipedia.org/wiki/Look-and-say_sequence
        1 -> 1 1
        1 1 -> 2 1 
        2 1 -> 1 2 1 1 
        1 2 1 1 -> 1 1 1 2 2 1 
        1 1 1 2 2 1 -> 3 1 1 2 1 1
    '''
    if len(L) == 0:
        return L
    
    to_return = []
    
    deb = L[0]
    count = 1
    for i in range(1,len(L)):
        if L[i] != deb:
            to_return.append(count)
            to_return.append(deb)
            
            deb = L[i]
            count = 1
        else:
            count += 1
    
    to_return.append(count)
    to_return.append(deb)
    
    return to_return
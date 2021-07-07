def ordernarDesc(var):
    desc = [] 
    pos = [] 
    
    
    for i in range(len(var)):        
        soma = 0

        for j in range(len(var)): 
            if var[i] <= var[j]:
                soma += 1

        pos.append(soma)
        
    for i in range(len(pos)):
        for j in range(len(pos)):
            if pos[j] == i+1:
                desc.append(var[j]) 
        

    return desc
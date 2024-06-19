from calendar import c


def crittografiaCesare():
    testoCifrato = []
    for i, x in testo:
        x = (testo[i] + k) % U_alf
        
        
        return str(testoCifrato)
        

alfabeto = {}
for i, lettera in enumerate('abcdefghijklmnopqrstuvwxyz'):
    alfabeto[i]=lettera
U_alf = len(alfabeto)
k = 3
testo = list(input(str('inserire testo : ')))
newTesto = {key: value for key, value in enumerate(testo)}
parola = {}
for key , value in newTesto.items():
    for key_alf, value_alf in alfabeto.items():
        if value == value_alf:
            parola[key_alf] = value

print(parola)

'''
1 ) Associare alla var 'testo' una nuova var contente chiave e lettera es. newTest = {'2:c', ...etc}
2 ) Richiamare nella funzione un ciclo che controlla ogni chiave della var newTest e implementa su essa la formula del cifrario
3 ) Salvare il testo cifrato su una var e scrivere in output il testo cifrato

'''

import random
import tkinter as tk

#queste variabili globali mi servono per impostare il livello di sensibilità e di profondità dell'albero
var=True;var1=True;var2=False;var3=False;var4=False;var5=False;


#leggiamo un file
def readFile(fileName):
    fileObj = open(fileName, "r")  # opens the file in read mode
    words = fileObj.read().splitlines()  # puts the file into an array
    fileObj.close()
    return words

dictionary = readFile("words.italian.txt")

#se p1 e p2 differiscono per solo una lettera (hanno lunghezza differente) -> return true
def r1(p1,p2):
    #pi=ciaoo   p2:ciao
    if((len(p1)-1)==(len(p2)) and len(p1)>1 and len(p2)>0):#p1 ha una lettera in più di p2
        i=0
        j=0
        count=0
        while(i<len(p1) and j<len(p2)):
            #analizzo il caso speciale p1:ca p2:a
                if(len(p2)==1):
                    if(p1[0]==p2[0]):
                        count=count +1;
                    if (p1[1] == p2[0]):
                        count = count + 1;
                    break
                #analizzo quando p1:ciaou p2:ciao, ovvero quando la lettera aggiuntiva è alla fine
                if(p1[i] == p2[j] and count==0 and j==len(p2)-1 and i==len(p1)-2 and len(p2)>1):
                    count = count +1;
                    break
                #analizzo i casi normali con la lettera aggiuntiva all'inizio o in mezzo
                else:
                    if (p1[i] == p2[j]):
                        i = i + 1
                        j = j + 1
                    else:
                        i = i + 1
                        count = count + 1

        if(count==1):
            return True
        else:
            return False
    #p1:ciao p2:civao
    if((len(p2)-1)==len(p1) and len(p1)>0 and len(p2)>0):#p1 ha una lettera in meno di p2
        if(r1(p2,p1)==True):
            return True
        else:
            return False
    else:
        return False

#se p1 e p2 hanno solo una lettera diversa (hanno la stessa lunghezza) -> return true
def r2(p1,p2):
    if len(p1) != len(p2):
        return False

    count = 0
    for i in range(0, len(p1)):
        if p1[i] != p2[i]:#conto le lettere diverse
            count = count + 1

    if count == 1:
        return True

    return False

#se p2 è l'anagramma di p1 (hanno la stessa lunghezza) -> return true
def r3(p1,p2):
    if (sorted(p1) == sorted(p2)):
       return True
    else:
        return False

#p2 è dentro dic -> return true
def contiene(p2,dic):
    i=0
    while(len(dic)>i):
        if(p2==dic[i]):
            return True
        i=i+1
    return False

#crea un dizionario di parole alfabeticamente vicine sulla base di dictionary
def creaDiz(p1,dictionary):
    i = 0
    temp = []

    while (len(dictionary) > i):
        # se vale la regola r1 aggiungo la parola dictionary[i] nell'array temp
        if (r1(p1, dictionary[i]) == True):
            temp.append(dictionary[i])
        # se vale la regola r2 aggiungo la parola dictionary[i] nell'array temp
        if (r2(p1, dictionary[i]) == True):
            temp.append(dictionary[i])
        # se vale la regola r3 aggiungo la parola dictionary[i] nell'array temp
        if (r3(p1, dictionary[i]) == True):
            temp.append(dictionary[i])
        i = i + 1
    return temp

#crea un percorso tra le parole word1 e word2 e restituisce il percorso
def percorso(word1,word2):
    cammino = [word1]
    #creo un dizionario di parole alfabeticamente vicine sulla base di dictionary
    temp = creaDiz(word1, dictionary)
    #se trovo word2 dentro temp allora ho trovato il cammino


    if (contiene(word2, temp) == True):
        cammino.append(word2)
        return cammino

    elif(var):
        i=0 #iterazione 1

        while(i<len(temp)):
            # creo un dizionario per ogni parola
            ii=random.randint(0, len(temp)-1)
            temp2 = creaDiz(temp[ii], dictionary)#creo un dizionario per ogni parola del diz 0
            print(temp[ii])

            if(contiene(word2, temp2) == True and word1!=temp[ii]!=word2):
                cammino.append(temp[ii])
                cammino.append(word2)
                return cammino
            elif (var1):  # ------------------------------------------------------------------------
                j = 0  # iterazione 2

                while (j < len(temp2)):
                    # creo un dizionario per ogni parola
                    jj = random.randint(0, len(temp2) - 1)
                    temp3 = creaDiz(temp2[jj], dictionary)  # creo un dizionario per ogni parola del diz 1
                    print(temp2[jj])

                    if (contiene(word2, temp3) == True and word1!=temp[ii]!=word2!=temp2[jj]):
                        cammino.append(temp[ii])#1
                        cammino.append(temp2[jj])#2
                        cammino.append(word2)
                        return cammino
                    elif(var2):#------------------------------------------------------------------------
                        k = 0  # iterazione 3

                        while (k < len(temp3)):
                            # creo un dizionario per ogni parola
                            kk = random.randint(0, len(temp3) - 1)
                            temp4 = creaDiz(temp3[kk], dictionary)  # creo un dizionario per ogni parola del diz 1
                            print(temp3[kk])

                            if (contiene(word2, temp4) == True and word1!=temp[ii]!=word2!=temp2[jj]!=temp3[kk]):
                                cammino.append(temp[ii])  #1
                                cammino.append(temp2[jj]) #2
                                cammino.append(temp3[kk]) #3
                                cammino.append(word2)
                                return cammino
                            elif (var3):  # ------------------------------------------------------------------------
                                h = 0  # iterazione 4

                                while (h < len(temp4)):
                                    # creo un dizionario per ogni parola
                                    hh = random.randint(0, len(temp4) - 1)
                                    temp5 = creaDiz(temp4[hh],dictionary)  # creo un dizionario per ogni parola del diz 1
                                    print(temp4[h])

                                    if (contiene(word2, temp5) == True and word1!=temp[ii]!=word2!=temp2[jj]!=temp3[kk]!=temp4[hh]):
                                        cammino.append(temp[ii])  # 1
                                        cammino.append(temp2[jj])  # 2
                                        cammino.append(temp3[kk])  # 3
                                        cammino.append(temp4[hh])  # 4
                                        cammino.append(word2)
                                        return cammino
                                    #devo ancora impostare il fattore random dalla var 4
                                    elif (var4):  # ------------------------------------------------------------------------
                                        o = 0  # iterazione 5

                                        while (o < len(temp5)):
                                            # creo un dizionario per ogni parola
                                            oo = random.randint(0, len(temp5) - 1)
                                            temp6 = creaDiz(temp5[oo],
                                                            dictionary)  # creo un dizionario per ogni parola del diz 1
                                            print(temp5[oo])

                                            if (contiene(word2, temp6) == True and word1!=temp[ii]!=word2!=temp2[jj]!=temp3[kk]!=temp4[hh]!=temp5[oo]):
                                                cammino.append(temp[ii])  # 1
                                                cammino.append(temp2[jj])  # 2
                                                cammino.append(temp3[kk])  # 3
                                                cammino.append(temp4[hh])  # 4
                                                cammino.append(temp5[oo])  # 5
                                                cammino.append(word2)
                                                return cammino

                                            elif (var5):  # ------------------------------------------------------------------------
                                                n = 0  # iterazione 6

                                                while (n < len(temp6)):
                                                    # creo un dizionario per ogni parola
                                                    nn = random.randint(0, len(temp6) - 1)
                                                    temp7 = creaDiz(temp6[nn],
                                                                    dictionary)  # creo un dizionario per ogni parola del diz 1
                                                    print(temp6[nn])

                                                    if (contiene(word2, temp7) == True and word1!=temp[ii]!=word2!=temp2[jj]!=temp3[kk]!=temp4[hh]!=temp5[oo]!=temp6[nn]):
                                                        cammino.append(temp[ii])  # 1
                                                        cammino.append(temp2[jj])  # 2
                                                        cammino.append(temp3[kk])  # 3
                                                        cammino.append(temp4[hh])  # 4
                                                        cammino.append(temp5[oo])  # 5
                                                        cammino.append(temp6[nn])  # 6
                                                        cammino.append(word2)
                                                        return cammino


                                                    n = n + 1

                                            o = o + 1

                                    h = h + 1

                            k = k + 1

                    j = j + 1

            i = i + 1

#metoto che avvia il programma e stampa a terminale le operazioni
def avvia(word1,word2):
    dictionary = readFile("words.italian.txt")
    LunghezzaCamminoMin = 100

    cammino=percorso(word1,word2)
    CamminoMin = cammino

    i=0
    while(i<3):
        cammino = percorso(word1, word2)

        # se il primo cammino non ha trovato nessun risultato, allora sblocco una profondità successiva
        if (cammino == None):
            Var2 = True
            cammino1 = percorso(word1, word2)
            print("Imposto la profondità dell'albero di ricerca a 4")
            print(cammino1)
            # print("lunghezza cammino:", len(cammino1))
            if (cammino1 == None):
                Var3 = True
                cammino2 = percorso(word1, word2)
                print("Imposto la profondità dell'albero di ricerca a 5")
                print(cammino2)
                # print("lunghezza cammino:", len(cammino2))
                if (False):  # TODO per ora è bloccato
                    Var4 = True
                    cammino3 = percorso(word1, word2)
                    print("Imposto la profondità dell'albero di ricerca a 6")
                    print(cammino3)
                    if (cammino3 == None):
                        Var5 = True
                        cammino4 = percorso(word1, word2)
                        print("Imposto la profondità dell'albero di ricerca a 7")
                        print(cammino4)

        if (cammino != None):
            #trovo il cammino di lunghezza minima
            if(len(cammino)<LunghezzaCamminoMin):
                LunghezzaCamminoMin=len(cammino)
                CamminoMin = cammino
        i=i+1


    return CamminoMin

#serve per prendere i dati dall'interfaccia e inviarli al metodo avvia
def invia():
    #prendo i dati da textfield
    if text_imput_start.get() and text_imput_end.get():

        user_input_start = text_imput_start.get()
        user_input_end = text_imput_end.get()

        #faccio la verifica se la parola è contenuta o meno nel dizionario
        if (contiene(user_input_start,dictionary)==False or contiene(user_input_end,dictionary)==False):
            text_response = "Errore - inserisci delle parole valide"
            text_response1 = "\n"
            text_response2 = "\n"
            text_response3 = "\n"
            text_response4 = "\n"

        else:
            temp = avvia(user_input_start, user_input_end)
            if(temp!=None):
                text_response = temp
                text_response1 = "\n\nLunghezza cammino: "
                text_response2 = len(text_response)
                text_response3 = "\nProfondità albero usata: "
                text_response4 = "3"
                if(var2==True):
                    text_response4 = "4"
                if(var3==True):
                    text_response4 = "5"
                if (var4 == True):
                    text_response4 = "6"
                if (var5 == True):
                    text_response4 = "7"


            else:
                text_response = "Errore"
                text_response1 = "\n"
                text_response2 = "Cammino non trovato -> riprovare con una maggiore profondità"
                text_response3 = "\n"
                text_response4 = "\n"

    else:
        text_response = "Completa i campi"
        text_response1 = "\n"
        text_response2 = "\n"
        text_response3 = "\n"
        text_response4 = "\n"

    textwidget = tk.Text()
    textwidget.insert(tk.END, text_response)
    textwidget.insert(tk.END, text_response1)
    textwidget.insert(tk.END, text_response2)
    textwidget.insert(tk.END, text_response3)
    textwidget.insert(tk.END, text_response4)
    textwidget.grid(row=4, column=1, sticky="W", pady=10,padx=10)


#main
#creo la finestra
window = tk.Tk()
window.geometry("800x700")
window.title("Progetto Python")
window.grid_columnconfigure(0, weight=1)


welcome_label = tk.Label(window,text = "Progetto Python",pady=10,font=("Helvetica", 15))
welcome_label.grid(row=0, column=1,sticky="N", padx=20, pady=10)

text_parola1 = tk.Label(window,text = "Parola 1",pady=10,font=("Helvetica", 10))
text_parola1.grid(row=1, column=0, sticky="W", padx=10)

text_imput_start = tk.Entry()
text_imput_start.grid(row=1, column=1, sticky="W", padx=10)

text_parola2 = tk.Label(window,text = "Parola 2",pady=10,font=("Helvetica", 10))
text_parola2.grid(row=2, column=0, sticky="W", padx=10)

text_imput_end = tk.Entry()
text_imput_end.grid(row=2, column=1, sticky="W", padx=10)

button = tk.Button(text="Avvia", command=invia)
button.grid(row=3,column=1, sticky="W", pady=20, padx=20)

textwidget = tk.Text()
textwidget.grid(row=4, column=1, sticky="WE", pady=10,padx=10)

credits_label = tk.Label(window, text="Progetto Python by Salvatore La Rosa and Matteo Tiboldo")
credits_label.grid(row=6, column=1, sticky="S", pady=10,padx=10)


window.mainloop()



#TEST 1: torta->trota
#['torta', 'trota']

#TEST 2: pro->porro
#['pro', 'poro', 'porro']
#['pro', 'oro', 'poro', 'porro']

#TEST 3: pro->ape
#['pro', 'pero', 'pera', 'apre', 'ape']
#pro apro apre ape

#TEST 4: aspira->raspati
#['aspira', 'spira', 'raspi', 'raspai', 'raspati']
#aspira raspai raspati

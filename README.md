#Autori
Matteo Tiboldo e Salvatore La Rosa

#Sviluppo progetto
Allora l'idea era di prendere la prima parola e di cercare all'interno del dizionario tutte le parole che differiscono per una singola lettera
	Le operazioni che possiamo fare sono
	
- aggiungere una lettera e quindi trovare una parola che ha solo una lettera in più
- togliere una lettera e quindi trovare solo una parola che ha una lettera in meno
- modificare una lettera e quindi trovare una parola che ha le stesse lettere tranne una che modifichiamo
- trovare una parola che è l'anagramma , ovvero che ha le stesse lettere dell'altra solo in posizione diversa

	Ora dobbiamo salvare all'interno di un array temporaneo la sequenza di parole trovate per arrivare ad ottenere la seconda parola
	poi confrontiamo questo array con l'array minimo che abbiamo trovato
	resettiamo infine l'array temporaneo per un nuovo ciclo
	
infine scriviamo l'array più corto che abbiamo trovato, ovvero la sequenza di parole più corta

#Consegna
##Progetto per il linguaggio python:
Progetto 1: 
1)  dato il seguente file su Moodle/sez Python:  “elenco parole italiane per progetto esame” costruire una struttura dati di accesso a tutte le parole.
2) l’utente sceglie due parole a caso, che possono essere gia’ presenti nel dizionario oppure nuove,
3) il sistema trova tutte le parole che sono alfabeticamente vicine, in base a un insieme di regole ad es :
     R!: aggiungo/tolgo una lettera : pro->poro->porro (sia agli estremi che in mezzo)
    R2:  anagramma            :   torta     -> trota  
R3:  sostituire una lettera           :   torta     -> torto  
……………………
Il sistema ripete le operazioni e creare dei cammini che collegano le due parole, A questo punto, date due parole possiamo calcolare una loro distanza.
Ad esempio nel primo caso
‘pro’ e ‘porro’ sono collegate da 2 R1 
torta e trota da R2
trota e torto da R2+ R3
……


Ogni regola puo’ avere un peso diverso a vostra completa discrezione, es aggiungere /togliere all’inizio/fondo costa meno che in mezzo, l’anagramma di due lettere vicine costa meno. Potete sdoppiare le regole (ad es aggiungo in mezzo o agli estremi) 
Si puo’ immaginare quindi di trovare una distanza minima, come l’insieme di regole meno costose che trasformano una parola in un’altra.   
nel seguente esempio, potremmo dire  che due cammini sono equivalenti:

casa casta costa costo cosmo
casa cosa coma como cosmo

in quanto si applicano R1 + 3R3 oppure 3R3+R1

Ovviamente il cammino deve contenere SOLO parole presenti nel dizionario
Non essendo un corso di algoritmi, potete usare qualunque algoritmo di qualunque complessita'.
Non esistono vincoli aggiuntivi.
Lo schema di base deve funzionare per un insieme N di regole arbitrario.
Ad occhio il programma dovrebbe essere rapido se cercate due parole molto vicine.
Se sono distanti potete opzionalmente introdurre euristiche, ad esempio
se vedete che a forza di applicare regole si generano troppe sequenze, potete stabilire un numero massimo di regole da applicare dopo cui fermarsi.

Se il progetto e’ svolto in gruppo, scrivere una GUI (ad es con tkinter) per inserire i dati e rappresentare tramite un disegno le sequenze di transizioni che trasformano la parola. Il disegno puo’ essere realizzato tramite qualunque libreria grafica a vostra scelta
si possono adottare euristiche, ad es se hanno lunghezze diverse potrei privilegiare la aggiunta,

Sono benvenute, anche se non richieste, funzionalita’ aggiuntive ottimizzazioni etc

Se opzionalmente intendete usare librerie esterne per la gestione di grafi, questi sono degli esempi:

https://igraph.org/python/
https://networkx.org/
https://graph-tool.skewed.de/ 

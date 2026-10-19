from stand import Stand, StandExtra, StandPremium
from espositore import Espositore

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome
        self.__espositori = []
        self.__stand_totali = []

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, 'r', encoding='utf-8') as f:
            for riga in f:
                campi = riga.rstrip("\n").split(",")
                while len(campi) < 5: #controllare che ci siano almeno 5 campi
                    campi.append("") #se la riga ne contiene di meno, aggiungere campi vuoti
                codice = campi[0]

                #controllare per cosa inizia il codice
                if codice.startswith("ES"): #se il codice inizia per ES, creo un oggetto espositore con gli attributi
                    codice_espositore = codice
                    nome_espositore = campi[1]
                    cognome_espositore = campi[2]
                    espositore =  Espositore(codice_espositore, nome_espositore, cognome_espositore)

                    self.__espositori.append(espositore)

                elif codice.startswith("ST"): #se il codice inizia per ST creo oggetto Stand
                    codice_stand = codice
                    superficie = int(campi[1])
                    padiglione = int(campi[2])
                    prezzo = int(campi[3])

                    #verificare di che stand si tratta in base all'ultimo campo
                    if campi[4]== "": #se è una stringa vuota significa che è uno stand normale
                        stand = Stand(codice_stand, superficie, padiglione, prezzo)

                    elif campi[4].isdigit():
                        stand = StandExtra(codice_stand, superficie, padiglione, prezzo, numero_prese=int(campi[4]))
                    else:
                        stand = StandPremium(codice_stand, superficie, padiglione, prezzo, posizione=campi[4])

                    self.__stand_totali.append(stand)


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato = None
        espositore_trovato = None

        for stand in self.__stand_totali: #verifico che lo stand esiste, altrimenti solleva eccezione
            if codice_stand == stand.codice_stand:
                stand_trovato = stand
        if stand_trovato is None:
            raise ValueError("stand non trovato")

        for espositore in self.__espositori: #verifico che l'espositore esiste
            if codice_espositore == espositore.codice_espositore:
                espositore_trovato= espositore
        if espositore_trovato is None: #se non esiste solleva eccezione
            raise ValueError("espositore non trovato")

        #controllo che stand sia disponibile
        if not stand_trovato.disponibile:
            raise ValueError("stand non disponibile")

        #controll che espositore non abbia già un altro stand
        for stand in self.__stand_totali:
            if stand.espositore == espositore_trovato:
                raise ValueError("espositore è già associato ad uno stand")

        stand_trovato.espositore = espositore_trovato #associo l'espositore allo stand
        stand_trovato.disponibile = False #lo stand diventa non disponibile

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """

        for espositore in self.__espositori:
            print(espositore)

            stand_trovato = None
            for stand in self.__stand_totali:
                if stand.espositore == espositore: #verificare se lo stand appartiene all'espositore corrente
                    stand_trovato = stand

            if stand_trovato is None:
                print("espositore non ha uno stand assegnato")
            else:
                print(stand_trovato)

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo dal più economico a quello più costoso"""
        stand_ordinati_per_prezzo = sorted(self.__stand_totali)
        return stand_ordinati_per_prezzo

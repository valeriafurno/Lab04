class Stand:

    def __init__(self, codice_stand, superficie, padiglione, prezzo): #costruttore della classe Stand
        self.__codice_stand = codice_stand
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo = prezzo
        self.__disponibile = True #lo stand è inizialmente disponibile
        self.__espositore = None # inizialmente non è associato a nessun espositore

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
        return f"{self.codice_stand}: {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - {stato}"

    def prezzo_finale(self):
        return self.prezzo

    def __lt__(self, other): #metodo speciale che permette di stabilire quando un oggetto è minore di un altro
        return self.prezzo_finale() < other.prezzo_finale()

    @property
    def codice_stand(self):
        return self.__codice_stand
    @codice_stand.setter
    def codice_stand(self, codice_stand):
        self.__codice_stand = codice_stand

    @property
    def superficie(self):
        return self.__superficie
    @superficie.setter
    def superficie(self, superficie):
        self.__superficie = superficie

    @property
    def padiglione(self):
        return self.__padiglione
    @padiglione.setter
    def padiglione(self, padiglione):
        self.__padiglione = padiglione

    @property
    def prezzo(self):
        return self.__prezzo
    @prezzo.setter
    def prezzo(self, prezzo):
        self.__prezzo = prezzo

    @property
    def disponibile(self):
        return self.__disponibile
    @disponibile.setter
    def disponibile(self, disponibile):
        self.__disponibile = disponibile

    @property
    def espositore(self):
        return self.__espositore
    @espositore.setter
    def espositore(self, espositore):
        self.__espositore = espositore

#creazione delle due classi figlio, richiamando il costruttore della classe padre e inizializzando gli attributi specifici della classe figlia

class StandExtra(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, numero_prese):
        super().__init__(codice_stand, superficie, padiglione, prezzo) #invocazione della costruzione del padre
        self.__numero_prese = numero_prese

    def prezzo_finale(self):
        # Calcolo il prezzo con il sovrapprezzo del 7% per ogni presa aggiuntiva
        prezzo_finale=self.prezzo * (1 + 0.07 * self.__numero_prese)
        return prezzo_finale

    def __str__(self):
        if self.disponibile: #controlla se lo stand è disponibile
            stato = "Disponibile"
        else:
            stato = "Non disponibile"

            # Restituisco una descrizione dello stand con prese extra e stato di disponibilità
        return f"{self.codice_stand}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - Prese aggiuntive: {self.__numero_prese} - {stato} "

class StandPremium(Stand):
    def __init__(self, codice_stand, superficie, padiglione, prezzo, posizione):
        super().__init__(codice_stand, superficie, padiglione, prezzo)
        self.__posizione = posizione

    def prezzo_finale(self):
        prezzo_finale= self.prezzo * 1.30
        return prezzo_finale

    def __str__(self):
        if self.disponibile:
            stato = "Disponibile"
        else:
            stato = "Non disponibile"
            #restituisce una descrizione dello stand premium con posizione e disponibilità
        return f"{self.codice_stand}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale():.2f}€ - posizione: {self.__posizione} - {stato} "



class Espositore:

    def __init__(self,codice_espositore, nome_espositore, cognome_espositore):
        self.__codice_espositore = codice_espositore
        self.__nome_espositore = nome_espositore
        self.__cognome_espositore = cognome_espositore

    def __str__(self):
        return f"{self.__codice_espositore} {self.__nome_espositore} {self.__cognome_espositore}"

    def __eq__(self,other): #metodo che definisce quando due espositori sono considerati uguali,
        # confrontando il codice identificativo
        if isinstance(other,Espositore):
            return self.__codice_espositore == other.__codice_espositore
        return False


    @property
    def codice_espositore(self):
        return self.__codice_espositore
    @codice_espositore.setter
    def codice_espositore(self,codice_espositore):
        self.__codice_espositore = codice_espositore




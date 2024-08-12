from Temperaturen import sub_class_temperatur


class Temperature:
    """Vermittelt nur die eigentliche Klasse und stellt exemplarisch die funktionen und Variablen zur verfügung
    vlaue ist die gradzahl die bei erstellen benötugt wird.
    unit legt die Einheit festgelegt => Default ist Celsius (C) auch möglich sind  Fahrenheit (F) & Kelvin (K)
    digits legt die bei ausgabe mit übergebenen Kommastellen fest. (Default ist 2)

    """
    def __new__(cls, value: int or float, unit: str = "C"):
        if unit in ["C", "c", "Celsius", "celsius"]:
            return sub_class_temperatur.Celsius(value)
        elif unit in ["F", "f", "Fahrenheit", "fahrenheit"]:
            return sub_class_temperatur.Fahrenheit(value)
        elif unit in ["K", "k", "Kelvin", "kelvin"]:
            return sub_class_temperatur.Kelvin(value)
        else:
            raise KeyError

    def __init__(self, value: int or float, unit: str = ""):
        """ Will never be reached.
         If new instanz will call the __new__ will direkt it"""
        self.temperatur = None
        self.unit = unit
        self.digits = 2
        self.__value = value

    def __call__(self, *args, **kwargs):
        pass

    def as_fahrenheit(self):
        pass

    def as_celsius(self):
        pass

    def as_kelvin(self):
        pass

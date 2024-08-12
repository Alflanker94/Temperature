
class TemperaturTemplate(object):
    """ Template Class with all relevant and universell functions for a Temperatures"""

    def __init__(self, temperatur: float or int):
        self._temperature: float = temperatur
        self._unit = None
        self._digits = 2

    def __repr__(self):
        """ build the represetiv name for the Class if asked"""
        return f"{type(self).__name__}(Unit={self.unit}, Temp={self.temperatur})"

    def __str__(self):
        """build a representative  human-readable sting if for example: if instance is printed"""
        return str(self.round(self.temperatur)) + "°" + str(self.unit[0]).upper()

    def round(self, value: int or float):
        """rounds a value by a class defined value of digits"""
        return value.__round__(self.digits)

    def retun_new_instanz(self, value):
        if self.unit == "Celsius":
            return Celsius(value)
        elif self.unit == "Fahrenheit":
            return Fahrenheit(value)
        elif self.unit == "Kelvin":
            return Kelvin(value)
        else:
            raise KeyError

    def __call__(self):
        """ defines the answer for a Call"""
        return self.round(self.temperatur)

    def __sub__(self, other):
        """ defines the answer for "-" operator"""
        loc = {}
        if self.unit == other.unit:
            return self.temperatur - other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("_temp = other.as_" + str(self.unit).lower() + "()", locals(), loc)
            return self.retun_new_instanz(self.temperatur - loc['_temp'])
        elif isinstance(other, (int, float)):
            return self.temperatur - other
        else:
            raise ValueError

    def __rsub__(self, other):
        self.__sub__(other)

    def __add__(self, other):
        """ defines the answer for "+" operator"""
        loc = {}
        if self.unit == other.unit:
            return self.temperatur + other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("_temp = other.as_" + str(self.unit).lower() + "()", locals(), loc)
            return self.retun_new_instanz(self.temperatur + loc['_temp'])
        elif isinstance(other, (int, float)):
            return self.temperatur + other
        else:
            raise ValueError

    def __radd__(self, other):
        self.__add__(other)

    def __eq__(self, other):
        """ defines the answer for "==" operator"""
        if self.unit == other.unit:
            return self.temperatur == other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("self.__temp = other.as_" + str(self.unit).lower() + "()")
            return self.temperatur == self.__temp
        elif isinstance(other, (int, float)):
            return self.temperatur == other
        else:
            raise ValueError

    def __mul__(self, other):
        loc = {}
        if self.unit == other.unit:
            return self.temperatur * other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("_temp = other.as_" + str(self.unit).lower() + "()", locals(), loc)
            return self.retun_new_instanz(self.temperatur * loc['_temp'])
        elif isinstance(other, (int, float)):
            return self.temperatur * other
        else:
            raise ValueError

    def __rmul__(self, other):
        self.__mul__(other)

    def __floordiv__(self, other):
        loc = {}
        if self.unit == other.unit:
            return self.temperatur // other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("_temp = other.as_" + str(self.unit).lower() + "()", locals(), loc)
            return self.retun_new_instanz(self.temperatur // loc['_temp'])
        elif isinstance(other, (int, float)):
            return self.temperatur // other
        else:
            raise ValueError

    def __truediv__(self, other):
        loc = {}
        if self.unit == other.unit:
            return self.temperatur // other.temperatur
        elif other.unit in [Celsius.unit, Kelvin.unit, Fahrenheit.unit]:
            exec("_temp = other.as_" + str(self.unit).lower() + "()", locals(), loc)
            return self.retun_new_instanz(self.temperatur // loc['_temp'])
        elif isinstance(other, (int, float)):
            return self.temperatur / other
        else:
            raise ValueError



    @property
    def digits(self):
        """ Digits property"""
        return self._digits

    @digits.setter
    def digits(self, value):
        if isinstance(value, int) and 0 < value < 10:
            self._digits = value
        else:
            raise AttributeError

    @property
    def unit(self):
        """ Unit property"""
        return self._unit

    #@unit.setter
    #def unit(self, value):
    #    if isinstance(value, str) and in [self._temperature = value]
    #    self._unit = value

    @property
    def temperatur(self):
        """ temperatur property"""
        # print("Get", self._temperature)
        return self._temperature

    @temperatur.setter
    def temperatur(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self._temperature = value
        else:
            raise AttributeError


    @temperatur.deleter
    def temperatur(self):
        del self._temperature


class Celsius(TemperaturTemplate):
    unit = "Celsius"

    def __init__(self, value=0):
        super().__init__(value)

    def as_celsius(self):
        """just for safety"""
        return self.round(self.temperatur)

    def as_fahrenheit(self):
        """Covert to different Unit"""
        return self.round((self.temperatur * 1.8) + 32)

    def as_kelvin(self):
        """Covert to different Unit"""
        return self.round(self.temperatur + 273.15)


class Kelvin(TemperaturTemplate):
    unit = "Kelvin"

    def __init__(self, value=0):
        super().__init__(value)

    def as_kelvin(self):
        """just for safety"""
        return self.round(self.temperatur)

    def as_fahrenheit(self):
        """Covert to different Unit"""
        return self.round((self.temperatur - 273.15) * (9 / 5) + 32)

    def as_celsius(self):
        """Covert to different Unit"""
        return self.round(self.temperatur - 273.15)


class Fahrenheit(TemperaturTemplate):
    unit = "Fahrenheit"

    def __init__(self, value=0):
        super().__init__(value)

    def as_celsius(self):
        """Covert to different Unit"""
        return self.round((self.temperatur - 32) * (5 / 9))

    def as_fahrenheit(self):
        """just for safety"""
        return self.round(self.temperatur)

    def as_kelvin(self):
        """Covert to different Unit"""
        return self.round((self.temperatur - 32) * (5 / 9) + 273.15)





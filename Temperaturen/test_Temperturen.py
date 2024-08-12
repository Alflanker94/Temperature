import random
import pytest
import pytest_check as check
from Temperaturen import Temperature


@pytest.fixture(params=["K", "F", "C"], scope="class")
def temperature_units(request):
    request.cls.unit = request.param


@pytest.mark.usefixtures("temperature_units")
class CrossTempretureUnitTesting:
    pass


@pytest.mark.run(order=0)
class TestAllwaysTrueAndXF:

    def test_always_passes(self):
        assert True

    @pytest.mark.xfail
    def test_always_fails_x(self):
        assert False


@pytest.mark.run(order=1)
def test_init_with_not_corect_unit():
    for unit in [None, "A", "G", 12, [], {}]:
        try:
            t = Temperature(20, unit)
            print(t)
        except KeyError:
            check.is_true(True)
        else:
            check.is_true(False)
        finally:
            t = Temperature(20)
            check.almost_equal(t(), 20, abs=2, msg="Should be True")


class TestTemperatures(CrossTempretureUnitTesting):
    unit = None
    neded_equal_digits = 2
    equal_by_diffren_lower_as = 0.1

    def test_init_with_not_corect_temperatur(self):
        for temp in [None, "abc", "ABC", [], {}]:
            try:
                t = Temperature(temp, self.unit)
                print(t)
            except AttributeError:
                check.is_true(True)
            else:
                check.is_true(False)

    def test_init_with_corect_params(self):
        for temp in [0, 10, 50, 100, 5000]:
            t = Temperature(temp, self.unit)
            check.almost_equal(t.temperatur, temp, msg="Value Check")
            check.almost_equal((t.unit[0]).upper(), self.unit, msg="Unit Check")

    def test_convert(self):
        print()
        temperatures = [0, 10, 50, 100, 5000]
        for i in range(100):
            temperatures.append(random.randint(-500, 500000))

        for temp in temperatures:
            t = Temperature(temp, self.unit)
            print(temp, self.unit)
            l_units = ["K", "F", "C"]
            l_units.remove(self.unit)
            for _unit in l_units:
                if _unit == "K":
                    _call = t.as_kelvin
                elif _unit == "F":
                    _call = t.as_fahrenheit
                elif _unit == "C":
                    _call = t.as_celsius
                else:
                    assert False

                _temp = None
                match self.unit:
                    case "C":
                        t = Temperature(temp, self.unit)
                        if _unit == "K":
                            _temp = temp + 273.15
                        elif _unit == "F":
                            _temp = (temp * 9 / 5) + 32
                        else:
                            assert False

                    case "F":
                        t = Temperature(temp, self.unit)
                        if _unit == "C":
                            _temp = (temp - 32) * 5 / 9
                        elif _unit == "K":
                            _temp = (temp - 32) * 5 / 9 + 273.15
                        else:
                            assert False

                    case "K":
                        t = Temperature(temp, self.unit)
                        if _unit == "C":
                            _temp = temp - 273.15
                        elif _unit == "F":
                            _temp = ((temp - 273.15) * (9 / 5)) + 32
                        else:
                            assert False

                print("\t", _call(), _unit, "==", _temp.__round__(self.neded_equal_digits), _unit)
                check.almost_equal(_call(), _temp.__round__(self.neded_equal_digits),
                                   abs=self.equal_by_diffren_lower_as, msg="Value Check")

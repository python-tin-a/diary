import pint

u = pint.UnitRegistry()

a = float(input()) * u.inch

b = a.to_base_units()
print(b)


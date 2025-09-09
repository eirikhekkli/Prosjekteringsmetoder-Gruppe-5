import pandas as pd
from pathlib import Path

legs = pd.read_csv("legs.csv")
# Fyll inn distance_nm i CSV først. Her validerer vi og lagrer xlsx.
total = legs["distance_nm"].sum()
print(f"Sum deldistanser: {total:.1f} nm")

TARGET = 1987  # fra oppgaveteksten
if abs(total - TARGET) > 5:  # toleranse
    print("⚠️ Advarsel: Sum avviker merkbart fra 1987 nm. Sjekk tallene.")
else:
    print("✅ Ser bra ut i forhold til 1987 nm.")

# Antagelser fra oppgaven
assumptions = pd.DataFrame([
    {"field": "Route name", "value": "Route Assignment 2"},
    {"field": "Total distance (nm)", "value": TARGET},
    {"field": "Tw (roundtrips/year)", "value": 12},
    {"field": "W_LL (loading rate)", "value": "1000 m²/hr"},
    {"field": "Annual transport Q", "value": "1 million tons/year"},
    {"field": "Cargo factor", "value": 0.9},
    {"field": "Pickup+delivery each port", "value": "Yes (Q = q_nRT * #port_visits)"},
])

out = Path("route_assignment_2.xlsx")
with pd.ExcelWriter(out, engine="xlsxwriter") as xw:
    legs.to_excel(xw, index=False, sheet_name="legs")
    try:
        order = pd.read_csv("route_order.csv")
        order.to_excel(xw, index=False, sheet_name="route_order")
    except FileNotFoundError:
        pass
    assumptions.to_excel(xw, index=False, sheet_name="assumptions")

print(f"Skrev fil: {out.resolve()}")

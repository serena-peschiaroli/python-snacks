# Definisci una funzione che, prendendo in input il raggio, restituisce l'area della circonferenza.

def area_circonferenza(raggio):
    return 3.14 * (raggio ** 2)

print(area_circonferenza(5))


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30))
# URI 1049
# CLEVERSON MENDES FARIA

dicionario = {
  "vertebrado-ave-carnivoro": "aguia", 
  "vertebrado-ave-onivoro": "pomba",
  "vertebrado-mamifero-onivoro": "homem",
  "vertebrado-mamifero-herbivoro": "vaca",
  "invertebrado-inseto-hematofago": "pulga",
  "invertebrado-inseto-herbivoro": "lagarta",
  "invertebrado-anelideo-hematofago": "sanguessuga",
  "invertebrado-anelideo-onivoro": "minhoca"
}

p1 = input()
p2 = input()
p3 = input()

palavra = (p1 + "-" + p2 + "-" + p3)

print(dicionario[palavra])

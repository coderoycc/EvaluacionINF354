from kanren import Relation, facts, var, run
x = var()
padre = Relation()
facts(padre, 
          ("Juan", "Paulino"), #abuelo, tio
          ("Juan", "Pascuala"), #Abuelo , madre
          ("Juan", "Aldo"),     
          ("Juan", "Marco"),
          ("Juan", "Rosmery"),          
          ("Juan", "Elizabeth"),
          ("Juan", "Martha"),
          ("Juan", "Litza"),
          ("Juan", "Lexi"),
          ("Paulino", "Pablo"), #TIO, PRIMO
          ("Paulino", "Eduardo"),
          ("Paulino", "Anghy"),
          ("Paulino", "Paola"),
          ("Paulino", "Josue"),
          ("Pascuala", "Andres"),
          ("Pascuala", "Roberto"),
          ("Pascuala", "Adaya"),  #Madre, Hermana
          ("Aldo", "Kimberly"),
          ("Aldo", "Aldo Junior"),
          ("Marco", "Juan Marco"),
          ("Marco", "Marco Antonio"), #Tio, Primo
          ("Marco", "Greyma"),
          ("Rosmery", "Victor"),
          ("Rosmery", "Manuel"),
          ("Elizabeth", "Emmanuel"),
          ("Litza", "Katya"),
          ("Lexy", "Mateo"),
          ("Pablo", "Piter"),   #primo, Sombrino
          ("Pablo", "Camila"),
          ("Eduardo", "Daniela"),
          ("Eduardo", "Bolivia"),
          ("Anghy", "Pedro Junior"), #Prima, sobrino
          ("Paola", "Robert")
      )

print(run(3, x, padre("Pascuala", x))) #Madre y mis hermanos

print(run(6, x, padre("Juan", x))) #Abuelo y Tios

print(run(4, x, padre("Paulino", x))) # Tio y Primos

print(run(1, x, padre(x, "Emmanuel"))) #Tia y primo
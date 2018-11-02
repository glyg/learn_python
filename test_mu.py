
def presentation_string(prenom, nom, age=None, birth_place=None):
    """Creates a phrase from the input data.
    
    
    """
    
    phrase = f"Bonjour, je m'appelle {prenom.capitalize()} {nom.capitalize()}"
    if age is not None:
        phrase += f", j'ai {int(age)} ans "
    if birth_place is not None:
        phrase += f"et je suis né à {birth_place}"

    phrase += '.'
    return phrase

print(presentation_string("Guillaume", "GAY", ages=39, 
      birth_place='Aire sur Adour'))
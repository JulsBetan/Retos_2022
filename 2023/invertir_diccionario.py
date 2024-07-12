colabs = {
    "Alice": ["Python", "Java", "C++"],
    "Bob": ["JavaScript", "HTML", "CSS"],
    "Carlos": ["Python", "Ruby", "Go"],
    "Diana": ["Java", "Kotlin", "Swift"],
    "Eva": ["C#", "F#", "SQL"]
}

languages = {}
print("Colaboradores:")
for name, language in colabs.items():
    print(f"{name} : {', '.join(language)}")

for name, language in colabs.items():
    for element in language:       
        if element in languages:
            languages[element].extend([name])
        else:
            languages[element] = [name]     
print("\nlenguajes:")
for language, names in languages.items():
    print(f"{language} : {', '.join(names)}")
languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
}

for language in languages.keys():
    creator = languages[language]
    print(f'{language} was created by {creator}')
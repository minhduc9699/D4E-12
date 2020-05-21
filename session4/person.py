person = ['Đức', 96, 'Sơn la', 1, False]

dictionary_person = {
  'name': 'Đức', 
  'yob': 95, 
  'home_town': 'Sơn La',
}

dictionary_person_name = dictionary_person['name']
if 'name' in dictionary_person: # check if key in a dictionary
  print(dictionary_person['name']) # access key 'name'

dictionary_person['rela_status'] = False # CREATE
dictionary_person['name'] = 'not Đức' # UPDATE
print(dictionary_person)
del dictionary_person['name']
print(dictionary_person)

for key in dictionary_person:
  print(key, dictionary_person[key])


data = {
    "total_results": 3,
    "results": [
        {
            "popularity": 512.119,
            "vote_count": 460,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg",
            "id": 475557,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/f5F4cRhQdUbyVbB5lTNCwUzD6BP.jpg",
            "original_language": "en",
            "original_title": "Joker",
            "genres": [
                80,
                18,
                53
            ],
            "title": "Joker",
            "vote_average": 8.8,
            "overview": "During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.",
            "release_date": "2019-10-04"
        },
        {
            "popularity": 241.402,
            "vote_count": 598,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/a4BfxRK8dBgbQqbRxPs8kmLd8LG.jpg",
            "id": 429203,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/6X2YjjYcs8XyZRDmJAHNDlls7L4.jpg",
            "original_language": "en",
            "original_title": "The Old Man & the Gun",
            "genres": [
                35,
                80,
                18
            ],
            "title": "The Old Man & the Gun",
            "vote_average": 6.3,
            "overview": "The true story of Forrest Tucker, from his audacious escape from San Quentin at the age of 70 to an unprecedented string of heists that confounded authorities and enchanted the public. Wrapped up in the pursuit are a detective, who becomes captivated with Forrest’s commitment to his craft, and a woman, who loves him in spite of his chosen profession.",
            "release_date": "2018-09-28"
        },
        {
            "popularity": 233.735,
            "vote_count": 4139,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/lcq8dVxeeOqHvvgcte707K0KVx5.jpg",
            "id": 429617,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/5myQbDzw3l8K9yofUXRJ4UTVgam.jpg",
            "original_language": "en",
            "original_title": "Spider-Man: Far from Home",
            "genres": [
                28,
                12,
                878
            ],
            "title": "Spider-Man: Far from Home",
            "vote_average": 7.6,
            "overview": "Peter Parker and his friends go on a summer trip to Europe. However, they will hardly be able to rest - Peter will have to agree to help Nick Fury uncover the mystery of creatures that cause natural disasters and destruction throughout the continent.",
            "release_date": "2019-07-02"
        },
        {
            "popularity": 158.333,
            "vote_count": 323,
            "video": False,
            "poster_path": "https://image.tmdb.org/t/p/w500/kTQ3J8oTTKofAVLYnds2cHUz9KO.jpg",
            "id": 522938,
            "adult": False,
            "backdrop_path": "https://image.tmdb.org/t/p/w500/spYx9XQFODuqEVoPpvaJI1ksAVt.jpg",
            "original_language": "en",
            "original_title": "Rambo: Last Blood",
            "genres": [
                28,
                53
            ],
            "title": "Rambo: Last Blood",
            "vote_average": 6.1,
            "overview": "When John Rambo's niece travels to Mexico to find the father that abandoned her and her mother, she finds herself in the grasps of Calle Mexican sex traffickers. When she doesn't return home as expected, John learns she's crossed into Mexico and sets out to get her back and make them pay.",
            "release_date": "2019-09-20"
        },
    ]  
}

# movies_list = data['results']
# for movie in movies_list:
#   movie_genres_dict = movie['genres']
  # print(movie['original_title']) 

input_genres = int(input())
movies_list = data['results']

for movie in movies_list:
  movie_genres = movie['genres']
  if input_genres in movie_genres:
    print(movie['title'])

for movie in movies_list:
  rl_date = movie['release_date']
  rl_year = rl_date.split('-')[0]
  # if '2019' in rl_date:

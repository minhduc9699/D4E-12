from pymongo import MongoClient

client = MongoClient()

db = client.get_database('mongo_practice')

movie_collection = db.get_collection('movies')

data = [
  {
    'title' : 'Fight Club',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
     ]
  },
  {
    'title' : 'Pulp Fiction',
    'writer' : 'Quentin Tarantino',
    'year' : 1994,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
  },
  {
    'title' : 'Inglorious Basterds',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
  },
  {
    'title' : 'The Hobbit: An Unexpected Journey',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
  },
  {
    'title' : 'The Hobbit: The Desolation of Smaug',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
  },
  {
    'title' : 'The Hobbit: The Battle of the Five Armies',
    'writer' : 'Chuck Palahniuk',
    'year' : 1999,
    'actors' : [
    'Brad Pitt',
    'Edward Norton',
  ]
  },
  {
   'title' : "Pee Wee Herman's Big Adventure",
  },
  {
    'title' : 'Avatar',
  },
]

# movie_collection.insert_many(data)

all_movies = movie_collection.find({
  '$or': [
    {'year': {'$lt': 2000}},
    {'year': {'$gt': 2010}}
  ]
})

# for movie in all_movies:
#   print(movie)

movie_collection.update(
  {'title': 'Pulp Fiction'}, 
  {
    '$push': {
      'actors': 'Samuel L. Jackson'
    }
  }
)

movie_found = movie_collection.find({
  '$and': [
    {
      'synopsis': {'$regex': '.*gold.*'}
    },
    {
      'synopsis': {'$regex': '.*dragon.*'}
    }
  ]
  
})

for movie in movie_found:
  print(movie)

movie_collection.delete_one({'title': 'Avatar'})
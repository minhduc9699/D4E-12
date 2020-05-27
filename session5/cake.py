from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()

db = client.get_database('d4e12')

cake_collection = db.get_collection('cakes')

data = {
	"items":
		{
			"item":
				[
					{
						"id": "0001",
						"type": "donut",
						"name": "Cake",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
										{ "id": "1002", "type": "Chocolate" },
										{ "id": "1003", "type": "Blueberry" },
										{ "id": "1004", "type": "Devil's Food" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5006", "type": "Chocolate with Sprinkles" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
					{
						"id": "0002",
						"type": "donut",
						"name": "Raised",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
		
					{
						"id": "0003",
						"type": "donut",
						"name": "Old Fashioned",
						"ppu": 0.55,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
										{ "id": "1002", "type": "Chocolate" }
									]
							},
						"topping":
							[
								{ "id": "5001", "type": "None" },
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							]
					},
					{
						"id": "0004",
						"type": "bar",
						"name": "Bar",
						"ppu": 0.75,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							],
						"fillings":
							{
								"filling":
									[
										{ "id": "7001", "name": "None", "addcost": 0 },
										{ "id": "7002", "name": "Custard", "addcost": 0.25 },
										{ "id": "7003", "name": "Whipped Cream", "addcost": 0.25 }
									]
							}
					},

					{
						"id": "0005",
						"type": "twist",
						"name": "Twist",
						"ppu": 0.65,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5005", "type": "Sugar" },
							]
					},

					{
						"id": "0006",
						"type": "filled",
						"name": "Filled",
						"ppu": 0.75,
						"batters":
							{
								"batter":
									[
										{ "id": "1001", "type": "Regular" },
									]
							},
						"topping":
							[
								{ "id": "5002", "type": "Glazed" },
								{ "id": "5007", "type": "Powdered Sugar" },
								{ "id": "5003", "type": "Chocolate" },
								{ "id": "5004", "type": "Maple" }
							],
						"fillings":
							{
								"filling":
									[
										{ "id": "7002", "name": "Custard", "addcost": 0 },
										{ "id": "7003", "name": "Whipped Cream", "addcost": 0 },
										{ "id": "7004", "name": "Strawberry Jelly", "addcost": 0 },
										{ "id": "7005", "name": "Rasberry Jelly", "addcost": 0 }
									]
							}
					}
				]
		}
}


cake_list = data['items']['item']

query = {
  # '_id': ObjectId("5ecbce6203c183d539108480"),
  # 'name': 'cake'
}

update = {
  '$set': {
    'name': 'Bánh'
  }
}
cake_collection.update_many(query, update) # UPDATE

cakes = cake_collection.find()
# for cake in cakes:
#   print(cake)
# for cake in cake_list:
cake_collection.insert_one(cake)


# cake_collection.insert_many(cake_list)

cake_collection.delete_one(query)
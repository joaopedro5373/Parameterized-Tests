class Product:
    def __init__(self, id=0, name="new product", buyprice=0, sellprice=0, weight=None, volume=None):
        self.id = id
        self.name = name
        self.buyprice = buyprice
        self.sellprice = sellprice
        self.weight = weight
        self.volume = volume

    def get_details(self):
        return {
            "id": self.id,
            "name": self.name,
            "buyprice": self.buyprice,
            "sellprice": self.sellprice,
            "weight": self.weight,
            "volume": self.volume
        }

    def apply_discount(self, discount_percentage)->float:
        if 0 <= discount_percentage <= 100:
            discount_amount = (self.sellprice * discount_percentage) / 100
            self.sellprice -= discount_amount
            return self.sellprice
        else:
            raise ValueError("Discount percentage must be between 0 and 100")
    
    def __str__(self):
        return f"Product(id={self.id}, name='{self.name}', buyprice={self.buyprice}, sellprice={self.sellprice}, weight={self.weight}, volume={self.volume})"
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.id == other.id
        return False
    
    def __hash__(self):
        return hash(self.id)
    
    def update_price(self, new_buyprice=None, new_sellprice=None)->bool:
        if new_buyprice is not None and new_sellprice is not None:
            self.buyprice = new_buyprice
            self.sellprice = new_sellprice
        else: raise ValueError("Os novos valores não podem ser nulos")
    
    def fromFile(cls, file_path):
        with open(file_path, 'r') as file:
            data = file.read().splitlines()
            id = int(data[0])
            name = data[1]
            buyprice = float(data[2])
            sellprice = float(data[3])
            weight = float(data[4]) if data[4] else None
            volume = float(data[5]) if data[5] else None
            return cls(id, name, buyprice, sellprice, weight, volume)
    
    def toFile(self, file_path):
        with open(file_path, 'w') as file:
            file.write(f"{self.id}\n")
            file.write(f"{self.name}\n")
            file.write(f"{self.buyprice}\n")
            file.write(f"{self.sellprice}\n")
            file.write(f"{self.weight if self.weight is not None else ''}\n")
            file.write(f"{self.volume if self.volume is not None else ''}\n")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "buyprice": self.buyprice,
            "sellprice": self.sellprice,
            "weight": self.weight,
            "volume": self.volume
        } 
    
    def from_dict(cls, data):
        return cls(
            id=data.get("id", 0),
            name=data.get("name", "new product"),
            buyprice=data.get("buyprice", 0),
            sellprice=data.get("sellprice", 0),
            weight=data.get("weight"),
            volume=data.get("volume")
        )
    
    def to_json(self):
        import json
        return json.dumps(self.to_dict())
    
    def from_json(cls, json_str):
        import json
        data = json.loads(json_str)
        return cls.from_dict(data)
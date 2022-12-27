class Film:
    def __init__(self, title, genre, director, distributor, stock_quantity, buying_price, selling_price, id = None ):
        self.title = title
        self.genre = genre
        self.director = director
        self.distributor = distributor
        self.stock_quantity = stock_quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.profit = int(selling_price) - int(buying_price)
        self.id = id

   
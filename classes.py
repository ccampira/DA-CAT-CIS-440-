# Devonne Le, CIS 440

class BookHotel:

    # def __init__(self, name, hotel, rooms, guests, addons=0, price=0.00):
    def __init__(self, name, hotel, rooms, guests, roomtype, price=0.00):
        # self.name = name
        try:
            fname = name.split()[0]
            self.name = fname
        except:
            pass
        self.hotel = hotel
        self.rooms = rooms
        # self.addons = addons
        self.guests = guests
        self.roomtype = roomtype
        self.price = price

    def custom_confirmation(self):
        return f'{self.name}, your booking is confirmed!'

    def order_details(self):
        return f'Booking: Staying at {self.hotel}, {self.rooms} room(s) with {self.guests} guest(s) with {self.roomtype}'

    def __str__(self):
        return f'{self.hotel}, {self.rooms} room(s), {self.guests} guest(s) with {self.roomtype} ' \
               f'${self.price:.2f}, Booking by: {self.name}'


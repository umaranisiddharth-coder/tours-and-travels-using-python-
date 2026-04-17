"""
Add Maharashtra cities: Pune, Sangli, Kolhapur, Satara, Miraj, Latur, Solapur, Nashik, Nagpur
Each city gets: 5 hotels + 10 buses + 10 routes
Run: py add_maharashtra.py
"""
from app import create_app, db
from app.models import Bus, BusRoute, Hotel, BusTracking
from datetime import time
import math

app = create_app()

CITIES = {
    'Pune':     (18.5204, 73.8567),
    'Sangli':   (16.8524, 74.5815),
    'Kolhapur': (16.7050, 74.2433),
    'Satara':   (17.6805, 74.0183),
    'Miraj':    (16.8267, 74.6455),
    'Latur':    (18.4088, 76.5604),
    'Solapur':  (17.6599, 75.9064),
    'Nashik':   (20.0059, 73.7797),
    'Nagpur':   (21.1458, 79.0882),
}

# Hotels per city — real names
CITY_HOTELS = {
    'Pune': [
        ('JW Marriott Pune',              5, 4.8, 14000, 'Pool,Spa,Gym,Fine Dining,WiFi',    True,  'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600'),
        ('Conrad Pune',                   5, 4.7, 13000, 'Pool,Spa,Restaurant,WiFi,Valet',   True,  'https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=600'),
        ('The Westin Pune Koregaon Park', 5, 4.6, 12000, 'Pool,Spa,Restaurant,WiFi',         False, 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=600'),
        ('Novotel Pune Nagar Road',       4, 4.3,  6500, 'Pool,Gym,Restaurant,WiFi',         False, 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=600'),
        ('Lemon Tree Hotel Pune',         3, 4.1,  3500, 'Gym,Restaurant,WiFi,Parking',      False, 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=600'),
    ],
    'Sangli': [
        ('Hotel Sangli Executive',        4, 4.4,  5500, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1564501049412-61c2a3083791?w=600'),
        ('Hotel Sai Residency Sangli',    4, 4.3,  4800, 'Restaurant,WiFi,Parking',          True,  'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=600'),
        ('Hotel Ashoka Sangli',           3, 4.1,  3500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1455587734955-081b22074882?w=600'),
        ('Hotel Rajmahal Sangli',         3, 4.0,  3000, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1582719508461-905c673771fd?w=600'),
        ('Hotel City Pride Sangli',       3, 3.9,  2500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1540541338287-41700207dee6?w=600'),
    ],
    'Kolhapur': [
        ('Hotel Opal Kolhapur',           4, 4.5,  6000, 'Pool,Restaurant,WiFi,Parking',     True,  'https://images.unsplash.com/photo-1561501900-3701fa6a0864?w=600'),
        ('Hotel Pavillion Kolhapur',      4, 4.3,  5000, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1590073242678-70ee3fc28e8e?w=600'),
        ('Hotel Shalini Palace Kolhapur', 4, 4.4,  5500, 'Heritage,Restaurant,WiFi',         False, 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=600'),
        ('Hotel Woodland Kolhapur',       3, 4.1,  3200, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=600'),
        ('Hotel Maharaja Kolhapur',       3, 4.0,  2800, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1549294413-26f195200c16?w=600'),
    ],
    'Satara': [
        ('Hotel Ajinkya Satara',          4, 4.3,  4500, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1445019980597-93fa8acb246c?w=600'),
        ('Hotel Pratap Satara',           3, 4.2,  3500, 'Restaurant,WiFi,Parking',          True,  'https://images.unsplash.com/photo-1496417263034-38ec4f0b665a?w=600'),
        ('Hotel Shivneri Satara',         3, 4.0,  3000, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1522798514-97ceb8c4f1c8?w=600'),
        ('Hotel Kaas Satara',             3, 3.9,  2500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1584132967334-10e028bd69f7?w=600'),
        ('Hotel Tapola Satara',           3, 3.8,  2200, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1568084680786-a84f91d1153c?w=600'),
    ],
    'Miraj': [
        ('Hotel Miraj Residency',         4, 4.2,  4000, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=600'),
        ('Hotel Sangam Miraj',            3, 4.0,  3200, 'Restaurant,WiFi,Parking',          True,  'https://images.unsplash.com/photo-1600011689032-8b628b8a8747?w=600'),
        ('Hotel Sai Inn Miraj',           3, 3.9,  2800, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600'),
        ('Hotel Shree Miraj',             3, 3.8,  2500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=600'),
        ('Hotel Comfort Miraj',           3, 3.7,  2000, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1600607687939-ce8a6c25118c?w=600'),
    ],
    'Latur': [
        ('Hotel Green Park Latur',        4, 4.3,  4500, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1512918728675-ed5a9ecdebfd?w=600'),
        ('Hotel Sai Latur',               3, 4.1,  3500, 'Restaurant,WiFi,Parking',          True,  'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=600'),
        ('Hotel Ashoka Latur',            3, 4.0,  3000, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1631049552057-403cdb8f0658?w=600'),
        ('Hotel Rajhans Latur',           3, 3.9,  2500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=600'),
        ('Hotel City Inn Latur',          3, 3.8,  2200, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1615460549969-36fa19521a4f?w=600'),
    ],
    'Solapur': [
        ('Hotel Surya Executive Solapur', 4, 4.4,  5000, 'Restaurant,WiFi,Parking,AC Rooms', True,  'https://images.unsplash.com/photo-1587213811864-c02b686f3a58?w=600'),
        ('Hotel Siddharth Solapur',       4, 4.2,  4200, 'Restaurant,WiFi,Parking',          True,  'https://images.unsplash.com/photo-1578774296842-c45e472b3028?w=600'),
        ('Hotel Abhishek Solapur',        3, 4.0,  3200, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1574643156929-51fa098b0394?w=600'),
        ('Hotel Rajmahal Solapur',        3, 3.9,  2800, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1573052905904-34ad8c27f0cc?w=600'),
        ('Hotel Laxmi Solapur',           3, 3.8,  2400, 'Restaurant,WiFi',                  False, 'https://images.unsplash.com/photo-1570213489059-0aac6626cade?w=600'),
    ],
    'Nashik': [
        ('Express Inn Nashik',            5, 4.6,  8000, 'Pool,Spa,Restaurant,WiFi,Gym',     True,  'https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=600'),
        ('Radisson Blu Nashik',           5, 4.5,  7500, 'Pool,Gym,Restaurant,WiFi',         True,  'https://images.unsplash.com/photo-1563911302283-d2bc129e7570?w=600'),
        ('Hotel Panchavati Nashik',       4, 4.3,  5000, 'Restaurant,WiFi,Parking,AC Rooms', False, 'https://images.unsplash.com/photo-1562790351-d273a961e0e9?w=600'),
        ('Hotel Ginger Nashik',           3, 4.1,  3500, 'Gym,Restaurant,WiFi',              False, 'https://images.unsplash.com/photo-1560347876-aeef00ee58a1?w=600'),
        ('Hotel Lemon Tree Nashik',       3, 4.0,  3200, 'Gym,Restaurant,WiFi,Parking',      False, 'https://images.unsplash.com/photo-1559508551-44bff1de756b?w=600'),
    ],
    'Nagpur': [
        ('Radisson Blu Nagpur',           5, 4.7,  9000, 'Pool,Spa,Gym,Restaurant,WiFi',     True,  'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600'),
        ('Le Meridien Nagpur',            5, 4.6,  8500, 'Pool,Spa,Restaurant,WiFi',         True,  'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=600'),
        ('Tuli Imperial Nagpur',          4, 4.4,  6000, 'Pool,Restaurant,WiFi,Parking',     False, 'https://images.unsplash.com/photo-1554995207-c18c203602cb?w=600'),
        ('Hotel Centre Point Nagpur',     3, 4.2,  3500, 'Restaurant,WiFi,Parking',          False, 'https://images.unsplash.com/photo-1553653924-39b70295f8da?w=600'),
        ('Lemon Tree Hotel Nagpur',       3, 4.0,  3000, 'Gym,Restaurant,WiFi',              False, 'https://images.unsplash.com/photo-1549638441-b787d2e11f14?w=600'),
    ],
}

BUS_TYPES = [
    ('Volvo 9400 AC',        'seater',  40, 'AC,WiFi,USB Charging,Water Bottle', 4.8),
    ('Volvo B11R Sleeper',   'sleeper', 30, 'AC,WiFi,Blanket,Pillow,USB',        4.7),
    ('Mercedes Tourismo',    'seater',  45, 'AC,WiFi,Entertainment,Snacks',      4.6),
    ('Scania Metrolink',     'seater',  42, 'AC,WiFi,Recliner Seats,USB',        4.5),
    ('Scania K410 Sleeper',  'sleeper', 34, 'AC,WiFi,Luxury Berths,Pillow',      4.9),
    ('Volvo 9600 Premium',   'sleeper', 32, 'AC,WiFi,Premium Berths,Blanket',    4.8),
    ('Tata Marcopolo AC',    'seater',  45, 'AC,WiFi,USB Charging',              4.4),
    ('Ashok Leyland Viking', 'seater',  48, 'AC,WiFi,Recliner Seats',            4.3),
    ('Mercedes Travego',     'sleeper', 36, 'AC,WiFi,Luxury Berths,Blanket',     4.7),
    ('Volvo Multi-Axle',     'sleeper', 40, 'AC,WiFi,Semi-Sleeper,Blanket',      4.6),
]

# Routes between Maharashtra cities
MAHA_ROUTES = {
    'Pune':     ['Mumbai','Nashik','Kolhapur','Solapur','Satara','Sangli','Nagpur','Latur','Miraj','Aurangabad'],
    'Sangli':   ['Pune','Kolhapur','Miraj','Solapur','Mumbai','Satara','Nashik','Latur','Nagpur','Hyderabad'],
    'Kolhapur': ['Pune','Sangli','Miraj','Mumbai','Goa','Satara','Solapur','Nashik','Nagpur','Bangalore'],
    'Satara':   ['Pune','Kolhapur','Sangli','Mumbai','Solapur','Nashik','Nagpur','Latur','Miraj','Hyderabad'],
    'Miraj':    ['Sangli','Kolhapur','Pune','Solapur','Mumbai','Satara','Nashik','Latur','Nagpur','Hyderabad'],
    'Latur':    ['Solapur','Pune','Nagpur','Hyderabad','Mumbai','Nashik','Sangli','Kolhapur','Satara','Aurangabad'],
    'Solapur':  ['Pune','Latur','Sangli','Mumbai','Hyderabad','Nashik','Nagpur','Kolhapur','Satara','Miraj'],
    'Nashik':   ['Mumbai','Pune','Nagpur','Aurangabad','Solapur','Kolhapur','Sangli','Satara','Latur','Delhi'],
    'Nagpur':   ['Mumbai','Pune','Nashik','Hyderabad','Latur','Solapur','Bhopal','Raipur','Aurangabad','Delhi'],
}

CITY_COORDS = {c: v for c, v in CITIES.items()}

def get_fare_hours(c1, c2):
    c1c = CITY_COORDS.get(c1, (18, 74))
    c2c = CITY_COORDS.get(c2, (18, 74))
    deg = math.sqrt((c1c[0]-c2c[0])**2 + (c1c[1]-c2c[1])**2)
    hours = max(2, min(14, int(deg * 1.4)))
    fm = {2:180,3:250,4:320,5:400,6:480,7:560,8:640,9:720,10:800,11:880,12:960,13:1040,14:1100}
    return fm.get(hours, 500), hours

DEP_HOURS = [6,7,8,9,10,20,21,22,23,0]

with app.app_context():
    from sqlalchemy import text
    row = db.session.execute(
        text("SELECT MAX(CAST(SUBSTRING(bus_number,4) AS UNSIGNED)) FROM buses WHERE bus_number LIKE 'SR-%'")
    ).scalar()
    bus_num = (row or 1200) + 1

    total_hotels = total_buses = total_routes = 0

    for city, (lat, lng) in CITIES.items():
        print(f"Adding {city}...")

        # Hotels
        for name, stars, rating, price, amenities, featured, image in CITY_HOTELS[city]:
            if not Hotel.query.filter_by(hotel_name=name, city=city).first():
                db.session.add(Hotel(
                    hotel_name=name, city=city,
                    address=f'Main Road, {city}, Maharashtra',
                    description=f'Comfortable stay at {name} in {city}.',
                    star_rating=stars, rating=rating,
                    total_reviews=int(rating * 100),
                    min_price=price, amenities=amenities,
                    image_url=image, featured=featured, status='active',
                ))
                total_hotels += 1
        db.session.commit()

        # Buses
        city_buses = []
        for i, (bname, btype, seats, amenities, rating) in enumerate(BUS_TYPES):
            bnum = f'SR-{bus_num}'
            bus_num += 1
            bus = Bus(
                bus_number=bnum, bus_name=bname,
                operator_name='SR Travels', bus_type=btype,
                total_seats=seats, available_seats=seats,
                amenities=amenities, rating=rating,
                total_reviews=0, status='active',
            )
            db.session.add(bus)
            db.session.flush()
            city_buses.append(bus)
            total_buses += 1
            if not BusTracking.query.filter_by(bus_id=bus.id).first():
                db.session.add(BusTracking(
                    bus_id=bus.id,
                    current_latitude=round(lat + i*0.005, 4),
                    current_longitude=round(lng + i*0.005, 4),
                    current_location=f'{city} Depot {i+1}',
                    speed=0, status='stopped',
                ))
        db.session.commit()

        # Routes
        dests = MAHA_ROUTES.get(city, [])
        for bi, dest in enumerate(dests[:10]):
            bus = city_buses[bi % len(city_buses)]
            if BusRoute.query.filter_by(bus_id=bus.id, from_city=city, to_city=dest).first():
                continue
            fare, hours = get_fare_hours(city, dest)
            dep_h = DEP_HOURS[bi % len(DEP_HOURS)]
            arr_h = (dep_h + hours) % 24
            db.session.add(BusRoute(
                bus_id=bus.id, from_city=city, to_city=dest,
                departure_time=time(dep_h, 0),
                arrival_time=time(arr_h, 0),
                duration=f'{hours}h 00m', fare=fare, frequency='Daily',
            ))
            total_routes += 1
        db.session.commit()

    print(f"\n✅ Maharashtra cities added!")
    print(f"   Hotels : {total_hotels}")
    print(f"   Buses  : {total_buses}")
    print(f"   Routes : {total_routes}")
    print(f"\n   Total buses  : {Bus.query.count()}")
    print(f"   Total routes : {BusRoute.query.count()}")
    print(f"   Total hotels : {Hotel.query.count()}")

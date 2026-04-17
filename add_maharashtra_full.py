"""
Add all Maharashtra districts + real Maharashtra bus operator names.
Run: py add_maharashtra_full.py
"""
import math
from datetime import time
from app import create_app, db
from app.models import Bus, BusRoute, BusTracking
from sqlalchemy import text

app = create_app()

# All 36 Maharashtra districts with GPS
MH_CITIES = {
    'Mumbai':       (19.0760, 72.8777),
    'Pune':         (18.5204, 73.8567),
    'Nagpur':       (21.1458, 79.0882),
    'Nashik':       (20.0059, 73.7797),
    'Aurangabad':   (19.8762, 75.3433),
    'Solapur':      (17.6599, 75.9064),
    'Kolhapur':     (16.7050, 74.2433),
    'Sangli':       (16.8524, 74.5815),
    'Satara':       (17.6805, 74.0183),
    'Ratnagiri':    (16.9902, 73.3120),
    'Sindhudurg':   (16.3490, 73.9862),
    'Thane':        (19.2183, 72.9781),
    'Raigad':       (18.5158, 73.1800),
    'Palghar':      (19.6967, 72.7697),
    'Ahmednagar':   (19.0952, 74.7496),
    'Dhule':        (20.9042, 74.7749),
    'Jalgaon':      (21.0077, 75.5626),
    'Nandurbar':    (21.3667, 74.2333),
    'Beed':         (18.9890, 75.7600),
    'Latur':        (18.4088, 76.5604),
    'Osmanabad':    (18.1860, 76.0400),
    'Nanded':       (19.1383, 77.3210),
    'Hingoli':      (19.7167, 77.1500),
    'Parbhani':     (19.2667, 76.7667),
    'Jalna':        (19.8347, 75.8816),
    'Buldhana':     (20.5292, 76.1842),
    'Akola':        (20.7002, 77.0082),
    'Washim':       (20.1167, 77.1333),
    'Amravati':     (20.9374, 77.7796),
    'Yavatmal':     (20.3888, 78.1204),
    'Wardha':       (20.7453, 78.6022),
    'Chandrapur':   (19.9615, 79.2961),
    'Gadchiroli':   (20.1809, 80.0000),
    'Gondia':       (21.4600, 80.1900),
    'Bhandara':     (21.1667, 79.6500),
    'Miraj':        (16.8267, 74.6455),
}

# Real Maharashtra bus operator names
MH_BUS_OPERATORS = [
    # MSRTC (State Transport)
    ('MSRTC Shivneri AC',          'seater',  45, 'AC, WiFi, USB Charging, Water Bottle',     4.7),
    ('MSRTC Asiad Semi-Luxury',    'seater',  52, 'AC, Recliner Seats',                        4.3),
    ('MSRTC Hirkani Ladies Special','seater', 45, 'AC, WiFi, Ladies Only',                     4.5),
    ('MSRTC Shivshahi AC',         'seater',  45, 'AC, WiFi, USB Charging',                    4.6),
    ('MSRTC Parivartan AC',        'sleeper', 36, 'AC, WiFi, Blanket, Pillow',                 4.4),
    # Private Maharashtra operators
    ('Konduskar Travels AC',       'sleeper', 34, 'AC, WiFi, Luxury Berths, Blanket, Pillow',  4.8),
    ('Neeta Tours & Travels',      'sleeper', 30, 'AC, WiFi, Blanket, Pillow, USB Charging',   4.7),
    ('Paulo Travels AC Sleeper',   'sleeper', 32, 'AC, WiFi, Premium Berths, Blanket',         4.6),
    ('Prasanna Purple Travels',    'seater',  42, 'AC, WiFi, Recliner Seats, USB Charging',    4.5),
    ('Raj National Express',       'seater',  45, 'AC, WiFi, USB Charging, Snacks',            4.4),
    ('Sharma Transports Pune',     'seater',  40, 'AC, WiFi, USB Charging',                    4.3),
    ('Shrinath Travel Agency',     'sleeper', 36, 'AC, WiFi, Luxury Berths, Blanket',          4.6),
    ('Sugama Tourist Travels',     'seater',  44, 'AC, WiFi, Recliner Seats',                  4.4),
    ('VRL Travels Maharashtra',    'sleeper', 30, 'AC, WiFi, Blanket, Pillow, USB',            4.7),
    ('Orange Tours Maharashtra',   'seater',  45, 'AC, WiFi, Entertainment, Snacks',           4.5),
    ('Parveen Travels Pune',       'sleeper', 34, 'AC, WiFi, Luxury Berths, Pillow',           4.6),
    ('Jabbar Travels AC',          'sleeper', 32, 'AC, WiFi, Premium Berths, Blanket',         4.5),
    ('Mahalaxmi Travels',          'seater',  42, 'AC, WiFi, USB Charging',                    4.3),
    ('Shivam Travels AC',          'seater',  40, 'AC, WiFi, Recliner Seats',                  4.4),
    ('Gajanan Travels',            'sleeper', 36, 'AC, WiFi, Blanket, Pillow',                 4.5),
]

# Routes between Maharashtra cities
MH_ROUTES = {
    'Mumbai':     ['Pune','Nashik','Aurangabad','Kolhapur','Nagpur','Thane','Raigad','Palghar','Solapur','Ratnagiri'],
    'Pune':       ['Mumbai','Nashik','Kolhapur','Solapur','Satara','Sangli','Nagpur','Aurangabad','Ahmednagar','Satara'],
    'Nagpur':     ['Mumbai','Pune','Nashik','Aurangabad','Amravati','Wardha','Chandrapur','Yavatmal','Bhandara','Gondia'],
    'Nashik':     ['Mumbai','Pune','Aurangabad','Dhule','Jalgaon','Ahmednagar','Nandurbar','Nagpur','Solapur','Kolhapur'],
    'Aurangabad': ['Mumbai','Pune','Nashik','Jalna','Beed','Latur','Nanded','Parbhani','Hingoli','Nagpur'],
    'Solapur':    ['Mumbai','Pune','Kolhapur','Sangli','Latur','Osmanabad','Bijapur','Nashik','Aurangabad','Satara'],
    'Kolhapur':   ['Mumbai','Pune','Sangli','Satara','Solapur','Ratnagiri','Sindhudurg','Nashik','Miraj','Belgaum'],
    'Sangli':     ['Pune','Kolhapur','Miraj','Solapur','Mumbai','Satara','Nashik','Latur','Nagpur','Hyderabad'],
    'Satara':     ['Pune','Kolhapur','Sangli','Mumbai','Solapur','Nashik','Nagpur','Latur','Miraj','Ratnagiri'],
    'Ratnagiri':  ['Mumbai','Pune','Kolhapur','Sindhudurg','Raigad','Nashik','Goa','Thane','Satara','Solapur'],
    'Sindhudurg': ['Mumbai','Kolhapur','Ratnagiri','Goa','Pune','Sangli','Satara','Nashik','Thane','Raigad'],
    'Thane':      ['Mumbai','Pune','Nashik','Raigad','Palghar','Aurangabad','Nagpur','Kolhapur','Solapur','Ahmednagar'],
    'Raigad':     ['Mumbai','Pune','Thane','Ratnagiri','Nashik','Kolhapur','Solapur','Aurangabad','Nagpur','Satara'],
    'Palghar':    ['Mumbai','Thane','Nashik','Pune','Raigad','Aurangabad','Nagpur','Dhule','Jalgaon','Nandurbar'],
    'Ahmednagar': ['Pune','Nashik','Aurangabad','Mumbai','Solapur','Beed','Latur','Nagpur','Kolhapur','Satara'],
    'Dhule':      ['Nashik','Mumbai','Pune','Jalgaon','Nandurbar','Aurangabad','Nagpur','Solapur','Kolhapur','Ahmednagar'],
    'Jalgaon':    ['Nashik','Mumbai','Pune','Dhule','Aurangabad','Nagpur','Nandurbar','Solapur','Kolhapur','Ahmednagar'],
    'Nandurbar':  ['Dhule','Nashik','Mumbai','Jalgaon','Pune','Aurangabad','Nagpur','Solapur','Kolhapur','Surat'],
    'Beed':       ['Aurangabad','Pune','Nashik','Ahmednagar','Latur','Osmanabad','Nanded','Mumbai','Solapur','Nagpur'],
    'Latur':      ['Solapur','Pune','Nagpur','Hyderabad','Mumbai','Nashik','Sangli','Kolhapur','Satara','Aurangabad'],
    'Osmanabad':  ['Solapur','Latur','Pune','Mumbai','Nashik','Aurangabad','Nagpur','Kolhapur','Sangli','Hyderabad'],
    'Nanded':     ['Aurangabad','Hyderabad','Pune','Mumbai','Nashik','Nagpur','Latur','Parbhani','Hingoli','Solapur'],
    'Hingoli':    ['Aurangabad','Nanded','Parbhani','Pune','Mumbai','Nashik','Nagpur','Latur','Solapur','Hyderabad'],
    'Parbhani':   ['Aurangabad','Nanded','Hingoli','Pune','Mumbai','Nashik','Nagpur','Latur','Solapur','Hyderabad'],
    'Jalna':      ['Aurangabad','Pune','Mumbai','Nashik','Nagpur','Beed','Latur','Solapur','Kolhapur','Ahmednagar'],
    'Buldhana':   ['Aurangabad','Akola','Amravati','Pune','Mumbai','Nashik','Nagpur','Jalgaon','Dhule','Solapur'],
    'Akola':      ['Amravati','Nagpur','Aurangabad','Pune','Mumbai','Nashik','Buldhana','Washim','Yavatmal','Wardha'],
    'Washim':     ['Akola','Amravati','Nagpur','Aurangabad','Pune','Mumbai','Nashik','Yavatmal','Buldhana','Solapur'],
    'Amravati':   ['Nagpur','Akola','Aurangabad','Pune','Mumbai','Nashik','Yavatmal','Wardha','Washim','Buldhana'],
    'Yavatmal':   ['Nagpur','Amravati','Aurangabad','Pune','Mumbai','Nashik','Wardha','Chandrapur','Akola','Washim'],
    'Wardha':     ['Nagpur','Amravati','Yavatmal','Pune','Mumbai','Nashik','Chandrapur','Aurangabad','Akola','Washim'],
    'Chandrapur': ['Nagpur','Yavatmal','Wardha','Pune','Mumbai','Nashik','Gadchiroli','Aurangabad','Amravati','Hyderabad'],
    'Gadchiroli': ['Nagpur','Chandrapur','Pune','Mumbai','Nashik','Yavatmal','Wardha','Aurangabad','Amravati','Raipur'],
    'Gondia':     ['Nagpur','Bhandara','Pune','Mumbai','Nashik','Aurangabad','Amravati','Wardha','Chandrapur','Raipur'],
    'Bhandara':   ['Nagpur','Gondia','Pune','Mumbai','Nashik','Aurangabad','Amravati','Wardha','Chandrapur','Yavatmal'],
    'Miraj':      ['Sangli','Kolhapur','Pune','Solapur','Mumbai','Satara','Nashik','Latur','Nagpur','Hyderabad'],
}

CITY_COORDS = MH_CITIES
DEP_HOURS = [6, 7, 8, 9, 10, 20, 21, 22, 23, 0]
FARE_MAP = {2:150,3:220,4:300,5:380,6:460,7:540,8:620,9:700,10:780,11:860,12:940,13:1020,14:1100}


def get_fare_hours(c1, c2):
    lat1, lng1 = CITY_COORDS.get(c1, (18, 74))
    lat2, lng2 = CITY_COORDS.get(c2, (18, 74))
    deg = math.sqrt((lat1-lat2)**2 + (lng1-lng2)**2)
    hours = max(2, min(14, int(deg * 1.5)))
    return FARE_MAP.get(hours, 500), hours


with app.app_context():
    row = db.session.execute(
        text("SELECT MAX(CAST(SUBSTRING(bus_number,4) AS UNSIGNED)) FROM buses WHERE bus_number LIKE 'SR-%'")
    ).scalar()
    bus_num = (row or 1500) + 1

    tb = tr = tt = 0

    for city, (lat, lng) in MH_CITIES.items():
        print(f"  Adding {city}...")

        # 20 buses per city (all MH operators)
        city_buses = []
        for i, (bname, btype, seats, amenities, rating) in enumerate(MH_BUS_OPERATORS):
            bnum = f'SR-{bus_num}'
            bus_num += 1
            bus = Bus(
                bus_number=bnum, bus_name=bname,
                operator_name=bname.split(' ')[0] + ' Travels',
                bus_type=btype, total_seats=seats, available_seats=seats,
                amenities=amenities, rating=rating, total_reviews=0, status='active'
            )
            db.session.add(bus)
            db.session.flush()
            city_buses.append(bus)
            tb += 1
            if not BusTracking.query.filter_by(bus_id=bus.id).first():
                db.session.add(BusTracking(
                    bus_id=bus.id,
                    current_latitude=round(lat + i*0.003, 4),
                    current_longitude=round(lng + i*0.003, 4),
                    current_location=f'{city} Depot {i+1}',
                    speed=0, status='stopped'
                ))
                tt += 1
        db.session.commit()

        # Routes
        dests = MH_ROUTES.get(city, [])
        for bi, dest in enumerate(dests[:10]):
            bus = city_buses[bi % len(city_buses)]
            if BusRoute.query.filter_by(bus_id=bus.id, from_city=city, to_city=dest).first():
                continue
            fare, hours = get_fare_hours(city, dest)
            dep_h = DEP_HOURS[bi % len(DEP_HOURS)]
            arr_h = (dep_h + hours) % 24
            db.session.add(BusRoute(
                bus_id=bus.id, from_city=city, to_city=dest,
                departure_time=time(dep_h, 0), arrival_time=time(arr_h, 0),
                duration=f'{hours}h 00m', fare=fare, frequency='Daily'
            ))
            tr += 1
        db.session.commit()

    print(f'\n✅ Maharashtra complete!')
    print(f'   Buses added   : {tb}')
    print(f'   Routes added  : {tr}')
    print(f'   Tracking added: {tt}')
    print(f'\n   Total buses   : {Bus.query.count()}')
    print(f'   Total routes  : {BusRoute.query.count()}')
    print(f'   MH cities     : {len(MH_CITIES)}')

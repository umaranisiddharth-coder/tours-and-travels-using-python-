"""
Seed: 10 buses + routes per major city, 5 hotels per city.
Run: py seed_cities.py
"""
from app import create_app, db
from app.models import Bus, BusRoute, Hotel, BusTracking
from datetime import time

app = create_app()

# Major cities and their GPS centres
CITIES = {
    'Delhi':     (28.6139, 77.2090),
    'Mumbai':    (19.0760, 72.8777),
    'Bangalore': (12.9716, 77.5946),
    'Chennai':   (13.0827, 80.2707),
    'Hyderabad': (17.3850, 78.4867),
    'Pune':      (18.5204, 73.8567),
    'Jaipur':    (26.9124, 75.7873),
    'Kolkata':   (22.5726, 88.3639),
    'Ahmedabad': (23.0225, 72.5714),
    'Surat':     (21.1702, 72.8311),
    'Lucknow':   (26.8467, 80.9462),
    'Nagpur':    (21.1458, 79.0882),
    'Indore':    (22.7196, 75.8577),
    'Bhopal':    (23.2599, 77.4126),
    'Patna':     (25.5941, 85.1376),
    'Kochi':     (9.9312,  76.2673),
    'Goa':       (15.2993, 74.1240),
    'Amritsar':  (31.6340, 74.8723),
    'Varanasi':  (25.3176, 82.9739),
    'Agra':      (27.1767, 78.0081),
}

# Route pairs: (from, to, dep_hour, arr_hour, duration, fare)
ROUTE_PAIRS = [
    ('Delhi',     'Jaipur',      6,  11, '5h 00m',  450),
    ('Delhi',     'Agra',        7,  10, '3h 30m',  300),
    ('Delhi',     'Lucknow',    21,   5, '8h 00m',  560),
    ('Delhi',     'Amritsar',   22,   6, '8h 00m',  620),
    ('Delhi',     'Chandigarh',  7,  11, '4h 00m',  380),
    ('Mumbai',    'Pune',        7,  11, '3h 30m',  350),
    ('Mumbai',    'Goa',        20,   8, '12h 00m', 850),
    ('Mumbai',    'Ahmedabad',  20,   5, '9h 00m',  700),
    ('Mumbai',    'Nashik',      9,  13, '4h 00m',  280),
    ('Mumbai',    'Surat',       8,  12, '4h 00m',  320),
    ('Bangalore', 'Chennai',    22,   6, '8h 00m',  600),
    ('Bangalore', 'Hyderabad',  20,   6, '10h 00m', 750),
    ('Bangalore', 'Mysore',      7,  10, '3h 00m',  250),
    ('Bangalore', 'Kochi',      21,   7, '10h 00m', 800),
    ('Bangalore', 'Goa',        20,   8, '12h 00m', 900),
    ('Chennai',   'Hyderabad',  20,   6, '10h 00m', 720),
    ('Chennai',   'Coimbatore', 21,   5, '8h 00m',  520),
    ('Chennai',   'Kochi',      21,   7, '10h 00m', 680),
    ('Chennai',   'Bangalore',   7,  15, '8h 00m',  600),
    ('Hyderabad', 'Bangalore',  20,   6, '10h 00m', 750),
    ('Hyderabad', 'Chennai',    21,   7, '10h 00m', 720),
    ('Hyderabad', 'Pune',       20,   6, '10h 00m', 700),
    ('Hyderabad', 'Mumbai',     19,   7, '12h 00m', 900),
    ('Hyderabad', 'Nagpur',     21,   5, '8h 00m',  550),
    ('Pune',      'Goa',        18,   6, '12h 00m', 850),
    ('Pune',      'Mumbai',      6,  10, '3h 30m',  320),
    ('Pune',      'Hyderabad',  20,   6, '10h 00m', 700),
    ('Pune',      'Nashik',      8,  12, '4h 00m',  250),
    ('Jaipur',    'Delhi',       6,  11, '5h 00m',  450),
    ('Jaipur',    'Udaipur',     8,  14, '6h 00m',  480),
    ('Jaipur',    'Agra',        7,  11, '4h 00m',  350),
    ('Jaipur',    'Jodhpur',     8,  13, '5h 00m',  420),
    ('Kolkata',   'Patna',      21,   5, '8h 00m',  580),
    ('Kolkata',   'Bhubaneswar',22,   6, '8h 00m',  550),
    ('Kolkata',   'Siliguri',   20,   6, '10h 00m', 650),
    ('Ahmedabad', 'Surat',       8,  12, '3h 30m',  280),
    ('Ahmedabad', 'Mumbai',     20,   5, '9h 00m',  700),
    ('Ahmedabad', 'Vadodara',    8,  11, '3h 00m',  220),
    ('Lucknow',   'Delhi',      21,   5, '8h 00m',  560),
    ('Lucknow',   'Varanasi',    8,  13, '5h 00m',  380),
    ('Lucknow',   'Agra',        7,  12, '5h 00m',  400),
    ('Nagpur',    'Hyderabad',  20,   4, '8h 00m',  550),
    ('Nagpur',    'Mumbai',     20,   6, '10h 00m', 700),
    ('Nagpur',    'Bhopal',      8,  13, '5h 00m',  380),
    ('Indore',    'Bhopal',      8,  11, '3h 00m',  220),
    ('Indore',    'Mumbai',     20,   6, '10h 00m', 750),
    ('Indore',    'Nagpur',     20,   4, '8h 00m',  500),
    ('Bhopal',    'Indore',      8,  11, '3h 00m',  220),
    ('Bhopal',    'Nagpur',     20,   4, '8h 00m',  500),
    ('Patna',     'Kolkata',    21,   5, '8h 00m',  580),
    ('Patna',     'Varanasi',    8,  12, '4h 00m',  320),
    ('Kochi',     'Bangalore',  21,   7, '10h 00m', 800),
    ('Kochi',     'Chennai',    21,   7, '10h 00m', 680),
    ('Goa',       'Mumbai',     20,   8, '12h 00m', 850),
    ('Goa',       'Bangalore',  20,   8, '12h 00m', 900),
    ('Amritsar',  'Delhi',      22,   6, '8h 00m',  620),
    ('Amritsar',  'Chandigarh', 8,   11, '3h 00m',  280),
    ('Varanasi',  'Lucknow',    8,   13, '5h 00m',  380),
    ('Varanasi',  'Patna',      8,   12, '4h 00m',  320),
    ('Agra',      'Delhi',      7,   10, '3h 30m',  300),
    ('Agra',      'Jaipur',     8,   12, '4h 00m',  350),
]

# Bus types cycling
BUS_TYPES = [
    ('Volvo 9400 AC',       'seater',  40, 'AC, WiFi, USB Charging, Water Bottle',    4.8),
    ('Volvo B11R Sleeper',  'sleeper', 30, 'AC, WiFi, Blanket, Pillow, USB Charging', 4.7),
    ('Mercedes Tourismo',   'seater',  45, 'AC, WiFi, Entertainment, Snacks',         4.6),
    ('Scania Metrolink',    'seater',  42, 'AC, WiFi, Recliner Seats, USB Charging',  4.5),
    ('Scania K410 Sleeper', 'sleeper', 34, 'AC, WiFi, Luxury Berths, Pillow, Blanket',4.9),
    ('Volvo 9600 Premium',  'sleeper', 32, 'AC, WiFi, Premium Berths, Blanket',       4.8),
    ('Tata Marcopolo AC',   'seater',  45, 'AC, WiFi, USB Charging',                  4.4),
    ('Ashok Leyland Viking','seater',  48, 'AC, WiFi, Recliner Seats',                4.3),
    ('Mercedes Travego',    'sleeper', 36, 'AC, WiFi, Luxury Berths, Blanket',        4.7),
    ('Volvo Multi-Axle',    'sleeper', 40, 'AC, WiFi, Semi-Sleeper, Blanket',         4.6),
]

# 5 hotel templates per city (name suffix varies)
HOTEL_TEMPLATES = [
    ('{city} Grand Palace',    5, 4.8, 8500,  'Pool, Spa, Gym, Fine Dining, WiFi, Valet',    True),
    ('{city} Business Suites', 4, 4.5, 4500,  'Business Center, Gym, Restaurant, WiFi',      False),
    ('{city} Heritage Inn',    4, 4.6, 5200,  'Heritage Decor, Restaurant, WiFi, Parking',   False),
    ('{city} Budget Stay',     3, 4.2, 1800,  'Restaurant, WiFi, Parking',                   False),
    ('{city} Comfort Hotel',   3, 4.3, 2400,  'AC Rooms, Restaurant, WiFi, 24h Reception',   False),
]

with app.app_context():
    bus_counter = 200   # start bus numbers from SR-200
    added_buses = added_routes = added_hotels = added_tracking = 0

    for city, (lat, lng) in CITIES.items():
        # ── 10 buses for this city ──────────────────────────────────────────────
        city_buses = []
        for i, (bname, btype, seats, amenities, rating) in enumerate(BUS_TYPES):
            bus_number = f'SR-{bus_counter}'
            bus_counter += 1
            existing = Bus.query.filter_by(bus_number=bus_number).first()
            if existing:
                city_buses.append(existing)
                continue
            bus = Bus(
                bus_number=bus_number,
                bus_name=f'{bname}',
                operator_name='SR Travels',
                bus_type=btype,
                total_seats=seats,
                available_seats=seats,
                amenities=amenities,
                rating=rating,
                total_reviews=0,
                status='active',
            )
            db.session.add(bus)
            db.session.flush()
            city_buses.append(bus)
            added_buses += 1

            # GPS tracking
            if not BusTracking.query.filter_by(bus_id=bus.id).first():
                db.session.add(BusTracking(
                    bus_id=bus.id,
                    current_latitude=lat + (i * 0.01),
                    current_longitude=lng + (i * 0.01),
                    current_location=f'{city} - Route {i+1}',
                    speed=60 + (i * 5),
                    status='moving',
                ))
                added_tracking += 1

        db.session.commit()

        # ── Routes from this city ───────────────────────────────────────────────
        city_routes = [r for r in ROUTE_PAIRS if r[0] == city]
        for bus_idx, (fc, tc, dep_h, arr_h, dur, fare) in enumerate(city_routes[:10]):
            bus = city_buses[bus_idx % len(city_buses)]
            if BusRoute.query.filter_by(bus_id=bus.id, from_city=fc, to_city=tc).first():
                continue
            db.session.add(BusRoute(
                bus_id=bus.id,
                from_city=fc, to_city=tc,
                departure_time=time(dep_h, 0),
                arrival_time=time(arr_h, 0),
                duration=dur, fare=fare, frequency='Daily',
            ))
            added_routes += 1

        db.session.commit()

        # ── 5 hotels for this city ──────────────────────────────────────────────
        for hname_tpl, stars, rating, price, amenities, featured in HOTEL_TEMPLATES:
            hname = hname_tpl.format(city=city)
            if Hotel.query.filter_by(hotel_name=hname).first():
                continue
            db.session.add(Hotel(
                hotel_name=hname,
                city=city,
                address=f'Main Road, {city}',
                description=f'A comfortable stay in the heart of {city}.',
                star_rating=stars,
                rating=rating,
                total_reviews=int(rating * 100),
                min_price=price,
                amenities=amenities,
                featured=featured,
                status='active',
            ))
            added_hotels += 1

        db.session.commit()
        print(f'✅ {city}: buses={len(city_buses)}, routes={len(city_routes[:10])}, hotels=5')

    print(f'\n🎉 Done!')
    print(f'   Buses added   : {added_buses}')
    print(f'   Routes added  : {added_routes}')
    print(f'   Hotels added  : {added_hotels}')
    print(f'   Tracking added: {added_tracking}')
    print(f'\n   Total buses  : {Bus.query.count()}')
    print(f'   Total routes : {BusRoute.query.count()}')
    print(f'   Total hotels : {Hotel.query.count()}')

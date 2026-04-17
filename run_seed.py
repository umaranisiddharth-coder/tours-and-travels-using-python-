"""Quick seed runner — called by PowerShell."""
import math
from datetime import time
from app import create_app, db
from app.models import Bus, BusRoute, Hotel, BusTracking
from sqlalchemy import text

app = create_app()

CITIES = [
    ('Delhi',28.6139,77.2090),('Mumbai',19.0760,72.8777),('Bangalore',12.9716,77.5946),
    ('Chennai',13.0827,80.2707),('Hyderabad',17.3850,78.4867),('Pune',18.5204,73.8567),
    ('Jaipur',26.9124,75.7873),('Kolkata',22.5726,88.3639),('Ahmedabad',23.0225,72.5714),
    ('Surat',21.1702,72.8311),('Lucknow',26.8467,80.9462),('Nagpur',21.1458,79.0882),
    ('Indore',22.7196,75.8577),('Bhopal',23.2599,77.4126),('Patna',25.5941,85.1376),
    ('Kochi',9.9312,76.2673),('Goa',15.2993,74.1240),('Amritsar',31.6340,74.8723),
    ('Varanasi',25.3176,82.9739),('Agra',27.1767,78.0081),('Chandigarh',30.7333,76.7794),
    ('Coimbatore',11.0168,76.9558),('Visakhapatnam',17.6868,83.2185),
    ('Bhubaneswar',20.2961,85.8245),('Mysore',12.2958,76.6394),('Udaipur',24.5854,73.7125),
    ('Jodhpur',26.2389,73.0243),('Shimla',31.1048,77.1734),('Manali',32.2396,77.1887),
    ('Rishikesh',30.0869,78.2676),('Haridwar',29.9457,78.1642),('Dehradun',30.3165,78.0322),
    ('Nashik',20.0059,73.7797),('Aurangabad',19.8762,75.3433),('Kolhapur',16.7050,74.2433),
    ('Solapur',17.6599,75.9064),('Vadodara',22.3072,73.1812),('Rajkot',22.3039,70.8022),
    ('Bhavnagar',21.7645,72.1519),('Gandhinagar',23.2156,72.6369),
    ('Jabalpur',23.1815,79.9864),('Gwalior',26.2183,78.1828),('Raipur',21.2514,81.6296),
    ('Ranchi',23.3441,85.3096),('Jamshedpur',22.8046,86.2029),('Dhanbad',23.7957,86.4304),
    ('Siliguri',26.7271,88.3953),('Guwahati',26.1445,91.7362),
    ('Thiruvananthapuram',8.5241,76.9366),('Kozhikode',11.2588,75.7804),
    ('Thrissur',10.5276,76.2144),('Madurai',9.9252,78.1198),
    ('Tiruchirappalli',10.7905,78.7047),('Salem',11.6643,78.1460),
    ('Vijayawada',16.5062,80.6480),('Tirupati',13.6288,79.4192),
    ('Guntur',16.3067,80.4365),('Warangal',17.9784,79.5941),
    ('Hubli',15.3647,75.1240),('Belgaum',15.8497,74.4977),
    ('Mangalore',12.9141,74.8560),('Davangere',14.4644,75.9218),
    ('Bikaner',28.0229,73.3119),('Ajmer',26.4499,74.6399),
    ('Kota',25.2138,75.8648),('Alwar',27.5530,76.6346),
    ('Mathura',27.4924,77.6737),('Aligarh',27.8974,78.0880),
    ('Meerut',28.9845,77.7064),('Kanpur',26.4499,80.3319),
    ('Allahabad',25.4358,81.8463),('Gorakhpur',26.7606,83.3732),
    ('Nellore',14.4426,79.9865),('Karimnagar',18.4386,79.1288),
    ('Nizamabad',18.6725,78.0941),('Shimoga',13.9299,75.5681),
    ('Tumkur',13.3379,77.1173),('Vellore',12.9165,79.1325),
    ('Tirunelveli',8.7139,77.7567),
]

CITY_COORDS = {c[0]: (c[1], c[2]) for c in CITIES}
CITY_NAMES  = [c[0] for c in CITIES]

BUS_TYPES = [
    ('Volvo 9400 AC',        'seater',  40, 'AC, WiFi, USB Charging, Water Bottle',     4.8),
    ('Volvo B11R Sleeper',   'sleeper', 30, 'AC, WiFi, Blanket, Pillow, USB Charging',  4.7),
    ('Mercedes Tourismo',    'seater',  45, 'AC, WiFi, Entertainment, Snacks',           4.6),
    ('Scania Metrolink',     'seater',  42, 'AC, WiFi, Recliner Seats, USB Charging',   4.5),
    ('Scania K410 Sleeper',  'sleeper', 34, 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.9),
    ('Volvo 9600 Premium',   'sleeper', 32, 'AC, WiFi, Premium Berths, Blanket',        4.8),
    ('Tata Marcopolo AC',    'seater',  45, 'AC, WiFi, USB Charging',                   4.4),
    ('Ashok Leyland Viking', 'seater',  48, 'AC, WiFi, Recliner Seats',                 4.3),
    ('Mercedes Travego',     'sleeper', 36, 'AC, WiFi, Luxury Berths, Blanket',         4.7),
    ('Volvo Multi-Axle',     'sleeper', 40, 'AC, WiFi, Semi-Sleeper, Blanket',          4.6),
]

HOTEL_TEMPLATES = [
    ('{city} Grand Palace',    5, 4.8, 8500, 'Pool, Spa, Gym, Fine Dining, WiFi, Valet', True),
    ('{city} Business Suites', 4, 4.5, 4500, 'Business Center, Gym, Restaurant, WiFi',   False),
    ('{city} Heritage Inn',    4, 4.6, 5200, 'Heritage Decor, Restaurant, WiFi, Parking', False),
    ('{city} Budget Stay',     3, 4.2, 1800, 'Restaurant, WiFi, Parking',                  False),
    ('{city} Comfort Hotel',   3, 4.3, 2400, 'AC Rooms, Restaurant, WiFi, 24h Reception',  False),
]

DEP_HOURS = [6, 7, 8, 9, 10, 20, 21, 22, 23, 0]
FARE_MAP   = {2:200,3:280,4:350,5:420,6:500,7:580,8:650,9:720,10:800,11:880,12:950,13:1020,14:1100}


def get_fare_hours(c1, c2):
    lat1, lng1 = CITY_COORDS.get(c1, (20, 78))
    lat2, lng2 = CITY_COORDS.get(c2, (20, 78))
    deg   = math.sqrt((lat1-lat2)**2 + (lng1-lng2)**2)
    hours = max(2, min(14, int(deg * 1.3)))
    return FARE_MAP.get(hours, 600), hours


def nearest(city, n=10):
    lat, lng = CITY_COORDS[city]
    others = [(c, math.sqrt((lat-CITY_COORDS[c][0])**2+(lng-CITY_COORDS[c][1])**2))
              for c in CITY_NAMES if c != city]
    others.sort(key=lambda x: x[1])
    return [c for c, _ in others[:n]]


with app.app_context():
    # Next bus number
    row = db.session.execute(
        text("SELECT MAX(CAST(SUBSTRING(bus_number,4) AS UNSIGNED)) "
             "FROM buses WHERE bus_number LIKE 'SR-%'")
    ).scalar()
    bus_num = (row or 400) + 1
    print(f"Starting at SR-{bus_num}")

    tb = tr = th = tt = 0

    for idx, (city, lat, lng) in enumerate(CITIES):
        print(f"[{idx+1}/{len(CITIES)}] {city}")

        # 10 buses
        city_buses = []
        for i, (bname, btype, seats, amenities, rating) in enumerate(BUS_TYPES):
            bnum = f'SR-{bus_num}'
            bus_num += 1
            bus = Bus(bus_number=bnum, bus_name=bname, operator_name='SR Travels',
                      bus_type=btype, total_seats=seats, available_seats=seats,
                      amenities=amenities, rating=rating, total_reviews=0, status='active')
            db.session.add(bus)
            db.session.flush()
            city_buses.append(bus)
            tb += 1
            if not BusTracking.query.filter_by(bus_id=bus.id).first():
                db.session.add(BusTracking(
                    bus_id=bus.id,
                    current_latitude=round(lat + i*0.005, 4),
                    current_longitude=round(lng + i*0.005, 4),
                    current_location=f'{city} Depot {i+1}',
                    speed=0, status='stopped'))
                tt += 1
        db.session.commit()

        # 10 routes
        for bi, dest in enumerate(nearest(city, 10)):
            bus = city_buses[bi % len(city_buses)]
            if BusRoute.query.filter_by(bus_id=bus.id, from_city=city, to_city=dest).first():
                continue
            fare, hours = get_fare_hours(city, dest)
            dep_h = DEP_HOURS[bi % len(DEP_HOURS)]
            arr_h = (dep_h + hours) % 24
            db.session.add(BusRoute(
                bus_id=bus.id, from_city=city, to_city=dest,
                departure_time=time(dep_h, 0), arrival_time=time(arr_h, 0),
                duration=f'{hours}h 00m', fare=fare, frequency='Daily'))
            tr += 1
        db.session.commit()

        # 5 hotels
        for tpl, stars, rating, price, amenities, featured in HOTEL_TEMPLATES:
            hname = tpl.format(city=city)
            if Hotel.query.filter_by(hotel_name=hname).first():
                continue
            db.session.add(Hotel(
                hotel_name=hname, city=city, address=f'Main Road, {city}',
                description=f'A comfortable stay in {city}.',
                star_rating=stars, rating=rating, total_reviews=int(rating*80),
                min_price=price, amenities=amenities, featured=featured, status='active'))
            th += 1
        db.session.commit()

    print(f"\nDone! Added: buses={tb} routes={tr} hotels={th} tracking={tt}")
    print(f"TOTAL: buses={Bus.query.count()} routes={BusRoute.query.count()} hotels={Hotel.query.count()}")
    print(f"Cities with routes: {db.session.execute(text('SELECT COUNT(DISTINCT from_city) FROM bus_routes')).scalar()}")

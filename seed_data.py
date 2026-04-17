"""
Seed script — adds 20 hotels + 20 buses with routes across India.
Run: py seed_data.py
"""
from app import create_app, db
from app.models import Bus, BusRoute, Hotel, BusTracking
from datetime import time

app = create_app()

# ── 20 Hotels ──────────────────────────────────────────────────────────────────
HOTELS = [
    dict(hotel_name='The Grand Palace Delhi', city='Delhi',
         address='Connaught Place, New Delhi', star_rating=5, rating=4.8,
         total_reviews=1240, min_price=8500,
         amenities='Pool, Spa, Gym, Restaurant, WiFi, Valet Parking',
         description='Luxury 5-star hotel in the heart of New Delhi.',
         featured=True),
    dict(hotel_name='Mumbai Harbour View', city='Mumbai',
         address='Marine Drive, Mumbai', star_rating=5, rating=4.7,
         total_reviews=980, min_price=9200,
         amenities='Sea View, Pool, Spa, Fine Dining, WiFi',
         description='Iconic hotel overlooking the Arabian Sea.',
         featured=True),
    dict(hotel_name='Bangalore Tech Park Suites', city='Bangalore',
         address='Whitefield, Bangalore', star_rating=4, rating=4.5,
         total_reviews=760, min_price=4500,
         amenities='Business Center, Gym, Restaurant, WiFi, Parking',
         description='Modern hotel near IT corridor.',
         featured=False),
    dict(hotel_name='Chennai Beach Resort', city='Chennai',
         address='ECR Road, Chennai', star_rating=4, rating=4.4,
         total_reviews=620, min_price=3800,
         amenities='Beach Access, Pool, Restaurant, WiFi',
         description='Relaxing beachside resort on East Coast Road.',
         featured=True),
    dict(hotel_name='Hyderabad Heritage Inn', city='Hyderabad',
         address='Banjara Hills, Hyderabad', star_rating=4, rating=4.6,
         total_reviews=840, min_price=4200,
         amenities='Rooftop Restaurant, Gym, WiFi, Parking',
         description='Elegant hotel with Nizami heritage decor.',
         featured=False),
    dict(hotel_name='Jaipur Royal Haveli', city='Jaipur',
         address='MI Road, Jaipur', star_rating=5, rating=4.9,
         total_reviews=1100, min_price=7800,
         amenities='Heritage Pool, Spa, Camel Ride, Restaurant, WiFi',
         description='Authentic Rajasthani palace hotel experience.',
         featured=True),
    dict(hotel_name='Goa Beach Shack Premium', city='Goa',
         address='Calangute Beach, Goa', star_rating=3, rating=4.3,
         total_reviews=540, min_price=2800,
         amenities='Beach Access, Bar, WiFi, Water Sports',
         description='Vibrant beach hotel steps from Calangute.',
         featured=False),
    dict(hotel_name='Pune Business Hotel', city='Pune',
         address='Koregaon Park, Pune', star_rating=4, rating=4.4,
         total_reviews=490, min_price=3500,
         amenities='Business Center, Gym, Restaurant, WiFi',
         description='Premium business hotel in Koregaon Park.',
         featured=False),
    dict(hotel_name='Kolkata Heritage Grand', city='Kolkata',
         address='Park Street, Kolkata', star_rating=5, rating=4.7,
         total_reviews=890, min_price=6500,
         amenities='Colonial Architecture, Fine Dining, Spa, WiFi',
         description='Grand colonial hotel on iconic Park Street.',
         featured=True),
    dict(hotel_name='Ahmedabad Business Inn', city='Ahmedabad',
         address='SG Highway, Ahmedabad', star_rating=3, rating=4.2,
         total_reviews=380, min_price=2200,
         amenities='Restaurant, WiFi, Parking, Gym',
         description='Comfortable business hotel on SG Highway.',
         featured=False),
    dict(hotel_name='Agra Taj View Hotel', city='Agra',
         address='Fatehabad Road, Agra', star_rating=4, rating=4.6,
         total_reviews=720, min_price=5200,
         amenities='Taj View, Pool, Restaurant, WiFi, Tour Desk',
         description='Wake up to a stunning view of the Taj Mahal.',
         featured=True),
    dict(hotel_name='Varanasi Ganga Retreat', city='Varanasi',
         address='Assi Ghat, Varanasi', star_rating=3, rating=4.5,
         total_reviews=610, min_price=2600,
         amenities='Ganga View, Yoga, Restaurant, WiFi',
         description='Spiritual retreat on the banks of the Ganges.',
         featured=True),
    dict(hotel_name='Shimla Mountain Lodge', city='Shimla',
         address='Mall Road, Shimla', star_rating=4, rating=4.7,
         total_reviews=830, min_price=4800,
         amenities='Mountain View, Fireplace, Restaurant, WiFi',
         description='Cozy mountain lodge with panoramic Himalayan views.',
         featured=True),
    dict(hotel_name='Manali Snow Peak Resort', city='Manali',
         address='Old Manali Road, Manali', star_rating=4, rating=4.8,
         total_reviews=950, min_price=5500,
         amenities='Snow View, Bonfire, Adventure Sports, Restaurant, WiFi',
         description='Premium resort surrounded by snow-capped peaks.',
         featured=True),
    dict(hotel_name='Kochi Backwater Villa', city='Kochi',
         address='Fort Kochi, Kerala', star_rating=4, rating=4.6,
         total_reviews=670, min_price=4100,
         amenities='Backwater View, Houseboat, Ayurveda Spa, Restaurant, WiFi',
         description='Serene villa with Kerala backwater experience.',
         featured=False),
    dict(hotel_name='Mysore Palace View Inn', city='Mysore',
         address='Sayyaji Rao Road, Mysore', star_rating=3, rating=4.3,
         total_reviews=420, min_price=2400,
         amenities='Palace View, Restaurant, WiFi, Parking',
         description='Budget-friendly hotel with views of Mysore Palace.',
         featured=False),
    dict(hotel_name='Udaipur Lake Palace Hotel', city='Udaipur',
         address='Lake Pichola, Udaipur', star_rating=5, rating=4.9,
         total_reviews=1380, min_price=12000,
         amenities='Lake View, Boat Ride, Spa, Fine Dining, Pool, WiFi',
         description='Iconic floating palace hotel on Lake Pichola.',
         featured=True),
    dict(hotel_name='Rishikesh Yoga Retreat', city='Rishikesh',
         address='Laxman Jhula, Rishikesh', star_rating=3, rating=4.5,
         total_reviews=560, min_price=1800,
         amenities='Yoga Hall, Ganga View, Organic Food, WiFi',
         description='Peaceful yoga and wellness retreat by the Ganges.',
         featured=False),
    dict(hotel_name='Amritsar Golden Temple Stay', city='Amritsar',
         address='Golden Temple Road, Amritsar', star_rating=3, rating=4.4,
         total_reviews=490, min_price=2100,
         amenities='Temple View, Restaurant, WiFi, Parking',
         description='Comfortable stay near the Golden Temple.',
         featured=False),
    dict(hotel_name='Surat Diamond City Hotel', city='Surat',
         address='Ring Road, Surat', star_rating=4, rating=4.3,
         total_reviews=360, min_price=3200,
         amenities='Business Center, Restaurant, Gym, WiFi, Parking',
         description='Modern hotel in the diamond city of India.',
         featured=False),
]

# ── 20 Buses ───────────────────────────────────────────────────────────────────
BUSES = [
    dict(bus_number='SR-101', bus_name='Volvo 9400 Gold',      operator_name='SR Travels', bus_type='seater', total_seats=40, amenities='AC, WiFi, USB Charging, Water Bottle', rating=4.8),
    dict(bus_number='SR-102', bus_name='Volvo 9600 Sleeper',   operator_name='SR Travels', bus_type='sleeper', total_seats=30, amenities='AC, WiFi, Blanket, Pillow, USB Charging', rating=4.7),
    dict(bus_number='SR-103', bus_name='Mercedes Tourismo',    operator_name='SR Travels', bus_type='seater', total_seats=45, amenities='AC, WiFi, Entertainment Screen, Snacks', rating=4.6),
    dict(bus_number='SR-104', bus_name='Scania Metrolink',     operator_name='SR Travels', bus_type='seater', total_seats=42, amenities='AC, WiFi, Recliner Seats, USB Charging', rating=4.5),
    dict(bus_number='SR-105', bus_name='Volvo B11R Sleeper',   operator_name='SR Travels', bus_type='sleeper', total_seats=36, amenities='AC, WiFi, Blanket, Pillow, Reading Light', rating=4.9),
    dict(bus_number='SR-106', bus_name='Scania Touring HD',    operator_name='SR Travels', bus_type='seater', total_seats=44, amenities='AC, WiFi, Panoramic Windows, USB Charging', rating=4.7),
    dict(bus_number='SR-107', bus_name='Mercedes Travego',     operator_name='SR Travels', bus_type='sleeper', total_seats=32, amenities='AC, WiFi, Luxury Berths, Blanket, Pillow', rating=4.8),
    dict(bus_number='SR-108', bus_name='Volvo 9400 Express',   operator_name='SR Travels', bus_type='seater', total_seats=40, amenities='AC, WiFi, Snacks, USB Charging', rating=4.5),
    dict(bus_number='SR-109', bus_name='Ashok Leyland Viking',  operator_name='SR Travels', bus_type='seater', total_seats=48, amenities='AC, WiFi, Recliner Seats', rating=4.3),
    dict(bus_number='SR-110', bus_name='Tata Marcopolo AC',    operator_name='SR Travels', bus_type='seater', total_seats=45, amenities='AC, WiFi, USB Charging', rating=4.4),
    dict(bus_number='SR-111', bus_name='Volvo Multi-Axle',     operator_name='SR Travels', bus_type='sleeper', total_seats=40, amenities='AC, WiFi, Semi-Sleeper, Blanket', rating=4.6),
    dict(bus_number='SR-112', bus_name='Scania K410 Sleeper',  operator_name='SR Travels', bus_type='sleeper', total_seats=34, amenities='AC, WiFi, Luxury Berths, Pillow, Blanket', rating=4.8),
    dict(bus_number='SR-113', bus_name='Mercedes Citaro',      operator_name='SR Travels', bus_type='seater', total_seats=50, amenities='AC, WiFi, USB Charging, Snacks', rating=4.4),
    dict(bus_number='SR-114', bus_name='Volvo 9700 Premium',   operator_name='SR Travels', bus_type='seater', total_seats=38, amenities='AC, WiFi, Premium Seats, Entertainment', rating=4.9),
    dict(bus_number='SR-115', bus_name='Tata Starbus Ultra',   operator_name='SR Travels', bus_type='seater', total_seats=46, amenities='AC, WiFi, USB Charging', rating=4.3),
    dict(bus_number='SR-116', bus_name='Scania Interlink',     operator_name='SR Travels', bus_type='sleeper', total_seats=36, amenities='AC, WiFi, Blanket, Pillow, Charging', rating=4.7),
    dict(bus_number='SR-117', bus_name='Volvo 9400 Night',     operator_name='SR Travels', bus_type='sleeper', total_seats=30, amenities='AC, WiFi, Luxury Berths, Blanket', rating=4.8),
    dict(bus_number='SR-118', bus_name='Mercedes Intouro',     operator_name='SR Travels', bus_type='seater', total_seats=44, amenities='AC, WiFi, Recliner, USB Charging', rating=4.5),
    dict(bus_number='SR-119', bus_name='Ashok Leyland Lynx',   operator_name='SR Travels', bus_type='seater', total_seats=42, amenities='AC, WiFi, USB Charging, Snacks', rating=4.4),
    dict(bus_number='SR-120', bus_name='Volvo 9600 Premium',   operator_name='SR Travels', bus_type='sleeper', total_seats=32, amenities='AC, WiFi, Premium Berths, Blanket, Pillow', rating=4.9),
]

# ── 20 Routes (one per bus) ────────────────────────────────────────────────────
ROUTES = [
    dict(bus_idx=0,  from_city='Delhi',     to_city='Jaipur',      dep=time(6,0),  arr=time(11,0),  dur='5h 00m', fare=450,  freq='Daily'),
    dict(bus_idx=1,  from_city='Mumbai',    to_city='Pune',        dep=time(7,30), arr=time(11,0),  dur='3h 30m', fare=350,  freq='Daily'),
    dict(bus_idx=2,  from_city='Bangalore', to_city='Chennai',     dep=time(22,0), arr=time(6,0),   dur='8h 00m', fare=600,  freq='Daily'),
    dict(bus_idx=3,  from_city='Hyderabad', to_city='Bangalore',   dep=time(20,0), arr=time(6,0),   dur='10h 00m',fare=750,  freq='Daily'),
    dict(bus_idx=4,  from_city='Delhi',     to_city='Agra',        dep=time(8,0),  arr=time(11,30), dur='3h 30m', fare=300,  freq='Daily'),
    dict(bus_idx=5,  from_city='Mumbai',    to_city='Nashik',      dep=time(9,0),  arr=time(13,0),  dur='4h 00m', fare=280,  freq='Daily'),
    dict(bus_idx=6,  from_city='Chennai',   to_city='Coimbatore',  dep=time(21,0), arr=time(5,0),   dur='8h 00m', fare=520,  freq='Daily'),
    dict(bus_idx=7,  from_city='Pune',      to_city='Goa',         dep=time(18,0), arr=time(6,0),   dur='12h 00m',fare=850,  freq='Daily'),
    dict(bus_idx=8,  from_city='Delhi',     to_city='Chandigarh',  dep=time(7,0),  arr=time(11,0),  dur='4h 00m', fare=380,  freq='Daily'),
    dict(bus_idx=9,  from_city='Kolkata',   to_city='Bhubaneswar', dep=time(22,0), arr=time(6,0),   dur='8h 00m', fare=550,  freq='Daily'),
    dict(bus_idx=10, from_city='Jaipur',    to_city='Udaipur',     dep=time(8,0),  arr=time(14,0),  dur='6h 00m', fare=480,  freq='Daily'),
    dict(bus_idx=11, from_city='Hyderabad', to_city='Chennai',     dep=time(21,30),arr=time(6,30),  dur='9h 00m', fare=680,  freq='Daily'),
    dict(bus_idx=12, from_city='Bangalore', to_city='Mysore',      dep=time(7,0),  arr=time(10,0),  dur='3h 00m', fare=250,  freq='Daily'),
    dict(bus_idx=13, from_city='Mumbai',    to_city='Ahmedabad',   dep=time(20,0), arr=time(5,0),   dur='9h 00m', fare=700,  freq='Daily'),
    dict(bus_idx=14, from_city='Delhi',     to_city='Amritsar',    dep=time(22,0), arr=time(6,0),   dur='8h 00m', fare=620,  freq='Daily'),
    dict(bus_idx=15, from_city='Chennai',   to_city='Hyderabad',   dep=time(20,0), arr=time(6,0),   dur='10h 00m',fare=720,  freq='Daily'),
    dict(bus_idx=16, from_city='Pune',      to_city='Mumbai',      dep=time(6,0),  arr=time(9,30),  dur='3h 30m', fare=320,  freq='Daily'),
    dict(bus_idx=17, from_city='Kolkata',   to_city='Patna',       dep=time(21,0), arr=time(5,0),   dur='8h 00m', fare=580,  freq='Daily'),
    dict(bus_idx=18, from_city='Ahmedabad', to_city='Surat',       dep=time(8,0),  arr=time(11,30), dur='3h 30m', fare=280,  freq='Daily'),
    dict(bus_idx=19, from_city='Delhi',     to_city='Lucknow',     dep=time(21,0), arr=time(5,0),   dur='8h 00m', fare=560,  freq='Daily'),
]

# ── GPS tracking locations ─────────────────────────────────────────────────────
TRACKING = [
    (0,  28.6139, 77.2090, 'Delhi - NH48',              65, 'moving'),
    (1,  19.0760, 72.8777, 'Mumbai - Western Expressway',80, 'moving'),
    (2,  12.9716, 77.5946, 'Bangalore - Hosur Road',     0,  'stopped'),
    (3,  17.3850, 78.4867, 'Hyderabad - ORR',            90, 'moving'),
    (4,  27.1767, 78.0081, 'Agra - NH19',                70, 'moving'),
    (5,  20.0059, 73.7797, 'Nashik - Mumbai Highway',    75, 'moving'),
    (6,  11.0168, 76.9558, 'Coimbatore - NH544',         60, 'moving'),
    (7,  15.4909, 73.8278, 'Goa - NH66',                 55, 'moving'),
    (8,  30.7333, 76.7794, 'Chandigarh - NH44',          80, 'moving'),
    (9,  20.2961, 85.8245, 'Bhubaneswar - NH16',         70, 'moving'),
    (10, 24.5854, 73.7125, 'Udaipur - NH48',             65, 'moving'),
    (11, 13.0827, 80.2707, 'Chennai - NH16',             85, 'moving'),
    (12, 12.2958, 76.6394, 'Mysore - NH275',             60, 'moving'),
    (13, 23.0225, 72.5714, 'Ahmedabad - NH48',           75, 'moving'),
    (14, 31.6340, 74.8723, 'Amritsar - NH44',            70, 'moving'),
    (15, 17.6868, 83.2185, 'Visakhapatnam - NH16',       80, 'moving'),
    (16, 18.5204, 73.8567, 'Pune - Mumbai Expressway',   90, 'moving'),
    (17, 25.5941, 85.1376, 'Patna - NH19',               65, 'moving'),
    (18, 21.1702, 72.8311, 'Surat - NH48',               70, 'moving'),
    (19, 26.8467, 80.9462, 'Lucknow - NH27',             75, 'moving'),
]


# ── Run seeding ────────────────────────────────────────────────────────────────
with app.app_context():

    # Hotels
    added_hotels = 0
    for h in HOTELS:
        if not Hotel.query.filter_by(hotel_name=h['hotel_name']).first():
            db.session.add(Hotel(**h, status='active'))
            added_hotels += 1
    db.session.commit()
    print(f"✅ {added_hotels} hotels added.")

    # Buses
    bus_objects = []
    added_buses = 0
    for b in BUSES:
        existing = Bus.query.filter_by(bus_number=b['bus_number']).first()
        if existing:
            bus_objects.append(existing)
        else:
            bus = Bus(
                bus_number=b['bus_number'],
                bus_name=b['bus_name'],
                operator_name=b['operator_name'],
                bus_type=b['bus_type'],
                total_seats=b['total_seats'],
                available_seats=b['total_seats'],
                amenities=b['amenities'],
                rating=b['rating'],
                total_reviews=0,
                status='active',
            )
            db.session.add(bus)
            db.session.flush()
            bus_objects.append(bus)
            added_buses += 1
    db.session.commit()
    print(f"✅ {added_buses} buses added.")

    # Routes
    added_routes = 0
    for r in ROUTES:
        idx = r['bus_idx']
        if idx >= len(bus_objects):
            continue
        bus = bus_objects[idx]
        if not BusRoute.query.filter_by(bus_id=bus.id, from_city=r['from_city'], to_city=r['to_city']).first():
            db.session.add(BusRoute(
                bus_id=bus.id,
                from_city=r['from_city'], to_city=r['to_city'],
                departure_time=r['dep'], arrival_time=r['arr'],
                duration=r['dur'], fare=r['fare'], frequency=r['freq'],
            ))
            added_routes += 1
    db.session.commit()
    print(f"✅ {added_routes} routes added.")

    # GPS Tracking
    added_tracking = 0
    for t in TRACKING:
        idx, lat, lng, loc, spd, status = t
        if idx >= len(bus_objects):
            continue
        bus = bus_objects[idx]
        if not BusTracking.query.filter_by(bus_id=bus.id).first():
            db.session.add(BusTracking(
                bus_id=bus.id,
                current_latitude=lat, current_longitude=lng,
                current_location=loc, speed=spd, status=status,
            ))
            added_tracking += 1
    db.session.commit()
    print(f"✅ {added_tracking} GPS tracking records added.")

    print("\n🎉 Seeding complete!")
    print(f"   Total hotels in DB : {Hotel.query.count()}")
    print(f"   Total buses in DB  : {Bus.query.count()}")
    print(f"   Total routes in DB : {BusRoute.query.count()}")

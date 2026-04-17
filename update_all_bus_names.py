"""
Update all buses with real Indian bus operator names.
Run: py update_all_bus_names.py
"""
from app import create_app, db
from app.models import Bus

app = create_app()

REAL_BUS_NAMES = [
    # Premium / National operators
    ('VRL Travels',                'seater',  'AC, WiFi, USB Charging, Water Bottle',     4.7),
    ('Neeta Tours & Travels',      'sleeper', 'AC, WiFi, Blanket, Pillow, USB Charging',  4.8),
    ('Orange Tours & Travels',     'seater',  'AC, WiFi, Entertainment, Snacks',           4.6),
    ('SRS Travels',                'sleeper', 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.7),
    ('Paulo Travels',              'sleeper', 'AC, WiFi, Premium Berths, Blanket',        4.6),
    ('Purple Bus',                 'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.5),
    ('Sharma Transports',          'seater',  'AC, WiFi, USB Charging',                   4.4),
    ('Citizen Travels',            'seater',  'AC, WiFi, Recliner Seats',                 4.3),
    ('IntrCity SmartBus',          'seater',  'AC, WiFi, USB Charging, Snacks',           4.6),
    ('National Travels',           'sleeper', 'AC, WiFi, Blanket, Pillow',                4.5),
    ('Konduskar Travels',          'sleeper', 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.8),
    ('Sai Travels',                'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Jakhar Travels',             'sleeper', 'AC, WiFi, Blanket, Pillow',                4.4),
    ('Mahadev Travels',            'seater',  'AC, WiFi, Recliner Seats',                 4.3),
    ('Shree Patel Travels',        'sleeper', 'AC, WiFi, Premium Berths, Blanket',        4.5),
    ('Gujarat Travels',            'seater',  'AC, WiFi, USB Charging, Water Bottle',     4.4),
    ('Shree Balaji Travels',       'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.4),
    ('Ravi Travels',               'sleeper', 'AC, WiFi, Blanket, Pillow',                4.5),
    ('Manish Travels',             'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Sangitam Travels',           'sleeper', 'AC, WiFi, Luxury Berths, Blanket',         4.5),
    ('Shree Krishna Travels',      'seater',  'AC, WiFi, Recliner Seats',                 4.4),
    ('N.T. Travels',               'sleeper', 'AC, WiFi, Blanket, Pillow, USB Charging',  4.5),
    ('Seabird Tourist',            'seater',  'AC, WiFi, USB Charging, Snacks',           4.4),
    ('Prasanna Purple Mobility',   'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.6),
    ('Jain Travels',               'sleeper', 'AC, WiFi, Blanket, Pillow',                4.4),
    ('Shree Vijay Travels',        'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Rathore Travels',            'sleeper', 'AC, WiFi, Luxury Berths, Blanket',         4.5),
    ('Maharaja Travels',           'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.5),
    ('Ganesh Travels',             'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Kaveri Travels',             'sleeper', 'AC, WiFi, Blanket, Pillow',                4.5),
    ('Morning Star Travels',       'seater',  'AC, WiFi, Recliner Seats',                 4.4),
    ('Royal Travels',              'sleeper', 'AC, WiFi, Premium Berths, Blanket',        4.6),
    ('National Parivahan',         'seater',  'AC, WiFi, USB Charging, Water Bottle',     4.4),
    ('Sundesha Travels',           'sleeper', 'AC, WiFi, Blanket, Pillow',                4.4),
    ('Shree Maruti Travels',       'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.4),
    ('Balaji Travels',             'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('KPN Travels',                'sleeper', 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.7),
    ('SVR Travels',                'seater',  'AC, WiFi, Recliner Seats',                 4.4),
    ('Komitla Travels',            'sleeper', 'AC, WiFi, Blanket, Pillow',                4.4),
    ('Shivam Travels',             'seater',  'AC, WiFi, USB Charging, Snacks',           4.4),
    ('Raj Travels',                'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.4),
    ('Citylink Travels',           'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Global Travels',             'sleeper', 'AC, WiFi, Luxury Berths, Blanket',         4.5),
    ('Vikas Travels',              'seater',  'AC, WiFi, Recliner Seats',                 4.3),
    ('Sai Krishna Travels',        'sleeper', 'AC, WiFi, Blanket, Pillow, USB Charging',  4.5),
    ('Yolo Bus',                   'seater',  'AC, WiFi, USB Charging, Entertainment',    4.5),
    ('Zingbus',                    'seater',  'AC, WiFi, USB Charging, Snacks',           4.6),
    ('AbhiBus Travels',            'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.5),
    ('TNT Travels',                'sleeper', 'AC, WiFi, Blanket, Pillow',                4.4),
    # More operators to fill remaining buses
    ('KSRTC Airavat',              'seater',  'AC, WiFi, USB Charging, Water Bottle',     4.7),
    ('MSRTC Shivneri',             'seater',  'AC, WiFi, USB Charging',                   4.6),
    ('TSRTC Garuda Plus',          'seater',  'AC, WiFi, Recliner Seats',                 4.5),
    ('APSRTC Indra',               'seater',  'AC, WiFi, USB Charging',                   4.4),
    ('Parveen Travels',            'sleeper', 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.6),
    ('Chartered Bus',              'seater',  'AC, WiFi, USB Charging, Snacks',           4.5),
    ('Raj National Express',       'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.5),
    ('Shrinath Travel Agency',     'sleeper', 'AC, WiFi, Blanket, Pillow',                4.6),
    ('Sugama Tourist',             'seater',  'AC, WiFi, USB Charging',                   4.4),
    ('Jabbar Travels',             'sleeper', 'AC, WiFi, Luxury Berths, Blanket',         4.5),
    ('Kesineni Travels',           'seater',  'AC, WiFi, Recliner Seats',                 4.5),
    ('Vijay Travels',              'seater',  'AC, WiFi, USB Charging, Snacks',           4.4),
    ('Dolphin Travels',            'sleeper', 'AC, WiFi, Blanket, Pillow, USB Charging',  4.5),
    ('Patel Travels',              'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.4),
    ('Khushbu Travels',            'seater',  'AC, WiFi, USB Charging',                   4.3),
    ('Sidhanath Travels',          'sleeper', 'AC, WiFi, Premium Berths, Blanket',        4.5),
    ('Om Sai Link Travels',        'seater',  'AC, WiFi, USB Charging, Snacks',           4.3),
    ('Shreyash Travels',           'seater',  'AC, WiFi, Recliner Seats',                 4.3),
    ('MB Link Travels',            'seater',  'AC, WiFi, USB Charging',                   4.4),
    ('Ashoka Travels',             'seater',  'AC, WiFi, Recliner Seats, USB Charging',   4.5),
]

with app.app_context():
    buses = Bus.query.order_by(Bus.id).all()
    total = len(buses)
    updated = 0

    for i, bus in enumerate(buses):
        op = REAL_BUS_NAMES[i % len(REAL_BUS_NAMES)]
        name, btype, amenities, rating = op
        bus.bus_name = name
        bus.operator_name = name
        bus.amenities = amenities
        bus.rating = rating
        updated += 1

    db.session.commit()
    print(f'✅ Updated {updated}/{total} buses with real operator names.')
    print(f'\nSample buses:')
    for b in Bus.query.order_by(Bus.id).limit(15).all():
        print(f'  {b.bus_number:12} | {b.bus_name}')

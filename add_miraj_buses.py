"""
Add specific Miraj bus operators with routes.
Run: py add_miraj_buses.py
"""
import math
from datetime import time
from app import create_app, db
from app.models import Bus, BusRoute, BusTracking
from sqlalchemy import text

app = create_app()

# Miraj specific bus operators
MIRAJ_BUSES = [
    ('Ashoka Travels Miraj',       'seater',  42, 'AC, WiFi, USB Charging, Water Bottle',     4.5),
    ('MB Link Travels',            'seater',  45, 'AC, WiFi, Recliner Seats, USB Charging',   4.4),
    ('Konduskar Travels Miraj',    'sleeper', 34, 'AC, WiFi, Luxury Berths, Pillow, Blanket', 4.8),
    ('Shreyash Travels',           'seater',  40, 'AC, WiFi, USB Charging',                   4.3),
    ('Balaji Travels Miraj',       'seater',  44, 'AC, WiFi, Recliner Seats',                 4.4),
    ('Sidhanath Travels',          'sleeper', 32, 'AC, WiFi, Premium Berths, Blanket',        4.5),
    ('Om Sai Link Travels',        'seater',  42, 'AC, WiFi, USB Charging, Snacks',           4.3),
    ('Dolphin Travels Miraj',      'sleeper', 36, 'AC, WiFi, Luxury Berths, Blanket',         4.6),
    ('Raj Travels Miraj',          'seater',  45, 'AC, WiFi, USB Charging',                   4.4),
    ('Sharma Travels Miraj',       'seater',  40, 'AC, WiFi, Recliner Seats',                 4.3),
    ('Patel Travels Miraj',        'sleeper', 30, 'AC, WiFi, Blanket, Pillow, USB Charging',  4.5),
    ('Khushbu Travels',            'seater',  42, 'AC, WiFi, USB Charging, Water Bottle',     4.3),
    ('Om Travels Miraj',           'seater',  44, 'AC, WiFi, Recliner Seats, USB Charging',   4.4),
]

# Miraj routes to nearby cities
MIRAJ_ROUTES = [
    ('Miraj', 'Sangli',      time(6,0),  time(6,30),  '0h 30m', 80),
    ('Miraj', 'Kolhapur',    time(7,0),  time(8,30),  '1h 30m', 150),
    ('Miraj', 'Pune',        time(6,0),  time(10,0),  '4h 00m', 350),
    ('Miraj', 'Mumbai',      time(20,0), time(6,0),   '10h 00m',700),
    ('Miraj', 'Solapur',     time(8,0),  time(12,0),  '4h 00m', 320),
    ('Miraj', 'Satara',      time(7,0),  time(10,0),  '3h 00m', 250),
    ('Miraj', 'Nashik',      time(21,0), time(5,0),   '8h 00m', 580),
    ('Miraj', 'Nagpur',      time(20,0), time(8,0),   '12h 00m',900),
    ('Miraj', 'Hyderabad',   time(19,0), time(7,0),   '12h 00m',850),
    ('Miraj', 'Bangalore',   time(18,0), time(8,0),   '14h 00m',1100),
    ('Miraj', 'Goa',         time(20,0), time(6,0),   '10h 00m',750),
    ('Miraj', 'Aurangabad',  time(21,0), time(5,0),   '8h 00m', 600),
    ('Miraj', 'Latur',       time(8,0),  time(14,0),  '6h 00m', 480),
    ('Miraj', 'Nanded',      time(9,0),  time(17,0),  '8h 00m', 580),
]

with app.app_context():
    row = db.session.execute(
        text("SELECT MAX(CAST(SUBSTRING(bus_number,4) AS UNSIGNED)) FROM buses WHERE bus_number LIKE 'SR-%'")
    ).scalar()
    bus_num = (row or 2000) + 1

    added_buses = 0
    added_routes = 0

    for i, (bname, btype, seats, amenities, rating) in enumerate(MIRAJ_BUSES):
        bnum = f'SR-{bus_num}'
        bus_num += 1
        bus = Bus(
            bus_number=bnum,
            bus_name=bname,
            operator_name=bname.split(' ')[0] + ' Travels',
            bus_type=btype,
            total_seats=seats,
            available_seats=seats,
            amenities=amenities,
            rating=rating,
            total_reviews=0,
            status='active'
        )
        db.session.add(bus)
        db.session.flush()
        added_buses += 1

        # GPS tracking for Miraj
        db.session.add(BusTracking(
            bus_id=bus.id,
            current_latitude=round(16.8267 + i * 0.003, 4),
            current_longitude=round(74.6455 + i * 0.003, 4),
            current_location=f'Miraj Bus Stand - {bname}',
            speed=0,
            status='stopped'
        ))

        # Assign routes to this bus (cycle through routes)
        route_idx = i % len(MIRAJ_ROUTES)
        fc, tc, dep, arr, dur, fare = MIRAJ_ROUTES[route_idx]

        if not BusRoute.query.filter_by(bus_id=bus.id, from_city=fc, to_city=tc).first():
            db.session.add(BusRoute(
                bus_id=bus.id,
                from_city=fc, to_city=tc,
                departure_time=dep, arrival_time=arr,
                duration=dur, fare=fare, frequency='Daily'
            ))
            added_routes += 1

    db.session.commit()

    # Also add return routes (Sangli/Kolhapur/Pune → Miraj)
    return_routes = [
        ('Sangli',     'Miraj', time(7,0),  time(7,30),  '0h 30m', 80),
        ('Kolhapur',   'Miraj', time(9,0),  time(10,30), '1h 30m', 150),
        ('Pune',       'Miraj', time(14,0), time(18,0),  '4h 00m', 350),
        ('Mumbai',     'Miraj', time(20,0), time(6,0),   '10h 00m',700),
        ('Solapur',    'Miraj', time(14,0), time(18,0),  '4h 00m', 320),
        ('Satara',     'Miraj', time(13,0), time(16,0),  '3h 00m', 250),
        ('Nashik',     'Miraj', time(20,0), time(4,0),   '8h 00m', 580),
        ('Nagpur',     'Miraj', time(18,0), time(6,0),   '12h 00m',900),
        ('Hyderabad',  'Miraj', time(18,0), time(6,0),   '12h 00m',850),
        ('Bangalore',  'Miraj', time(16,0), time(6,0),   '14h 00m',1100),
        ('Goa',        'Miraj', time(18,0), time(4,0),   '10h 00m',750),
        ('Aurangabad', 'Miraj', time(20,0), time(4,0),   '8h 00m', 600),
        ('Latur',      'Miraj', time(14,0), time(20,0),  '6h 00m', 480),
    ]

    # Use existing Miraj buses for return routes
    miraj_buses = Bus.query.filter(Bus.bus_name.like('%Miraj%') | Bus.bus_name.like('%Konduskar%') | Bus.bus_name.like('%Ashoka%')).all()

    for j, (fc, tc, dep, arr, dur, fare) in enumerate(return_routes):
        if miraj_buses:
            bus = miraj_buses[j % len(miraj_buses)]
            if not BusRoute.query.filter_by(bus_id=bus.id, from_city=fc, to_city=tc).first():
                db.session.add(BusRoute(
                    bus_id=bus.id,
                    from_city=fc, to_city=tc,
                    departure_time=dep, arrival_time=arr,
                    duration=dur, fare=fare, frequency='Daily'
                ))
                added_routes += 1

    db.session.commit()

    print(f'✅ Miraj buses added!')
    print(f'   Buses added  : {added_buses}')
    print(f'   Routes added : {added_routes}')
    print(f'\n   Operators:')
    for b in MIRAJ_BUSES:
        print(f'   - {b[0]}')

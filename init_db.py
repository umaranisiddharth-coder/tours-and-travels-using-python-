"""
Run once to create all tables and seed sample data.
Usage: python init_db.py
"""
from app import create_app, db
from app.models import User, Bus, BusRoute, BusTracking
from datetime import time

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ All tables created.")

    # ── Admin user ──────────────────────────────────────────────────────────────
    if not User.query.filter_by(email='admin@srtravels.com').first():
        admin = User(
            username='admin',
            email='admin@srtravels.com',
            full_name='SR Travels Admin',
            phone='+91-9876543210',
            user_type='admin',
            status='active',
        )
        admin.set_password('Admin@123')
        db.session.add(admin)
        print("✅ Admin created: admin@srtravels.com / Admin@123")

    # ── Sample buses ────────────────────────────────────────────────────────────
    buses_data = [
        dict(bus_number='SR-001', bus_name='Volvo Gold Express', operator_name='SR Travels',
             bus_type='seater', total_seats=40, available_seats=40,
             amenities='AC, WiFi, Charging Point, Water Bottle', rating=4.8, total_reviews=320),
        dict(bus_number='SR-002', bus_name='Mercedes Sleeper Deluxe', operator_name='SR Travels',
             bus_type='sleeper', total_seats=30, available_seats=30,
             amenities='AC, WiFi, Blanket, Pillow, Charging Point', rating=4.6, total_reviews=210),
        dict(bus_number='SR-003', bus_name='Scania Multi-Axle', operator_name='SR Travels',
             bus_type='seater', total_seats=45, available_seats=45,
             amenities='AC, WiFi, Entertainment Screen', rating=4.5, total_reviews=180),
        dict(bus_number='SR-004', bus_name='Volvo Sleeper Premium', operator_name='SR Travels',
             bus_type='sleeper', total_seats=36, available_seats=36,
             amenities='AC, WiFi, Blanket, Pillow, USB Charging', rating=4.7, total_reviews=260),
    ]
    created_buses = []
    for bd in buses_data:
        if not Bus.query.filter_by(bus_number=bd['bus_number']).first():
            bus = Bus(**bd)
            db.session.add(bus)
            db.session.flush()
            created_buses.append(bus)
            print(f"✅ Bus added: {bd['bus_name']}")
        else:
            created_buses.append(Bus.query.filter_by(bus_number=bd['bus_number']).first())

    # ── Sample routes ───────────────────────────────────────────────────────────
    routes_data = [
        dict(bus_idx=0, from_city='Delhi', to_city='Jaipur',
             departure_time=time(6, 0), arrival_time=time(11, 0), duration='5h 00m', fare=450),
        dict(bus_idx=1, from_city='Mumbai', to_city='Pune',
             departure_time=time(7, 30), arrival_time=time(11, 0), duration='3h 30m', fare=350),
        dict(bus_idx=2, from_city='Bangalore', to_city='Chennai',
             departure_time=time(22, 0), arrival_time=time(6, 0), duration='8h 00m', fare=600),
        dict(bus_idx=3, from_city='Hyderabad', to_city='Bangalore',
             departure_time=time(20, 0), arrival_time=time(6, 0), duration='10h 00m', fare=750),
        dict(bus_idx=0, from_city='Delhi', to_city='Agra',
             departure_time=time(8, 0), arrival_time=time(11, 30), duration='3h 30m', fare=300),
        dict(bus_idx=1, from_city='Mumbai', to_city='Nashik',
             departure_time=time(9, 0), arrival_time=time(13, 0), duration='4h 00m', fare=280),
        dict(bus_idx=2, from_city='Chennai', to_city='Coimbatore',
             departure_time=time(21, 0), arrival_time=time(5, 0), duration='8h 00m', fare=520),
        dict(bus_idx=3, from_city='Pune', to_city='Goa',
             departure_time=time(18, 0), arrival_time=time(6, 0), duration='12h 00m', fare=850),
    ]
    for rd in routes_data:
        bus = created_buses[rd['bus_idx']] if rd['bus_idx'] < len(created_buses) else None
        if bus and not BusRoute.query.filter_by(
            bus_id=bus.id, from_city=rd['from_city'], to_city=rd['to_city']
        ).first():
            route = BusRoute(
                bus_id=bus.id,
                from_city=rd['from_city'], to_city=rd['to_city'],
                departure_time=rd['departure_time'], arrival_time=rd['arrival_time'],
                duration=rd['duration'], fare=rd['fare'], frequency='Daily',
            )
            db.session.add(route)
            print(f"✅ Route: {rd['from_city']} → {rd['to_city']} ₹{rd['fare']}")

    # ── GPS tracking for buses ──────────────────────────────────────────────────
    tracking_data = [
        dict(bus_idx=0, lat=28.6139, lng=77.2090, location='Delhi - NH48', speed=65, status='moving'),
        dict(bus_idx=1, lat=19.0760, lng=72.8777, location='Mumbai - Expressway', speed=80, status='moving'),
        dict(bus_idx=2, lat=12.9716, lng=77.5946, location='Bangalore - Hosur Road', speed=0, status='stopped'),
        dict(bus_idx=3, lat=17.3850, lng=78.4867, location='Hyderabad - ORR', speed=90, status='moving'),
    ]
    for td in tracking_data:
        bus = created_buses[td['bus_idx']] if td['bus_idx'] < len(created_buses) else None
        if bus and not BusTracking.query.filter_by(bus_id=bus.id).first():
            tracking = BusTracking(
                bus_id=bus.id,
                current_latitude=td['lat'], current_longitude=td['lng'],
                current_location=td['location'], speed=td['speed'], status=td['status'],
            )
            db.session.add(tracking)

    db.session.commit()
    print("\n🚌 SR Travels Python app is ready!")
    print("   Admin login: admin@srtravels.com / Admin@123")
    print("   Run with:    python run.py")
    print("   Open:        http://localhost:5000")

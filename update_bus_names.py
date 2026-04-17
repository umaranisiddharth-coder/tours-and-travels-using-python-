"""
Update all bus names to real Indian bus operator names.
Run: py update_bus_names.py
"""
from app import create_app, db
from app.models import Bus

app = create_app()

# Real Indian bus operator names cycling through all buses
INDIAN_BUS_NAMES = [
    # Premium Volvo operators
    "VRL Travels Volvo AC",
    "SRS Travels Volvo Sleeper",
    "Orange Tours Volvo AC",
    "Parveen Travels Volvo",
    "KSRTC Airavat Club Class",
    "MSRTC Shivneri AC",
    "TSRTC Garuda Plus",
    "APSRTC Indra AC",
    "KPN Travels Volvo",
    "Chartered Bus Volvo AC",
    # Sleeper operators
    "Neeta Tours Sleeper",
    "Raj National Express",
    "National Travels Sleeper",
    "Kallada Travels AC Sleeper",
    "Paulo Travels Sleeper",
    "Sugama Tourist Sleeper",
    "Jabbar Travels Sleeper",
    "Konduskar Travels Sleeper",
    "Shrinath Travel Agency",
    "Prasanna Purple Sleeper",
    # Semi-sleeper / seater
    "GSRTC Volvo AC",
    "HRTC Himachal Volvo",
    "UPSRTC Jan Rath AC",
    "RSRTC Rajasthan Volvo",
    "BSRTC Bihar Sampark",
    "Greenline Travels AC",
    "Dolphin Travels AC",
    "Sharma Transports AC",
    "Intercity Smart Bus",
    "Zingbus Premium AC",
    # More operators
    "IntrCity SmartBus",
    "Wohoo Bus AC",
    "Bharat Benz AC",
    "Kesineni Travels",
    "Vijay Travels AC",
    "Seabird Tourist Bus",
    "Shree Sai Travels",
    "Mahalaxmi Travels",
    "Shivam Travels AC",
    "Balaji Travels AC",
    "Patel Travels Volvo",
    "Gajanan Travels AC",
    "Swaraj Travels AC",
    "Agarwal Travels AC",
    "Rathi Travels Volvo",
    "Hanuman Travels AC",
    "Durga Travels AC",
    "Ganesh Travels AC",
    "Shiva Travels AC",
    "Laxmi Travels AC",
    "Saibaba Travels AC",
    "Tirupati Travels AC",
    "Venkateswara Travels",
    "Balaji Bus Service",
    "Sri Sai Travels AC",
    "Kaveri Travels AC",
    "Cauvery Travels AC",
    "Godavari Travels AC",
    "Krishna Travels AC",
    "Ganga Travels AC",
    "Yamuna Travels AC",
    "Narmada Travels AC",
    "Tapti Travels AC",
    "Mahanadi Travels AC",
    "Brahmaputra Travels",
    "Indus Travels AC",
    "Sabarmati Travels AC",
    "Chambal Travels AC",
    "Betwa Travels AC",
    "Ken Travels AC",
    "Son Travels AC",
    "Damodar Travels AC",
    "Subarnarekha Travels",
    "Baitarani Travels AC",
    "Rushikulya Travels",
    "Vamsadhara Travels",
    "Nagavali Travels AC",
    "Sileru Travels AC",
    "Machkund Travels AC",
    "Kolab Travels AC",
    "Indravati Travels AC",
    "Jonk Travels AC",
    "Hasdeo Travels AC",
    "Mand Travels AC",
    "Ib Travels AC",
    "Brahmani Travels AC",
    "Koel Travels AC",
    "Sankh Travels AC",
    "North Koel Travels",
    "Auranga Travels AC",
    "Falgu Travels AC",
    "Punpun Travels AC",
    "Sone Travels AC",
    "Karmanasa Travels",
    "Tons Travels AC",
    "Rihand Travels AC",
    "Kanhar Travels AC",
    "Banas Travels AC",
    "Berach Travels AC",
    "Gambhiri Travels AC",
]

with app.app_context():
    buses = Bus.query.order_by(Bus.id).all()
    total = len(buses)
    updated = 0

    for i, bus in enumerate(buses):
        new_name = INDIAN_BUS_NAMES[i % len(INDIAN_BUS_NAMES)]
        bus.bus_name = new_name
        bus.operator_name = new_name.split(' ')[0] + ' Travels'
        updated += 1

    db.session.commit()
    print(f"Updated {updated}/{total} buses with Indian names.")
    print("\nSample:")
    for b in Bus.query.order_by(Bus.id).limit(10).all():
        print(f"  {b.bus_number} | {b.bus_name} | {b.bus_type}")

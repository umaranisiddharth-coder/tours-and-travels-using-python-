"""All Bus Images in ONE File — assigns images to all buses by operator name."""
from app import create_app, db
from app.models import Bus

app = chttpsreate_app()

BUS_IMAGES = {
    # --- Your exact list ---
    "VRL Travels":              "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/VRL_Travels_Volvo_Bus.jpg/640px-VRL_Travels_Volvo_Bus.jpg",
    "Neeta Travels":            "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Neeta_Travels_Bus.jpg/640px-Neeta_Travels_Bus.jpg",
    "Orange Travels":           "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800",
    "SRS Travels":              "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800",
    "Paulo Travels":            "https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800",
    "Purple Bus":               "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
    "Sharma Travels":           "https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800",
    "Citizen Travels":          "https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800",
    "IntrCity SmartBus":        "https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800",
    "National Travels":         "https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800",
    "Konduskar Travels":        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Konduskar_Travels.jpg/640px-Konduskar_Travels.jpg",
    "Sai Travels":              "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800",
    "Jakhar Travels":           "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800",
    "Mahadev Travels":          "https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800",
    "Shree Patel Travels":      "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800",
    "Gujarat Travels":          "https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800",
    "Shree Balaji Travels":     "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800",
    "Ravi Travels":             "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    "Manish Travels":           "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800",
    "Sangitam Travels":         "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800",
    "Shree Krishna Travels":    "https://images.unsplash.com/photo-1553440569-bcc63803a83d?w=800",
    "N.T. Travels":             "https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800",
    "Seabird Travels":          "https://images.unsplash.com/photo-1586201375761-83865001e8ac?w=800",
    "Prasanna Purple Mobility": "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800",
    "Jain Travels":             "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800",
    "Shree Vijay Travels":      "https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800",
    "Rathore Travels":          "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
    "Maharaja Travels":         "https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800",
    "Ganesh Travels":           "https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800",
    "Kaveri Travels":           "https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800",
    "Morning Star Travels":     "https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800",
    "Royal Travels":            "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800",
    "National Parivahan":       "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800",
    "Sundesha Travels":         "https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800",
    "Shree Maruti Travels":     "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800",
    "Balaji Travels":           "https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800",
    "KPN Travels":              "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/KPN_Travels_Bus.jpg/640px-KPN_Travels_Bus.jpg",
    "SVR Travels":              "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800",
    "Komitla Travels":          "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    "Shivam Travels":           "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800",
    "Raj Travels":              "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800",
    "Citylink Travels":         "https://images.unsplash.com/photo-1553440569-bcc63803a83d?w=800",
    "Global Travels":           "https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800",
    "Vikas Travels":            "https://images.unsplash.com/photo-1586201375761-83865001e8ac?w=800",
    "Sai Krishna Travels":      "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800",
    "Yolo Bus":                 "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800",
    "Zingbus":                  "https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800",
    "AbhiBus Travels":          "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
    "TNT Travels":              "https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800",
    # --- DB name aliases (update_all_bus_names.py uses these) ---
    "Neeta Tours & Travels":    "://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Neeta_Travels_Bus.jpg/640px-Neeta_Travels_Bus.jpg",
    "Orange Tours & Travels":   "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800",
    "Sharma Transports":        "https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800",
    "Seabird Tourist":          "https://images.unsplash.com/photo-1586201375761-83865001e8ac?w=800",
    # --- Extra operators from seeding ---
    "KSRTC Airavat":            "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/KSRTC_Airavat_Club_Class.jpg/640px-KSRTC_Airavat_Club_Class.jpg",
    "MSRTC Shivneri":           "https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800",
    "TSRTC Garuda Plus":        "https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800",
    "APSRTC Indra":             "https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800",
    "Parveen Travels":          "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800",
    "Chartered Bus":            "https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800",
    "Raj National Express":     "https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800",
    "Shrinath Travel Agency":   "https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800",
    "Sugama Tourist":           "https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800",
    "Jabbar Travels":           "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800",
    "Kesineni Travels":         "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800",
    "Vijay Travels":            "https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800",
    "Dolphin Travels":          "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800",
    "Patel Travels":            "https://images.unsplash.com/photo-1553440569-bcc63803a83d?w=800",
    "Khushbu Travels":          "https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800",
    "Sidhanath Travels":        "https://images.unsplash.com/photo-1586201375761-83865001e8ac?w=800",
    "Om Sai Link Travels":      "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800",
    "Shreyash Travels":         "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800",
    "MB Link Travels":          "https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800",
    "Ashoka Travels":           "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800",
}

DEFAULT_BUS_IMAGE = "https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800"


def get_bus_image(bus_name):
    return BUS_IMAGES.get(bus_name, DEFAULT_BUS_IMAGE)


with app.app_context():
    buses = Bus.query.order_by(Bus.id).all()
    updated = matched = 0

    for bus in buses:
        img = BUS_IMAGES.get(bus.bus_name)
        if img:
            bus.image = img
            matched += 1
        else:
            bus.image = DEFAULT_BUS_IMAGE
        updated += 1

    db.session.commit()
    print(f'✅ {updated} buses updated  |  {matched} matched to operator image  |  {updated - matched} used default')
    print('\nSample:')
    for b in Bus.query.order_by(Bus.id).limit(10).all():
        print(f'  {b.bus_name:30} | {(b.image or "")[:60]}')

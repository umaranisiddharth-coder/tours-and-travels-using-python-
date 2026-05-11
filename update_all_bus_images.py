"""
Update bus images for all operators with stable, working image URLs.
Uses Unsplash (always available) + Wikipedia (stable) + official sites.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from app import create_app, db
from app.models import Bus

# ── Stable image pools ─────────────────────────────────────────────────────────
# Unsplash bus images — always available, high quality
SEATER = [
    'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
    'https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800&q=80',
    'https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800&q=80',
    'https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800&q=80',
    'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
    'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
    'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',
    'https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800&q=80',
]
SLEEPER = [
    'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800&q=80',
    'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
    'https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800&q=80',
    'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80',
    'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800&q=80',
    'https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800&q=80',
    'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80',
    'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800&q=80',
    'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
]

# ── Operator-specific images (manually verified, stable URLs) ──────────────────
# Already set manually — keep these exact
KEEP_AS_IS = ['vrl', 'neeta', 'sugama', 'balaji', 'shree balaji']

# Operator keyword → stable image URL
IMAGE_MAP = {
    # State transport corporations
    'msrtc':        'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/MSRTC_Shivshahi_Bus.jpg/640px-MSRTC_Shivshahi_Bus.jpg',
    'shivneri':     'https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/MSRTC_Shivshahi_Bus.jpg/640px-MSRTC_Shivshahi_Bus.jpg',
    'ksrtc':        'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/KSRTC_Airavata_Club_Class.jpg/640px-KSRTC_Airavata_Club_Class.jpg',
    'airavat':      'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/KSRTC_Airavata_Club_Class.jpg/640px-KSRTC_Airavata_Club_Class.jpg',
    'apsrtc':       'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'tsrtc':        'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',
    'garuda':       'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',

    # Major private operators
    'konduskar':    'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/Konduskar_Travels.jpg/640px-Konduskar_Travels.jpg',
    'orange':       'https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800&q=80',
    'srs':          'https://images.unsplash.com/photo-1544620347-c4fd4a3d5957?w=800&q=80',
    'paulo':        'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'purple':       'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800&q=80',
    'prasanna':     'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800&q=80',
    'kpn':          'https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800&q=80',
    'parveen':      'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
    'intracity':    'https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800&q=80',
    'zingbus':      'https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800&q=80',
    'yolo':         'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
    'chartered':    'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
    'kesineni':     'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'kaveri':       'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',
    'jabbar':       'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80',
    'dolphin':      'https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800&q=80',
    'seabird':      'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
    'svr':          'https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800&q=80',
    'abhibus':      'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80',
    'citylink':     'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800&q=80',
    'mb link':      'https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800&q=80',
    'morning star': 'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'national parivahan': 'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
    'om sai':       'https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800&q=80',
    'komitla':      'https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800&q=80',
    'sundesha':     'https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800&q=80',
    'tnt':          'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
    'shrinath':     'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
    'sidhanath':    'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'shreyash':     'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',
    'shivam':       'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80',
    'ganesh':       'https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800&q=80',
    'global':       'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
    'gujarat':      'https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800&q=80',
    'ashoka':       'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80',
    'citizen':      'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800&q=80',
    'jakhar':       'https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800&q=80',
    'jain':         'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'khushbu':      'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
    'mahadev':      'https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800&q=80',
    'maharaja':     'https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800&q=80',
    'manish':       'https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800&q=80',
    'n.t.':         'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
    'patel':        'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
    'rathore':      'https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=800&q=80',
    'ravi':         'https://images.unsplash.com/photo-1603988492906-4fb0fb251cf8?w=800&q=80',
    'royal':        'https://images.unsplash.com/photo-1504148455328-c376907d081c?w=800&q=80',
    'sai krishna':  'https://images.unsplash.com/photo-1570125909517-53cb21c89ff2?w=800&q=80',
    'sangitam':     'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&q=80',
    'sharma':       'https://images.unsplash.com/photo-1494515843206-f3117d3f51b7?w=800&q=80',
    'shree krishna':'https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=800&q=80',
    'shree maruti': 'https://images.unsplash.com/photo-1571902943202-507ec2618e8f?w=800&q=80',
    'shree patel':  'https://images.unsplash.com/photo-1464219789935-c2d9d9aba644?w=800&q=80',
    'shree vijay':  'https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=800&q=80',
    'vijay':        'https://images.unsplash.com/photo-1553063807-6534ff4a4e9c?w=800&q=80',
    'vikas':        'https://images.unsplash.com/photo-1591545566161-ec6f136f36e1?w=800&q=80',
    'raj national': 'https://images.unsplash.com/photo-1586611292717-f828b167408c?w=800&q=80',
    'raj':          'https://images.unsplash.com/photo-1517542198065-455de843c0f9?w=800&q=80',
    'national':     'https://images.unsplash.com/photo-1449965408869-eaa3f722e40d?w=800&q=80',
    'sai':          'https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=800&q=80',
}

app = create_app()
with app.app_context():
    buses = Bus.query.all()
    print(f"Processing {len(buses)} buses...")
    updated = skipped = 0

    for bus in buses:
        name = (bus.bus_name or '').lower()

        # Skip buses that were manually set with specific real images
        skip = False
        for kw in KEEP_AS_IS:
            if kw in name:
                skip = True
                break
        if skip:
            skipped += 1
            continue

        # Match longest keyword first (more specific wins)
        img = None
        for kw in sorted(IMAGE_MAP.keys(), key=len, reverse=True):
            if kw in name:
                img = IMAGE_MAP[kw]
                break

        # Fallback: type-based pool
        if not img:
            pool = SLEEPER if bus.bus_type == 'sleeper' else SEATER
            img = pool[bus.id % len(pool)]

        bus.image = img
        updated += 1

    db.session.commit()
    print(f"✅ Updated {updated} buses.")
    print(f"   Kept {skipped} manually-set buses unchanged.")

    # Show sample
    print("\nSample (one per operator):")
    seen = set()
    for b in Bus.query.order_by(Bus.bus_name).all():
        if b.bus_name not in seen:
            seen.add(b.bus_name)
            print(f"  {b.bus_name:28s} → {b.image[:55]}...")

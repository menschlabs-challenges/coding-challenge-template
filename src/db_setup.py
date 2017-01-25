from app import Address, User, db

db.drop_all()
db.create_all()

admin = User(username='admin')
guest = User(username='guest')
admin_address = Address(full_address='1 Market St, San Francisco CA 94105',
                        user=admin)
guest_address = Address(
    full_address='1 Telegraph Hill Blvd, San Francisco, CA 94133',
    user=guest)
db.session.add(admin)  # This will also add admin_address to the session.
db.session.add(guest)  # This will also add guest_address to the session.
db.session.commit()

print User.query.all()
print Address.query.all()

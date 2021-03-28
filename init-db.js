db.auth('root', 'mongoadmin')

db = db.getSiblingDB('restApi')

db.createUser({
  user: "root",
  pwd: "mongoadmin",
  roles: [{role: "readWrite", db: "restApi"}]
});
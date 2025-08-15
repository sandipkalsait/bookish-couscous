// 1. Create adminUser with full administrative privileges
use admin;
db.createUser({
  user: "adminUser",
  pwd: "admin123",
  roles: [
    { role: "userAdminAnyDatabase", db: "admin" },
    { role: "dbAdminAnyDatabase", db: "admin" },
    { role: "readWriteAnyDatabase", db: "admin" }
  ]
});

// 2. Create readerOnly with read access to library and school
use library;
db.createUser({
  user: "readerOnly",
  pwd: "reader123",
  roles: [{ role: "read", db: "library" }]
});
use school;
db.grantRolesToUser("readerOnly", [{ role: "read", db: "school" }]);

// 3. Create collegeAdmin with full admin rights only on college DB
use college;
db.createUser({
  user: "collegeAdmin",
  pwd: "college123",
  roles: [
    { role: "userAdmin", db: "college" },
    { role: "dbAdmin", db: "college" }
  ]
});

// 4. Create dualAccessUser
use school;
db.createUser({
  user: "dualAccessUser",
  pwd: "dual123",
  roles: [{ role: "read", db: "school" }]
});
use college;
db.grantRolesToUser("dualAccessUser", [{ role: "readWrite", db: "college" }]);

// 5. Create custom role readStudentsOnly and assign to limitedUser
use school;
db.createRole({
  role: "readStudentsOnly",
  privileges: [
    {
      resource: { db: "school", collection: "students" },
      actions: ["find"]
    }
  ],
  roles: []
});
db.createUser({
  user: "limitedUser",
  pwd: "limited123",
  roles: [{ role: "readStudentsOnly", db: "school" }]
});

// 6. Create ipRestrictedUser with access only from 192.168.1.50
use finance;
db.createUser({
  user: "ipRestrictedUser",
  pwd: "finance123",
  roles: [{ role: "readWrite", db: "finance" }],
  authenticationRestrictions: [
    { clientSource: ["192.168.1.50"], serverAddress: [] }
  ]
});

// 7. Create tempUser and update its role
use testDB;
db.createUser({
  user: "tempUser",
  pwd: "temp123",
  roles: [{ role: "readWrite", db: "testDB" }]
});
// Now update role to read only
db.updateUser("tempUser", {
  roles: [{ role: "read", db: "testDB" }]
});

// 8. Create deleteMe user and drop it
use training;
db.createUser({
  user: "deleteMe",
  pwd: "delete123",
  roles: [{ role: "readWrite", db: "training" }]
});
db.dropUser("deleteMe");

// 9. Display all users in admin DB
use admin;
db.getUsers();

// 10. List all roles in school DB with full privilege details
use school;
db.getRoles({ showPrivileges: true });

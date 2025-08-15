// a. 2 documents having same joining date
db.employees.find({ dateOfJoining: ISODate("2023-01-15") }).pretty();

// b. 2 documents having same skills
db.employees.find({ skills: { $all: ["Java", "Spring"] } }).pretty();

// c. 1 document having AI project
db.employees.find({ "project.name": "AI Recommendation Engine" }).limit(1).pretty();

// d. 1 document having same project
db.employees.find({ "project.name": "Retail System" }).limit(1).pretty();

// e. 2 documents having experience more than 3 years
db.employees.find({ experience: { $gt: 3 } }).limit(2).pretty();

// f. 2 documents having same designation
db.employees.find({ designation: "Software Engineer" }).limit(2).pretty();

// g. 2 documents having salary more than 30000
db.employees.find({ salary: { $gt: 30000 } }).limit(2).pretty();

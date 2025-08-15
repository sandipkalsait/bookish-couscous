db.createCollection("employees");

function insertEmployee(
  employeeId,
  firstName,
  lastName,
  email,
  phoneNumber,
  addressArray,
  salary,
  designation,
  skills,
  experience,
  projectName,
  projectExperience,
  dateOfJoining,
  birthDate
) {
  const [houseNo, street, city, state, country, pincode] = addressArray;

  const employee = {
    employeeId,
    firstName,
    lastName,
    email,
    phoneNumber,
    birthDate: ISODate(birthDate),
    address: {
      houseNo,
      street,
      city,
      state,
      country,
      pincode
    },
    salary,
    designation,
    skills,
    experience,
    dateOfJoining: ISODate(dateOfJoining),
    project: {
      name: projectName,
      experience: projectExperience
    }
  };

  db.employees.insertOne(employee);
  print("Inserted employee:", employeeId);
}


insertEmployee("EMP001", "Raj", "Kumar", "raj.kumar@pervasive-services.com", "9991112222",["101", "MG Road", "Pune", "Maharashtra", "India", "411001"],35000, "Software Engineer", ["Java", "Spring"], 4,"Retail System", 2, "2023-01-15", "1990-05-10");

insertEmployee("EMP002", "Neha", "Verma", "neha.verma@pervasive-services.com", "9992223333",["102", "Link Road", "Delhi", "Delhi", "India", "110001"],40000, "Software Engineer", ["Java", "Spring"], 5,"Retail System", 2, "2023-01-15", "1992-08-25");

insertEmployee("EMP003", "Amit", "Shah", "amit.shah@pervasive-services.com", "9993334444",["103", "Park Street", "Mumbai", "Maharashtra", "India", "400001"],28000, "QA Engineer", ["Selenium", "JMeter"], 2,"E-Commerce Portal", 1, "2022-12-01", "1991-03-14");

insertEmployee("EMP004", "Sara", "Khan", "sara.khan@pervasive-services.com", "9994445555",["104", "Nehru Road", "Bangalore", "Karnataka", "India", "560001"],32000, "QA Engineer", ["Postman", "JMeter"], 1,"E-Commerce Portal", 1, "2022-11-20", "1994-07-21");

insertEmployee("EMP005", "Vikram", "Desai", "vikram.desai@pervasive-services.com", "9995556666",["105", "Brigade Road", "Bangalore", "Karnataka", "India", "560002"],50000, "Data Scientist", ["Python", "Pandas", "AI"], 6,"AI Recommendation Engine", 3, "2021-06-01", "1987-01-18");

insertEmployee("EMP006", "Pooja", "Rao", "pooja.rao@pervasive-services.com", "9996667777",["106", "Infotech Lane", "Hyderabad", "Telangana", "India", "500001"],30000, "Business Analyst", ["Excel", "SQL"], 3,"Finance Dashboard", 2, "2022-09-15", "1995-09-12");

insertEmployee("EMP007", "Anil", "Mehta", "anil.mehta@pervasive-services.com", "9997778888",["107", "Model Colony", "Pune", "Maharashtra", "India", "411005"],31000, "DevOps Engineer", ["Docker", "Kubernetes"], 4,"CI/CD Automation", 2, "2022-08-01", "1990-02-10");

insertEmployee("EMP008", "Sneha", "Sharma", "sneha.sharma@pervasive-services.com", "9998889999",["108", "VIP Road", "Chandigarh", "Punjab", "India", "160001"],25000, "UI Designer", ["Figma", "AdobeXD"], 1,"Web Revamp", 1, "2023-03-01", "1996-10-30");

insertEmployee("EMP009", "Arjun", "Nair", "arjun.nair@pervasive-services.com", "9999990000",["109", "Tech Park", "Chennai", "Tamil Nadu", "India", "600001"],27000, "HR Executive", ["Recruitment", "Onboarding"], 2,"HRMS Deployment", 1, "2023-04-10", "1993-11-05");

insertEmployee("EMP010", "Ritika", "Joshi", "ritika.joshi@pervasive-services.com", "9990001111",["110", "River Road", "Ahmedabad", "Gujarat", "India", "380001"],33000, "DevOps Engineer", ["Ansible", "Docker"], 3,"Infrastructure Setup", 2, "2022-08-01", "1991-06-17");

insertEmployee("EMP011", "Manoj", "Singh", "manoj.singh@pervasive-services.com", "9988776655",["111", "Golden Street", "Lucknow", "UP", "India", "226001"],29000, "Support Engineer", ["Shell Scripting", "Linux"], 2,"Monitoring System", 1, "2023-02-14", "1988-12-01");

insertEmployee("EMP012", "Kavita", "Iyer", "kavita.iyer@pervasive-services.com", "9977665544",["112", "Green Avenue", "Kolkata", "West Bengal", "India", "700001"],26000, "Support Engineer", ["Linux", "Nagios"], 1,"Monitoring System", 1, "2023-02-14", "1992-04-09");


db.createCollection("transactions");
function insertTransaction(transactionId, transactionDate, employeeFirstName, itemId, itemName, quantity, price, paymentType, totalAmount, paymentSuccess, remark) {
  db.transactions.insertOne({
    transactionId: transactionId,
    transactionDate: ISODate(transactionDate),
    name: employeeFirstName,
    transactionDetails: {
      itemId: itemId,
      itemName: itemName,
      quantity: quantity,
      price: price
    },
    payment: {
      type: paymentType,
      totalAmountPaid: totalAmount,
      paymentSuccessful: paymentSuccess
    },
    remark: remark
  });
}

insertTransaction("TXN001", "2025-07-28", "Raj", "ITM1001", "Mechanical Keyboard", 2, 4500, "Credit", 9000, true, "Delivered successfully");
insertTransaction("TXN002", "2025-07-27", "Neha", "ITM1002", "Wireless Mouse", 1, 1200, "Cash", 1200, true, "");
insertTransaction("TXN003", "2025-07-26", "Amit", "ITM1003", "Laptop Stand", 1, 2000, "Debit", 2000, false, "Payment pending");

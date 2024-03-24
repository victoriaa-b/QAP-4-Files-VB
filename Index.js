// Montel Customers Information
// Author: Victoria Breen
// Date(s): March 18, 2024

// Note: NEVER FORGET THOSE SEMICOLONS

const MotelCustomer = {
  /// Customers attributes
  name: "Victoria Breen",
  gender: "Female",
  birthDate: "2001-02-22",
  pmtMethod: "Credit Card",
  phoneNumber: "709-123-1234",
  roomPrefer: ["King", "Queen", "Double", "Pet-friendly", "Honeymoon Retreat"],
  // make an array

  // Indcates the sub-objects
  mailingAddress: {
    streetAddress: "1 Commonwealth Ave",
    town: "Mount Pearl",
    postalCode: "A1N 1W3",
    province: "Newfoundland",
  },

  // Still sub-objects
  checkIn: {
    date: "2024-03-10",
  },

  checkOut: {
    date: "2024-03-15",
  },

  calcAge: function () {
    const today = new Date();
    const birthDate = new Date(this.birthDate);
    let age = today.getFullYear() - birthDate.getFullYear();
    const monthChange = today.getMonth() - birthDate.getMonth();
    if (
      monthChange < 0 ||
      (monthChange === 0 && today.getDate() < birthDate.getDate())
    ) {
      age--;
    }
    return age;
  },

  calcStay: function () {
    const checkInDate = new Date(this.checkIn.date);
    const checkOutDate = new Date(this.checkOut.date);
    const durationInMS = checkOutDate - checkInDate;
    const durationOfStay = Math.floor(durationInMS / (1000 * 60 * 60 * 24));
    return durationOfStay;
  },
};

// Template literal string - ${...}
const customersDes = `

    Name: ${MotelCustomer.name}
    Address: ${MotelCustomer.mailingAddress.streetAddress}, ${
  MotelCustomer.mailingAddress.town
}, ${MotelCustomer.mailingAddress.postalCode}, ${
  MotelCustomer.mailingAddress.province
}
    Gender: ${MotelCustomer.gender}
    Age: ${MotelCustomer.calcAge()}
    Room Preferences: ${MotelCustomer.roomPrefer.join(",")}
    Payment Method: ${MotelCustomer.pmtMethod}
    Phone Number: ${MotelCustomer.phoneNumber}
    Check-in Date: ${MotelCustomer.checkIn.date}
    Check-out Date: ${MotelCustomer.checkOut.date}
    Stay Time: ${MotelCustomer.calcStay()} days 

  Today ${
    MotelCustomer.name
  } is checking in at the motel, she is ${MotelCustomer.calcAge()} year old ${
  MotelCustomer.gender
}. The room they're checking into is a room labelled as ${
  MotelCustomer.roomPrefer[3]
}, but they also want to include a ${
  MotelCustomer.roomPrefer[1]
} size bed. Her payment method is going to be ${
  MotelCustomer.pmtMethod
}, it's is the same as her mailing address of ${
  MotelCustomer.streetAddress
} of ${MotelCustomer.town}. Oops almost forgot! she checks in ${
  MotelCustomer.checkInDate
} and leaves on the ${MotelCustomer.checkOutDate}. Have a good day!
    `;

console.log(customersDes);


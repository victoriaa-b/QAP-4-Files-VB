# Description: A program for an insurance company to enter and calculate new policies
# Author: Victoria Breen
# Date(s): March 15, 2024

# Define required libraries.
import datetime
import FormatValues as FV
import time
import sys

# Define program constants.
POLICY_NUM = 1944
BASIC_PREMIUM = 869.00
DIS_ADD_CARS = 0.25
EXTRA_LIAB_COVERAGE = 130.00 # DOUBLE CHECK
GLASS_COVERAGE = 86.00
LOANER_CAR_COVERAGE = 58.00
HST_RATE = 0.15
PROCESS_MONTH_FEE = 39.99

CurrDate = datetime.datetime.now()

# Define the program Functions

def TitleCase(st):
    # This coverts any string into .title()
    return ' '.join(word.capitalize() for word in st.split())


def ExtraCost (OptGlassCov, OptExtraLiab, OptLoanCar, NumCarsIns):
    global GlassCovAmt
    global ExtraLiabAmt
    global LoanAmt
    global TotalExtraCost

    if OptGlassCov == "Y":
        GlassCovAmt = GLASS_COVERAGE * NumCarsIns
    else:
        GlassCovAmt = 0  # No would give you no extra cost 
    
    if OptExtraLiab == "Y":
        ExtraLiabAmt = EXTRA_LIAB_COVERAGE * NumCarsIns
    else:
        ExtraLiabAmt = 0 # No would give you no extra cost 
    
    if OptLoanCar == "Y":
        LoanAmt= LOANER_CAR_COVERAGE * NumCarsIns
    else:
        LoanAmt = 0 # No would give you no extra cost 
    TotalExtraCost = GlassCovAmt + ExtraLiabAmt + LoanAmt
    return GlassCovAmt, ExtraLiabAmt, LoanAmt


def CalcMonthlyPMT(PayOpt, TotalCost):
    global DownPMT
    global MonthlyPMT
    # D - Down payment M - Monthly payment, only goes if downpayment or if they required monhtly.
    # Don't need fully as it would be paid 

    if PayOpt == "D":
        DownPMT = float(input("Enter the customers down payment amount: "))
        MonthlyPMT = ((TotalCost - DownPMT) + PROCESS_MONTH_FEE) / 8
        return DownPMT, MonthlyPMT
    elif PayOpt == "M": 
        DownPMT = "N/A"
        MonthlyPMT = (TotalCost + PROCESS_MONTH_FEE) / 8 # eight months
    else:
        DownPMT = "N/A"
        MonthlyPMT = 0
    
    return DownPMT, MonthlyPMT

        
# State lists 
PayOptList = ["F","M","D"]  # F - Fully, M - Monthly and D - Downpay, 
# check having trouble with full words 
ClaimsList = []
ValidProv = ["NL", "PEI", "NS", "NB","QB", "ON","SK", "MB", "AB", "BC", "YT", "NU", "NT" ]


# Main program starts here.
while True:

    # Gather user inputs.
    CustFirstName = input("Enter the customer first name (END to quit): ")
    if CustFirstName == "END":
        break

    CustFirstName = TitleCase('Name')
   
    while True:
        CustLastName = input("Enter the customer last name: ")
        if CustLastName == "":
            print("Data Entry Error - The customer last name cannot be blank.")
        else:
            break
    
    while True:
        StrAdd = input("Enter the customer street address: ").title()
        if StrAdd == "":
            print("Data Entry Error - The customer address cannot be blank.")
        else:
            break
    
    while True:
        City = input("Enter the customer city: ").title()
        if City == "":
            print("Data Entry Error - The customer city cannot be blank.")
        else:
            break

            # Vaildate the province with list
    
    while True:
        CustProv = input("Enter the customers province(XX): ").upper()
        if CustProv not in ValidProv:
            print("Data Entry Error - Province is not vaild.")
        elif CustProv == "":
            print("Data Entry Error - Province can not be blank.")
        else:
            break
    
    while True:
        PostalCode =   input("Enter the postal code (XXX-XXX): ").upper()
        if PostalCode == "":
            print("Data Entry Error - Postal Code cannot be blank.")
        elif len(PostalCode) !=6:
            print("Data Entry Error - Postal Code must be 6 digits.")
        else:
            break
    
        allowed_phone_char = set("1234567890")
    while True:
        PhoneNum = input("Enter the customer phone number (999-999-9999):  ")
        if len(PhoneNum) != 10:
          print("Data Entry Error - Phone number must be 10 digits.")
        elif PhoneNum.isdigit() == False:
            print("Data Entry Error - Phone number must be a digit.")
        elif PhoneNum == "":
            print("Data Entry Error - A phone number must be entered.")
        else:
            break
    
    while True:
    # Number of cars being insured
        NumCarsIns = input("Enter the number of cars to be insured: ")
        if NumCarsIns.isdigit():
            NumCarsIns = int(NumCarsIns)
            break
        elif NumCarsIns == "":
            print("Data Entry Error - Number of car cannot be blank.")
        else:
            break

    DisAmt = (BASIC_PREMIUM/ (DIS_ADD_CARS + 1)) # One for car and dis for every other
    InsPrem = (BASIC_PREMIUM + ((NumCarsIns - 1) * DisAmt)) # Discount for every addintional car
    
    while True:
        OptExtraLiab = input("Would the customer like extra liability (Y/N): ").upper()
        if OptExtraLiab != "Y" and OptExtraLiab !="N":
            print("Data Entry Error - Extra Liability needs to be (Y or N)")
        elif OptExtraLiab == "":
            print("Data Entry Error - Extra Liability option cannot be blank.")
        else:
            break

    while True:
        OptGlassCov = input("Would the customer like to add extra glass coverage (Y/N): ").upper()
        if OptGlassCov !="Y" and OptGlassCov != "N":
            print("Data Entry Error - Extra glass coverage needs to be (Y or N)")
        elif OptGlassCov == "":
            print("Data Entry Error - Extra glass coverage option cannot be blank.")
        else:
            break

    while True:
        OptLoanCar = input("Would the customer like to add loaner car coverage (Y/N): ").upper()
        if OptLoanCar  !="Y" and OptLoanCar != "N":
            print("Data Entry Error - The loaner car coverage needs to be (Y or N)")
        elif OptLoanCar == "":
            print("Data Entry Error - The loaner car coverage option cannot be blank.")
        else:
            break

    TotalExtraCost = sum(ExtraCost(OptGlassCov, OptExtraLiab, OptLoanCar, NumCarsIns))
    TotalInsPrem = InsPrem + TotalExtraCost
    HST = TotalInsPrem * HST_RATE
    TotalCost = TotalInsPrem + HST

    while True:
        PayOpt = input("How would the customer lke to pay? (F for Fully, M for Monthly, D for DownPayment): ").upper()
        if PayOpt not in PayOptList:
            print("Data Entry Error - Pay options must be from the list.")
        elif PayOpt == "":
            print("Data Entry Error - Pay options cannot be blank.")
        else:
            MonthlyPMT, DownPMT = CalcMonthlyPMT(PayOpt,TotalCost)
            break

    while True:
        ClaimNum = input("Enter the claim number: ")
        ClaimDate = input("Enter the claim date (YYYY-MM-DD): ")
        ClaimAmt = input("Enter the claim amount: ")
        ClaimAmt = int(ClaimAmt) # needs to be a number 

        ClaimsList.append((ClaimNum, ClaimDate, ClaimAmt))
            
        PrevClaim = input("Enter if you would like to process another previous claim: ")
        if PrevClaim == "Y":
            continue
        else:
            PrevClaim =="N"
            break 
        
        #Check placement 
    for _ in range(5):
        print('Saving claim data ...', end='\r')
        time.sleep(.3) 
        sys.stdout.write('\033[2K\r')  
        time.sleep(.3)

    f = open("ClaimsValues.dat", "a")
 
    f.write("{}, ".format(str(ClaimNum)))
    f.write("{}, ".format(str(ClaimDate))) 
    f.write("{}\n".format(str(ClaimAmt)))

    POLICY_NUM += 1
    f.close()

    
    print()
    print("Claim data successfully saved ...", end='\r')
    time.sleep(2)  # To create the blinking effect
    sys.stdout.write('\033[2K\r') # clears 



 # Peform calcuation 
    # Some calculations are within the functions 
    InvoiceDate = CurrDate
    # Need in order to find the first payment date
    PMTMonth = CurrDate.month + 1 
    PMTYear = CurrDate.year
    if  PMTMonth > 12:   #12 MONTHS
        PMTMonth = 1
        PMTYear += 1
    
    PMTDate = datetime.datetime(year = PMTYear, month = PMTMonth, day = 1)


 # Formatting 
   
    HSTDsp ="${:,.2f}".format(HST)
    TotalCostDsp ="${:,.2f}".format(TotalCost)
    

  # Display results

    print()
    print()
    print(f"                    One Stop Insurance Company                      ")
    print(f"--------------------------------------------------------------")
    print(f"                                    ")
    print(f"Clients Information:                 Invoice Date:  {FV.FDateS(CurrDate)}                  ")
    print(f"                                                                    ")
    print(f"Customer Name:       {CustFirstName:<25s}                                ")
    print(f"Customer Address:    {StrAdd:<18s} , {City:<25s}")
    print(f"                     {CustProv:<2s}, {PostalCode:<6s}") 
    print(f"Customer Phone #:    {PhoneNum:<12s}")
    print(f"-------------------------------------------------------------")
    print()
    print(f"Insurance Details:                       Policy Number: {POLICY_NUM:>5d}             ")
    print()
    print(f"Number of cars insured:  {NumCarsIns:<2d}")
    print()
    print(f"             Basic Premium:                      {FV.FDollar2(BASIC_PREMIUM):>12s}")
    print(f"             Optional Glass Coverage:            {FV.FDollar2(GlassCovAmt):>12s}")
    print(f"             Liability Coverage:                 {FV.FDollar2(ExtraLiabAmt):>12s}")
    print(f"             Loaner Car coverage                 {FV.FDollar2(LoanAmt):>12s}")
    print(f"                                      -----------------------")
    print(f"                                            HST: {HSTDsp:>12s}")
    print(f"                                      -----------------------")
    print(f"                                      Total Cost:{TotalCostDsp:>12s}")
    print(f"-------------------------------------------------------------")
    print(f"")
    print("Payment Details:                                                     ") 
    print(f"")
    print(f"             Down Payment Amount:                {FV.FDollar2(DownPMT):>12s}                  ")
    print(f"             Monthly Processing Fee:             {FV.FDollar2(PROCESS_MONTH_FEE):>12s}     ")
    print(f"             Monthly Payment Due:                {FV.FDollar2(MonthlyPMT):>12s} ") 
    print(f"             Next Payment Due:                     {FV.FDateS(PMTDate):<10s}    ")
    print(f"")
    print(f"")
    print(f"")
    print(f"Previous Claim Information:                             ")
    print(f"")
    print(f"--------------------------------------------------------------")
    print(f"     Claim #              Claim Date            Amount                ")
    print(f"--------------------------------------------------------------")
    for Claim in ClaimsList:
        print(f"      {Claim[0]:<10}          {Claim[1]:<10}           ${Claim[2]:,.2f}")
    print(f"--------------------------------------------------------------")
    print(f"                  Your Claim has been saved.")
    print(f"--------------------------------------------------------------")
    print(f" ")
    print(f" ")
  

    
    f = open('DatValues.dat', 'w')
    f.write(f"{POLICY_NUM}\n")
    f.write(f"{BASIC_PREMIUM}\n")
    f.write(f"{DIS_ADD_CARS}\n")
    f.write(f"{GLASS_COVERAGE}\n")
    f.write(f"{LOANER_CAR_COVERAGE}\n")
    f.write(f"{HST_RATE}\n")
    f.write(f"{PROCESS_MONTH_FEE}\n")
    f.close()
    print()
    

    NextClaim = input("Is there another insurance claim to be process? (Y/N): ")
    if NextClaim =="Y":
        continue
    else:
        NextClaim =="N"
        print(f" ")
        print("Just remember, The Deer might not have car insurance!")
        print(f" ")
   
   
 

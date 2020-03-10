import sql

print("=== ERIK Opening Load Checker ===")
varOpt = int(input("""Please select one of the following:

1: Check historic date (ALL Exchanges)
2: Check historic date (One Exchange)
3: Run ad-hoc

Option: """))

connObj = sql.DBconnector("Erik.db")

if varOpt == 1:
    print()
    varDate = input("Please enter date in fromat ddMMMyyyy e.g. 03Mar2020: ")
    exchangeList = ["LSA", 'LSB', 'LSC','LSD', 'LSE']
    for x in exchangeList:
        print(f"{x} = {connObj.returnData(x,varDate)}")
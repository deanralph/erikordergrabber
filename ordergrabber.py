import os # Used for file interactions
import sys # Used to get the system arguments
import shutil # Used for file coping
import datetime # used to create filename

exchangeList = ["LSA", 'LSB', 'LSC','LSD', 'LSE']
fileList = [r'\\tdwh-aplim-v1\e$\Logs\Erik\LSA\erikLog.txt', r'\\tdwh-arlim-v2\e$\Logs\Erik\LSB\erikLog.txt',  r'\\tdwh-aplim-v3\e$\Logs\Erik\LSC\erikLog.txt',  r'\\tdwh-aplim-v4\e$\Logs\Erik\LSD\erikLog.txt', r'\\tdwh-arlim-v5\e$\Logs\Erik\LSE\erikLog.txt']
date = datetime.datetime.now()
dateString = date.strftime("%d%b%Y%H%M%S")

# If the debug argument is present, pring the debug info
def debugPrint(PrintString):
    if len(sys.argv) > 1:
        if sys.argv[1] == "debug":
            print (PrintString)

def printToFile(PrintString):
    with open(f"{dateString}.txt", "a") as f:
        f.writelines(PrintString)

# Main log reading function. 
def ReadLog(varSourceFileName, varDestFileName):

# Copies file to local machine for processing 
    shutil.copyfile(varSourceFileName, f'c:\Temp\{exchangeList[varDestFileName]}.txt')
    debugPrint("File Copied")

# Sets maker varables
    varData = []
    fetched = False
    tsp = False

# Opens log file for processing.
    with open (f'c:\Temp\{exchangeList[varDestFileName]}.txt', "r") as f:
        debugPrint("Starting read")
        for line in f:
            if fetched:
                break
            varLine = f.readline()
            listLine = str(varLine).split(" ")
            if len(listLine) >= 4:
                if "07:" in listLine[1] and "TSP" in listLine[2]:
                    varData.append(listLine[3])
                    tsp = True
                if "59" in listLine[1].split(":")[1] and "59" in listLine[1].split(":")[2] and tsp:
                    fetched = True
                if f.readline() == "":
                    fetched = True

# Cleans up log files
    os.remove(f'c:\Temp\{exchangeList[varDestFileName]}.txt')

    debugPrint("Ending Read")

    varSet = set(varData)

# Prints out Order Data
    varReturn = f"Found a total of {len(varData)} entries\n"
    varReturn += f"{len(varSet)} were unique\n"

    return varReturn

# Checkes the file is not being called from another script and runs the main job
if __name__ == "__main__":
    for enum, x in enumerate(fileList):
        if os.path.exists(x):
            print(f'---------------------------------')
            print(f'|              {exchangeList[enum]}              |')
            print(f'---------------------------------')
            print(ReadLog(x, enum))
            print()
            printToFile(f'---------------------------------\n')
            printToFile(f'|              {exchangeList[enum]}              |\n')
            printToFile(f'---------------------------------\n')
            printToFile(ReadLog(x, enum))
            printToFile("\n")
    
    input("Press Enter to continue...")
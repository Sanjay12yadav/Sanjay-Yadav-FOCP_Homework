import sys
def catShelter(filePath):
    try:
        with open(filePath, 'r') as file:
            lines = file.readlines()
            
        oursCat=0
        theirsCat=0
        totalTimeInHouse=0
        visitLengths=[]
        
        for line in lines:
            if line.strip() == 'END':
                break
            a=line.strip().split(',')
            
            catType=a[0]
            entryTime=int(a[1])
            exitTime=int(a[2])
            # print(catType,entryTime,exitTime)
            
            if catType == 'OURS':
                oursCat+=1
                totalTimeInHouse+=exitTime-entryTime
                visitLengths.append(exitTime-entryTime)
            elif catType == 'THEIRS':
                theirsCat+=1
        if oursCat==0:
            print("No visits recorded for the correct cat.")
        else:
            averageVisitLength=totalTimeInHouse/oursCat
            longestVisit=max(visitLengths)
            shortestVisit=min(visitLengths)
            
            print("\nLog File Analysis")
            print("==================\n")
            
            print(f"Cat Visits: {oursCat}")
            print(f"Other Cats: {theirsCat}\n")
            print(f"Total Time in House: {totalTimeInHouse//60} Hours, {totalTimeInHouse%60} Minutes\n")
            
            print(f"Average Visit Length: {int(averageVisitLength)} Minutes")
            print(f"Longest Visit:        {longestVisit} Minutes")
            print(f"Shortest Visit:       {shortestVisit} Minutes\n")

    except FileNotFoundError:
        print(f'Cannot open "{filePath}"!')
        
        
        
if __name__ == "__main__":
    if len(sys.argv)  != 2:
        print("Missing command line argument!")
    else:
        catShelter(sys.argv[1])
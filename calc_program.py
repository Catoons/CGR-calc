def calc_monthly_stats(csvfile1, csvfile2, date):
    
    rev_Jan = 0
    rev_Feb = 0 
    rev_Mar = 0 
    rev_Apr = 0 
    rev_May = 0 
    rev_Jun = 0 
    rev_Jul = 0 
    rev_Aug = 0 
    rev_Sep = 0 
    rev_Oct = 0 
    rev_Nov = 0 
    rev_Dec = 0 
    
    impressions_Jan = 0
    impressions_Feb = 0
    impressions_Mar = 0
    impressions_Apr = 0
    impressions_May = 0
    impressions_Jun = 0
    impressions_Jul = 0
    impressions_Aug = 0
    impressions_Sep = 0
    impressions_Oct = 0
    impressions_Nov = 0
    impressions_Dec = 0
    
    twofiles = True
    
    myfile1 = open(csvfile1, 'r')
    lines_one = myfile1.readlines()
    
    if '.csv' in csvfile2:
        myfile2 = open(csvfile2, 'r')
        lines_two = myfile2.readlines()
    else:
        twofiles = False 
    
   

    
    
    for x in lines_one[1:]:
        better = x.split(',')
        mon = better[0]
        monn = mon[:2]
        if monn == '01':
            impressions_Jan += float(better[2])
        if monn == '02':
            impressions_Feb += float(better[2])
        if monn == '03':
            impressions_Mar += float(better[2])
        if monn == '04':
            impressions_Apr += float(better[2])
        if monn == '05':
            impressions_May += float(better[2])
        if monn == '06':
            impressions_Jun += float(better[2])
    
    if twofiles == True:
        for x in lines_two[1:]:
            better = x.split(',')
            mon = better[0]
            monn = mon[:2]
        
            if monn == '07':
                impressions_Jul += float(better[2])
            if monn == '08':
                impressions_Aug += float(better[2])
            if monn == '09':
                impressions_Sep += float(better[2])
            if monn == '10':
                impressions_Oct += float(better[2])
            if monn == '11':
                impressions_Nov += float(better[2])
            if monn == '12':
                impressions_Dec += float(better[2])
            

            
    
    if lines_one[1][:2] == '01':
        
        total_impressions1 = impressions_Jan + impressions_Feb + impressions_Mar + impressions_Apr + impressions_May + impressions_Jun
   
        print(f'January {date} Impressions: {round(impressions_Jan)}')
        print(f'February {date} Impressions: {round(impressions_Feb)}')
        print(f'March {date} Impressions: {round(impressions_Mar)}')
        print(f'April {date} Impressions: {round(impressions_Apr)}')
        print(f'May {date} Impressions: {round(impressions_May)}')
        print(f'June {date} Impressions: {round(impressions_Jun)}')
    
    if twofiles == True:
        
        total_impressions2 = impressions_Jul + impressions_Aug + impressions_Sep + impressions_Oct + impressions_Nov + impressions_Dec
   
        print(f'July {date} Impressions: {round(impressions_Jul)}')
        print(f'August {date} Impressions: {round(impressions_Aug)}')
        print(f'September {date} Impressions: {round(impressions_Sep)}')
        print(f'October {date} Impressions: {round(impressions_Oct)}')
        print(f'November {date} Impressions: {round(impressions_Nov)}')
        print(f'December {date} Impressions: {round(impressions_Dec)}')
    
    if twofiles == True:
        print('\n')
        print(f'Total Impressions for {date}: {round(total_impressions1 + total_impressions2)}', end='\n')
    else:
        print('\n')
        print(f'Total Impressions for first half of {date}: {round(total_impressions1)}', end='\n')
        

        
#-----------------------------------------------------------------------#
    
    for x in lines_one[1:]:
        better = x.split(',')
        mon = better[0]
        monn = mon[:2]
        if monn == '01':
            rev_Jan += float(better[-2])
        if monn == '02':
            rev_Feb += float(better[-2])
        if monn == '03':
            rev_Mar += float(better[-2])
        if monn == '04':
            rev_Apr += float(better[-2])
        if monn == '05':
            rev_May += float(better[-2])
        if monn == '06':
            rev_Jun += float(better[-2])
            
    if twofiles == True:   
        for x in lines_two[1:]:
            better = x.split(',')
            mon = better[0]
            monn = mon[:2]
        
            if monn == '07':
                rev_Jul += float(better[-2])
            if monn == '08':
                rev_Aug += float(better[-2])
            if monn == '09':
                rev_Sep += float(better[-2])
            if monn == '10':
                rev_Oct += float(better[-2])
            if monn == '11':
                rev_Nov += float(better[-2])
            if monn == '12':
                rev_Dec += float(better[-2])
            

    print('\n')            
    
    if lines_one[1][:2] == '01':
        
        total_rev1 = rev_Jan + rev_Feb + rev_Mar + rev_Apr + rev_May + rev_Jun
   
        print(f'January {date} Revenue: ${round(rev_Jan,2)}')
        print(f'February {date} Revenue: ${round(rev_Feb,2)}')
        print(f'March {date} Revenue: ${round(rev_Mar,2)}')
        print(f'April {date} Revenue: ${round(rev_Apr,2)}')
        print(f'May {date} Revenue: ${round(rev_May,2)}')
        print(f'June {date} Revenue: ${round(rev_Jun,2)}')
      
    if twofiles == True:
        
        total_rev2 = rev_Jul + rev_Aug + rev_Sep + rev_Oct + rev_Nov + rev_Dec
   
        print(f'July {date} Revenue: ${round(rev_Jul,2)}')
        print(f'August {date} Revenue: ${round(rev_Aug,2)}')
        print(f'September {date} Revenue: ${round(rev_Sep,2)}')
        print(f'October {date} Revenue: ${round(rev_Oct,2)}')
        print(f'November {date} Revenue: ${round(rev_Nov,2)}')
        print(f'December {date} Revenue: ${round(rev_Dec,2)}')
        
    
    
    if twofiles == True:
        print('\n')
        print(f'Total Revenue for {date}: ${round(total_rev1 + total_rev2,2)}')
        print('\n')

    else:
        print('\n')
        print(f'Total Revenue for first half of {date}: ${round(total_rev1,2)}')
        print('\n')
        
     
# END OF FUNCTION
        


# User Input Loop

csv1=0
i=1

print('Welcome to the CGR ad data analyzer! Make sure to include file extensions when writing out their names.')
print("It's recommended that the files are stored in the same location as this program. Else, you'll have to enter the entire file path.")

# loop runs until user enters 'x' as name for csv file 1

while i > 0:

    csv1 = input("\nEnter the name of csv file 1 (or 'x' to exit): ")
    if csv1 == 'x' or csv1 == 'X':
        print('\nSee you later. God bless!')
        break
    csv2 = input("Enter the name of csv file 2. If there's no second file, just type 'n': ")
    year = input('Enter the year: ')
    print('\n')
    
    calc_monthly_stats(csv1, csv2, year)
    
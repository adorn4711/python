import re 
import sys
print ("Day4")
def passportCheck(data):
    valid = 0
    passport = {}
    for i in range(len(data)):
        line = data[i]
        if (len(line)==0):
            check = True;
            try:
                for field in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]:
                    fieldCheck = field in passport
                    if field == "byr":
                        intfield = int(passport[field])
                        fieldCheck = intfield <=2002 and intfield >=1920
                    if field == "iyr":
                        intfield = int(passport[field])
                        fieldCheck = intfield <=2020 and intfield >=2010
                    if field == "eyr":
                        intfield = int(passport[field])
                        fieldCheck = intfield <=2030 and intfield >=2020
                    if field == "hgt":
                        intfield = int(passport[field][0:-2])
                        measure = passport[field][-2:]
                        if measure == "cm":
                            fieldCheck = intfield <=193 and intfield >=150
                        elif measure == "in":
                            fieldCheck = intfield <=76 and intfield >=59
                        else:    
                            fieldCheck = False
                        #print (field,measure,intfield,fieldCheck)
                    if field == "hcl":
                        value = passport[field]
                        fieldCheck0 = value[0]=='#'
                        matchObj1 = re.match( r'[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', value[1:], re.M|re.I)
                        if (matchObj1):
                            fieldCheck1 = True
                        else:     
                            fieldCheck1 = False
                        fieldCheck = fieldCheck0 and fieldCheck1
                        #print(field,value,value[1:],fieldCheck1,fieldCheck)
                    if field == "ecl":
                        value = passport[field]
                        fieldCheck = value in ['amb','blu','brn','gry','grn','hzl','oth']
                    if field == "pid":
                        value = passport[field]
                        matchObj1 = re.match( r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', value, re.M|re.I)
                        if (matchObj1):
                            fieldCheck = True
                        else:     
                            fieldCheck = False
                        fieldCheck = fieldCheck and len(value) == 9    
                    #print (field,fieldCheck)
                    check = check and fieldCheck
            except:
                print (passport)
                print("Oops!", sys.exc_info()[0], "occurred.")
                check = False
            if check:
                valid +=1
            passport.clear()
        else:    
            for field in line.split():
                key,value = field.split(':')
                #print (key,value)
                passport[key]=value
    return valid
    
    
        
        
data = [line.strip() for line in open("input_day4.txt", 'r')]
print(passportCheck(data))
# You should to count each day of rest (Saturday and Sunday) starting from the initial date to final date. 
# Count the initial and final dates if they fall on a Saturday or Sunday. 

from datetime import date,timedelta

def weekCount(from_date, to_date):        
    return len([1 for i in range((to_date - from_date).days + 1) 
                if (from_date + timedelta(i)).isoweekday() in [6,7]]) 

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert weekCount(date(2013, 9, 18), date(2013, 9, 23)) == 2, "1st example"
    assert weekCount(date(2013, 1, 1), date(2013, 2, 1)) == 8, "2nd example"
    assert weekCount(date(2013, 2, 2), date(2013, 2, 3)) == 2, "3rd example"

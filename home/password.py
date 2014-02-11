# The password will be considered strong enough if its length is greater than or equal to 10 symbols,
# it has at least one number, as well as containing one uppercase letter and one lowercase letter in it.


def pass(data):    
    return bool(len(data) >= 10  \
        and filter(lambda x:x.isupper() , data) \
        and filter(lambda x:x.islower(), data) \
        and filter(lambda x:x.isdigit(), data))

def pass2any(data):
      return (len(data) >= 10 and
        any([ch.isupper() for ch in data]) and
        any([ch.isdigit() for ch in data]) and
        any([ch.islower() for ch in data]))    


if __name__ == '__main__':
    assert pass('A1213pokl') == False, "1st example"
    assert pass('bAse730onE4') == True, "2nd example"
    assert pass('asasasasasasasaas') == False, "3rd example"
    assert pass('QWERTYqwerty') == False, "4th example"
    assert pass('123456123456') == False, "5th example"
    assert pass('QwErTy911poqqqq') == True, "6th example"
    
    assert pass2any('A1213pokl') == False, "1st example"
    assert pass2any('bAse730onE4') == True, "2nd example"

import re

license_plate_regex = re.compile(r'(\D\D\D)(\d\d\d\d)')
matches = license_plate_regex.findall(
'''
    EIO2456
    blah blah blah
    blah blah KEO3921blah blah
    23iugjiro932wro93tgu934356j
    ABCDE12345
    EWkK3294
    '''
)
print(matches)
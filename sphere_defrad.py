rad = 0
volume = 0
print 'enter radius in meters'
rad = input()
print 'radius value is:', rad,'meters'

def vol(rad):
    volume = ((4/3)*(3.142*(rad**3)))
    print 'volume of sphere of radius',rad,'meters is\n',volume,'meters^3'                 
vol(rad)
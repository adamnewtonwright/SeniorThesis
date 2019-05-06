##################################################
# RepRate returns the necessary repetition rate in kHz
# of the laser given a magnetic field
##################################################
def RepRate(B):
    reprate = .7*B*1000
    return reprate

##################################################
# MagField returns the necessary magnetic field in
# gauss for a given repetition rate
##################################################
def MagField(rep):
    bfield = rep/(.7*1000)
    return bfield

def CurrentToMag(I):
    B = 13.23 * I -.28
    return B
def MagToCurrent(B):
    I = .28+B/13.23
    return I

response1 = input('Enter Current (C),  Mag Field (B), or Rep Rate (R): ')

if response1 =='C':
    response2 = float(input('Enter Current in amps: '))
    mag = CurrentToMag(response2)
    rep = RepRate(mag)
    print('You will have a magnetic field of %f gauss and need a repetition rate of %f kHz.' %(mag,rep))

if response1 =='R':
    response2 = float(input('Enter Rep Rate in kHz: '))
    mag = MagField(response2)
    curr = MagToCurrent(mag)
    print('You need a magnetic field of %f gauss which will need a current of %f amps.' %(mag,curr))

if response1 =='B':
    response2 = float(input('Enter magnetic field in gauss: '))
    rep = RepRate(response2)
    curr = MagToCurrent(response2)
    print('You need a repetition rate of %f kHz and a current of %f amps.' %(rep,curr))

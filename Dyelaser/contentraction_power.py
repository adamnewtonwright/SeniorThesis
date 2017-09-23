import matplotlib.pyplot as plt

concentration1 = '0.088'

# This is the power in mW of the quanta ray as our pump beam
inputpower088 = [0,145,300,423,563,753,871,1003,1177,1205]
#These are the data we collected of the output energy of the dye beam in mirco Joules
output_energy088 = [0,14,48,89,132,162,190,223,245,240]

concentration2 = ".093"
inputpower093 =    [0,100,203,373,527,677,814,965,1142,1290]
output_energy093 = [0,10 ,29 ,38 ,105,136,176,207,245,278]

concentration3 = '.100'
inputpower100 =    [0,90,242,310]
output_energy100 = [0,7 ,25 ,27 ]

#I then convert this power into Joules per pulse
def pow_to_energy(power):
    input_energy=[]
    for item in power:
        item_J = item/1000 #converting from mW to W
        item_J = item_J/10 #converting from W to J
        input_energy.append(item_J)
    return input_energy


#I then convert this into Joules
def micro_to_joules(something):
    output_energy_J =[]
    for item in something:
        item_J = item/(10**6)
        output_energy_J.append(item_J)
    return output_energy_J

# And I plot the dye beam output energy versus the quanta ray input energy
plt.figure()
plot_088, = plt.plot(pow_to_energy(inputpower088),micro_to_joules(output_energy088),label = 'concentration at 0.088')
plot_093, = plt.plot(pow_to_energy(inputpower093),micro_to_joules(output_energy093),label = 'concentration at 0.093')
plot_100, = plt.plot(pow_to_energy(inputpower100),micro_to_joules(output_energy100),label = 'concentration at 0.100')
plt.legend(handles=[plot_088, plot_093,plot_100])
plt.legend(loc=(.4,0))
plt.title('Input Energy versus Output energy for various dye concentrations')
plt.xlabel('Input Energy J')
plt.ylabel('Output Energy J')
plt.grid(True)
plt.show()

# Calculating how much energy is actually entering the dye cell at 95/5 beam splitter
def into_oscillator(power):
    input_oscillator = []
    for item in power:
        neww= item*.05
        input_oscillator.append(neww)
    return input_oscillator

# Calculating the efficiency of the dye laser by dividing the output energy of the dye laser by the input energy going into the dye laser and then
#multiplying by 1000
def efficiency(output_energy_J,input_energy_J):
    outputefficiency = [0] #initialize value 1 to 0 since you cant divide by 0
    for i in range(1,len(output_energy_J)):
        eff = output_energy_J[i]/into_oscillator(input_energy_J)[i]
        eff = eff *100
        outputefficiency.append(eff)
    return outputefficiency

#Plotting the efficiency versus the total input energy
plt.figure()
plot_088, = plt.plot(pow_to_energy(inputpower088),efficiency(micro_to_joules(output_energy088),pow_to_energy(inputpower088)),label= 'concentation of 0.088g/L')
plot_093, = plt.plot(pow_to_energy(inputpower093),efficiency(micro_to_joules(output_energy093),pow_to_energy(inputpower093)),label = 'concentration of 0.093 g/L')
plot_100, = plt.plot(pow_to_energy(inputpower100),efficiency(micro_to_joules(output_energy100),pow_to_energy(inputpower100)),label = 'concentration of 0.100 g/L')
plt.legend(handles=[plot_088, plot_093,plot_100])
plt.legend(loc=(.14,0))
plt.title('Output efficiency versus input energy for concentration 0.088')
plt.xlabel('input energy J')
plt.ylabel('output efficiency %')
plt.grid(True)
plt.show()

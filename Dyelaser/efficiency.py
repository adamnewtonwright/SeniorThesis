def eff(inputpower_mw,outputenergy_microw):
    inputenergy = inputpower_mw/10
    into_osc = inputenergy*.05
    outputenergy_mw = outputenergy_microw/1000
    eff = outputenergy_mw/into_osc
    eff = eff*100
    print(eff,'%')

eff(500,200)


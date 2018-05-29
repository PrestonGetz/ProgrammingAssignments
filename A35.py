age=int(input("what is your age in years?"))
age2=int(input("how many months?"))
age3=(age*365*24*60*60)+(age2*30*24*60*60)

earth_year=31557600
mercury_year=7600544
venus_year=19414149
mars_year=59354032
jupiter_year=374355659
saturn_year=929292363
uranus_year=2651370019
neptune_year=5200418560

earth_age=age3/earth_year
mercury_age=age3/mercury_year
venus_age=age3/venus_year
mars_age=age3/mars_year
jupiter_age=age3/jupiter_year
saturn_age=age3/saturn_year
uranus_age=age3/uranus_year
neptune_age=age3/neptune_year

print("Your age on murcury is ",mercury_age," years.")
print("Your age on venus is ",venus_age," years.")
print("Your age on earth is ",earth_age," years.")
print("Your age on mars is ",mars_age," years.")
print("Your age on jupiter is ",jupiter_age," years.")
print("Your age on saturn is ",saturn_age," years.")
print("Your age on uranus is ",uranus_age," years.")
print("Your age on neptune is ",neptune_age," years.")

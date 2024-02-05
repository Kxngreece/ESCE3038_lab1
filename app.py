#Qu1
def parallel(*resistor):
    
    if len(resistor) < 2:
    parares = 0
    
    # Calculate the reciprocal of each resistance using a for loop
    for resistance in resistor:
        parares = parares + (1/resistance)

    totalres = 1 / parares

    return totalres


result = parallel(330, 1000, 2200)

#Qu 2
def potential_divider(powersupply, resistors):
    

    # Calculate total resistance in the circuit
    total_resistance = sum(resistors)

    # Calculate voltage drop across each resistor using the potential divider formula
    voltage_drops = [powersupply * (resistor / total_resistance) for resistor in resistors]

    return voltage_drops


# powersupply = 9.0  # Replace with your desired voltage supply value
# resistors= [1000, 3000]  # Replace with your list of resistor values

result = potential_divider(9, [3000, 1000])

# Q3
def temperature_check(temperature, unit):
  
    # Define temperature limits for hypothermia, normal, and hyperthermia
    hypothermia_limit_C = 35.0
    hyperthermia_limit_C = 38.0
    hypothermia_limit_F = 95.0
    hyperthermia_limit_F = 100.4

    # Convert temperature to Celsius if it's in Fahrenheit
    if unit == "F":
        temperature = (temperature - 32) * 5/9

    # Check the patient's temperature condition
    if temperature < hypothermia_limit_C:
        result = "the patient is hypothermic"
    elif hypothermia_limit_C <= temperature <= hyperthermia_limit_C:
        result = "the patient's temperature is normal"
    else:
        result = "the patient is hyperthermic"

    return result


    

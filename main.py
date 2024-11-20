import skfuzzy.control as ctrl
from membership_functions import create_membership_functions, plot_membership_functions
from data_analysis import data_process, evaluate_dog_conditions, plot_dog_condition

# Create Membership Functions
body_temperature, heart_rate, barking_volume, is_dog_ok = create_membership_functions()

# Plot Membership Functions
plot_membership_functions(body_temperature)
plot_membership_functions(heart_rate)
plot_membership_functions(barking_volume)
plot_membership_functions(is_dog_ok)


# ____________________ 3 Define the Fuzzy Rules ____________________ #

#Define fuzzy rules
rule1 = ctrl.Rule(body_temperature['normal'] & heart_rate['low'], is_dog_ok['normal'])
rule2 = ctrl.Rule(body_temperature['normal'] & heart_rate['normal'], is_dog_ok['perfect'])
rule3 = ctrl.Rule(body_temperature['normal'] & heart_rate['high'], is_dog_ok['need help'])

rule4 = ctrl.Rule(body_temperature['high'] & heart_rate['low'], is_dog_ok['urgent'])
rule5 = ctrl.Rule(body_temperature['high'] & heart_rate['high'], is_dog_ok['urgent'])
rule6 = ctrl.Rule(body_temperature['high'] & heart_rate['normal'], is_dog_ok['need help'])

rule7 = ctrl.Rule(body_temperature['low'] & heart_rate['low'], is_dog_ok['urgent'])
rule8 = ctrl.Rule(body_temperature['low'] & heart_rate['normal'], is_dog_ok['need help'])
rule9 = ctrl.Rule(body_temperature['low'] & heart_rate['high'], is_dog_ok['urgent'])

#create a control system and simulation
system = ctrl.ControlSystem([rule1,rule2,rule3, rule4, rule5, rule6, rule7, rule8, rule9])



#  ____________________ 6 Running the Project ____________________ #
dog_1='Data/fine_dog_data.csv'
dog_2='Data/sick_dog_data.csv'
dog_3='Data/critical_dog_data.csv'
dog_1_data_list = data_process(dog_3)

results = evaluate_dog_conditions(dog_1_data_list, system, is_dog_ok)
plot_dog_condition(results)




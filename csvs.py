import csv
import random
import string

def generate_user_id_password():
    user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
    return user_id, password

def generate_pnr_numbers(count):
    pnrs = set()
    while len(pnrs) < count:
        pnr = ''.join(random.choices(string.digits, k=10))
        pnrs.add(pnr)
    return list(pnrs)

def generate_train_number():
    return ''.join(random.choices(string.digits, k=5))

stations_route_1 = ["Station A", "Station B", "Station C", "Station D", "Station E"]
stations_route_2 = ["Station F", "Station G", "Station H", "Station I", "Station J"]
stations_route_3 = ["Station K", "Station L", "Station M", "Station N", "Station O"]
stations_route_4 = ["Station P", "Station Q", "Station R", "Station S", "Station T"]
stations_route_5 = ["Station U", "Station V", "Station W", "Station X", "Station Y"]

routes = {
    "Route 1": {"stations": stations_route_1},
    "Route 2": {"stations": stations_route_2},
    "Route 3": {"stations": stations_route_3},
    "Route 4": {"stations": stations_route_4},
    "Route 5": {"stations": stations_route_5},
}

station_masters = []
tte_personnel = []
crpf_personnel = []
pnr_numbers = []
train_numbers = []
route_incharges = []

for route, data in routes.items():
    # Assigning station masters
    for station in data["stations"]:
        user_id, password = generate_user_id_password()
        station_masters.append([route, station, user_id, password])

    # Assigning TTE and CRPF personnel
    tte_id, tte_password = generate_user_id_password()
    crpf_id, crpf_password = generate_user_id_password()
    tte_personnel.append([route, tte_id, tte_password])
    crpf_personnel.append([route, crpf_id, crpf_password])
    
    # Generating train number and PNRs
    train_number = generate_train_number()
    pnrs = generate_pnr_numbers(3)
    
    train_numbers.append([route, train_number])
    for pnr in pnrs:
        pnr_numbers.append([route, train_number, pnr])

    # Assigning route incharge
    route_incharge_id, route_incharge_password = generate_user_id_password()
    route_incharges.append([route, route_incharge_id, route_incharge_password])

# Writing to CSV files
with open('station_masters.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "Station", "Station Master ID", "Station Master Password"])
    writer.writerows(station_masters)

with open('tte_personnel.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "TTE ID", "TTE Password"])
    writer.writerows(tte_personnel)

with open('crpf_personnel.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "CRPF ID", "CRPF Password"])
    writer.writerows(crpf_personnel)

with open('train_numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "Train Number"])
    writer.writerows(train_numbers)

with open('pnr_numbers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "Train Number", "PNR Number"])
    writer.writerows(pnr_numbers)

with open('route_incharges.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Route", "Route Incharge ID", "Route Incharge Password"])
    writer.writerows(route_incharges)

print("CSV files generated successfully!")

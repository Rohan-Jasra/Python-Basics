#the idea behind this is to make a function which accepts other functions as inputs to come up with a total cost

def case_cost(case):
    if case=="rosewill":
        return 40
    if case=="corsair":
        return 80
    if case=="nzxt":
        return 120
    if case=="phanteks":
        return 150

def cpu_cost(cpu):
    if cpu=="g3258":
        return 80
    if cpu=="i54460":
        return 250
    if cpu=="i74790k":
        return 450

def gpu_cost(gpu):
    if gpu=="gtx1050ti":
        return 200
    if gpu=="gtx1060":
        return 375
    if gpu=="gtx1070":
        return 600
    if gpu=="1080ti":
        return 1000

def motherboard_cost(motherboard):
    if motherboard=="asus":
        return 100
    if motherboard=="asrock":
        return 120
    if motherboard=="gigabyte":
        return 150

def powersupply_cost(powersupply):
    if powersupply=="evgaB":
        return 80
    if powersupply=="evgaG":
        return 120

def ram_cost(ram):
    if ram=="8gb":
        return 80
    if ram=="16gb":
        return 150

def hdd_cost(hdd):
    if hdd=="1tb":
        return 60
    if hdd=="2tb":
        return 90

def total_cost(case,cpu,gpu,motherboard,powersupply,ram,hdd):
    return case_cost(case)+cpu_cost(cpu)+gpu_cost(gpu)+motherboard_cost(motherboard)+powersupply_cost(powersupply)+ram_cost(ram)+hdd_cost(hdd)
    

print (total_cost("corsair","i54460","gtx1060","asus","evgaB","8gb","1tb"))

   

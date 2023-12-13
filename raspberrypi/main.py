# ---- Imports ------------
from import_file import*
import analyser
import api_handler
import handel_file #not in Use
import handelprog
import mail
import time_util

#import raspberrypi_func
#not in work


# ----- Global Variables -----------
Stock = "SMI"               #default value
email = mail.Send_email()
exe = 0                     #number of executet mails
# ----------------------------------


# ----- Functions -----------------------------------------------------------------------------
def end_day_routine():
    analyse = analyser.Analyser(api_handler.get_data_from_api(time_util.get_date(),Stock))
    data = analyse.end_day_routine()
    email.send_email(data, "end_day")
    print("finsish")

def routing_check():
    email = mail.Send_email()
    comands = email.get_commands()
    execute_comands(comands)

def execute_comands(data):
    global exe
    global Stock
    global email
    for i in range(exe,len(data)):
        j = data[i]
        while ":" in j:
            j = j.replace(":", "")
        comand = j.split(" ")[1]

        exe += 1
        
        if "send" in comand:
            end_day_routine()

        elif "@" in comand:
            if comand[0] == "-":
                email.emails.remove(comand)
            else:
                email.emails.append(comand)

        else:
            Stock = comand

    print("everyting ap to date")
# ---------------------------------------------------------------------------------------------


# ------------------ Time Functions ----------------------
def call_20():
    return time_util.call_interval(20,21)

def call_23():
    return time_util.call_interval(23,24)

def call_16():
    return time_util.call_interval(16,17)
# --------------------------------------------------------


# ----------- Initialising HandelProg Object -------------
prog = handelprog.HandelProg("Stockanalyser")


# ----------- Function for reseting Internal Values ------
def reset_day_fuc():
    handelprog.HandelProg.reset_number_run(prog,"END_DAY")


# ------------ Initialising HandelProg "System" -----------------------------------------------
prog.add_func(end_day_routine,call_16, "END_DAY",["MAXITER1"])
prog.add_func(reset_day_fuc,call_23,"RESET_END_DAY")
prog.add_func(routing_check, handelprog.HandelProg.run_anyway, "ROUTINE_CHECK", ["ITER10"])
# ---------------------------------------------------------------------------------------------


# #############################################################################################
# -----------------------------------Starting the Main Loop ----------------------------------#
# #############################################################################################
prog.main_loop()





#prog.add_func(end_day_routine, raspberrypi_func.check_button_port,"BUTTON_PRESS")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST",["MAXITER300"])
#prog.add_func(get_data_from_api,HandelProg.run_anyway,"TEST_API")
#prog.triger_func("TEST_API")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST_F",["ITER2","MAXITER30"])

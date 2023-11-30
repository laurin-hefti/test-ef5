
from import_file import*
import analyser
import api_handler
import handel_file
import handelprog
import mail
import time_util
#import raspberrypi_func

def end_day_routine():
    analyse = analyser.Analyser(api_handler.get_data_from_api(time_util.get_date()))
    email = mail.Send_email()
    data = analyse.end_day_routine()
    email.send_email(data, "end_day")
    print("finsish")

#end_day_routine()

def call_20():
    return time_util.call_interval(20,21)

def call_23():
    return time_util.call_interval(23,24)

def call_16():
    return time_util.call_interval(16,17)

prog = handelprog.HandelProg("test2")

def test_f():
    handelprog.HandelProg.reset_number_run(prog,"TEST")

def reset_day_fuc():
    handelprog.HandelProg.reset_number_run(prog,"END_DAY")


prog.add_func(end_day_routine,call_16, "END_DAY",["MAXITER1"])
#prog.add_func(end_day_routine, raspberrypi_func.check_button_port,"BUTTON_PRESS")
prog.add_func(reset_day_fuc,call_23,"RESET_END_DAY")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST",["MAXITER300"])
prog.main_loop()
#prog.add_func(get_data_from_api,HandelProg.run_anyway,"TEST_API")
#prog.triger_func("TEST_API")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST_F",["ITER2","MAXITER30"])

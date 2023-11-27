import import_file
import analyser
import api_handler
import handel_file
import handelprog
import mail
import raspberrypi_func

def end_day_routine():
    analyse = Analyser(get_data_from_api())
    email = Send_email()
    data = analyse.end_day_routine()
    email.send_email(data, "end_day")
    print("finsish")



def get_time():
    time = datetime.now()
    return time

def call_interval(t,t2):
    time = str(get_time().time())
    time = time[0:2]
    if int(time) >= t and int(time) < t2:
        return True
    else:
        return False

def call_20():
    return call_interval(20,21)

def call_23():
    return call_interval(23,24)

def call_16():
    return call_interval(16,17)

prog = HandelProg("test2")

def test_f():
    HandelProg.reset_number_run(prog,"TEST")

def reset_day_fuc():
    HandelProg.reset_number_run(prog,"END_DAY")

prog.add_func(end_day_routine,call_16, "END_DAY",["MAXITER1"])
prog.add_func(end_day_routine, check_button_port,"BUTTON_PRESS")
prog.add_func(reset_day_fuc,call_23,"RESET_END_DAY")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST",["MAXITER300"])
prog.main_loop()
#prog.add_func(get_data_from_api,HandelProg.run_anyway,"TEST_API")
#prog.triger_func("TEST_API")
#prog.add_func(test_f,HandelProg.run_anyway,"TEST_F",["ITER2","MAXITER30"])
#prog.main_loop()  

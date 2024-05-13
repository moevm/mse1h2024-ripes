import os
from .check import *
from .gen import *

check_dict = {1: check_1.check, 2: check_2.check, 3: check_3.check}
txt_dict = {1: gen_1.get_txt, 2: gen_2.get_txt, 3: gen_3.get_txt}

def check_submit(s_id, t_id, solution, condition):
	path = "{cdir}/check/tmp_solution".format(cdir=os.path.dirname(__file__))
	if not os.path.exists(path):
		os.makedirs(path)
	path += "/{sid}_{tid}.s".format(sid = s_id, tid = t_id)
	solution_file = os.open(path, os.O_WRONLY | os.O_CREAT)
	os.write(solution_file, str.encode(solution))
	os.sync()
	os.close(solution_file)
	return check_dict[t_id](s_id, condition)

def get_tasks():
	return {"len": len(txt_dict), "tasks": [{"title": txt_dict[key]()[0] ,"text": txt_dict[key]()[1] , "id": txt_dict[key]()[2]} for key, value in txt_dict.items()]}

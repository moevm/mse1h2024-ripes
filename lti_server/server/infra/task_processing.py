import os
import json

from tasks import *

check_dict = {1: task_1.check, 2: task_2.check, 3: task_3.check}
txt_dict = {1: task_1.get_txt, 2: task_2.get_txt, 3: task_3.get_txt}

def check_submit(s_id, t_id, solution):
	path = "./tmp_solution/{sid}_{tid}.s".format(sid = s_id, tid = t_id)
	solution_file = os.open(path, O_WRONLY)
	os.write(solution_file)
	os.sync()
	os.close(solution_file)
	return check_dict[t_id]()

def get_tasks():
	return {"len": len(txt_dict), "tasks": [{"title": txt_dict[key]()[0] ,"text": txt_dict[key]()[1] , "id": txt_dict[key]()[2]} for key, value in txt_dict.items()]}

import os
from tasks import *

check_dict = {1: task_1.check, 2: task_2.check, 3: task_3.check}
txt_dict = {1: task_1.get_txt, 2: task_2.get_txt, 3: task_3.get_txt}

def check_submit(s_id, t_id, solution):
	path = "{cdir}/tasks/tmp_solution/{sid}_{tid}.s".format(cdir=os.path.dirname(__file__), sid = s_id, tid = t_id)
	solution_file = os.open(path, os.O_WRONLY | os.O_CREAT)
	os.write(solution_file, str.encode(solution))
	os.sync()
	os.close(solution_file)
	return check_dict[t_id](s_id)

def get_tasks():
	return {"len": len(txt_dict), "tasks": [{"title": txt_dict[key]()[0] ,"text": txt_dict[key]()[1] , "id": txt_dict[key]()[2]} for key, value in txt_dict.items()]}

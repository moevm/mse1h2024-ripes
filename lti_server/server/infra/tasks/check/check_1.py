import subprocess, os
import re, math
from .ripes_parser import parse_ripes
	
def check(student_id, condition):
	params = re.findall(r"большую|меньшую|Число: [1-7]", condition)
	params[1] = int(params[1][7:])
	ev1 = answer(params)
	run1 = parse_ripes(subprocess.check_output("{d}/Ripes --appimage-extract-and-run --mode cli --src {d}/tmp_solution/{sid}_1.s -t asm --proc RV64_SS --regs --json -v".format(d=os.path.dirname(__file__), sid = student_id).split()).decode("utf-8"))	
	return "All tests for the first task passed!"
	
def answer(params):
	return params[1]**(math.ceil(params[1]/2)) if (params[0] == "большую") else params[1]**(math.floor(params[1]/2))
		

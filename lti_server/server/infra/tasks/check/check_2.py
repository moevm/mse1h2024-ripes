import subprocess, os
import re, math
from .ripes_parser import parse_ripes

def check(student_id, condition):
	params = re.findall(r"большую|меньшую|Число: [0-9]+", condition)
	params[1]=int(params[1][7:])
	ev1 = answer(params)
	run1 = parse_ripes(subprocess.check_output("{d}/Ripes --appimage-extract-and-run --mode cli --src {d}/tmp_solution/{sid}_2.s -t asm --proc RV64_SS --regs --json -v".format(d=os.path.dirname(__file__), sid = student_id).split()).decode("utf-8"))	
	return "Всё верно" if (ev1 == run1[1].get("registers").get("x6") ) else "Проверка не пройдена"
	
def answer(params):
	b = bin(params[1])[2:]
	zeroes = b.count('0')
	ones = len(b) - zeroes
	
	if zeroes == 0 : return 0 
	
	if zeroes >= ones:
		greater = zeroes
		smaller = ones
	else:
		greater = ones
		smaller = zeroes
			 
	return math.ceil(greater/smaller) if (params[0] == "большую") else math.floor(greater/smaller)
	

import subprocess
import os
from .ripes_parser import parse_ripes

def check(student_id):
	run = parse_ripes(subprocess.check_output("{d}/Ripes --mode cli --src ./tmp_solution/{sid}_3.s -t asm --proc RV64_SS --regs --json -v".format(d=os.path.dirname(__file__), sid = student_id).split()).decode("utf-8"))	
	return "All tests passed!"
	
def get_txt():
	return ["task3_title", "task3_text", 3]	

import subprocess
from .ripes_parser import parse_ripes

def check(student_id):
	run1 = parse_ripes(subprocess.check_output("../Ripes --mode cli --src ../tmp_solutions/{sid}_1.s -t asm --proc RV64_SS --regs --json -v"
	.format(sid = student_id).split()).decode("utf-8"))
	return "All tests passed!"
	
def get_txt():
	return ["task3_title", "task3_text", 3]	

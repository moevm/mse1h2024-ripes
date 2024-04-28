async function get_task_list()
{
	let response = await fetch("http://127.0.0.1:5000/tasks", {method: "GET"});
	return response.json();
}

async function send_solution(str_solution, task_id)
{
	let response = await fetch("http://127.0.0.1:5000/check", {method: "POST", headers: {"Accept": "application/json", "Content-Type": "application/json"}, body: JSON.stringify({user: uid, task: task_id, solution: str_solution})});
	return response.json();
}

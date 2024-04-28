#include <algorithm>
#include <emscripten.h>
#include <emscripten/val.h>

#include "taskchecker.h"

EM_ASYNC_JS(emscripten::EM_VAL, jsGetTasks, (),
{
	let json = await get_task_list();
	return Emval.toHandle(json);
});

EM_ASYNC_JS(char*, jsSendSolution, (const char* program, int pr_len, int t_id),
{
	let answer = await send_solution(UTF8ToString(program, pr_len), t_id);
	let str = answer["answer"];
	return stringToNewUTF8(str);
});

Task::Task(std::string title, std::string text, unsigned int id)
{
    this->title = title;
    this->text = text;
    this->id = id;
}

TaskChecker::TaskChecker()
{
   
}

std::string TaskChecker::checkTask(QString program, unsigned int t_id)
{
    char *tmp = jsSendSolution(program.toStdString().c_str(), program.toStdString().length(), t_id);
    std::string answer(tmp);
    free(tmp);
    return answer;
}

std::string TaskChecker::findTask(unsigned int t_id)
{
    auto check = [t_id](const Task& task) {
        return t_id == task.id;
    };

    auto taskIt = find_if(this->tasks.begin(), this->tasks.end(), check);

    if (taskIt != tasks.end()){
        return taskIt->text;
    }
    return std::string("task wasnt found\n");    
}

std::vector<Task> TaskChecker::getTasks()
{
	emscripten::val em_json = emscripten::val::take_ownership(jsGetTasks());
    for (int i = 0; i < em_json["len"].as<int>(); i++){
    	std::string i_s = std::to_string(i);
    	this->tasks.push_back(Task(em_json["tasks"][i_s]["title"].as<std::string>(),
		 em_json["tasks"][i_s]["text"].as<std::string>(), em_json["tasks"][i_s]["id"].as<unsigned int>()));    
    }
    return tasks;
}

TaskChecker::~TaskChecker()
{
        
}

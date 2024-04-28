#include <QString>

class Task{

public:
	Task(std::string title, std::string text, unsigned int id);
	std::string title;
	std::string text;
	unsigned int id;
};

class TaskChecker {

public:
	TaskChecker();
	~TaskChecker();
	std::string checkTask(QString program, unsigned int t_id);
	std::vector<Task> getTasks();
	std::string findTask(unsigned int t_id);
private:
	std::vector<Task> tasks;
};

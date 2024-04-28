#include "tasktab.h"
#include "ui_tasktab.h"
#include "processorhandler.h"
#include "io/iomanager.h"

#include <QObject>
#include <QComboBox>
#include <QPushButton>

namespace Ripes {
TaskTab::TaskTab(QToolBar *toolbar, EditTab *edittab, QWidget *parent)
    : RipesTab(toolbar, parent), m_ui(new Ui::TaskTab) {

	m_ui->setupUi(this);
	this->edittab = edittab;
	
	connect(m_ui->taskBox, &QComboBox::currentIndexChanged,
	this, &TaskTab::showTask);
	connect(m_ui->checkButton, &QPushButton::clicked, this, &TaskTab::checkTask);
	
	m_ui->taskBox->setEditable(true);
	m_ui->taskBox->setInsertPolicy(QComboBox::NoInsert);
	m_ui->taskBox->setPlaceholderText(QStringLiteral("Выберите задание"));
	m_ui->taskBox->setCurrentIndex(-1);

	m_ui->taskText->setReadOnly(true);
	m_ui->answerText->setReadOnly(true);
	m_ui->checkButton->setEnabled(false);
	
}

TaskTab::~TaskTab() { delete m_ui; }

void TaskTab::checkTask()
{
	std::string answer;
	auto res = ProcessorHandler::getAssembler()->assembleRaw(
      edittab->getAssemblyText(), &IOManager::get().assemblerSymbols());
  	
  	if (res.errors.size() == 0) {
		answer = taskchecker.checkTask(edittab->getAssemblyText(), currentTaskId);
	} else {
		answer = "No check for program with syntax errors";
	}
	m_ui->answerText->setPlainText(QString::fromStdString(answer));
}

void TaskTab::showTask()
{
	if(m_ui->taskBox->currentIndex() > -1){
		currentTaskId = m_ui->taskBox->itemData(m_ui->taskBox->currentIndex()).toUInt();
		std::string txt = taskchecker.findTask(currentTaskId);
		m_ui->taskText->setPlainText(QString::fromStdString(txt));
		m_ui->checkButton->setEnabled(true);
	} else {
		m_ui->checkButton->setEnabled(false);
	}	
}

void TaskTab::addTasksToTab(){
	if(m_ui->taskBox->count() == 0){
		std::vector<Task>tasks = taskchecker.getTasks();

		for (unsigned int i = 0; i < tasks.size(); i++){
			m_ui->taskBox->addItem(QString::fromStdString(std::to_string(tasks[i].id) + ": "+ tasks[i].title), tasks[i].id);
		}
	}	
}
}

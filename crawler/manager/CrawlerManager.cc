#include "CrawlerManager.hh"

#include <iostream>
#include <vector>

#include "../task/CrawlerTask.hh"

namespace manager {
// Vector of tasks to run
std::vector<crawler::CrawlerTask> taskQueue;
int completedTasks = 0;

void beginCrawling(std::string url, int maxDepth, int maxWidth,
                   bool logOnTaskComplete) {
    // Add a new task
    taskQueue.push_back(crawler::CrawlerTask(url, maxDepth, maxWidth));

    // Handle running the queue
    completedTasks = 0;
    crawler::init();
    while (taskQueue.size() > 0) {
        // Run the task
        taskQueue.front().run(taskQueue);

        // Remove the task from the queue
        taskQueue.erase(taskQueue.begin());

        // Incr the counter, and maybe log
        completedTasks++;
        if (logOnTaskComplete) {
            std::cout << "Completed crawl task #" << completedTasks
                      << std::endl;
        }
    }
    crawler::close();
}

int getCompletedTaskCount() { return completedTasks; }
}
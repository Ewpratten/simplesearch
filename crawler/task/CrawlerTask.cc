#include "CrawlerTask.hh"

#include <curlpp/cURLpp.hpp>

namespace crawler {

void init() { cURLpp::initialize(); }
void close() { cURLpp::terminate(); }

CrawlerTask::CrawlerTask(std::string url, int maxDepth, int maxWidth) {
    this->url = url;
    this->maxDepth = maxDepth;
    this->maxWidth = maxWidth;
}

void CrawlerTask::run(std::vector<CrawlerTask> &taskQueue) {}

void CrawlerTask::createNewSubTask(std::string url,
                                   std::vector<CrawlerTask> &taskQueue) {
    // If this depth is 1, it cannot create any more tasks
    if (this->maxDepth <= 1) {
        return;
    }

    // Add a new task with a smaller depth
    taskQueue.push_back(CrawlerTask(url, this->maxDepth - 1, this->maxWidth));
}

}  // namespace crawler
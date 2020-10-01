#include "CrawlerTask.hh"

#include <curlpp/Easy.hpp>
#include <curlpp/Exception.hpp>
#include <curlpp/Options.hpp>
#include <curlpp/cURLpp.hpp>
#include <iostream>

namespace crawler {

void init() { cURLpp::initialize(); }
void close() { cURLpp::terminate(); }

CrawlerTask::CrawlerTask(std::string url, int maxDepth, int maxWidth) {
    this->url = url;
    this->maxDepth = maxDepth;
    this->maxWidth = maxWidth;
}

void CrawlerTask::run(std::vector<CrawlerTask> &taskQueue) {
    // Get an easy handle
    cURLpp::Easy handle;

    // Begin the request
    try {
        handle.setOpt(cURLpp::Options::Url(this->url));
        handle.perform();
    } catch (cURLpp::LibcurlRuntimeError &e) {
        std::cout << "Invalid URL: " << this->url << std::endl;
        return;
    }
}

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
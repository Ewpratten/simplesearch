#if !defined(_SIMPLESEARCH_CRAWLER_TASK_CRAWLERTASK_HH)
#define _SIMPLESEARCH_CRAWLER_TASK_CRAWLERTASK_HH

#include <string>
#include <vector>

namespace crawler {
class CrawlerTask {
   public:
    CrawlerTask(std::string url, int maxDepth, int maxWidth);

    void run(std::vector<CrawlerTask> &taskQueue);
};
}  // namespace crawler

#endif  // _SIMPLESEARCH_CRAWLER_TASK_CRAWLERTASK_HH

#if !defined(_SIMPLESEARCH_CRAWLER_MANAGER_CRAWLERMANAGER_HH)
#define _SIMPLESEARCH_CRAWLER_MANAGER_CRAWLERMANAGER_HH

#include <string>

namespace manager {

void beginCrawling(std::string url, int maxDepth, int maxWidth,
                   bool logOnTaskComplete);

int getCompletedTaskCount();

}  // namespace manager

#endif  // _SIMPLESEARCH_CRAWLER_MANAGER_CRAWLERMANAGER_HH

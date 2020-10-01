#include <cxxopts.hpp>
#include <iostream>
#include <string>

#include "manager/CrawlerManager.hh"

int main(int argc, char *argv[]) {
    // Set up a program argument parser
    cxxopts::Options options("crawler", "Web crawler CLI for SimpleSearch");

    // Add program opts
    options.add_options()

        // URL to start at
        ("url", "Url to start crawling at", cxxopts::value<std::string>(),
         "URL")

        // Maximum depth
        ("d,depth", "Maximum recursive depth",
         cxxopts::value<int>()->default_value("5"))

        // Maximum width
        ("w,width", "Maximum number of branches per webpage",
         cxxopts::value<int>()->default_value("100"))

        // Program help
        ("h,help", "Print usage");

    // Parse
    auto args = options.parse(argc, argv);

    // Check if called without options
    if (args.count("help")) {
        std::cout << options.help() << std::endl;
        return 0;
    }

    if (!args.count("url")) {
        std::cout << "--url is required. See help (-h) for info" << std::endl;
        return 1;
    }

    // Begin crawling
    std::cout << "Beginning to crawl URL: " << args["url"].as<std::string>()
              << std::endl;
    manager::beginCrawling(args["url"].as<std::string>(),
                           args["depth"].as<int>(), args["width"].as<int>(),
                           true);
    std::cout << "Done crawling URL: " << args["url"].as<std::string>()
              << std::endl;
    std::cout << manager::getCompletedTaskCount() << " Tasks completed"
              << std::endl;

    return 0;
}

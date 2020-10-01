#include <cxxopts.hpp>

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

    return 0;
}

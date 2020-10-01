load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "task",
    srcs = [
        "CrawlerTask.cc",
        "CrawlerTask.hh",
    ],
    hdrs = [
        "CrawlerTask.hh",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//thirdparty/curlpp",
    ],
)

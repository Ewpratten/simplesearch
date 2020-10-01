load("@rules_cc//cc:defs.bzl", "cc_library")

cc_library(
    name = "manager",
    srcs = [
        "CrawlerManager.cc",
        "CrawlerManager.hh",
    ],
    hdrs = [
        "CrawlerManager.hh",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//crawler/task",
    ],
)

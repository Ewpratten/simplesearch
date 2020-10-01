load("@rules_cc//cc:defs.bzl", "cc_binary")

cc_binary(
    name = "crawler",
    srcs = [
        "main.cc",
    ],
    deps = [
        "@cxxopts",
        "//thirdparty/curlpp",
        "//crawler/manager"
    ],
)

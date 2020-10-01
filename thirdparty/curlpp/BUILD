load("@rules_foreign_cc//tools/build_defs:cmake.bzl", "cmake_external")

cmake_external(
    name = "curlpp",
    cache_entries = {
    },
    linkopts = [
        "-pthread",
    ],
    lib_source = "@curlpp//:all",
    static_libraries = ["libcurlpp.a"],
    visibility = ["//visibility:public"],
    deps = [
        "@curl",
    ],
)

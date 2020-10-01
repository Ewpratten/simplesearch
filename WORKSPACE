workspace(
    name = "simplesearch",
)

all_content = """filegroup(name = "all", srcs = glob(["**"]), visibility = ["//visibility:public"])"""

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# CMake
http_archive(
    name = "rules_foreign_cc",
    strip_prefix = "rules_foreign_cc-master",
    url = "https://github.com/bazelbuild/rules_foreign_cc/archive/master.zip",
)

load("@rules_foreign_cc//:workspace_definitions.bzl", "rules_foreign_cc_dependencies")

rules_foreign_cc_dependencies()

# NodeJS
http_archive(
    name = "build_bazel_rules_nodejs",
    sha256 = "4952ef879704ab4ad6729a29007e7094aef213ea79e9f2e94cbe1c9a753e63ef",
    urls = ["https://github.com/bazelbuild/rules_nodejs/releases/download/2.2.0/rules_nodejs-2.2.0.tar.gz"],
)

load("@build_bazel_rules_nodejs//:index.bzl", "node_repositories")

node_repositories(package_json = ["//server:package.json"])

# CXXOpts
http_archive(
    name = "cxxopts",
    build_file = "//thirdparty/cxxopts:BUILD",
    sha256 = "984aa3c8917d649b14d7f6277104ce38dd142ce378a9198ec926f03302399681",
    strip_prefix = "cxxopts-2.2.1",
    url = "https://github.com/jarro2783/cxxopts/archive/v2.2.1.tar.gz",
)

http_archive(
    name = "curl",
    build_file = "//thirdparty/curl:BUILD",
    strip_prefix = "curl-master",
    url = "https://github.com/curl/curl/archive/master.zip",
)

# cURLpp
http_archive(
    name = "curlpp",
    build_file_content = all_content,
    strip_prefix = "curlpp-master",
    url = "https://github.com/jpbarrette/curlpp/archive/master.zip",
)

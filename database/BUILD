load("@rules_python//python:defs.bzl", "py_library")
load("@py3_deps//:requirements.bzl", "requirement")

py_library(
    name = "database",
    srcs = [
        "database.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        requirement("tinydb"),
    ],
)

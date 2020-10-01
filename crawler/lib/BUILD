load("@rules_python//python:defs.bzl", "py_library")
load("@py3_deps//:requirements.bzl", "requirement")

# py_library(
#     name = "crawler",
#     srcs = [
#         "main.py",
#     ],
# )

py_library(
    name = "taskmanager",
    srcs = [
        "taskmanager.py",
    ],
    visibility = ["//visibility:public"],
    deps = [
        ":crawltask",
    ],
)

py_library(
    name = "crawltask",
    srcs = [
        "crawltask.py",
    ],
    deps = [
        requirement("requests"),
        requirement("BeautifulSoup4"),
    ],
)

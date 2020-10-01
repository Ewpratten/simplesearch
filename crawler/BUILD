load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
    name = "crawler",
    srcs = [
        "main.py",
    ],
    main = "main.py",
    deps = [
        "//crawler/lib:taskmanager",
    ],
)

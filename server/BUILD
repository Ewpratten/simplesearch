load("@rules_python//python:defs.bzl", "py_binary")
load("@py3_deps//:requirements.bzl", "requirement")

py_binary(
    name = "server",
    srcs = [
        "main.py",
    ],
    data = glob(["templates/*.html"]),
    main = "main.py",
    deps = [
        "//crawler/lib:taskmanager",
        "//database",
        requirement("flask"),
    ],
)

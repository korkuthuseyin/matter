// bindings.cpp
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

#include "matter.cpp"

namespace py = pybind11;

PYBIND11_MODULE(matter_sdk, m) {
    py::class_<MatterDevice>(m, "MatterDevice")
        .def(py::init<>())
        .def("initialize", &MatterDevice::initialize)
        .def("controlDevice", &MatterDevice::controlDevice);
}


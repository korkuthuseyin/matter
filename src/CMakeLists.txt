cmake_minimum_required(VERSION 3.10)

# Project name
project(MatterSDK)

# Specify C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the library
add_library(matter_sdk SHARED matter.cpp)

# Specify include directories (if any)
# target_include_directories(matter_sdk PRIVATE ${CMAKE_SOURCE_DIR}/include)


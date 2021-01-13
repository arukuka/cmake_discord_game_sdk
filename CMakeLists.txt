# Sets the minimal required CMake version to run this script
cmake_minimum_required(VERSION 3.13)

project(cmake_discord_game_sdk VERSION 0.1)

# `OS` contains your current operating system.
if (NOT OS)
    if (WIN32)
        set(OS Windows)
    elseif (APPLE)
        set(OS Macos)
    elseif (UNIX)
        set(OS Linux)
    else ()
        message(FATAL_ERROR "Cannot detect operating system")
    endif ()
    message(STATUS "OS was not defined, automatically set to ${OS}")
endif ()

# `ARCH` contains your current processor architecture.
if (NOT ARCH)
    message(WARNING "ARCH not defined, automatically set to x64")
    set(ARCH x86_64)
endif ()

# `ARCH` can be x86 only on Windows
if (ARCH STREQUAL "x86" AND NOT OS STREQUAL "Windows")
    message(FATAL_ERROR "x86 is only possible on Windows")
endif ()

### Configuration target (definitions + include dir)
set(CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME ${PROJECT_NAME}_config)

set(CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/c;${CMAKE_CURRENT_SOURCE_DIR}/cpp)

# Discord Game SDK version
set(DISCORD_GAME_SDK_V_MAJOR 2)
set(DISCORD_GAME_SDK_V_MINOR 5)
set(DISCORD_GAME_SDK_V_BUILD 6)

add_library(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME} INTERFACE)
target_include_directories(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME}
    INTERFACE ${CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR})
set_target_properties(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME} PROPERTIES INTERFACE_COMPILE_DEFINITIONS
    CMAKE_DISCORD_GAME_SDK_VERSION="${DISCORD_GAME_SDK_V_MAJOR}.${DISCORD_GAME_SDK_V_MINOR}.${DISCORD_GAME_SDK_V_BUILD}")

### Library target
set(CMAKE_DISCORD_GAME_SDK_TARGET_NAME ${PROJECT_NAME})

set(CMAKE_DISCORD_GAME_SDK_SOURCES
    cpp/achievement_manager.cpp
    cpp/activity_manager.cpp
    cpp/application_manager.cpp
    cpp/core.cpp
    cpp/image_manager.cpp
    cpp/lobby_manager.cpp
    cpp/network_manager.cpp
    cpp/overlay_manager.cpp
    cpp/relationship_manager.cpp
    cpp/storage_manager.cpp
    cpp/store_manager.cpp
    cpp/types.cpp
    cpp/user_manager.cpp
    cpp/voice_manager.cpp)

if (OS STREQUAL "Windows")
    if (ARCH STREQUAL "x86_64")
        set(CMAKE_DISCORD_GAME_SDK_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86_64/discord_game_sdk.dll.lib)
    else ()
        set(CMAKE_DISCORD_GAME_SDK_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86/discord_game_sdk.dll.lib)
    endif ()
elseif (OS STREQUAL "Linux")
    set(CMAKE_DISCORD_GAME_SDK_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86_64/discord_game_sdk.so)
elseif (OS STREQUAL "Macos")
    set(CMAKE_DISCORD_GAME_SDK_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86_64/discord_game_sdk.dylib)
endif ()

add_library(${CMAKE_DISCORD_GAME_SDK_TARGET_NAME} STATIC ${CMAKE_DISCORD_GAME_SDK_SOURCES})

target_link_libraries(${CMAKE_DISCORD_GAME_SDK_TARGET_NAME}
    PUBLIC ${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME} ${CMAKE_DISCORD_GAME_SDK_LIB_PATH})


### Unit tests target
set(CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME ${PROJECT_NAME}_tests)
set(CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_SOURCES
    tests/main.cpp)
add_executable(${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME} ${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_SOURCES})
target_link_libraries(${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME} ${CMAKE_DISCORD_GAME_SDK_TARGET_NAME})
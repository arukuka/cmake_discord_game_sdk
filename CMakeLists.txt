# Sets the minimal required CMake version to run this script
cmake_minimum_required(VERSION 3.13)

project(cmake_discord_game_sdk VERSION 0.1)

# Discord Game SDK version
set(CMAKE_DISCORD_GAME_SDK_V_MAJOR 2)
set(CMAKE_DISCORD_GAME_SDK_V_MINOR 5)
set(CMAKE_DISCORD_GAME_SDK_V_BUILD 6)

# Include directory target name
set(CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME ${PROJECT_NAME}_config)

# 64-bit target name
set(CMAKE_DISCORD_GAME_SDK_X64_TARGET_NAME ${PROJECT_NAME}_64)

# 32-bit target name
set(CMAKE_DISCORD_GAME_SDK_X86_TARGET_NAME ${PROJECT_NAME}_86)

# Include directory
set(CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/c;${CMAKE_CURRENT_SOURCE_DIR}/cpp)

# Sources
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

# 64-bit lib path
set(CMAKE_DISCORD_GAME_SDK_X64_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86_64/discord_game_sdk.dll.lib)

# 32-bit lib path
set(CMAKE_DISCORD_GAME_SDK_X64_LIB_PATH ${CMAKE_CURRENT_SOURCE_DIR}/lib/x86/discord_game_sdk.dll.lib)

##### Include directory target
add_library(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME} INTERFACE)
target_include_directories(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME}
    INTERFACE ${CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR})
set_target_properties(${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME} PROPERTIES
    INTERFACE_COMPILE_DEFINITIONS
    CMAKE_DISCORD_GAME_SDK_VERSION="${CMAKE_DISCORD_GAME_SDK_V_MAJOR}.${CMAKE_DISCORD_GAME_SDK_V_MINOR}.${CMAKE_DISCORD_GAME_SDK_V_BUILD}")

##### 64-bit target
add_library(${CMAKE_DISCORD_GAME_SDK_X64_TARGET_NAME} STATIC ${CMAKE_DISCORD_GAME_SDK_SOURCES})
target_link_libraries(${CMAKE_DISCORD_GAME_SDK_X64_TARGET_NAME}
    PUBLIC  ${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME}
    PRIVATE ${CMAKE_DISCORD_GAME_SDK_X64_LIB_PATH})
target_include_directories(${CMAKE_DISCORD_GAME_SDK_X64_TARGET_NAME} PUBLIC ${CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR})

##### 32-bit target
add_library(${CMAKE_DISCORD_GAME_SDK_X86_TARGET_NAME} STATIC ${CMAKE_DISCORD_GAME_SDK_SOURCES})
target_link_libraries(${CMAKE_DISCORD_GAME_SDK_X86_TARGET_NAME}
    PUBLIC  ${CMAKE_DISCORD_GAME_SDK_CONFIG_TARGET_NAME}
    PRIVATE ${CMAKE_DISCORD_GAME_SDK_X86_LIB_PATH})
target_include_directories(${CMAKE_DISCORD_GAME_SDK_X86_TARGET_NAME} PUBLIC ${CMAKE_DISCORD_GAME_SDK_INCLUDE_DIR})

##### Unit tests
set(CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME ${PROJECT_NAME}_tests)
set(CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_SOURCES
    tests/main.cpp)
add_executable(${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME} ${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_SOURCES})
target_link_libraries(${CMAKE_DISCORD_GAME_SDK_UNIT_TESTS_TARGET_NAME} ${CMAKE_DISCORD_GAME_SDK_X64_TARGET_NAME})
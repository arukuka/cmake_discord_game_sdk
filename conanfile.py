from conans import ConanFile, CMake, tools
from pprint import pprint

class CmakeDiscordGameSdkConan(ConanFile):
    name = "cmake_discord_game_sdk"
    version = "0.1"
    author = "syl <syleze.contact@gmail.com>"
    url = "https://github.com/SylEze/cmake_discord_game_sdk"
    description = "The Discord Game SDK bundled with a CMake buildsystem."
    topics = ("discord", "cmake", "sdk")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"

    exports_sources = [ 'CMakeLists.txt' ]

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ARCH"] = self.settings.arch
        cmake.definitions["OS"] = self.settings.os
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.definitions["ARCH"] = self.settings.arch
        cmake.definitions["OS"] = self.settings.os
        cmake.configure()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["cmake_discord_game_sdk"]


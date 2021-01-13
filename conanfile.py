from conans import ConanFile, CMake, tools


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

    exports_sources = [
        'CMakeLists.txt',
        'cpp/*',
        'c/*',
        'tests/*',
        'lib/*'
    ]

    def build(self):
        cmake = CMake(self)
        cmake.definitions["ARCH"] = self.settings.arch
        cmake.definitions["OS"] = self.settings.os
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="cpp")
        self.copy("*.h", dst="include", src="c")

        if self.settings.os == "Windows":
            if self.settings.arch == "x86_64":
                self.copy("*.dll", dst="bin", src="lib/x86_64")
                self.copy("*.lib", dst="lib", src="lib/x86_64")
            else:
                self.copy("*.dll", dst="bin", src="lib/x86")
                self.copy("*.lib", dst="lib", src="lib/x86")
        elif self.settings.os == "Linux":
            self.copy("*.so", dst="lib", src="lib/x86_64")
        elif self.settings.os == "Macos":
            self.copy("*.dylib", dst="lib", src="lib/x86_64")

    def package_info(self):
        self.cpp_info.libs = ["cmake_discord_game_sdk"]


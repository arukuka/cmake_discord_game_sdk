//! std
#include <string>
#undef NDEBUG
#include <cassert>

inline void test_version_defs()
{
    assert(CMAKE_DISCORD_GAME_SDK_VERSION == std::string("2.5.6"));
}
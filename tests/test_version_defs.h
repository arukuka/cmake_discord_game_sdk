//! std
#undef NDEBUG
#include <assert.h>
#include <string>

inline void test_version_defs()
{
    assert(CMAKE_DISCORD_GAME_SDK_VERSION == std::string("2.5.6"));
}
pkgname = "juce"
pkgver = "8.0.1"
pkgrel = 0
build_style = "cmake"
configure_args = ["-DJUCE_BUILD_EXTRAS=ON"]
hostmakedepends = ["cmake", "ninja", "pkgconf"]
makedepends = [
    "alsa-lib-devel",
    "flac-devel",
    "freetype-devel",
    "gtk+3-devel",
    "ladspa-sdk",
    "libcurl-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libvorbis-devel",
    "linux-headers",
    "zlib-ng-compat-devel",
]
depends = [
    "flac-devel",
    "libjpeg-turbo-devel",
    "libpng-devel",
    "libvorbis-devel",
    "zlib-ng-compat-devel",
]
pkgdesc = "Cross-platform framework for audio plugins"
maintainer = "Erica Z <zerica@callcc.eu>"
license = "GPL-3.0-only"
url = "https://juce.com"
source = (
    f"https://github.com/juce-framework/JUCE/archive/refs/tags/{pkgver}.tar.gz"
)
sha256 = "1a5aae997075ae2df045793fd47a4dc16234b2a7939d445fea17075219397b05"


def post_extract(self):
    # ensure these are never vendored
    for path in [
        "modules/juce_audio_formats/codecs/flac/libFLAC",
        "modules/juce_audio_formats/codecs/oggvorbis",
        "modules/juce_core/zip/zlib",
        "modules/juce_graphics/image_formats/jpglib",
        "modules/juce_graphics/image_formats/pnglib",
    ]:
        self.rm(path, recursive=True)


def post_install(self):
    self.install_bin("build/extras/Projucer/Projucer_artefacts/None/Projucer")


@subpackage("projucer")
def _(self):
    self.pkgdesc = "Cross-platform IDE for audio plugins"
    self.depends = [self.parent]

    return ["cmd:Projucer"]
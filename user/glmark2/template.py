pkgname = "glmark2"
pkgver = "2023.01"
pkgrel = 0
build_style = "meson"
configure_args = [
    "-Dflavors=drm-gl,drm-glesv2,wayland-gl,wayland-glesv2,x11-gl,x11-glesv2",
]
hostmakedepends = [
    "pkgconf",
    "meson",
    "cmake",
    "ninja",
]
makedepends = [
    "libpng-devel",
    "libjpeg-turbo-devel",
    "libgbm-devel",
    "wayland-devel",
    "wayland-protocols",
    "xserver-xorg-devel",
    "libdrm-devel",
    "libgl",
    "libegl",
    "libgles2",
]
pkgdesc = "OpenGL 2.0 and ES 2.0 benchmark"
maintainer = "metalparade <comer@live.cn>"
license = "GPL-3.0-or-later"
url = "https://github.com/glmark2/glmark2"
source = f"{url}/archive/refs/tags/{pkgver}.tar.gz"
sha256 = "8fece3fc323b643644a525be163dc4931a4189971eda1de8ad4c1712c5db3d67"

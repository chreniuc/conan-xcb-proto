#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
import os


class XCBProtoConan(ConanFile):
    name = "xcb-proto"
    version = "1.13"
    description = """The xcb-proto package provides the XML-XCB protocol
        descriptions that libxcb uses to generate the majority of its code and
        API. """
    url = "https://github.com/chreniuc/conan-xcb-proto"
    homepage = "https://xcb.freedesktop.org/"
    author = "Hreniuc Cristian-Alexandru <cristi@hreniuc.pw>"
    license = "GPL-3.0"
    exports = ["LICENSE"]
    settings = "os", "arch", "compiler", "build_type"

    source_subfolder = 'xcb-proto-%s' % version

    def source(self):
        archive_name = '%s.tar.gz' % self.source_subfolder
        # https://xcb.freedesktop.org/dist/xcb-proto-1.13.tar.gz
        tools.get('https://xcb.freedesktop.org/dist/%s' % archive_name)

    def build(self):
        with tools.chdir(self.source_subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            env_build.make()
            env_build.install()

    def package(self):
        install = os.path.join(self.build_folder, "package")
        self.copy(pattern="*", dst="lib", src=os.path.join(install, "lib"))
        self.copy(pattern="*", dst="share", src=os.path.join(install, "share"))
  

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "lib"))
        self.env_info.path.append(os.path.join(self.package_folder, "share"))
        self.env_info.path.append(os.path.join(self.package_folder))

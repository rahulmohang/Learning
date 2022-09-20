# Result of audit of OpenHarmony-3.0.1-LTS

## Table of contents

  * [Introduction](#introduction)
  - [1. First party components that have issues](#1-first-party-components-that-have-issues)
  - [1.1. applications.standard.hap@OpenHarmony-v3.0.1-LTS](#11-applicationsstandardhapopenharmony-v301-lts)
  - [1.2. base.update.packaging_tools@OpenHarmony-v3.0-LTS](#12-baseupdatepackagingtoolsopenharmony-v30-lts)
  - [1.3. developtools.profiler@OpenHarmony-v3.0-LTS](#13-developtoolsprofileropenharmony-v30-lts)
  - [1.4. foundation.ace.ace_engine@OpenHarmony-v3.0.1-LTS](#14-foundationaceaceengineopenharmony-v301-lts)
  - [1.5. applications.standard.hap@OpenHarmony-v3.0.1-LTS](#15-applicationsstandardhapopenharmony-v301-lts)
  - [1.6. base.update.packaging_tools@OpenHarmony-v3.0-LTS](#16-baseupdatepackagingtoolsopenharmony-v30-lts)
  - [1.7. foundation.graphic.standard@OpenHarmony-v3.0.1-LTS](#16-baseupdatepackagingtoolsopenharmony-v30-lts)
  * [2. Third party components that have issues](#2-third-party-components-that-have-issues)
  * [2.1. third_party.flutter@OpenHarmony-v3.0-LTS](#21-thirdpartyflutteropenharmony-v30-lts)
  * [2.2. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz](#22-thirdpartye2fsprogsopenharmony-v30-ltstarxz)
  * [2.3. third_party.ejdb@OpenHarmony-v3.0.1-LTS](#23-thirdpartyejdbopenharmony-v301-lts)
  * [2.4. third_party.libphonenumber@OpenHarmony-v3.0-Beta1](#24-thirdpartylibphonenumberopenharmony-v30-beta1)
  * [2.5. third_party.node@OpenHarmony-v3.0.1-LTS](#25-thirdpartynodeopenharmony-v301-lts)

  
## Introduction 
This document list the components that were audited to prepare a risk analysis of the first party and third party source code of OpenHarmony-3.0.1-LTS. The audit has been done and this intermediate report has been  prepared so that the team could take actions on issues, if any, much before the SBOMs are ready. By issues, we mean any findings that may need further action from either the Eclipse Oniro team, or the OpenHarmony team or a third party community.    

## 1. First party components that have issues 

### 1.1. applications.standard.hap@OpenHarmony-v3.0.1-LTS 
There is an image at the location, ‘applications.standard.hap@OpenHarmony-v3.0.1-LTS/Launcher.hap/assets/js/default/common/pics/img_wallpaper_default.jpg’. We found a copyright statement from Apple in the image ﬁle, 'img_wallpaper_default.jpg'. So, we suspect that the image may be
licensed by someone and we could not ﬁnd a license in the component for the image. So, please remove the image when you distribute the software. If the other images are from unknown sources, please remove them as well.

[Back to table of contents](#table-of-contents)

### 1.2. base.update.packaging_tools@OpenHarmony-v3.0-LTS
We have found the following binaries:
1. base.update.packaging_tools@OpenHarmony-v3.0-LTS/lib/libpackageL1.so
2. base.update.packaging_tools@OpenHarmony-v3.0-LTS/lib/libpackage.so

We could not find the corresponding source files in the source code. 

[Back to table of contents](#table-of-contents)

### 1.3. developtools.profiler@OpenHarmony-v3.0-LTS
We have found the following executables without a corresponding source code:
1. developtools.profiler@OpenHarmony-v3.0-LTS/trace_analyzer/prebuilts/trace_streamer.exe
2. developtools.profiler@OpenHarmony-v3.0-LTS/trace_analyzer/prebuilts/windows/trace_streamer.exe

The files could be related to Mac and Windows. 

[Back to table of contents](#table-of-contents)

### 1.4. foundation.ace.ace_engine@OpenHarmony-v3.0.1-LTS 
We have found binaries in the following folder:
foundation.ace.ace_engine@OpenHarmony-v3.0/frameworks/base/resource/binary/mac/. We could not verify if there are source files for the binaries.

[Back to table of contents](#table-of-contents)

### 1.5. applications.standard.hap@OpenHarmony-v3.0.1-LTS
The component source code tree contais contains predoiminantly, '.hap' files. The hap files contains files with the extension, '.bin', minified javascripts and some images. We have found the following files with the '.bin' extension. Javascript files with the same names has been found in the folders as well.

1. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/afterSelect/afterSelect.bin
2. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/app.bin
3. applications.standard.hap@OpenHarmony-v3.0.1-LTS/DeviceManager_UI.hap/assets/js/default/app.bin
4. applications.standard.hap@OpenHarmony-v3.0.1-LTS/DeviceManager_UI.hap/assets/js/default/pages/index/index.bin
5. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/main/main.bin
6. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/photoDetail/photoDetail.bin
7. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/photoList/photoList.bin
8. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/selectAlbum/selectAlbum.bin
9. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/selectAlbumPhoto/selectAlbumPhoto.bin
10. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap/assets/js/default/pages/videoList/videoList.bin
    
The following are the hap files:
1. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Airquality_Demo.hap
2. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Calc_Demo.hap
3. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Camera.hap
4. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Clock_Demo.hap
5. applications.standard.hap@OpenHarmony-v3.0.1-LTS/DeviceManager_UI.hap
6. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Ecg_Demo.hap
7. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Flashlight_Demo.hap
8. applications.standard.hap@OpenHarmony-v3.0.1-LTS/kikaInput.hap
9. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Launcher.hap
10. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Launcher_Recents.hap
11. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Launcher_Settings.hap
12. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Music_Demo.hap
13. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Photos.hap
14. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Settings.hap
15. applications.standard.hap@OpenHarmony-v3.0.1-LTS/Shopping_Demo.hap
16. applications.standard.hap@OpenHarmony-v3.0.1-LTS/SystemUI-NavigationBar.hap
17. applications.standard.hap@OpenHarmony-v3.0.1-LTS/SystemUI-StatusBar.hap
18. applications.standard.hap@OpenHarmony-v3.0.1-LTS/SystemUI-SystemDialog.hap

[Back to table of contents](#table-of-contents)

### 1.6. base.update.packaging_tools@OpenHarmony-v3.0-LTS 
Binaries found in the location, 'base.update.packaging_tools@OpenHarmony-v3.0-LTS/lib'

[Back to table of contents](#table-of-contents)

### 1.7. foundation.graphic.standard@OpenHarmony-v3.0.1-LTS
Binaries found:
foundation.graphic.standard@OpenHarmony-v3.0.1-LTS/frameworks/bootanimation/data/bootanimation-480x960.raw
We could not find the license information or the corresponding source code.

[Back to table of contents](#table-of-contents)

## 2. Third party components that have issues 

### 2.1. third_party.flutter@OpenHarmony-v3.0-LTS
Binaries found in the following locations: 
third_party_flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/opencl-lib/3-0/lib
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/cpp/ext/redist/icu4c-4_6_1-Win32-msvc10.zip/icu/lib
third_party.flutter@OpenHarmony-v3/skia/third_party/externals/icu/windows/icudt.dll

Java archive files were found in the scan of the source code.

third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/libwebp/gradle/wrapper/gradle-wrapper.jar
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/libwebp/swig/libwebp.jar
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/java/lib/jcommander-1.27.jar
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/java/lib/junit-4.10.jar
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/java/lib/icu4j-4_8_1_1.jar
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/java/lib/icu4j-charset-4_8_1_1.jar

We have not found the corresponding source code.

There are executable files at the following locations:

third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sdl/premake/MinGW/build-scripts/premake4.exe
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sdl/premake/VisualC/build-scripts/premake4.exe
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sdl/premake/Cygwin/build-scripts/premake4.exe
third_party.flutter@OpenHarmony-v3.0-LTS/skia/third_party/externals/sfntly/cpp/ext/redist/cmake-2.8.5-win32-x86.zip/cmake-2.8.5-win32-x86/bin

The files may not be relevant in the context of embedded linux projects. But, there is no corresponding source code found.

[Back to table of contents](#table-of-contents)

### 2.2. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz 
Binaries found in the following folders: 
1. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz/prebuilt/host/bin
2. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz/prebuilt/target/bin
3. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz/prebuilt/target/lib

We have not found corresponding source code files in the folders

[Back to table of contents](#table-of-contents)

### 2.3. third_party.ejdb@OpenHarmony-v3.0.1-LTS
We have found the following java archive files without corresponding source code:

1. third_party.ejdb@OpenHarmony-v3.0/src/bindings/ejdb2_flutter/android/gradle/wrapper/gradle-wrapper.jar

[Back to table of contents](#table-of-contents)

### 2.4. third_party.libphonenumber@OpenHarmony-v3.0-Beta1
There are many java archive files in the source code:
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/java/demo/war/WEB-INF/lib/commons-lang-2.6.jar
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/java/demo/war/WEB-INF/lib/commons-io-1.4.jar
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/java/demo/war/WEB-INF/lib/commons-fileupload-1.2.1.jar
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/java/lib/junit-4.8.1.jar
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/tools/java/cpp-build/target/cpp-build-1.0-SNAPSHOT-jar-with-dependencies.jar
third_party.libphonenumber@OpenHarmony-v3.0-Beta1/tools/java/java-build/target/java-build-1.0-SNAPSHOT-jar-with-dependencies.jar

There are no complete corresponding source files.

[Back to table of contents](#table-of-contents)

### 2.5. third_party.node@OpenHarmony-v3.0.1-LTS
The binary, 'third_party.node@OpenHarmony-v3.0.1-LTS/deps/brotli/c/common/dictionary.bin' is in the sources. There are two files called dictionary.c and dictionary.h. We are not sure if mentioned files are used to create the binaries.

[Back to table of contents](#table-of-contents)


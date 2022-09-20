# Result of audit of OpenHarmony-3.0.1-LTS

## Table of contents

  * [Introduction](#introduction)
  - [1. First party components that have issues](#1-first-party-components-that-have-issues)
  - [1.1. applications.standard.hap@OpenHarmony-v3.0.1-LTS](#11-applicationsstandardhapopenharmony-v301-lts)
  - [1.2. base.update.packaging_tools@OpenHarmony-v3.0-LTS](#12-baseupdatepackagingtoolsopenharmony-v30-lts)
  - [1.3. base.update.updater@OpenHarmony-v3.0-LTS](#13-baseupdateupdateropenharmony-v30-lts)
  - [1.4. developtools.profiler@OpenHarmony-v3.0-LTS](#14-developtoolsprofileropenharmony-v30-lts)
  - [1.5. foundation.ace.ace_engine@OpenHarmony-v3.0.1-LTS](#15-foundationaceaceengineopenharmony-v301-lts)
  - [1.6. foundation.graphic.standard@OpenHarmony-v3.0.1-LTS](#16-foundationgraphicstandardopenharmony-v301-lts)
  * [2. Third party components that have issues](#2-third-party-components-that-have-issues)
  * [2.1. third_party.flutter@OpenHarmony-v3.0-LTS](#21-thirdpartyflutteropenharmony-v30-lts)
  * [2.2. third_party_e2fsprogs@OpenHarmony-v3.0-LTS.tar.xz](#22-thirdpartye2fsprogsopenharmony-v30-ltstarxz)
  * [2.3. third_party.ejdb@OpenHarmony-v3.0.1-LTS](#23-thirdpartyejdbopenharmony-v301-lts)
  * [2.4. third_party.libphonenumber@OpenHarmony-v3.0-Beta1](#24-thirdpartylibphonenumberopenharmony-v30-beta1)
  * [2.5. third_party.node@OpenHarmony-v3.0.1-LTS](#25-thirdpartynodeopenharmony-v301-lts)
  * [2.6. third_party.boringssl@OpenHarmony-v3.0.1-LTS](#26-thirdpartyboringsslopenharmony-v301-lts)
  * [2.7. third_party.icu@OpenHarmony-v3.0.1-LTS](#27-thirdpartyicuopenharmony-v301-lts)
  * [2.8. third_party.grpc@OpenHarmony-v3.0.1-LTS](#28-thirdpartygrpcopenharmony-v301-lts)
  * [2.9. third_party.toybox@OpenHarmony-v3.0-LTS](#29-thirdpartytoyboxopenharmony-v30-lts)

  
## Introduction 
This document list the components that were audited to prepare a risk analysis of the first party and third party source code of OpenHarmony-3.0.1-LTS. The audit has been done and this intermediate report has been  prepared so that the team could take actions on issues, if any, much before the SBOMs are ready. By issues, we mean any findings that may need further action from either the Eclipse Oniro team, or the OpenHarmony team or a third party community.    

## 1. First party components that have issues 

### 1.1. applications.standard.hap@OpenHarmony-v3.0.1-LTS 
There is an image at the location, ‘applications.standard.hap@OpenHarmony-v3.0.1-LTS/Launcher.hap/assets/js/default/common/pics/img_wallpaper_default.jpg’. We found a copyright statement from Apple in the image, 'img_wallpaper_default.jpg'. So, we suspect that the image may be
licensed by someone and we could not ﬁnd a license in the component for the image. So, please remove the image when you distribute the software. If the other images are from unknown sources, please remove them as well.

[Back to table of contents](#table-of-contents)

### 1.2. base.update.packaging_tools@OpenHarmony-v3.0-LTS
We have found the following binaries:
1. base.update.packaging_tools@OpenHarmony-v3.0-LTS/lib/libpackageL1.so
2. base.update.packaging_tools@OpenHarmony-v3.0-LTS/lib/libpackage.so

We could not find the corresponding source files in the source code. 

[Back to table of contents](#table-of-contents)

### 1.3. base.update.updater@OpenHarmony-v3.0-LTS
We have found the following binaries without source code in a test folders. So, we assume that it is not an issue. Please verify. 

base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/allCmdUnitTest.bin
base.update.updater@OpenHarmony-v3/test/fuzztest/fuzz_src_data/libthirdInstruction.z.so
base.update.updater@OpenHarmony-v3/test/unittest/test_data/src/libthirdInstruction.z.so


Binary files found in test folder:

1. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/src/libthirdInstruction.z.so
2. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_lz4.img_patch/ImgageDiffPatchLz4File_1_lz4
3. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_3_lz4.img_patch/ImgageDiffPatchLz4File_3_lz4
4. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchZipFile_1_zip.img_patch/ImgageDiffPatchZipFile_1_zip
5. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchZipFile_3_zip.img_patch/ImgageDiffPatchZipFile_3_zip
6. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/PatchGztest_gz.img_patch/PatchGztest_gz
7. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/PatchLz4test_lz4.img_patch/PatchLz4test_lz4
8. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/patchtest.img_patch/patchtest
9. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/patchtest.patch/patchtest
10. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_lz4_new.lz
11. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_new.lz
12. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_old.lz
13. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_3_lz4_new.lz
14. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_new.lz
15. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_1_old.lz
16. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_3_lz4_new.lz
17. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_3_new.lz4
18. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchLz4File_3_old.lz4
19. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchZipFile_2_zip.img_patch
20. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchZipFile_4_zip.img_patch
21. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/ImgageDiffPatchZipFile_zip.img_patch
22. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/PatchLz4test_lz4_new.lz
23. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/PatchLz4test_new.lz4
24. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/diffpatch/PatchLz4test_old.lz4
25. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/applypatch/TestGZipModeImagePatch.gz.patch
26. base.update.updater@OpenHarmony-v3.0-LTS/test/unittest/test_data/applypatch/zip-patch-file

There are binaries without sources in the following zip files:

1. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_diff_1.zip
2. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/unsign_updater.zip
3. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_success.zip
4. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_without_updater_binary.zip
5. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_binary_abnormal.zip
6. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/raw_image_write.zip
7. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/parts/updatestatus01.zip
8. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/parts/updaterpart01.zip
9. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/parts/updatestatus02.zip
10. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/parts/updaterpart02.zip
11. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/parts/updatestatus03.zip
12. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_with_incorrect_binary.zip
13. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater_diff_2.zip
14. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/updater.zip
15. base.update.updater@OpenHarmony-v3/test/unittest/test_data/updater/wrong_hash_updater.zip

The files may not be used to build images. Please verify.

[Back to table of contents](#table-of-contents)

### 1.4. developtools.profiler@OpenHarmony-v3.0-LTS
We have found the following executables without a corresponding source code:
1. developtools.profiler@OpenHarmony-v3.0-LTS/trace_analyzer/prebuilts/trace_streamer.exe
2. developtools.profiler@OpenHarmony-v3.0-LTS/trace_analyzer/prebuilts/windows/trace_streamer.exe

The files could be related to Mac and Windows. 

We have found the following binary file in a test folder. We could not find the corresponding source code. 

1. developtools.profiler@OpenHarmony-v3.0-LTS/trace_analyzer/test/resource/htrace.bin

[Back to table of contents](#table-of-contents)

### 1.5. foundation.ace.ace_engine@OpenHarmony-v3.0.1-LTS 
We have found binaries in the following folder:
foundation.ace.ace_engine@OpenHarmony-v3.0/frameworks/base/resource/binary/mac/. We could not verify if there are source files for the binaries.

[Back to table of contents](#table-of-contents)

### 1.6. foundation.graphic.standard@OpenHarmony-v3.0.1-LTS
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

The following binaries were found in samples folder:
third_party.flutter@OpenHarmony-v3/skia/third_party/externals/icu/source/samples/ucnv/data02.bin

The files may not be used to build images. Please verify.

The following binaries were found in test folders:
third_party.flutter@OpenHarmony-v3/flutter/packages/flutter_tools/test/data/intellij/plugins/flutter-intellij.jar
third_party.flutter@OpenHarmony-v3/flutter/packages/flutter_tools/test/data/intellij/plugins/Dart/lib/Dart.jar

The files may not be used to build images. Please verify. 

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

We have found the following java archive files in the tests and test folders respectively:
1. third_party.ejdb@OpenHarmony-v3.0/src/bindings/ejdb2_react_native/tests/android/gradle/wrapper/gradle-wrapper.jar
2. third_party.ejdb@OpenHarmony-v3.0/src/bindings/ejdb2_android/test/gradle/wrapper/gradle-wrapper.jar

We have found the following jaa archive files in example folder:

1. third_party.ejdb@OpenHarmony-v3.0/src/bindings/ejdb2_flutter/example/android/gradle/wrapper/gradle-wrapper.jar

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
The binary, 'third_party.node@OpenHarmony-v3.0.1-LTS/deps/brotli/c/common/dictionary.bin' is in the sources folders. There are two files called dictionary.c and dictionary.h. We are not sure if mentioned files are used to create the binaries.

We have found the following executables:
third_party.node@OpenHarmony-v3.0.1-LTS/deps/npm/node_modules/term-size/vendor/macos/term-size
third_party.node@OpenHarmony-v3.0.1-LTS/deps/npm/node_modules/term-size/vendor/windows/term-size.exe

From the names of the folders, it could be assumed that the executables are used for macos and windows.

The following archive files with binaries inside were found in a test folders:
third_party.node@OpenHarmony-v3.0/deps/npm/test/fixtures/github-com-BryanDonovan-dummy-npm-bar.git.tar.gz
third_party.node@OpenHarmony-v3.0/deps/npm/test/fixtures/github-com-BryanDonovan-npm-git-test.git.tar.gz
third_party.node@OpenHarmony-v3.0/deps/npm/test/fixtures/github-com-BryanDonovan-dummy-npm-buzz.git.tar.gz
third_party.node@OpenHarmony-v3.0/deps/npm/test/fixtures/github-com-BryanDonovan-dummy-npm-foo.git.tar.gz

We assume that it is not an issue. Please verify. 

The following binary was found in a test folder:
third_party.node@OpenHarmony-v3.0.1-LTS/test/fixtures/google_ssl_hello.bin

[Back to table of contents](#table-of-contents)

### 2.6. third_party.boringssl@OpenHarmony-v3.0.1-LTS
There are binaries without corresponding source code in the following folders:

1. third_party.boringssl@OpenHarmony-v3.0.1-LTS/src/util/ar/testdata/linux
2. third_party.boringssl@OpenHarmony-v3.0.1-LTS/src/util/ar/testdata/mac
3. third_party.boringssl@OpenHarmony-v3.0.1-LTS/src/util/ar/testdata/windows

These files could be test data. So, they may not be used. Please verify. 

[Back to table of contents](#table-of-contents)


### 2.7. third_party.icu@OpenHarmony-v3.0.1-LTS
We found the following binaries without corresponding source code:

1. third_party.icu@OpenHarmony-v3.0.1-LTS/icu4c/source/test/testdata/uni-text.bin
2. third_party.icu@OpenHarmony-v3.0.1-LTS/icu4c/source/test/testdata/importtest.bin
3. third_party.icu@OpenHarmony-v3.0.1/icu4c/source/samples/ucnv/data02.bin

The files were found in test and sample folders. So, they may not be used. Please verify.   

[Back to table of contents](#table-of-contents)

### 2.8. third_party.grpc@OpenHarmony-v3.0.1-LTS
We found the following binaries without corresponding source code:

1	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/client_fuzzer_corpus/data_frame.bin
2	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/client_fuzzer_corpus/hdr_frame.bin
3	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/client_fuzzer_corpus/settings_frame_1.bin
4	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a7e64803.bin
5	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/18f00b5f.bin
6	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/58b88a24.bin
7	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/459c0bf6.bin
8	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/6499e2db.bin
9	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/67b04816.bin
10	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/fd26e0a6.bin
11	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b1128694.bin
12	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/5780565e.bin
13	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/ff227015.bin
14	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0d10bb63.bin
15	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/90224b8e.bin
16	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/21a2dcda.bin
17	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/22ad891a.bin
18	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0aa7b949.bin
19	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/5f758756.bin
20	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/eb66106b.bin
21	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/e2c954e1.bin
22	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/5429f0da.bin
23	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c4534867.bin
24	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/93beeba2.bin
25	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/55f6fb1a.bin
26	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/8da521d9.bin
27	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/3e3ae35a.bin
28	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/954337ef.bin
29	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/1f992057.bin
30	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/e9d96662.bin
31	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/2c6660ba.bin
32	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/aa3c8974.bin
33	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/32b11997.bin
34	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/27ac2ae2.bin
35	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/4558ddeb.bin
36	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/8de81717.bin
37	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/8338ebee.bin
38	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a24bf2dc.bin
39	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/aa825693.bin
40	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/d9074e68.bin
41	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/bfcbffa9.bin
42	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/86e6dbf2.bin
43	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/10724098.bin
44	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b28959dd.bin
45	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c35968bf.bin
46	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/97aed4bd.bin
47	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0f700e05.bin
48	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/d0f7eebc.bin
49	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f3220426.bin
50	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/e0d9a9a7.bin
51	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f74b9428.bin
52	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/cdba6c45.bin
53	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a3a2b1af.bin
54	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/53de507f.bin
55	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b924c842.bin
56	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/4aa883d0.bin
57	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f5c877c4.bin
58	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/7f15bbce.bin
59	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/57918260.bin
60	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c1188b44.bin
61	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/9bf7553a.bin
62	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/1cfdde7a.bin
63	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/41b31ef0.bin
64	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/326ec4d5.bin
65	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/65099066.bin
66	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/5435005f.bin
67	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/dab172ff.bin
68	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/59dcfde4.bin
69	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/7ffd05db.bin
70	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0384345c.bin
71	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f826100f.bin
72	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/eba8472a.bin
73	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/5d817877.bin
74	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b06ce623.bin
75	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/d6979f0f.bin
76	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/e3bab014.bin
77	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/282b6585.bin
78	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c43d97f2.bin
79	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/42b0afca.bin
80	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/746715fe.bin
81	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/2e4805c3.bin
82	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/3de41f3f.bin
83	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/330ad4b6.bin
84	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0abd533e.bin
85	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/ed8da77f.bin
86	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/1ea5651f.bin
87	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/033dd2f6.bin
88	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a9e22d93.bin
89	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b829143b.bin
90	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/1e92aaa5.bin
91	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/6dc4455c.bin
92	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c559f565.bin
93	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/4d55d5ae.bin
94	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c81dec02.bin
95	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/11516d58.bin
96	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/69891e9f.bin
97	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/90240c7c.bin
98	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/3e787760.bin
99	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/6e050e98.bin
100	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/422708b4.bin
101	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b431df13.bin
102	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/2814d70c.bin
103	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a357658d.bin
104	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/37ec9df8.bin
105	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/a5348197.bin
106	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/b5acaa52.bin
107	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/021ec59f.bin
108	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/fe66893c.bin
109	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/407607d2.bin
110	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/652bfdce.bin
111	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/aa8729d7.bin
112	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/fb3b0d80.bin
113	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/cca29902.bin
114	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/c66e84d1.bin
115	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f4024b01.bin
116	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/3ca5da2f.bin
117	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/44f342a6.bin
118	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/39ea47bb.bin
119	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/88e1329b.bin
120	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/be9b6e78.bin
121	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/540ada69.bin
122	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/8b186384.bin
123	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/34bba9e4.bin
124	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0ff4d220.bin
125	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/51a1abd1.bin
126	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/1a69d5fc.bin
127	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/hope.bin
128	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/e2652fbb.bin
129	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/597fdab5.bin
130	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/0b275a7f.bin
131	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/4eb269c3.bin
132	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/25ab638f.bin
133	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/3224e6cd.bin
134	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/da7e44a9.bin
135	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/f541d27e.bin
136	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/01c008fa.bin
137	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/bad4f467.bin
138	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/21475569.bin
139	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/422fa704.bin
140	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/ff898c08.bin
141	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/ad810f7f.bin
142	third_party.grpc@OpenHarmony-v3.0/test/core/end2end/fuzzers/server_fuzzer_corpus/54d0fc6c.bin

We have found the following java archive files:
1. third_party.grpc@OpenHarmony-v3.0/src/android/test/interop/gradle/wrapper/gradle-wrapper.jar
2. third_party.grpc@OpenHarmony-v3.0/examples/android/helloworld/gradle/wrapper/gradle-wrapper.jar

The files were found in test and example folders. So, they may not be used. Please verify.   

[Back to table of contents](#table-of-contents)

### 2.9. third_party.toybox@OpenHarmony-v3.0-LTS
We have found the following binary file in the test folder:
third_party.toybox@OpenHarmony-v3.0-LTS/tests/files/java.class

[Back to table of contents](#table-of-contents)

# Result of audit of Eclipse Oniro Goofy release

## Table of contents

  * [Introduction](#introduction)
  - [1. Third party components that have issues](#1-third-party-components-that-have-issues)
  - [1.1. firmware-imx@8.15-r0-c54a37db](#11-firmware-imx815-r0-c54a37db)
  - [1.2. intel-media-driver@22.3.1-r0-11c2246d](#12-intel-media-driver2231-r0-11c2246d)
  - [1.3. intel-mediasdk@22.1.0-r0-6c8a31a6](#13-intel-mediasdk2210-r0-6c8a31a6)
  - [1.4. linux-firmware@20220411-r0-1a6a4201](#14-linux-firmware20220411-r0-1a6a4201)
  - [1.5. linux-intel@5.10.100+gitAUTOINC+64fb693a6c_8e5c6f8269-r0-5edf7c20](#15-linux-intel510100gitautoinc64fb693a6c8e5c6f8269-r0-5edf7c20)
  - [1.6. python3@3.10.4-r0-3eeee379](#16-python33104-r0-3eeee379)
  - [1.7. shared-mime-info@2.1-r0-1abd20e0](#17-shared-mime-info21-r0-1abd20e0)
  - [1.8. zephyr-philosophers@3.0.0+gitAUTOINC+4f8d78ceeb_b0612c97c1-r0-cc89ed88](#18-zephyr-philosophers300gitautoinc4f8d78ceebb0612c97c1-r0-cc89ed88)
  * [2. Third party components that are clear in the initial audit](#2-third-party-components-that-are-clear-in-the-initial-audit)
  - [3. Third party components with binaries in the source tree](#3-third-party-components-with-baniaries-in-the-source-tree)
  * [4. List of image files found in the sources of third party components](#4-list-of-image-files-found-in-the-sources)
  - [5. List of audio files found in sources of third party components](#5-list-of-audio-files-found-in-sources)
  * [6. List of video files found in sources of third party components](#6-list-of-video-files-found-in-sources)

## Introduction 
This document list the components that were audited to prepare a risk analysis of the third party source code of the Goofy release of the Eclipse Oniro project. The audit has been done and this intermediate report has been  prepared so that the team could take actions on issues, if any, much before the SBOMs are ready. By issues, we mean any findings that may need further action from either the Eclipse Oniro team or a third party community.    

## 1. Third party components that have issues 

### 1.1. firmware-imx@8.15-r0-c54a37db 
The NXP Software License Agreement does not seem to cover the use case of Oniro.
All the rights granted to licensee are based on whether the licensee's product is a "Authorized System" or not. The definition of 'Authorized System' is the following:
1.2    "Authorized System" means either (i) Licensee's hardware product which
incorporates an NXP Product or (ii) Licensee's software program which is used
exclusively in connection with an NXP Product and with which the Licensed
Software will be integrated.

Oniro is not a program that is 'used exclusively' in connection with an NXP Product 'and' with which the Licensed Software will be integrated.

So, the following are the priliminary conclusions:

1. making Seco-IMX images available as pipeline artifacts is not allowed by the license (redistribution rights are tied to the physical device which embeds NXP components, and also demonstration use is expressly restricted)
2. making such images available to developers only internally (eg. in a private storage) would not be allowed, too, - but the risk would be lower
3. in any case a risk minimization approach would not be consistent with the spirit anettle@3.7.3-r0-56dac4cand the goals of the Oniro project; we should seek compliance, since we publicly and transparently claim that we are compliant
4. Work with NXP to upstream their firmware into linux-firmware package thereby removing the need for an EULA

The only clean solutions could be:

either have such images internally built and tested only by Seco (not very practical, though)
or ask upstream (NXP) for an explicit permission, or to release the software as FOSS


Please follow the issue, https://git.ostc-eu.org/oss-compliance/sbom/private_bom/-/issues/25 for further information. 

[Back to table of contents](#table-of-contents)

### 1.2. intel-media-driver@22.3.1-r0-11c2246d
The license header in the following files do not have explicit grant of rights to use or redistribute:
https://github.com/intel/media-driver/blob/master/media_driver/agnostic/common/vp/hal/vphal_render_16alignment.h
https://github.com/intel/media-driver/blob/master/media_driver/agnostic/common/vp/hal/vphal_render_16alignment.cpp

The license text is just a disclaimer:

"
INTEL MAKES NO WARRANTY OF ANY KIND REGARDING THE CODE. THIS CODE IS
LICENSED ON AN "AS IS" BASIS AND INTEL WILL NOT PROVIDE ANY SUPPORT,
ASSISTANCE, INSTALLATION, TRAINING OR OTHER SERVICES. INTEL DOES NOT
PROVIDE ANY UPDATES, ENHANCEMENTS OR EXTENSIONS. INTEL SPECIFICALLY
DISCLAIMS ANY WARRANTY OF MERCHANTABILITY, NONINFRINGEMENT, FITNESS FOR ANY
PARTICULAR PURPOSE, OR ANY OTHER WARRANTY. Intel disclaims all liability,
including liability for infringement of any proprietary rights, relating to
use of the code. No license, express or implied, by estoppel or otherwise,
to any intellectual property rights is granted herein.
"


An issue has been opened in the github page of the upstream project:
https://github.com/intel/media-driver/issues/1460

Please follow the issue, https://git.ostc-eu.org/oss-compliance/sbom/private_bom/-/issues/53 for further information.

[Back to table of contents](#table-of-contents)

### 1.3. intel-mediasdk@22.1.0-r0-6c8a31a6
1. The following files have references to license agreements from Intel, but the corresponding license agreement has not been not found:
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/dumps/dump_mfxfei.cpp
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/Properties/AssemblyInfo.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/ConfigManager.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/EtlDataCollector.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/EtlToTextConverter.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/Import.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/MsdkAnalyzerCpp.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/Program.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/SdkAnalyzerForm.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/SdkAnalyzerForm.Designer.cs
intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/tools/tracer/gui/WinApi.cs

An issue has been raised upstream and has been fixed.The issue could be found at https://github.com/Intel-Media-SDK/MediaSDK/issues/2937.

2. The header of the file, 'intel-mediasdk@22.1.0-r0-6c8a31a6/github.com.Intel-Media-SDK.MediaSDK.git@0db73aa1.tar.xz/contrib/ipp/src/ippversion.h' has the following statement:

"No part of the Material may be used,
// copied, reproduced, modified, published, uploaded, posted, transmitted,
// distributed or disclosed in any way without Intel's prior express written
// permission. No license under any patent, copyright or other intellectual
// property rights in the Material is granted to or conferred upon you,
// either expressly, by implication, inducement, estoppel or otherwise.
// Any license under such intellectual property rights must be express and
// approved by Intel in writing."

Getting a written agreement from Intel is no practical. An issue has been raised upstream and has been fixed:
https://github.com/Intel-Media-SDK/MediaSDK/issues/2937

[Back to table of contents](#table-of-contents)

### 1.4. linux-firmware@20220411-r0-1a6a4201
1. The following license text was found in linux-firmware@20220411-r0-1a6a4201/linux-firmware-20220411.tar.xz/linux-firmware-20220411/WHENCE:
"

The firmware this driver downloads into the tokenring card is a
separate program and is not GPL'd source code, even though the Linux
side driver and the routine that loads this data into the card are.


This firmware is licensed to you strictly for use in conjunction
with the use of 3Com 3C359 TokenRing adapters. There is no
waranty expressed or implied about its fitness for any purpose.
"

The file in Fossology could be found at https://100.91.115.62/repo/?mod=view-license&upload=1200&item=7748232&page=0.
The firmware is licensed to us strictly to be used in conjunction with the use of 3Com 3C359 ToeknRing adapters. There is no mention of distribution. If the 'use' covers distribution, should we interpret that distribution should only be in conjunction with the use of 3Com 3C359 TokenRing adapters?

2. The following statement has been found in the section, '4.TERMINATION' in the license agreement from QUALCOMM:
   
"4. TERMINATION. This Agreement shall be effective upon acceptance, or access or
use of the Materials (whichever occurs first) by You and shall continue until
terminated. You may terminate the Agreement at any time by deleting and
destroying all copies of the Materials and all related information in Your
possession or control. This Agreement terminates immediately and automatically,
with or without notice, if You fail to comply with any provision hereof.
Additionally, QTI may at any time terminate this Agreement, without cause, upon
notice to You. Upon termination You must, to the extent possible, delete or
destroy all copies of the Materials in Your possession and the license granted
to You in this Agreement shall terminate. Sections 1.2 through 10 shall survive
the termination of this Agreement. In the event that any restrictions,
conditions, limitations are found to be either invalid or unenforceable, the
rights granted to You in Section 1 (License) shall be null, void and ineffective
from the Effective Date, and QTI shall also have the right to terminate thisnettle@3.7.3-r0-56dac4ca
Agreement immediately, and with retroactive effect to the effective date."
File - linux-firmware@20220411-r0-1a6a4201/linux-firmware-20220411.tar.xz/linux-firmware-20220411/LICENSE.qcom
Link to Fossology upload of the component - https://100.91.115.62/repo/?mod=view-license&upload=1200&item=7746579

As per a statement in the license text, an unconditional termination is possible if QUALCOMM chooses to do so. This is a risk.

An issue has been raised in gitlab. Please check 'https://git.ostc-eu.org/oss-compliance/sbom/private_bom/-/issues/35'.

3. Files in the folders, 'linux-firmware@20220411-r0-1a6a4201/_tagged/oniro/kirkstone-v1.0.0-rc-340-gc066689/oniro-linux/seco-imx8mm-c61-4gb/github.com.murata-wireless.cyw-fmac-fw.git@ba140e42.tar.xz' and 'linux-firmware@20220411-r0-1a6a4201/_tagged/oniro/kirkstone-v1.0.0-rc-340-gc066689/oniro-linux/seco-imx8mm-c61-4gb/github.com.murata-wireless.cyw-fmac-nvram.git@8710e74e.tar.xz' are licensed by Cypress Semiconductors. The following statement in the LICENSE agreement could be a problem and risk for the project:
   
"This Agreement is effective until terminated, and either
party may terminate this Agreement at any time with or without cause."

The files need to be removed. Action to be taken by developers from Seco. 

[Back to table of contents](#table-of-contents)

### 1.5. linux-intel@5.10.100+gitAUTOINC+64fb693a6c_8e5c6f8269-r0-5edf7c20
The following license text has been found in the file, linux-intel@5.10.100+gitAUTOINC+64fb693a6c_8e5c6f8269-r0-5edf7c20/github.com.intel.linux-intel-lts.git@8e5c6f82.tar.xz/drivers/net/appletalk/cops_ffdrv.h:

"
The firmware this driver downloads into the Localtalk card is a
separate program and is not GPL'd source code, even though the Linux
side driver and the routine that loads this data into the card are.


It is taken from the COPS SDK and is under the following license


This material is licensed to you strictly for use in conjunction with
the use of COPS LocalTalk adapters.
There is no charge for this SDK. And no waranty express or implied
about its fitness for any purpose. However, we will cheerefully
refund every penny you paid for this SDK...
Regards,


Thomas F. Divine
Chief Scientist
"

An issue has been raised in gitlab. Please check 'https://git.ostc-eu.org/oss-compliance/sbom/private_bom/-/issues/31'.

[Back to table of contents](#table-of-contents)

### 1.6. python3@3.10.4-r0-3eeee379
The file, 'python3@3.10.4-r0-3eeee379/Python-3.10.4.tar.xz/Python-3.10.4/PC/crtlicense.txt' has the license text,
"
This program is linked with and uses Microsoft Distributable Code,
copyrighted by Microsoft Corporation. The Microsoft Distributable Code
is embedded in each .exe, .dll and .pyd file as a result of running
the code through a linker.
If you further distribute programs that include the Microsoft
Distributable Code, you must comply with the restrictions on
distribution specified by Microsoft. In particular, you must require
distributors and external end users to agree to terms that protect the
Microsoft Distributable Code at least as much as Microsoft's own
requirements for the Distributable Code. See Microsoft's documentation
(included in its developer tools and on its website at microsoft.com)
for specific details.
Redistribution of the Windows binary build of the Python interpreter
complies with this agreement, provided that you do not:


alter any copyright, trademark or patent notice in Microsoft's
Distributable Code;


use Microsoft's trademarks in your programs' names or in a way that
suggests your programs come from or are endorsed by Microsoft;


distribute Microsoft's Distributable Code to run on a platform other
than Microsoft operating systems, run-time technologies or application
platforms; or


include Microsoft Distributable Code in malicious, deceptive or
unlawful programs.


These restrictions apply only to the Microsoft Distributable Code as
defined above, not to Python itself or any programs running on the
Python interpreter. The redistribution of the Python interpreter and
libraries is governed by the Python Software License included with this
file, or by other licenses as marked.
"

I believe that in the use case of Oniro, the files licensed under the license may not be used because they are targeted at Microsoft Distributable Code. However, if Oniro does use it, it is not practical to fulfill the condition that distributors and external end users to agree to terms that protect the Microsoft Distributable Code at least as much as Microsoft's own requirements for the Distributable Code.

An issue has been raised in gitlab private SBOM: https://git.ostc-eu.org/oss-compliance/sbom/private_bom/-/issues/42 

[Back to table of contents](#table-of-contents)

### 1.7. shared-mime-info@2.1-r0-1abd20e0
We have found the following note in the file, 'shared-mime-info@2.1-r0-1abd20e0/gitlab.freedesktop.org.xdg.shared-mime-info.git@18e558fa.tar.xz/tests/mime-detection/debian-goodies_0.63_all.deb/data.tar.gz/data.tar/usr/share/doc/debian-goodies/copyright':

The program 'debpaste' has been retrieved (2010-10-02) from
http://paste.debian.net/paste.pl?show_template=clients
and is distributed under the GNU AFFERO GENERAL PUBLIC LICENSE (AGPL 3.0)
license

As the AGPL 3.0 is a very strong copyleft license, we have kept track of it since Jasmine release. In this case, it was found in a folder related to tests. However, it needs to be verified. 

[Back to table of contents](#table-of-contents)

### 1.8. zephyr-philosophers@3.0.0+gitAUTOINC+4f8d78ceeb_b0612c97c1-r0-cc89ed88
1. A reference to an EULA has been found in the file, 'zephyr-philosophers@3.0.0+gitAUTOINC+4f8d78ceeb_b0612c97c1-r0-cc89ed88/github.com.zephyrproject-rtos.mcuboot.git@89936c33.tar.xz/boot/cypress/cy_flash_pal/include/cy_smif_psoc6.h'. 

License text:
"
This software, including source code, documentation and related
materials ("Software"), is owned by Cypress Semiconductor
Corporation or one of its subsidiaries ("Cypress") and is protected by
and subject to worldwide patent protection (United States and foreign),
United States copyright laws and international treaty provisions.
Therefore, you may use this Software only as providhttps://github.com/zephyrproject-rtos/zephyr/issues/46954mission of Cypress.
Disclaimer: THIS SOFTWARE IS PROVIDED AS-IS, WITH NO
WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING,
BUT NOT LIMITED TO, NONINFRINGEMENT, IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A
PARTICULAR PURPOSE. Cypress reserves the right to make
changes to the Software without notice. Cypress does not assume any
liability arising out of the application or use of the Software or any
product or circuit described in the Software. Cypress does not
authorize its products for use in any products where a malfunction or
failure of the Cypress product may reasonably be expected to result in
significant property damage, injury or death ("High Risk Product"). By
including Cypress's product in a High Risk Product, the manufacturer
of such system or application assumes all risk of such use and in doing
so agrees to indemnify Cypress against all liability.
"
We did not find the EULA. If no EULA applies, a license to copy, modify, and compile the Software source code solely for use in connection with Cypress' integrated circuit products is granted. No explicit license to redistribute.

2. There are many binaries in the source package. We have raised an issue in the github link, 'https://github.com/zephyrproject-rtos/zephyr/issues/46954'. There was an issue already in github to remove the binaries. So, the binaries will be removed. 

[Back to table of contents](#table-of-contents)

## 2. Third party components that are clear in the initial audit 
### acl@2.3.1-r0-963c29b5
### acpid@2.0.33-r0-c931e98d
### adwaita-icon-theme@41.0-r0-6a54553f
### alsa-lib@1.2.6.1-r0-b83ad896
### alsa-plugins@1.2.6-r0-47385cc5
### alsa-state@0.2.0-r5-a991fbf7
### alsa-topology-conf@1.2.5.1-r0-2935158f
### alsa-ucm-conf@1.2.6.3-r0-f82ae864
### alsa-utils@1.2.6-r0-7f207143
### apmd@3.2.2-15-r0-e1d0034c
### atk@2.38.0-r0-51a46612
### attr@2.5.1-r0-44a5af26
### autoconf@2.71-r0-1a661cc1
### automake@1.16.5-r0-fb9e52cf
### avahi@0.8-r0-29562424
### babeltrace2@2.0.4-r0-b3b8bdf1
### base-files@3.0.14-r89-53400fab
### base-passwd@3.5.29-r0-f89d1beb
### bash@5.1.16-r0-6061a027
### bash@5.1.16-r0-2e94bdaf
### bash-completion@2.11-r0-2f09b97e
### binutils@2.38-r0-0b7c0579
### binutils@2.38-r0-f0c5a927
### blktrace@1.3.0+gitAUTOINC+366d30b9cd-r0-bbcbca31
### btrfs-tools@5.16.2-r0-49924eaa
### busybox@1.35.0-r0-4c1dafd8
### bzip2@1.0.8-r0-ccbe0bc0.tar.xz
### cantarell-fonts@0.303.1-r0-6fb91381
### ccache@4.6-r0-9efaaf7d
### coreutils@9.0-r0-e5180a0b
### cpio@2.13-r0-aac316a8
### cracklib@2.9.7-r0-d259f9fc
### cronie@1.6.0-r0-14e8107b
### cronie@1.6.1-r0-670bcc9a
### curl@7.82.0-r0-494be295
### curl@7.82.0-r0-95d86e77
### dbus@1.14.0-r0-86b2777f
### diffstat@1.64-r0-b1348766
### diffutils@3.8-r0-c2fb6ea6
### dosfstools@4.2-r0-2b3d2506
### dropbear@2020.81-r0-b6ac3437
### e2fsprogs@1.46.5-r0-030da5de 
### e2fsprogs@1.46.5-r0-dc2a968c 
### elfutils@0.186-r0-83234b67
### expat@2.4.7-r0-6e807a22
### expect@5.45.4-r0-fefefbb1
### file@5.41-r0-67c8fb67
### findutils@4.9.0-r0-7e2ece93
### flac@1.3.4-r0-4e6fceb8nettle@3.7.3-r0-56dac4ca
### gdbm@1.23-r0-687300b1
### gdk-pixbuf@2.42.6-r0-2d183b94
### gettext@0.21-r0-f6f870e9
### glib-2.0@2.72.1-r0-9680b555
### glib-2.0@2.72.2-r0-36d438ee
### gmmlib@22.0.3-r0-3bfb8070
### gmmlib@22.1.2-r0-f730e761
### gmp@6.2.1-r0-97166601
### gnome-desktop-testing@2021.1-r0-5024e7e7
### gnu-config@20211108+gitAUTOINC+191bcb948f-r0-f251175c
### gnutls@3.7.4-r0-0692ca8f
### gobject-introspection@1.72.0-r0-9fd22ee7
### grep@3.7-r0-f68b5eff
### grub@2.06-r0-73d95324
### grub-efi@2.06-r0-c93a88da
### gtk+3@3.24.33-r0-46e5384d
### gtk+3@3.24.34-r0-777cb6da
### gzip@1.12-r0-2311f5d5
### harfbuzz@4.0.1-r0-181653fa
### hdparm@9.63-r0-17f9a7be
### icu@70.1-r0-ce7b9c21
### intel-media-driver@22.1.1-r0-086b1c33
### intel-microcode@20220207-r0-6b84a01d
### intel-microcode@20220419-r0-f74f2984
### intel-microcode@20220510-r0-9facafd8
### iperf3@3.11-r0-9f71dc12
### iproute2@5.17.0-r0-e27aa404
### iptables@1.8.7-r0-a3146c75
### itt@3.23.0-r0-023d596b
### Iw@5.16-r0-f6aadef7
### json-glib@1.6.6-r0-29815e1e
### kbd@2.4.0-r0-1e8a623f
### kernel-selftest@1.0-r0-c051ada7
### keymaps@1.0-r31-fbf72951
### kmod@29-r0-9c1bf6fd
### less@600-r0-506dc772
### libaio@0.3.112-r0-b938202e
### libarchive@3.6.1-r0-57b1b320 
### libatomic-ops@7.6.12-r0-c8b0ae02
### libbsd@0.11.5-r0-a285f475
### libcap@2.63-r0-663722df
### libcap-ng@0.8.2-r0-4394c22b 
### libcheck@0.15.2-r0-85c0431f
### libdrm@2.4.110-r0-29c0d672
### libepoxy@1.5.9-r0-8ab0e5dc
### liberation-fonts@2.1.5-r0-b832b6f2
### liberror-perl@0.17029-r0-db7b02be
### libevdev@1.12.1-r0-4462b4ac
### libffi@3.4.2-r0-b4810d93
### libgcc@11.2.0-r0-c4150531
### libgcc@11.3.0-r0-29f322de
### libgcrypt@1.9.4-r0-c000b872
### libgloss@4.2.0-r0-2c957574
### libgpg-error@1.44-r0-153db2cd
### libgudev@237-r0-b9a71551
### libical@3.0.14-r0-7ccd2b16
### libidn2@2.3.2-r0-2bd5a618
### libinput@1.19.3-r0-e120670c
### libinput@1.19.4-r0-626dc428
### libjpeg-turbo@2.1.3-r0-50484961
### libmbim@1.26.2-r0-7c2966d5
### libmd@1.0.4-r0-5312fb94
### libmicrohttpd@0.9.75-r0-cd7bfefc 
### libmpc@1.2.1-r0-3ecc58de
### libndp@1.8-r0-f1c2ab60
### libnl@3.5.0-r0-269ef0bd
### libnsl2@2.0.0-r0-1a512744
### libogg@1.3.5-r0-165a3260
### libpam@1.5.2-r0-78d5b606
### libpcre@8.45-r0-e7a5a8f6
### libqmi@1.30.4-r0-e7d3aa08
### libsamplerate0@0.2.2-r0-5af537b8
### libseccomp@2.5.3-r0-699bb743
### libsndfile1@1.0.31-r0-84ec9d30
### libtirpc@1.3.2-r0-325f34cc
### libtool@2.4.7-r0-a2619c74
### libubootenv@0.3.2-r0-0f021e76
### libucontext@1.2-r0-b4584e6d
### libunistring@1.0-r0-802fffc5
### libunwind@1.6.2-r0-5db2c409
### liburcu@0.13.1-r0-17ca8246
### libusb1@1.0.26-r0-03101705
### libva-intel@2.13.0-r0-51b767a3
### libva-intel@2.14.0-r0-6c141272
### libvorbis@1.3.7-r0-0b07a7c1
### libx11-compose-data@1.6.8-r0-925a2ed6
### libxkbcommon@1.4.0-r0-c33fdc3a
### libxkbcommon@1.4.1-r0-99d35b04
### libxml2@2.9.13-r0-e7062a8d
### libxml2@2.9.14-r0-cc6b37db
### linux-firmware-bluetooth-bcm43455@1.0-r0-5070c2cf
### linux-firmware-rpidistro@20210315-3+rpt4-r0-78d02a5a
### linux-libc-headers@5.16-r0-4aa647f9
### linux-oniro@5.10.61+gitAUTOINC+3b283fa8d4_452ea6a15e-r0-dbcbbde3
### linux-raspberrypi@5.15.34+gitAUTOINC+e1b976ee4f_0086da6acd-r0-5ca9642b
### linux-seco@5.10.35+gitAUTOINC+6722bbc49b-r0-3eaa43d6 
### logrotate@3.19.0-r0-cdb3c403
### logrotate@3.20.1-r0-13b30abb
### lttng-modules@2.13.3-r0-e8260c78 
### lttng-tools@2.13.4-r0-4b8199ea
### lttng-ust@2.13.2-r0-11e09caa
### ltp@20220121-r0-fdbfb6d9
### lz4@1.9.3-r0-92710781
### lzo@2.10-r0-5435f7a1
### m4@1.4.19-r0-38f92dfe 
### mdadm@4.2-r0-d02f54fd
### mesa@22.0.0-r0-b1c07a1f
### mesa@22.0.3-r0-b23b3039 
### mesa-etnaviv-env@0.1-r0-a49a7497
### mobile-broadband-provider-info@20220315-r0-919cdeb4
### mobile-broadband-provider-info@20220511-r0-d5ec75b6
### modemmanager@1.18.6-r0-68952762
### mpfr@4.1.0-r0-905e4b43
### musl@1.2.3+gitAUTOINC+7a43f6fea9-r0-f525f6a8
### ncurses@6.3+20220423-r0-e1e51b54
### ncurses@6.3-r0-f3fd572b
### netbase@6.3-r0-abc099e9
### newlib@4.2.0-r0-3831d01f
### Snettle@3.7.3-r0-56dac4ca
### net-tools@2.10-r0-54546fb9
### networkmanager@1.36.2-r0-5de28f44
### networkmanager@1.36.2-r0-7bc90fb3
### nspr@4.29-r0-47f1e326
### nss@3.74-r0-e86214e0
### oniro-grub-bootconf@1.0-r0-86e4d382
### oniro-grub-bootconf@1.0-r0-a47b38d1
### oniro-modprobe@1.0-r0-538ef214
### oniro-sysctl@1.0-r0-fb4f2328
### openssl@3.0.2-r0-21876434
### openssl@3.0.3-r0-051bb610
### openssl@3.0.3-r0-803c5fa2
### opkg-utils@0.5.0-r0-39746cc7
### pkgconfig@0.29.2+gitAUTOINC+d97db4fae4-r0-d4d7f855
### pango@1.50.4-r0-357ebb32nettle@3.7.3-r0-56dac4ca
### perl@5.34.1-r0-6074bfb2
### pi-bluetooth@0.1.17-r0-6d148d74
### pixman@0.40.0-r0-444093a1
### popt@1.18-r0-295d15b9
### powertop@2.14-r0-000ae550
### procps@3.3.17-r0-7cb29cbb
### psmisc@23.4-r0-73db4678
### psplash@0.1+gitAUTOINC+44afb7506d-r0-d658f440
### ptest-runner@2.4.2+gitAUTOINC+bcb82804da-r0-8f49fd99
### pulseaudio@15.0-r0-4e53fb21
### python3-dbus@1.2.18-r0-e05d7bdc
### python3-pycairo@1.21.0-r0-da6c86bf
### python3-pygobject@3.42.0-r0-f67f9bc8
### quilt@0.67-r0-f1566a66
### quota@4.06-r0-9a48efbb
### rauc@1.6-r0-0707e649
### rauc-hawkbit-updater@1.1-r0-11f2b27b
### readline@8.1.2-r0-a9ee84e7
### sbc@1.5-r0-e4bafae5
### sed@4.8-r0-10ed7993
### shadow@4.11.1-r0-3c87d384
### shared-mime-info@2.1-r0-1abd20e0
### slang@2.3.2-r0-a90471d3
### socat@1.7.4.3-r0-48ace89a
### speexdsp@1.2.0-r0-980c12a9
### sqlite3@3.38.2-r0-ce907067
### sqlite3@3.38.5-r0-f7f07421
### squashfs-tools@4.5-r0-f7d902fe
### strace@5.16-r0-eb650380
### strace@5.16-r0-ecaffda3
### sysota@unpinnedgit4fc590e1-r0-0ace8025
### systemd@250.4-r0-3d446d70
### systemd@250.5-r0-2640db65
### systemd@250.5-r0-b441f57b
### systemd-conf@1.0-r0-9913e2b8
### systemd-serialgetty@1.0-r5-2d79ba7d
### tar@1.34-r0-e183e56c
### tcp-wrappers@7.6-r10-e14f061e
### tzdata@2022a-r0-03d87816
### unzip@6.0-r5-ea73dd62
### usbutils@014-r0-6454a21a
### util-linux@2.37.4-r0-06429f4d
### util-linux-libuuid@2.37.4-r0-06429f4d
### util-macros@1.19.3-r0-18a12217
### vala@0.56.0-r0-65656ce9
### volatile-binds@1.0-r0-060aa3b9
### volatile-binds@1.0-r0-7c04e4dc
### wayland@1.20.0-r0-b7dd49f1
### wayland-protocols@1.25-r0-3c295367
### wayland-utils@1.0.0-r0-3617919f
### weston@10.0.0-r0-79919612 
### weston-init@1.0-r0-9e89f9c8
### wireless-regdb@2022.04.08-r0-77888ca2
### wpa-supplicant@2.10-r0-ee70fa20
### xkeyboard-config@2.35.1-r0-393066aa
### xz@5.2.5-r0-0e925a18
### zip@3.0-r2-8e5c2cc2
### zip@3.0-r2-c56718f5
### zlib@1.2.11-r0-e3b0ae2b
### zstd@1.5.2-r0-78e94c68


[Back to table of contents](#table-of-contents)

## 3. Third party components with baniaries in the source tree
The source trees of the first party components were checked for the presence of binaries. The listed components in this section are those with binaries in the source tree. The extensions searched for were '.o', '.so', '.a', '.hap' etc. We have excluded the components where binaries were found in test folders, example folders etc. 

### 3.1. bluez5@5.64-r0-02e251e0
### 3.2. bluez-alsa@unpinnedgit9045edb4-r0-9f4aadae
### 3.3. bluez-firmware-rpidistro@1.2-4+rpt8-r0-d199ca2d
### 3.4. tcl@8.6.11-r0-3d116db0
### 3.5. unzip@6.0-r5-13a22510
### 3.6. zephyr-philosophers@3.0.0+gitAUTOINC+4f8d78ceeb_b0612c97c1-r0-cc89ed88
### 3.7. wireless-regdb@2022.04.08-r0-77888ca2

[Back to table of contents](#table-of-contents)

## 4. List of image files found in the sources
The search was made with extensions, 'jpeg', '.jpg', '.png', '.svg' The number of image files found are too large to include here. We will document it separately in the project archives.  

[Back to table of contents](#table-of-contents)

## 5. List of audio files found in sources
No audio files were found in the audit.

[Back to table of contents](#table-of-contents)

## 6. List of video files found in sources
No video files were found in the audit.

[Back to table of contents](#table-of-contents)
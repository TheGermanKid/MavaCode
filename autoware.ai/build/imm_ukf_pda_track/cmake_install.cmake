# Install script for directory: /home/capstone/autoware.ai/src/autoware/core_perception/lidar_imm_ukf_pda_track

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/capstone/autoware.ai/install/imm_ukf_pda_track")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/capstone/autoware.ai/build/imm_ukf_pda_track/catkin_generated/installspace/imm_ukf_pda_track.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/imm_ukf_pda_track/cmake" TYPE FILE FILES
    "/home/capstone/autoware.ai/build/imm_ukf_pda_track/catkin_generated/installspace/imm_ukf_pda_trackConfig.cmake"
    "/home/capstone/autoware.ai/build/imm_ukf_pda_track/catkin_generated/installspace/imm_ukf_pda_trackConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/imm_ukf_pda_track" TYPE FILE FILES "/home/capstone/autoware.ai/src/autoware/core_perception/lidar_imm_ukf_pda_track/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track" TYPE EXECUTABLE FILES "/home/capstone/autoware.ai/build/imm_ukf_pda_track/devel/lib/imm_ukf_pda_track/imm_ukf_pda")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda"
         OLD_RPATH "/home/capstone/autoware.ai/install/lanelet2_extension/lib:/home/capstone/autoware.ai/install/amathutils_lib/lib:/home/capstone/autoware.ai/install/lanelet2_validation/lib:/home/capstone/autoware.ai/install/lanelet2_projection/lib:/home/capstone/autoware.ai/install/lanelet2_io/lib:/home/capstone/autoware.ai/install/lanelet2_routing/lib:/home/capstone/autoware.ai/install/lanelet2_traffic_rules/lib:/home/capstone/autoware.ai/install/lanelet2_core/lib:/opt/ros/melodic/lib:/usr/lib/x86_64-linux-gnu/hdf5/openmpi:/usr/lib/x86_64-linux-gnu/openmpi/lib:/home/capstone/autoware.ai/install/vector_map/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2")
    file(RPATH_CHECK
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2"
         RPATH "")
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track" TYPE EXECUTABLE FILES "/home/capstone/autoware.ai/build/imm_ukf_pda_track/devel/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2")
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2" AND
     NOT IS_SYMLINK "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2")
    file(RPATH_CHANGE
         FILE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2"
         OLD_RPATH "/home/capstone/autoware.ai/install/lanelet2_extension/lib:/home/capstone/autoware.ai/install/amathutils_lib/lib:/home/capstone/autoware.ai/install/lanelet2_validation/lib:/home/capstone/autoware.ai/install/lanelet2_projection/lib:/home/capstone/autoware.ai/install/lanelet2_io/lib:/home/capstone/autoware.ai/install/lanelet2_routing/lib:/home/capstone/autoware.ai/install/lanelet2_traffic_rules/lib:/home/capstone/autoware.ai/install/lanelet2_core/lib:/opt/ros/melodic/lib:/usr/lib/x86_64-linux-gnu/hdf5/openmpi:/usr/lib/x86_64-linux-gnu/openmpi/lib:/home/capstone/autoware.ai/install/vector_map/lib:"
         NEW_RPATH "")
    if(CMAKE_INSTALL_DO_STRIP)
      execute_process(COMMAND "/usr/bin/strip" "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/imm_ukf_pda_track/imm_ukf_pda_lanelet2")
    endif()
  endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/imm_ukf_pda_track/launch" TYPE DIRECTORY FILES "/home/capstone/autoware.ai/src/autoware/core_perception/lidar_imm_ukf_pda_track/launch/" REGEX "/\\.svn$" EXCLUDE)
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/capstone/autoware.ai/build/imm_ukf_pda_track/gtest/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/capstone/autoware.ai/build/imm_ukf_pda_track/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")

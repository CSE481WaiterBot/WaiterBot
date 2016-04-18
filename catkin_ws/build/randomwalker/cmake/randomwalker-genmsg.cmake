# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "randomwalker: 0 messages, 2 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(randomwalker_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_custom_target(_randomwalker_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "randomwalker" "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv" ""
)

get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_custom_target(_randomwalker_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "randomwalker" "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
)
_generate_srv_cpp(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_cpp(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(randomwalker_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_cpp _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_cpp _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_gencpp)
add_dependencies(randomwalker_gencpp randomwalker_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
)
_generate_srv_lisp(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_lisp(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(randomwalker_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_lisp _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_lisp _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_genlisp)
add_dependencies(randomwalker_genlisp randomwalker_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
)
_generate_srv_py(randomwalker
  "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
)

### Generating Module File
_generate_module_py(randomwalker
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(randomwalker_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(randomwalker_generate_messages randomwalker_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetBounds.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_py _randomwalker_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/cse/Documents/logoshi/catkin_ws/src/randomwalker/srv/GetScore.srv" NAME_WE)
add_dependencies(randomwalker_generate_messages_py _randomwalker_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(randomwalker_genpy)
add_dependencies(randomwalker_genpy randomwalker_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS randomwalker_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/randomwalker
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
add_dependencies(randomwalker_generate_messages_cpp std_msgs_generate_messages_cpp)

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/randomwalker
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
add_dependencies(randomwalker_generate_messages_lisp std_msgs_generate_messages_lisp)

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/randomwalker
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
add_dependencies(randomwalker_generate_messages_py std_msgs_generate_messages_py)

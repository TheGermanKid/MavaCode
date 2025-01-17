# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autoware_config_msgs/ConfigRayGroundFilter.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class ConfigRayGroundFilter(genpy.Message):
  _md5sum = "1b9a20593709b07932fff996671d4ed6"
  _type = "autoware_config_msgs/ConfigRayGroundFilter"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """std_msgs/Header header

float64  sensor_height
float64  clipping_height
float64  min_point_distance
float64  radial_divider_angle
float64  concentric_divider_distance
float64  local_max_slope
float64  general_max_slope
float64  min_height_threshold
float64  reclass_distance_threshold
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id
"""
  __slots__ = ['header','sensor_height','clipping_height','min_point_distance','radial_divider_angle','concentric_divider_distance','local_max_slope','general_max_slope','min_height_threshold','reclass_distance_threshold']
  _slot_types = ['std_msgs/Header','float64','float64','float64','float64','float64','float64','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,sensor_height,clipping_height,min_point_distance,radial_divider_angle,concentric_divider_distance,local_max_slope,general_max_slope,min_height_threshold,reclass_distance_threshold

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ConfigRayGroundFilter, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.sensor_height is None:
        self.sensor_height = 0.
      if self.clipping_height is None:
        self.clipping_height = 0.
      if self.min_point_distance is None:
        self.min_point_distance = 0.
      if self.radial_divider_angle is None:
        self.radial_divider_angle = 0.
      if self.concentric_divider_distance is None:
        self.concentric_divider_distance = 0.
      if self.local_max_slope is None:
        self.local_max_slope = 0.
      if self.general_max_slope is None:
        self.general_max_slope = 0.
      if self.min_height_threshold is None:
        self.min_height_threshold = 0.
      if self.reclass_distance_threshold is None:
        self.reclass_distance_threshold = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.sensor_height = 0.
      self.clipping_height = 0.
      self.min_point_distance = 0.
      self.radial_divider_angle = 0.
      self.concentric_divider_distance = 0.
      self.local_max_slope = 0.
      self.general_max_slope = 0.
      self.min_height_threshold = 0.
      self.reclass_distance_threshold = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_9d().pack(_x.sensor_height, _x.clipping_height, _x.min_point_distance, _x.radial_divider_angle, _x.concentric_divider_distance, _x.local_max_slope, _x.general_max_slope, _x.min_height_threshold, _x.reclass_distance_threshold))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.sensor_height, _x.clipping_height, _x.min_point_distance, _x.radial_divider_angle, _x.concentric_divider_distance, _x.local_max_slope, _x.general_max_slope, _x.min_height_threshold, _x.reclass_distance_threshold,) = _get_struct_9d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_9d().pack(_x.sensor_height, _x.clipping_height, _x.min_point_distance, _x.radial_divider_angle, _x.concentric_divider_distance, _x.local_max_slope, _x.general_max_slope, _x.min_height_threshold, _x.reclass_distance_threshold))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 72
      (_x.sensor_height, _x.clipping_height, _x.min_point_distance, _x.radial_divider_angle, _x.concentric_divider_distance, _x.local_max_slope, _x.general_max_slope, _x.min_height_threshold, _x.reclass_distance_threshold,) = _get_struct_9d().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_9d = None
def _get_struct_9d():
    global _struct_9d
    if _struct_9d is None:
        _struct_9d = struct.Struct("<9d")
    return _struct_9d

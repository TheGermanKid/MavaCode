# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autoware_config_msgs/ConfigApproximateNDTMapping.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class ConfigApproximateNDTMapping(genpy.Message):
  _md5sum = "687f2daa2d34290b27e1b1cbc58023a7"
  _type = "autoware_config_msgs/ConfigApproximateNDTMapping"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header
float32 resolution
float32 step_size
float32 trans_epsilon
int32 max_iterations
float32 leaf_size
float32 min_scan_range
float32 max_scan_range
float32 min_add_scan_shift
float32 max_submap_size

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
  __slots__ = ['header','resolution','step_size','trans_epsilon','max_iterations','leaf_size','min_scan_range','max_scan_range','min_add_scan_shift','max_submap_size']
  _slot_types = ['std_msgs/Header','float32','float32','float32','int32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,resolution,step_size,trans_epsilon,max_iterations,leaf_size,min_scan_range,max_scan_range,min_add_scan_shift,max_submap_size

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(ConfigApproximateNDTMapping, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.resolution is None:
        self.resolution = 0.
      if self.step_size is None:
        self.step_size = 0.
      if self.trans_epsilon is None:
        self.trans_epsilon = 0.
      if self.max_iterations is None:
        self.max_iterations = 0
      if self.leaf_size is None:
        self.leaf_size = 0.
      if self.min_scan_range is None:
        self.min_scan_range = 0.
      if self.max_scan_range is None:
        self.max_scan_range = 0.
      if self.min_add_scan_shift is None:
        self.min_add_scan_shift = 0.
      if self.max_submap_size is None:
        self.max_submap_size = 0.
    else:
      self.header = std_msgs.msg.Header()
      self.resolution = 0.
      self.step_size = 0.
      self.trans_epsilon = 0.
      self.max_iterations = 0
      self.leaf_size = 0.
      self.min_scan_range = 0.
      self.max_scan_range = 0.
      self.min_add_scan_shift = 0.
      self.max_submap_size = 0.

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
      buff.write(_get_struct_3fi5f().pack(_x.resolution, _x.step_size, _x.trans_epsilon, _x.max_iterations, _x.leaf_size, _x.min_scan_range, _x.max_scan_range, _x.min_add_scan_shift, _x.max_submap_size))
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
      end += 36
      (_x.resolution, _x.step_size, _x.trans_epsilon, _x.max_iterations, _x.leaf_size, _x.min_scan_range, _x.max_scan_range, _x.min_add_scan_shift, _x.max_submap_size,) = _get_struct_3fi5f().unpack(str[start:end])
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
      buff.write(_get_struct_3fi5f().pack(_x.resolution, _x.step_size, _x.trans_epsilon, _x.max_iterations, _x.leaf_size, _x.min_scan_range, _x.max_scan_range, _x.min_add_scan_shift, _x.max_submap_size))
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
      end += 36
      (_x.resolution, _x.step_size, _x.trans_epsilon, _x.max_iterations, _x.leaf_size, _x.min_scan_range, _x.max_scan_range, _x.min_add_scan_shift, _x.max_submap_size,) = _get_struct_3fi5f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3fi5f = None
def _get_struct_3fi5f():
    global _struct_3fi5f
    if _struct_3fi5f is None:
        _struct_3fi5f = struct.Struct("<3fi5f")
    return _struct_3fi5f
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I

# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autoware_map_msgs/LaneArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import autoware_map_msgs.msg
import std_msgs.msg

class LaneArray(genpy.Message):
  _md5sum = "1849af6a05682cff6c714d459a3e51f9"
  _type = "autoware_map_msgs/LaneArray"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """# This consists of multiple lanes in a map with reference coordinate frame. 

Header header
Lane[] data

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

================================================================================
MSG: autoware_map_msgs/Lane
# This represents a lane in a map.

# Id of this Lane object. Must be unique among all lane objects.
int32 lane_id

# Id of the first waypoint that belongs to this lane
int32 start_waypoint_id

# Id of the last waypoint that belongs to this lane
int32 end_waypoint_id

# This describes how many lanes there are in left side of this lane.
# E.g. If there are 2 lanes on the left side, then lane_number will be 2. 
# If the road is single lane, then this will be 0. 
# This will be always 0 in intersection. 
int32 lane_number

# Total number of lanes present in road. 
int32 num_of_lanes

# Speed limit of this lane in [km/h]
float64 speed_limit

# Length of this lane in [m]
# i.e. accumulated length from start_waypoint to end_waypoint of this lane
float64 length

# Maximum width of vehicle that can drive this lane in [m]
float64 width_limit

# Maximum height of vehicle that can drive this lane in [m]. 
float64 height_limit

# Maximum weight of vehicle that can drive this lane in [kg]. 
float64 weight_limit
"""
  __slots__ = ['header','data']
  _slot_types = ['std_msgs/Header','autoware_map_msgs/Lane[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,data

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaneArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.data is None:
        self.data = []
    else:
      self.header = std_msgs.msg.Header()
      self.data = []

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
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_5i5d().pack(_x.lane_id, _x.start_waypoint_id, _x.end_waypoint_id, _x.lane_number, _x.num_of_lanes, _x.speed_limit, _x.length, _x.width_limit, _x.height_limit, _x.weight_limit))
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
      if self.data is None:
        self.data = None
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = autoware_map_msgs.msg.Lane()
        _x = val1
        start = end
        end += 60
        (_x.lane_id, _x.start_waypoint_id, _x.end_waypoint_id, _x.lane_number, _x.num_of_lanes, _x.speed_limit, _x.length, _x.width_limit, _x.height_limit, _x.weight_limit,) = _get_struct_5i5d().unpack(str[start:end])
        self.data.append(val1)
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
      length = len(self.data)
      buff.write(_struct_I.pack(length))
      for val1 in self.data:
        _x = val1
        buff.write(_get_struct_5i5d().pack(_x.lane_id, _x.start_waypoint_id, _x.end_waypoint_id, _x.lane_number, _x.num_of_lanes, _x.speed_limit, _x.length, _x.width_limit, _x.height_limit, _x.weight_limit))
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
      if self.data is None:
        self.data = None
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
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.data = []
      for i in range(0, length):
        val1 = autoware_map_msgs.msg.Lane()
        _x = val1
        start = end
        end += 60
        (_x.lane_id, _x.start_waypoint_id, _x.end_waypoint_id, _x.lane_number, _x.num_of_lanes, _x.speed_limit, _x.length, _x.width_limit, _x.height_limit, _x.weight_limit,) = _get_struct_5i5d().unpack(str[start:end])
        self.data.append(val1)
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
_struct_5i5d = None
def _get_struct_5i5d():
    global _struct_5i5d
    if _struct_5i5d is None:
        _struct_5i5d = struct.Struct("<5i5d")
    return _struct_5i5d

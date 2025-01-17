# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from autoware_map_msgs/LaneAttributeRelation.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class LaneAttributeRelation(genpy.Message):
  _md5sum = "e65c2a2db848427c6061a3bc2aff585f"
  _type = "autoware_map_msgs/LaneAttributeRelation"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """# This describes an attribute of lane in a map.

# ATTRIBUTE_TYPES
uint32 PLANE = 1
uint32 INTERSECTION = 2
uint32 CROSS_WALK = 3
uint32 DISABLE_LANE_CHANGE = 4
uint32 DISABLE_PARKING = 5
uint32 RAILROAD = 6
uint32 PEDESTRIAN_SPACE = 7
uint32 PARKING_AREA = 8

# Id of Lane object which attribute is applied.
int32 lane_id

# Attribute that is applied to lane
# Must be one of ATTRIBUTE_TYPES
int32 attribute_type

# Id of Area object that is relevant to the attribute (if exists). 
# e.g. Id of Area object that describes crosswalk when attribute_type = CROSS_WALK. 
int32 area_id
"""
  # Pseudo-constants
  PLANE = 1
  INTERSECTION = 2
  CROSS_WALK = 3
  DISABLE_LANE_CHANGE = 4
  DISABLE_PARKING = 5
  RAILROAD = 6
  PEDESTRIAN_SPACE = 7
  PARKING_AREA = 8

  __slots__ = ['lane_id','attribute_type','area_id']
  _slot_types = ['int32','int32','int32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       lane_id,attribute_type,area_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(LaneAttributeRelation, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.lane_id is None:
        self.lane_id = 0
      if self.attribute_type is None:
        self.attribute_type = 0
      if self.area_id is None:
        self.area_id = 0
    else:
      self.lane_id = 0
      self.attribute_type = 0
      self.area_id = 0

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
      buff.write(_get_struct_3i().pack(_x.lane_id, _x.attribute_type, _x.area_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.lane_id, _x.attribute_type, _x.area_id,) = _get_struct_3i().unpack(str[start:end])
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
      buff.write(_get_struct_3i().pack(_x.lane_id, _x.attribute_type, _x.area_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 12
      (_x.lane_id, _x.attribute_type, _x.area_id,) = _get_struct_3i().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3i = None
def _get_struct_3i():
    global _struct_3i
    if _struct_3i is None:
        _struct_3i = struct.Struct("<3i")
    return _struct_3i

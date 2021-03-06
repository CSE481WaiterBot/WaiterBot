// Generated by gencpp from file randomwalker/GetBoundsResponse.msg
// DO NOT EDIT!


#ifndef RANDOMWALKER_MESSAGE_GETBOUNDSRESPONSE_H
#define RANDOMWALKER_MESSAGE_GETBOUNDSRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace randomwalker
{
template <class ContainerAllocator>
struct GetBoundsResponse_
{
  typedef GetBoundsResponse_<ContainerAllocator> Type;

  GetBoundsResponse_()
    : num_rows(0)
    , num_cols(0)  {
    }
  GetBoundsResponse_(const ContainerAllocator& _alloc)
    : num_rows(0)
    , num_cols(0)  {
    }



   typedef int32_t _num_rows_type;
  _num_rows_type num_rows;

   typedef int32_t _num_cols_type;
  _num_cols_type num_cols;




  typedef boost::shared_ptr< ::randomwalker::GetBoundsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::randomwalker::GetBoundsResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetBoundsResponse_

typedef ::randomwalker::GetBoundsResponse_<std::allocator<void> > GetBoundsResponse;

typedef boost::shared_ptr< ::randomwalker::GetBoundsResponse > GetBoundsResponsePtr;
typedef boost::shared_ptr< ::randomwalker::GetBoundsResponse const> GetBoundsResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::randomwalker::GetBoundsResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace randomwalker

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::randomwalker::GetBoundsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::randomwalker::GetBoundsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::randomwalker::GetBoundsResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "b43c3f7151561a46ea4332c06c9db277";
  }

  static const char* value(const ::randomwalker::GetBoundsResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xb43c3f7151561a46ULL;
  static const uint64_t static_value2 = 0xea4332c06c9db277ULL;
};

template<class ContainerAllocator>
struct DataType< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "randomwalker/GetBoundsResponse";
  }

  static const char* value(const ::randomwalker::GetBoundsResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n\
int32 num_rows\n\
int32 num_cols\n\
\n\
";
  }

  static const char* value(const ::randomwalker::GetBoundsResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.num_rows);
      stream.next(m.num_cols);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER;
  }; // struct GetBoundsResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::randomwalker::GetBoundsResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::randomwalker::GetBoundsResponse_<ContainerAllocator>& v)
  {
    s << indent << "num_rows: ";
    Printer<int32_t>::stream(s, indent + "  ", v.num_rows);
    s << indent << "num_cols: ";
    Printer<int32_t>::stream(s, indent + "  ", v.num_cols);
  }
};

} // namespace message_operations
} // namespace ros

#endif // RANDOMWALKER_MESSAGE_GETBOUNDSRESPONSE_H

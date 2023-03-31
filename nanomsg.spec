%define major 5
%define libname %mklibname nanomsg %{major}
%define devname %mklibname nanomsg -d

Name: nanomsg
Version:	1.1.5
Release:	2
Source0: https://github.com/nanomsg/nanomsg/archive/%{version}.tar.gz
Summary: Socket library providing several common communication patterns
URL: http://nanomsg.org/
License: MIT
Group: System/Libraries
BuildRequires: cmake ninja

%description
nanomsg is a socket library that provides several common communication
patterns. It aims to make the networking layer fast, scalable, and
easy to use. Implemented in C, it works on a wide range of operating
systems with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you
can create a vast array of distributed applications.

The following scalability protocols are currently available:

    PAIR - simple one-to-one communication
    BUS - simple many-to-many communication
    REQREP - allows to build clusters of stateless services
             to process user requests
    PUBSUB - distributes messages to large sets of interested subscribers
    PIPELINE - aggregates messages from multiple sources and load balances
               them among many destinations
    SURVEY - allows to query state of multiple applications in a single go 

Scalability protocols are layered on top of the transport layer in the network
stack.
At the moment, the nanomsg library supports the following transports
mechanisms:

    INPROC - transport within a process (between threads, modules etc.)
    IPC - transport between processes on a single machine
    TCP - network transport via TCP 

The library exposes a BSD-socket-like C API to the applications.

%package -n %{libname}
Summary: Socket library providing several common communication patterns
Group: System/Libraries

%description -n %{libname}
nanomsg is a socket library that provides several common communication
patterns. It aims to make the networking layer fast, scalable, and
easy to use. Implemented in C, it works on a wide range of operating
systems with no further dependencies.

The communication patterns, also called "scalability protocols", are
basic blocks for building distributed systems. By combining them you
can create a vast array of distributed applications.

The following scalability protocols are currently available:

    PAIR - simple one-to-one communication
    BUS - simple many-to-many communication
    REQREP - allows to build clusters of stateless services
             to process user requests
    PUBSUB - distributes messages to large sets of interested subscribers
    PIPELINE - aggregates messages from multiple sources and load balances
               them among many destinations
    SURVEY - allows to query state of multiple applications in a single go 

Scalability protocols are layered on top of the transport layer in the network
stack.
At the moment, the nanomsg library supports the following transports
mechanisms:

    INPROC - transport within a process (between threads, modules etc.)
    IPC - transport between processes on a single machine
    TCP - network transport via TCP 

The library exposes a BSD-socket-like C API to the applications.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_libdir}/cmake/%{name}-%{version}/*.cmake

import datetime
import decimal
import ipaddress
import uuid
from codecs import CodecInfo
from typing import Any

infinity_date: datetime.date
infinity_datetime: datetime.datetime
negative_infinity_date: datetime.date
negative_infinity_datetime: datetime.datetime
pg_epoch_date: datetime.date
pg_epoch_datetime: datetime.datetime
pg_epoch_datetime_utc: datetime.datetime
utc = datetime.timezone.utc
date_from_ordinal = datetime.date.fromordinal
_ipaddr = ipaddress.ip_address
_ipnet = ipaddress.ip_network

def __pyx_unpickle_CodecContext(*args: Any, **kwargs: Any) -> Any: ...

class CodecContext:
    __pyx_vtable__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def get_text_codec(self) -> CodecInfo: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state: Any) -> Any: ...

class ReadBuffer:
    __pyx_vtable__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state: Any) -> Any: ...

class WriteBuffer:
    __pyx_vtable__: Any = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __reduce__(self) -> Any: ...
    def __setstate__(self, state: Any) -> Any: ...

_Dec = decimal.Decimal
_UUID = uuid.UUID
timedelta = datetime.timedelta

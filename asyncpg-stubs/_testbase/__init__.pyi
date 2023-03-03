import unittest
from collections.abc import Callable, Iterator
from typing import Any, TypeVar

from . import fuzzer as fuzzer

_F = TypeVar('_F', bound=Callable[..., Any])

def silence_asyncio_long_exec_warning() -> Iterator[None]: ...
def with_timeout(timeout: Any) -> Callable[[_F], _F]: ...

class TestCaseMeta(type):
    TEST_TIMEOUT: Any = ...
    def __new__(cls: Any, name: Any, bases: Any, ns: Any) -> Any: ...

class TestCase(unittest.TestCase, metaclass=TestCaseMeta):
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def assertRunUnder(self, delta: Any) -> None: ...
    def assertLoopErrorHandlerCalled(self, msg_re: str) -> Any: ...
    def loop_exception_handler(self, loop: Any, context: Any) -> None: ...

def create_pool(
    dsn: Any | None = ...,
    *,
    min_size: int = ...,
    max_size: int = ...,
    max_queries: int = ...,
    max_inactive_connection_lifetime: float = ...,
    setup: Any | None = ...,
    init: Any | None = ...,
    loop: Any | None = ...,
    pool_class: Any = ...,
    connection_class: Any = ...,
    record_class: Any = ...,
    **connect_kwargs: Any,
) -> Any: ...

class ClusterTestCase(TestCase):
    @classmethod
    def get_server_settings(cls) -> Any: ...
    @classmethod
    def new_cluster(
        cls, ClusterCls: Any, *, cluster_kwargs: Any = ..., initdb_options: Any = ...
    ) -> Any: ...
    @classmethod
    def start_cluster(cls, cluster: Any, *, server_settings: Any = ...) -> None: ...
    @classmethod
    def setup_cluster(cls) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    @classmethod
    def get_connection_spec(cls, kwargs: Any = ...) -> Any: ...
    @classmethod
    def connect(cls, **kwargs: Any) -> Any: ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...
    def create_pool(
        self, pool_class: Any = ..., connection_class: Any = ..., **kwargs: Any
    ) -> Any: ...

class ProxiedClusterTestCase(ClusterTestCase):
    @classmethod
    def get_server_settings(cls) -> Any: ...
    @classmethod
    def get_proxy_settings(cls) -> Any: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    @classmethod
    def tearDownClass(cls) -> None: ...
    @classmethod
    def get_connection_spec(cls, kwargs: Any) -> Any: ...  # type: ignore[override]
    def tearDown(self) -> None: ...

def with_connection_options(**options: Any) -> Any: ...

class ConnectedTestCase(ClusterTestCase):
    con: Any = ...
    server_version: Any = ...
    def setUp(self) -> None: ...
    def tearDown(self) -> None: ...

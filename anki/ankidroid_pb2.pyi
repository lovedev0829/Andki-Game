"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DebugActiveDatabaseSequenceNumbersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_NUMBERS_FIELD_NUMBER: builtins.int
    @property
    def sequence_numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        sequence_numbers: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["sequence_numbers", b"sequence_numbers"]) -> None: ...

global___DebugActiveDatabaseSequenceNumbersResponse = DebugActiveDatabaseSequenceNumbersResponse

@typing_extensions.final
class SchedTimingTodayLegacyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CREATED_SECS_FIELD_NUMBER: builtins.int
    CREATED_MINS_WEST_FIELD_NUMBER: builtins.int
    NOW_SECS_FIELD_NUMBER: builtins.int
    NOW_MINS_WEST_FIELD_NUMBER: builtins.int
    ROLLOVER_HOUR_FIELD_NUMBER: builtins.int
    created_secs: builtins.int
    created_mins_west: builtins.int
    now_secs: builtins.int
    now_mins_west: builtins.int
    rollover_hour: builtins.int
    def __init__(
        self,
        *,
        created_secs: builtins.int = ...,
        created_mins_west: builtins.int | None = ...,
        now_secs: builtins.int = ...,
        now_mins_west: builtins.int = ...,
        rollover_hour: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["_created_mins_west", b"_created_mins_west", "created_mins_west", b"created_mins_west"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["_created_mins_west", b"_created_mins_west", "created_mins_west", b"created_mins_west", "created_secs", b"created_secs", "now_mins_west", b"now_mins_west", "now_secs", b"now_secs", "rollover_hour", b"rollover_hour"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["_created_mins_west", b"_created_mins_west"]) -> typing_extensions.Literal["created_mins_west"] | None: ...

global___SchedTimingTodayLegacyRequest = SchedTimingTodayLegacyRequest

@typing_extensions.final
class SqlValue(google.protobuf.message.Message):
    """We expect in Java: Null, String, Short, Int, Long, Float, Double, Boolean,
    Blob (unused) We get: DbResult (Null, String, i64, f64, Vec<u8>), which
    matches SQLite documentation
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    STRINGVALUE_FIELD_NUMBER: builtins.int
    LONGVALUE_FIELD_NUMBER: builtins.int
    DOUBLEVALUE_FIELD_NUMBER: builtins.int
    BLOBVALUE_FIELD_NUMBER: builtins.int
    stringValue: builtins.str
    longValue: builtins.int
    doubleValue: builtins.float
    blobValue: builtins.bytes
    def __init__(
        self,
        *,
        stringValue: builtins.str = ...,
        longValue: builtins.int = ...,
        doubleValue: builtins.float = ...,
        blobValue: builtins.bytes = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["Data", b"Data", "blobValue", b"blobValue", "doubleValue", b"doubleValue", "longValue", b"longValue", "stringValue", b"stringValue"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["Data", b"Data", "blobValue", b"blobValue", "doubleValue", b"doubleValue", "longValue", b"longValue", "stringValue", b"stringValue"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["Data", b"Data"]) -> typing_extensions.Literal["stringValue", "longValue", "doubleValue", "blobValue"] | None: ...

global___SqlValue = SqlValue

@typing_extensions.final
class Row(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FIELDS_FIELD_NUMBER: builtins.int
    @property
    def fields(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___SqlValue]: ...
    def __init__(
        self,
        *,
        fields: collections.abc.Iterable[global___SqlValue] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["fields", b"fields"]) -> None: ...

global___Row = Row

@typing_extensions.final
class DbResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROWS_FIELD_NUMBER: builtins.int
    @property
    def rows(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Row]: ...
    def __init__(
        self,
        *,
        rows: collections.abc.Iterable[global___Row] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["rows", b"rows"]) -> None: ...

global___DbResult = DbResult

@typing_extensions.final
class DbResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RESULT_FIELD_NUMBER: builtins.int
    SEQUENCENUMBER_FIELD_NUMBER: builtins.int
    ROWCOUNT_FIELD_NUMBER: builtins.int
    STARTINDEX_FIELD_NUMBER: builtins.int
    @property
    def result(self) -> global___DbResult: ...
    sequenceNumber: builtins.int
    rowCount: builtins.int
    startIndex: builtins.int
    def __init__(
        self,
        *,
        result: global___DbResult | None = ...,
        sequenceNumber: builtins.int = ...,
        rowCount: builtins.int = ...,
        startIndex: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["result", b"result", "rowCount", b"rowCount", "sequenceNumber", b"sequenceNumber", "startIndex", b"startIndex"]) -> None: ...

global___DbResponse = DbResponse

@typing_extensions.final
class GetNextResultPageRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SEQUENCE_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    sequence: builtins.int
    index: builtins.int
    def __init__(
        self,
        *,
        sequence: builtins.int = ...,
        index: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["index", b"index", "sequence", b"sequence"]) -> None: ...

global___GetNextResultPageRequest = GetNextResultPageRequest

@typing_extensions.final
class GetActiveSequenceNumbersResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NUMBERS_FIELD_NUMBER: builtins.int
    @property
    def numbers(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    def __init__(
        self,
        *,
        numbers: collections.abc.Iterable[builtins.int] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["numbers", b"numbers"]) -> None: ...

global___GetActiveSequenceNumbersResponse = GetActiveSequenceNumbersResponse

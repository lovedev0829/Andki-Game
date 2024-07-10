"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
Copyright: Ankitects Pty Ltd and contributors
License: GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _UpdateDeckConfigsMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _UpdateDeckConfigsModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_UpdateDeckConfigsMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    UPDATE_DECK_CONFIGS_MODE_NORMAL: _UpdateDeckConfigsMode.ValueType  # 0
    UPDATE_DECK_CONFIGS_MODE_APPLY_TO_CHILDREN: _UpdateDeckConfigsMode.ValueType  # 1
    UPDATE_DECK_CONFIGS_MODE_COMPUTE_ALL_WEIGHTS: _UpdateDeckConfigsMode.ValueType  # 2

class UpdateDeckConfigsMode(_UpdateDeckConfigsMode, metaclass=_UpdateDeckConfigsModeEnumTypeWrapper): ...

UPDATE_DECK_CONFIGS_MODE_NORMAL: UpdateDeckConfigsMode.ValueType  # 0
UPDATE_DECK_CONFIGS_MODE_APPLY_TO_CHILDREN: UpdateDeckConfigsMode.ValueType  # 1
UPDATE_DECK_CONFIGS_MODE_COMPUTE_ALL_WEIGHTS: UpdateDeckConfigsMode.ValueType  # 2
global___UpdateDeckConfigsMode = UpdateDeckConfigsMode

@typing_extensions.final
class DeckConfigId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DCID_FIELD_NUMBER: builtins.int
    dcid: builtins.int
    def __init__(
        self,
        *,
        dcid: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["dcid", b"dcid"]) -> None: ...

global___DeckConfigId = DeckConfigId

@typing_extensions.final
class DeckConfig(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class Config(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        class _NewCardInsertOrder:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _NewCardInsertOrderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._NewCardInsertOrder.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            NEW_CARD_INSERT_ORDER_DUE: DeckConfig.Config._NewCardInsertOrder.ValueType  # 0
            NEW_CARD_INSERT_ORDER_RANDOM: DeckConfig.Config._NewCardInsertOrder.ValueType  # 1

        class NewCardInsertOrder(_NewCardInsertOrder, metaclass=_NewCardInsertOrderEnumTypeWrapper): ...
        NEW_CARD_INSERT_ORDER_DUE: DeckConfig.Config.NewCardInsertOrder.ValueType  # 0
        NEW_CARD_INSERT_ORDER_RANDOM: DeckConfig.Config.NewCardInsertOrder.ValueType  # 1

        class _NewCardGatherPriority:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _NewCardGatherPriorityEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._NewCardGatherPriority.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            NEW_CARD_GATHER_PRIORITY_DECK: DeckConfig.Config._NewCardGatherPriority.ValueType  # 0
            """Decks in alphabetical order (preorder), then ascending position.
            Siblings are consecutive, provided they have the same position.
            """
            NEW_CARD_GATHER_PRIORITY_DECK_THEN_RANDOM_NOTES: DeckConfig.Config._NewCardGatherPriority.ValueType  # 5
            """Notes are randomly picked from each deck in alphabetical order.
            Siblings are consecutive, provided they have the same position.
            """
            NEW_CARD_GATHER_PRIORITY_LOWEST_POSITION: DeckConfig.Config._NewCardGatherPriority.ValueType  # 1
            """Ascending position.
            Siblings are consecutive, provided they have the same position.
            """
            NEW_CARD_GATHER_PRIORITY_HIGHEST_POSITION: DeckConfig.Config._NewCardGatherPriority.ValueType  # 2
            """Descending position.
            Siblings are consecutive, provided they have the same position.
            """
            NEW_CARD_GATHER_PRIORITY_RANDOM_NOTES: DeckConfig.Config._NewCardGatherPriority.ValueType  # 3
            """Siblings are consecutive."""
            NEW_CARD_GATHER_PRIORITY_RANDOM_CARDS: DeckConfig.Config._NewCardGatherPriority.ValueType  # 4
            """Siblings are neither grouped nor ordered."""

        class NewCardGatherPriority(_NewCardGatherPriority, metaclass=_NewCardGatherPriorityEnumTypeWrapper): ...
        NEW_CARD_GATHER_PRIORITY_DECK: DeckConfig.Config.NewCardGatherPriority.ValueType  # 0
        """Decks in alphabetical order (preorder), then ascending position.
        Siblings are consecutive, provided they have the same position.
        """
        NEW_CARD_GATHER_PRIORITY_DECK_THEN_RANDOM_NOTES: DeckConfig.Config.NewCardGatherPriority.ValueType  # 5
        """Notes are randomly picked from each deck in alphabetical order.
        Siblings are consecutive, provided they have the same position.
        """
        NEW_CARD_GATHER_PRIORITY_LOWEST_POSITION: DeckConfig.Config.NewCardGatherPriority.ValueType  # 1
        """Ascending position.
        Siblings are consecutive, provided they have the same position.
        """
        NEW_CARD_GATHER_PRIORITY_HIGHEST_POSITION: DeckConfig.Config.NewCardGatherPriority.ValueType  # 2
        """Descending position.
        Siblings are consecutive, provided they have the same position.
        """
        NEW_CARD_GATHER_PRIORITY_RANDOM_NOTES: DeckConfig.Config.NewCardGatherPriority.ValueType  # 3
        """Siblings are consecutive."""
        NEW_CARD_GATHER_PRIORITY_RANDOM_CARDS: DeckConfig.Config.NewCardGatherPriority.ValueType  # 4
        """Siblings are neither grouped nor ordered."""

        class _NewCardSortOrder:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _NewCardSortOrderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._NewCardSortOrder.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            NEW_CARD_SORT_ORDER_TEMPLATE: DeckConfig.Config._NewCardSortOrder.ValueType  # 0
            """Ascending card template ordinal.
            For a given ordinal, cards appear in gather order.
            """
            NEW_CARD_SORT_ORDER_NO_SORT: DeckConfig.Config._NewCardSortOrder.ValueType  # 1
            """Preserves original gather order (eg deck order)."""
            NEW_CARD_SORT_ORDER_TEMPLATE_THEN_RANDOM: DeckConfig.Config._NewCardSortOrder.ValueType  # 2
            """Ascending card template ordinal.
            For a given ordinal, cards appear in random order.
            """
            NEW_CARD_SORT_ORDER_RANDOM_NOTE_THEN_TEMPLATE: DeckConfig.Config._NewCardSortOrder.ValueType  # 3
            """Random note order. For a given note, cards appear in template order."""
            NEW_CARD_SORT_ORDER_RANDOM_CARD: DeckConfig.Config._NewCardSortOrder.ValueType  # 4
            """Fully randomized order."""

        class NewCardSortOrder(_NewCardSortOrder, metaclass=_NewCardSortOrderEnumTypeWrapper): ...
        NEW_CARD_SORT_ORDER_TEMPLATE: DeckConfig.Config.NewCardSortOrder.ValueType  # 0
        """Ascending card template ordinal.
        For a given ordinal, cards appear in gather order.
        """
        NEW_CARD_SORT_ORDER_NO_SORT: DeckConfig.Config.NewCardSortOrder.ValueType  # 1
        """Preserves original gather order (eg deck order)."""
        NEW_CARD_SORT_ORDER_TEMPLATE_THEN_RANDOM: DeckConfig.Config.NewCardSortOrder.ValueType  # 2
        """Ascending card template ordinal.
        For a given ordinal, cards appear in random order.
        """
        NEW_CARD_SORT_ORDER_RANDOM_NOTE_THEN_TEMPLATE: DeckConfig.Config.NewCardSortOrder.ValueType  # 3
        """Random note order. For a given note, cards appear in template order."""
        NEW_CARD_SORT_ORDER_RANDOM_CARD: DeckConfig.Config.NewCardSortOrder.ValueType  # 4
        """Fully randomized order."""

        class _ReviewCardOrder:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ReviewCardOrderEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._ReviewCardOrder.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            REVIEW_CARD_ORDER_DAY: DeckConfig.Config._ReviewCardOrder.ValueType  # 0
            REVIEW_CARD_ORDER_DAY_THEN_DECK: DeckConfig.Config._ReviewCardOrder.ValueType  # 1
            REVIEW_CARD_ORDER_DECK_THEN_DAY: DeckConfig.Config._ReviewCardOrder.ValueType  # 2
            REVIEW_CARD_ORDER_INTERVALS_ASCENDING: DeckConfig.Config._ReviewCardOrder.ValueType  # 3
            REVIEW_CARD_ORDER_INTERVALS_DESCENDING: DeckConfig.Config._ReviewCardOrder.ValueType  # 4
            REVIEW_CARD_ORDER_EASE_ASCENDING: DeckConfig.Config._ReviewCardOrder.ValueType  # 5
            REVIEW_CARD_ORDER_EASE_DESCENDING: DeckConfig.Config._ReviewCardOrder.ValueType  # 6
            REVIEW_CARD_ORDER_RELATIVE_OVERDUENESS: DeckConfig.Config._ReviewCardOrder.ValueType  # 7
            REVIEW_CARD_ORDER_RANDOM: DeckConfig.Config._ReviewCardOrder.ValueType  # 8
            REVIEW_CARD_ORDER_ADDED: DeckConfig.Config._ReviewCardOrder.ValueType  # 9
            REVIEW_CARD_ORDER_REVERSE_ADDED: DeckConfig.Config._ReviewCardOrder.ValueType  # 10

        class ReviewCardOrder(_ReviewCardOrder, metaclass=_ReviewCardOrderEnumTypeWrapper): ...
        REVIEW_CARD_ORDER_DAY: DeckConfig.Config.ReviewCardOrder.ValueType  # 0
        REVIEW_CARD_ORDER_DAY_THEN_DECK: DeckConfig.Config.ReviewCardOrder.ValueType  # 1
        REVIEW_CARD_ORDER_DECK_THEN_DAY: DeckConfig.Config.ReviewCardOrder.ValueType  # 2
        REVIEW_CARD_ORDER_INTERVALS_ASCENDING: DeckConfig.Config.ReviewCardOrder.ValueType  # 3
        REVIEW_CARD_ORDER_INTERVALS_DESCENDING: DeckConfig.Config.ReviewCardOrder.ValueType  # 4
        REVIEW_CARD_ORDER_EASE_ASCENDING: DeckConfig.Config.ReviewCardOrder.ValueType  # 5
        REVIEW_CARD_ORDER_EASE_DESCENDING: DeckConfig.Config.ReviewCardOrder.ValueType  # 6
        REVIEW_CARD_ORDER_RELATIVE_OVERDUENESS: DeckConfig.Config.ReviewCardOrder.ValueType  # 7
        REVIEW_CARD_ORDER_RANDOM: DeckConfig.Config.ReviewCardOrder.ValueType  # 8
        REVIEW_CARD_ORDER_ADDED: DeckConfig.Config.ReviewCardOrder.ValueType  # 9
        REVIEW_CARD_ORDER_REVERSE_ADDED: DeckConfig.Config.ReviewCardOrder.ValueType  # 10

        class _ReviewMix:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _ReviewMixEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._ReviewMix.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            REVIEW_MIX_MIX_WITH_REVIEWS: DeckConfig.Config._ReviewMix.ValueType  # 0
            REVIEW_MIX_AFTER_REVIEWS: DeckConfig.Config._ReviewMix.ValueType  # 1
            REVIEW_MIX_BEFORE_REVIEWS: DeckConfig.Config._ReviewMix.ValueType  # 2

        class ReviewMix(_ReviewMix, metaclass=_ReviewMixEnumTypeWrapper): ...
        REVIEW_MIX_MIX_WITH_REVIEWS: DeckConfig.Config.ReviewMix.ValueType  # 0
        REVIEW_MIX_AFTER_REVIEWS: DeckConfig.Config.ReviewMix.ValueType  # 1
        REVIEW_MIX_BEFORE_REVIEWS: DeckConfig.Config.ReviewMix.ValueType  # 2

        class _LeechAction:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _LeechActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._LeechAction.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            LEECH_ACTION_SUSPEND: DeckConfig.Config._LeechAction.ValueType  # 0
            LEECH_ACTION_TAG_ONLY: DeckConfig.Config._LeechAction.ValueType  # 1

        class LeechAction(_LeechAction, metaclass=_LeechActionEnumTypeWrapper): ...
        LEECH_ACTION_SUSPEND: DeckConfig.Config.LeechAction.ValueType  # 0
        LEECH_ACTION_TAG_ONLY: DeckConfig.Config.LeechAction.ValueType  # 1

        class _AnswerAction:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _AnswerActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._AnswerAction.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            ANSWER_ACTION_BURY_CARD: DeckConfig.Config._AnswerAction.ValueType  # 0
            ANSWER_ACTION_ANSWER_AGAIN: DeckConfig.Config._AnswerAction.ValueType  # 1
            ANSWER_ACTION_ANSWER_GOOD: DeckConfig.Config._AnswerAction.ValueType  # 2
            ANSWER_ACTION_ANSWER_HARD: DeckConfig.Config._AnswerAction.ValueType  # 3
            ANSWER_ACTION_SHOW_REMINDER: DeckConfig.Config._AnswerAction.ValueType  # 4

        class AnswerAction(_AnswerAction, metaclass=_AnswerActionEnumTypeWrapper): ...
        ANSWER_ACTION_BURY_CARD: DeckConfig.Config.AnswerAction.ValueType  # 0
        ANSWER_ACTION_ANSWER_AGAIN: DeckConfig.Config.AnswerAction.ValueType  # 1
        ANSWER_ACTION_ANSWER_GOOD: DeckConfig.Config.AnswerAction.ValueType  # 2
        ANSWER_ACTION_ANSWER_HARD: DeckConfig.Config.AnswerAction.ValueType  # 3
        ANSWER_ACTION_SHOW_REMINDER: DeckConfig.Config.AnswerAction.ValueType  # 4

        class _QuestionAction:
            ValueType = typing.NewType("ValueType", builtins.int)
            V: typing_extensions.TypeAlias = ValueType

        class _QuestionActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[DeckConfig.Config._QuestionAction.ValueType], builtins.type):
            DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
            QUESTION_ACTION_SHOW_ANSWER: DeckConfig.Config._QuestionAction.ValueType  # 0
            QUESTION_ACTION_SHOW_REMINDER: DeckConfig.Config._QuestionAction.ValueType  # 1

        class QuestionAction(_QuestionAction, metaclass=_QuestionActionEnumTypeWrapper): ...
        QUESTION_ACTION_SHOW_ANSWER: DeckConfig.Config.QuestionAction.ValueType  # 0
        QUESTION_ACTION_SHOW_REMINDER: DeckConfig.Config.QuestionAction.ValueType  # 1

        LEARN_STEPS_FIELD_NUMBER: builtins.int
        RELEARN_STEPS_FIELD_NUMBER: builtins.int
        FSRS_WEIGHTS_FIELD_NUMBER: builtins.int
        NEW_PER_DAY_FIELD_NUMBER: builtins.int
        REVIEWS_PER_DAY_FIELD_NUMBER: builtins.int
        NEW_PER_DAY_MINIMUM_FIELD_NUMBER: builtins.int
        INITIAL_EASE_FIELD_NUMBER: builtins.int
        EASY_MULTIPLIER_FIELD_NUMBER: builtins.int
        HARD_MULTIPLIER_FIELD_NUMBER: builtins.int
        LAPSE_MULTIPLIER_FIELD_NUMBER: builtins.int
        INTERVAL_MULTIPLIER_FIELD_NUMBER: builtins.int
        MAXIMUM_REVIEW_INTERVAL_FIELD_NUMBER: builtins.int
        MINIMUM_LAPSE_INTERVAL_FIELD_NUMBER: builtins.int
        GRADUATING_INTERVAL_GOOD_FIELD_NUMBER: builtins.int
        GRADUATING_INTERVAL_EASY_FIELD_NUMBER: builtins.int
        NEW_CARD_INSERT_ORDER_FIELD_NUMBER: builtins.int
        NEW_CARD_GATHER_PRIORITY_FIELD_NUMBER: builtins.int
        NEW_CARD_SORT_ORDER_FIELD_NUMBER: builtins.int
        NEW_MIX_FIELD_NUMBER: builtins.int
        REVIEW_ORDER_FIELD_NUMBER: builtins.int
        INTERDAY_LEARNING_MIX_FIELD_NUMBER: builtins.int
        LEECH_ACTION_FIELD_NUMBER: builtins.int
        LEECH_THRESHOLD_FIELD_NUMBER: builtins.int
        DISABLE_AUTOPLAY_FIELD_NUMBER: builtins.int
        CAP_ANSWER_TIME_TO_SECS_FIELD_NUMBER: builtins.int
        SHOW_TIMER_FIELD_NUMBER: builtins.int
        STOP_TIMER_ON_ANSWER_FIELD_NUMBER: builtins.int
        SECONDS_TO_SHOW_QUESTION_FIELD_NUMBER: builtins.int
        SECONDS_TO_SHOW_ANSWER_FIELD_NUMBER: builtins.int
        QUESTION_ACTION_FIELD_NUMBER: builtins.int
        ANSWER_ACTION_FIELD_NUMBER: builtins.int
        WAIT_FOR_AUDIO_FIELD_NUMBER: builtins.int
        SKIP_QUESTION_WHEN_REPLAYING_ANSWER_FIELD_NUMBER: builtins.int
        BURY_NEW_FIELD_NUMBER: builtins.int
        BURY_REVIEWS_FIELD_NUMBER: builtins.int
        BURY_INTERDAY_LEARNING_FIELD_NUMBER: builtins.int
        DESIRED_RETENTION_FIELD_NUMBER: builtins.int
        IGNORE_REVLOGS_BEFORE_DATE_FIELD_NUMBER: builtins.int
        HISTORICAL_RETENTION_FIELD_NUMBER: builtins.int
        WEIGHT_SEARCH_FIELD_NUMBER: builtins.int
        OTHER_FIELD_NUMBER: builtins.int
        @property
        def learn_steps(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
        @property
        def relearn_steps(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
        @property
        def fsrs_weights(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.float]: ...
        new_per_day: builtins.int
        reviews_per_day: builtins.int
        new_per_day_minimum: builtins.int
        """not currently used"""
        initial_ease: builtins.float
        easy_multiplier: builtins.float
        hard_multiplier: builtins.float
        lapse_multiplier: builtins.float
        interval_multiplier: builtins.float
        maximum_review_interval: builtins.int
        minimum_lapse_interval: builtins.int
        graduating_interval_good: builtins.int
        graduating_interval_easy: builtins.int
        new_card_insert_order: global___DeckConfig.Config.NewCardInsertOrder.ValueType
        new_card_gather_priority: global___DeckConfig.Config.NewCardGatherPriority.ValueType
        new_card_sort_order: global___DeckConfig.Config.NewCardSortOrder.ValueType
        new_mix: global___DeckConfig.Config.ReviewMix.ValueType
        review_order: global___DeckConfig.Config.ReviewCardOrder.ValueType
        interday_learning_mix: global___DeckConfig.Config.ReviewMix.ValueType
        leech_action: global___DeckConfig.Config.LeechAction.ValueType
        leech_threshold: builtins.int
        disable_autoplay: builtins.bool
        cap_answer_time_to_secs: builtins.int
        show_timer: builtins.bool
        stop_timer_on_answer: builtins.bool
        seconds_to_show_question: builtins.float
        seconds_to_show_answer: builtins.float
        question_action: global___DeckConfig.Config.QuestionAction.ValueType
        answer_action: global___DeckConfig.Config.AnswerAction.ValueType
        wait_for_audio: builtins.bool
        skip_question_when_replaying_answer: builtins.bool
        bury_new: builtins.bool
        bury_reviews: builtins.bool
        bury_interday_learning: builtins.bool
        desired_retention: builtins.float
        """for fsrs"""
        ignore_revlogs_before_date: builtins.str
        historical_retention: builtins.float
        weight_search: builtins.str
        other: builtins.bytes
        def __init__(
            self,
            *,
            learn_steps: collections.abc.Iterable[builtins.float] | None = ...,
            relearn_steps: collections.abc.Iterable[builtins.float] | None = ...,
            fsrs_weights: collections.abc.Iterable[builtins.float] | None = ...,
            new_per_day: builtins.int = ...,
            reviews_per_day: builtins.int = ...,
            new_per_day_minimum: builtins.int = ...,
            initial_ease: builtins.float = ...,
            easy_multiplier: builtins.float = ...,
            hard_multiplier: builtins.float = ...,
            lapse_multiplier: builtins.float = ...,
            interval_multiplier: builtins.float = ...,
            maximum_review_interval: builtins.int = ...,
            minimum_lapse_interval: builtins.int = ...,
            graduating_interval_good: builtins.int = ...,
            graduating_interval_easy: builtins.int = ...,
            new_card_insert_order: global___DeckConfig.Config.NewCardInsertOrder.ValueType = ...,
            new_card_gather_priority: global___DeckConfig.Config.NewCardGatherPriority.ValueType = ...,
            new_card_sort_order: global___DeckConfig.Config.NewCardSortOrder.ValueType = ...,
            new_mix: global___DeckConfig.Config.ReviewMix.ValueType = ...,
            review_order: global___DeckConfig.Config.ReviewCardOrder.ValueType = ...,
            interday_learning_mix: global___DeckConfig.Config.ReviewMix.ValueType = ...,
            leech_action: global___DeckConfig.Config.LeechAction.ValueType = ...,
            leech_threshold: builtins.int = ...,
            disable_autoplay: builtins.bool = ...,
            cap_answer_time_to_secs: builtins.int = ...,
            show_timer: builtins.bool = ...,
            stop_timer_on_answer: builtins.bool = ...,
            seconds_to_show_question: builtins.float = ...,
            seconds_to_show_answer: builtins.float = ...,
            question_action: global___DeckConfig.Config.QuestionAction.ValueType = ...,
            answer_action: global___DeckConfig.Config.AnswerAction.ValueType = ...,
            wait_for_audio: builtins.bool = ...,
            skip_question_when_replaying_answer: builtins.bool = ...,
            bury_new: builtins.bool = ...,
            bury_reviews: builtins.bool = ...,
            bury_interday_learning: builtins.bool = ...,
            desired_retention: builtins.float = ...,
            ignore_revlogs_before_date: builtins.str = ...,
            historical_retention: builtins.float = ...,
            weight_search: builtins.str = ...,
            other: builtins.bytes = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing_extensions.Literal["answer_action", b"answer_action", "bury_interday_learning", b"bury_interday_learning", "bury_new", b"bury_new", "bury_reviews", b"bury_reviews", "cap_answer_time_to_secs", b"cap_answer_time_to_secs", "desired_retention", b"desired_retention", "disable_autoplay", b"disable_autoplay", "easy_multiplier", b"easy_multiplier", "fsrs_weights", b"fsrs_weights", "graduating_interval_easy", b"graduating_interval_easy", "graduating_interval_good", b"graduating_interval_good", "hard_multiplier", b"hard_multiplier", "historical_retention", b"historical_retention", "ignore_revlogs_before_date", b"ignore_revlogs_before_date", "initial_ease", b"initial_ease", "interday_learning_mix", b"interday_learning_mix", "interval_multiplier", b"interval_multiplier", "lapse_multiplier", b"lapse_multiplier", "learn_steps", b"learn_steps", "leech_action", b"leech_action", "leech_threshold", b"leech_threshold", "maximum_review_interval", b"maximum_review_interval", "minimum_lapse_interval", b"minimum_lapse_interval", "new_card_gather_priority", b"new_card_gather_priority", "new_card_insert_order", b"new_card_insert_order", "new_card_sort_order", b"new_card_sort_order", "new_mix", b"new_mix", "new_per_day", b"new_per_day", "new_per_day_minimum", b"new_per_day_minimum", "other", b"other", "question_action", b"question_action", "relearn_steps", b"relearn_steps", "review_order", b"review_order", "reviews_per_day", b"reviews_per_day", "seconds_to_show_answer", b"seconds_to_show_answer", "seconds_to_show_question", b"seconds_to_show_question", "show_timer", b"show_timer", "skip_question_when_replaying_answer", b"skip_question_when_replaying_answer", "stop_timer_on_answer", b"stop_timer_on_answer", "wait_for_audio", b"wait_for_audio", "weight_search", b"weight_search"]) -> None: ...

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    MTIME_SECS_FIELD_NUMBER: builtins.int
    USN_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    mtime_secs: builtins.int
    usn: builtins.int
    @property
    def config(self) -> global___DeckConfig.Config: ...
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
        mtime_secs: builtins.int = ...,
        usn: builtins.int = ...,
        config: global___DeckConfig.Config | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "id", b"id", "mtime_secs", b"mtime_secs", "name", b"name", "usn", b"usn"]) -> None: ...

global___DeckConfig = DeckConfig

@typing_extensions.final
class DeckConfigsForUpdate(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing_extensions.final
    class ConfigWithExtra(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CONFIG_FIELD_NUMBER: builtins.int
        USE_COUNT_FIELD_NUMBER: builtins.int
        @property
        def config(self) -> global___DeckConfig: ...
        use_count: builtins.int
        def __init__(
            self,
            *,
            config: global___DeckConfig | None = ...,
            use_count: builtins.int = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["config", b"config"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config", b"config", "use_count", b"use_count"]) -> None: ...

    @typing_extensions.final
    class CurrentDeck(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        @typing_extensions.final
        class Limits(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor

            REVIEW_FIELD_NUMBER: builtins.int
            NEW_FIELD_NUMBER: builtins.int
            REVIEW_TODAY_FIELD_NUMBER: builtins.int
            NEW_TODAY_FIELD_NUMBER: builtins.int
            REVIEW_TODAY_ACTIVE_FIELD_NUMBER: builtins.int
            NEW_TODAY_ACTIVE_FIELD_NUMBER: builtins.int
            review: builtins.int
            new: builtins.int
            review_today: builtins.int
            new_today: builtins.int
            review_today_active: builtins.bool
            """Whether review_today applies to today or a past day."""
            new_today_active: builtins.bool
            """Whether new_today applies to today or a past day."""
            def __init__(
                self,
                *,
                review: builtins.int | None = ...,
                new: builtins.int | None = ...,
                review_today: builtins.int | None = ...,
                new_today: builtins.int | None = ...,
                review_today_active: builtins.bool = ...,
                new_today_active: builtins.bool = ...,
            ) -> None: ...
            def HasField(self, field_name: typing_extensions.Literal["_new", b"_new", "_new_today", b"_new_today", "_review", b"_review", "_review_today", b"_review_today", "new", b"new", "new_today", b"new_today", "review", b"review", "review_today", b"review_today"]) -> builtins.bool: ...
            def ClearField(self, field_name: typing_extensions.Literal["_new", b"_new", "_new_today", b"_new_today", "_review", b"_review", "_review_today", b"_review_today", "new", b"new", "new_today", b"new_today", "new_today_active", b"new_today_active", "review", b"review", "review_today", b"review_today", "review_today_active", b"review_today_active"]) -> None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal["_new", b"_new"]) -> typing_extensions.Literal["new"] | None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal["_new_today", b"_new_today"]) -> typing_extensions.Literal["new_today"] | None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal["_review", b"_review"]) -> typing_extensions.Literal["review"] | None: ...
            @typing.overload
            def WhichOneof(self, oneof_group: typing_extensions.Literal["_review_today", b"_review_today"]) -> typing_extensions.Literal["review_today"] | None: ...

        NAME_FIELD_NUMBER: builtins.int
        CONFIG_ID_FIELD_NUMBER: builtins.int
        PARENT_CONFIG_IDS_FIELD_NUMBER: builtins.int
        LIMITS_FIELD_NUMBER: builtins.int
        name: builtins.str
        config_id: builtins.int
        @property
        def parent_config_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
        @property
        def limits(self) -> global___DeckConfigsForUpdate.CurrentDeck.Limits: ...
        def __init__(
            self,
            *,
            name: builtins.str = ...,
            config_id: builtins.int = ...,
            parent_config_ids: collections.abc.Iterable[builtins.int] | None = ...,
            limits: global___DeckConfigsForUpdate.CurrentDeck.Limits | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing_extensions.Literal["limits", b"limits"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing_extensions.Literal["config_id", b"config_id", "limits", b"limits", "name", b"name", "parent_config_ids", b"parent_config_ids"]) -> None: ...

    ALL_CONFIG_FIELD_NUMBER: builtins.int
    CURRENT_DECK_FIELD_NUMBER: builtins.int
    DEFAULTS_FIELD_NUMBER: builtins.int
    SCHEMA_MODIFIED_FIELD_NUMBER: builtins.int
    CARD_STATE_CUSTOMIZER_FIELD_NUMBER: builtins.int
    NEW_CARDS_IGNORE_REVIEW_LIMIT_FIELD_NUMBER: builtins.int
    FSRS_FIELD_NUMBER: builtins.int
    APPLY_ALL_PARENT_LIMITS_FIELD_NUMBER: builtins.int
    DAYS_SINCE_LAST_FSRS_OPTIMIZE_FIELD_NUMBER: builtins.int
    @property
    def all_config(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeckConfigsForUpdate.ConfigWithExtra]: ...
    @property
    def current_deck(self) -> global___DeckConfigsForUpdate.CurrentDeck: ...
    @property
    def defaults(self) -> global___DeckConfig: ...
    schema_modified: builtins.bool
    card_state_customizer: builtins.str
    """only applies to v3 scheduler"""
    new_cards_ignore_review_limit: builtins.bool
    """only applies to v3 scheduler"""
    fsrs: builtins.bool
    apply_all_parent_limits: builtins.bool
    days_since_last_fsrs_optimize: builtins.int
    def __init__(
        self,
        *,
        all_config: collections.abc.Iterable[global___DeckConfigsForUpdate.ConfigWithExtra] | None = ...,
        current_deck: global___DeckConfigsForUpdate.CurrentDeck | None = ...,
        defaults: global___DeckConfig | None = ...,
        schema_modified: builtins.bool = ...,
        card_state_customizer: builtins.str = ...,
        new_cards_ignore_review_limit: builtins.bool = ...,
        fsrs: builtins.bool = ...,
        apply_all_parent_limits: builtins.bool = ...,
        days_since_last_fsrs_optimize: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["current_deck", b"current_deck", "defaults", b"defaults"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["all_config", b"all_config", "apply_all_parent_limits", b"apply_all_parent_limits", "card_state_customizer", b"card_state_customizer", "current_deck", b"current_deck", "days_since_last_fsrs_optimize", b"days_since_last_fsrs_optimize", "defaults", b"defaults", "fsrs", b"fsrs", "new_cards_ignore_review_limit", b"new_cards_ignore_review_limit", "schema_modified", b"schema_modified"]) -> None: ...

global___DeckConfigsForUpdate = DeckConfigsForUpdate

@typing_extensions.final
class UpdateDeckConfigsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TARGET_DECK_ID_FIELD_NUMBER: builtins.int
    CONFIGS_FIELD_NUMBER: builtins.int
    REMOVED_CONFIG_IDS_FIELD_NUMBER: builtins.int
    MODE_FIELD_NUMBER: builtins.int
    CARD_STATE_CUSTOMIZER_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    NEW_CARDS_IGNORE_REVIEW_LIMIT_FIELD_NUMBER: builtins.int
    FSRS_FIELD_NUMBER: builtins.int
    APPLY_ALL_PARENT_LIMITS_FIELD_NUMBER: builtins.int
    FSRS_RESCHEDULE_FIELD_NUMBER: builtins.int
    target_deck_id: builtins.int
    @property
    def configs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DeckConfig]:
        """/ Unchanged, non-selected configs can be omitted. Deck will
        / be set to whichever entry comes last.
        """
    @property
    def removed_config_ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]: ...
    mode: global___UpdateDeckConfigsMode.ValueType
    card_state_customizer: builtins.str
    @property
    def limits(self) -> global___DeckConfigsForUpdate.CurrentDeck.Limits: ...
    new_cards_ignore_review_limit: builtins.bool
    fsrs: builtins.bool
    apply_all_parent_limits: builtins.bool
    fsrs_reschedule: builtins.bool
    def __init__(
        self,
        *,
        target_deck_id: builtins.int = ...,
        configs: collections.abc.Iterable[global___DeckConfig] | None = ...,
        removed_config_ids: collections.abc.Iterable[builtins.int] | None = ...,
        mode: global___UpdateDeckConfigsMode.ValueType = ...,
        card_state_customizer: builtins.str = ...,
        limits: global___DeckConfigsForUpdate.CurrentDeck.Limits | None = ...,
        new_cards_ignore_review_limit: builtins.bool = ...,
        fsrs: builtins.bool = ...,
        apply_all_parent_limits: builtins.bool = ...,
        fsrs_reschedule: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["limits", b"limits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["apply_all_parent_limits", b"apply_all_parent_limits", "card_state_customizer", b"card_state_customizer", "configs", b"configs", "fsrs", b"fsrs", "fsrs_reschedule", b"fsrs_reschedule", "limits", b"limits", "mode", b"mode", "new_cards_ignore_review_limit", b"new_cards_ignore_review_limit", "removed_config_ids", b"removed_config_ids", "target_deck_id", b"target_deck_id"]) -> None: ...

global___UpdateDeckConfigsRequest = UpdateDeckConfigsRequest

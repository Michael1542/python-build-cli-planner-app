from abc import ABCMeta, abstractmethod
from _collections_abc import Iterable


class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):

    @abstractmethod
    def is_due(self):
        pass



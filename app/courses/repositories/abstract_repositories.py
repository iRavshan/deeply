from uuid import UUID
from abc import abstractmethod
from typing import List
from common.repositories import AbstractBaseRepository
from ..models import Course, Topic, CourseProgress


class AbstractCourseRepository(AbstractBaseRepository[Course]):
    
    @abstractmethod
    def get_by_slug(self, slug: str) -> Course:
        pass

    @abstractmethod
    def get_topics(self, course_id: UUID) -> List[Topic]:
        pass 
     


class AbstractTopicRepository(AbstractBaseRepository[Topic]):
    
    @abstractmethod
    def get_by_slug(self, slug: str) -> Topic:
        pass

    @abstractmethod
    def get_next_topic(self, id: UUID) -> Topic:
        pass

    @abstractmethod
    def get_previous_topic(self, id: UUID) -> Topic:
        pass

    @abstractmethod   
    def is_latest(self, id: UUID) -> bool:
        pass

    @abstractmethod   
    def is_first(self, id: UUID) -> bool:
        pass


class AbstractCourseProgressRepository():

    @abstractmethod
    def get_last_completed_topic(self, user_id: UUID, course_id: UUID) -> Topic:
        pass
    
    
    @abstractmethod
    def set_last_completed_topic(self, user_id: UUID, topic_id: UUID) -> bool:
        pass 
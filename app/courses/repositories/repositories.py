from typing import List
from uuid import UUID
from .abstract_repositories import AbstractCourseRepository
from .abstract_repositories import AbstractTopicRepository
from .abstract_repositories import AbstractCourseProgressRepository
from courses.models import Course, Topic, Unit, CourseProgress
from users.models import CustomUser


class CourseRepository(AbstractCourseRepository):
    
    def get_by_id(self, id: UUID) -> Course:
        return Course.objects.get(id=id)
    
    def get_by_slug(self, slug: str) -> Course:
        return Course.objects.get(slug=slug)

    def get_list(self) -> List[Course]:
        return Course.objects.all()
    
    def get_units_with_topics(self, course_id: UUID) -> List[Unit]:
        units = Unit.objects.filter(course=course_id).order_by('order')
        units_with_topics = []
        for unit in units:
            topics = Topic.objects.filter(course=course_id, unit=unit.id)
            units_with_topics.append({
                'title': unit.title,
                'order': unit.order,
                'topics': topics
            })
        return units_with_topics
    
    def create(self, **kwargs) -> Course:
        return Course.objects.create(kwargs)
    
    def update(self, id: UUID, **kwargs) -> Course:
        course = self.get(id)
        for attr, value in kwargs.items():
            setattr(course, attr, value)
        course.save()
        return course
    
    def delete(self, id: UUID) -> None:
        course = self.get(id)
        course.delete()



class TopicRepository(AbstractTopicRepository):

    def get_by_id(self, id: UUID) -> Topic:
        return Topic.objects.get(id=id)
    
    def get_by_slug(self, slug: str) -> Topic:
        return Topic.objects.get(slug=slug)
    
    def get_next_topic(self, id: UUID) -> Topic:
        current_topic = Topic.objects.get(id=id)
        next_topic = Topic.objects.get(order = current_topic.order + 1)
        return next_topic
    
    def get_previous_topic(self, id: UUID) -> Topic:
        current_topic = Topic.objects.get(id=id)
        previous_topic = Topic.objects.get(order = current_topic.order - 1)
        return previous_topic
    
    def is_first(self, id: UUID) -> bool:
        topic = Topic.objects.get(id=id)
        first_topic = Topic.objects.filter(course=topic.course.id).order_by('order')[0]
        return topic.order == first_topic.order
    
    def is_latest(self, id: UUID) -> bool:
        topic = Topic.objects.get(id=id)
        latest_topic = Topic.objects.filter(course=topic.course.id).order_by('-order')[0]
        return topic.order == latest_topic.order

    def get_list(self) -> List[Topic]:
        return Topic.objects.all()
    
    def create(self, **kwargs) -> Topic:
        return Topic.objects.create(kwargs)
    
    def update(self, id: UUID, **kwargs) -> Topic:
        topic = self.get(id)
        for attr, value in kwargs.items():
            setattr(topic, attr, value)
        topic.save()
        return topic
    
    def delete(self, id: UUID) -> None:
        topic = self.get(id)
        topic.delete()


class CourseProgressRepository(AbstractCourseProgressRepository):

    def get_last_completed_topic(self, user_id: UUID, course_id: UUID) -> Topic | None:
        course = Course.objects.get(id=course_id)
        exist_progress = CourseProgress.objects.filter(user=user_id, course=course)
        
        if exist_progress.exists():
            progress = CourseProgress.objects.get(user=user_id, course=course)

            if progress.last_completed_topic is None:
                return None
            else:
                return progress.last_completed_topic
        else:
            return None


    def set_last_completed_topic(self, user_id: UUID, topic_id: UUID) -> bool:
        topic = Topic.objects.get(id=topic_id)
        exist_progress = CourseProgress.objects.filter(user=user_id, course=topic.course)

        if not exist_progress.exists():
            user = CustomUser.objects.get(id=user_id)
            new_progress = CourseProgress(user=user, course=topic.course)
            new_progress.save()
            
        progress = CourseProgress.objects.get(user=user_id, course=topic.course)
            
        if progress.last_completed_topic is None:
            first_topic = Topic.objects.filter(course=topic.course.id).order_by('order')[0]
            if first_topic.order == topic.order:
                progress.last_completed_topic = topic
                progress.save()
                return True
            else:
                return False
        else:
            if progress.last_completed_topic.order + 1 == topic.order:
                progress.last_completed_topic = topic
                progress.save()
                return True
            else:
                return False

            

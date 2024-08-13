from django.shortcuts import render
from .repositories.repositories import CourseRepository, TopicRepository, CourseProgressRepository


courseRepository = CourseRepository()
topicRepository = TopicRepository()
courseProgressRepository = CourseProgressRepository()


def course(request, course_slug):
    course = courseRepository.get_by_slug(slug=course_slug)
    last_completed_topic = None

    if request.user.is_authenticated:
        last_completed_topic = courseProgressRepository.get_last_completed_topic(request.user.id, course.id)
        
    if last_completed_topic is None:
        last_completed_topic = courseRepository.get_topics(course.id)[0]

    return topic(request, course_slug, last_completed_topic.slug)



def topic(request, course_slug, topic_slug):
    course = courseRepository.get_by_slug(slug=course_slug)
    all_topics = courseRepository.get_topics(course_id=course.id)
    current_topic = topicRepository.get_by_slug(slug=topic_slug)
    
    topics_with_status = []

    if request.user.is_authenticated:
        last_completed_topic = courseProgressRepository.get_last_completed_topic(request.user.id, course.id)
        courseProgressRepository.set_last_completed_topic(request.user.id, current_topic.id)
        last_completed_order = last_completed_topic.order if last_completed_topic else -1

        topics_with_status = [
            {
                'id': topic.id,
                'title': topic.title,
                'slug': topic.slug,
                'is_completed': last_completed_order >= topic.order
            }
            for topic in all_topics
        ]
    else:
        topics_with_status = [
            {
                'id': topic.id,
                'title': topic.title,
                'slug': topic.slug
            }
            for topic in all_topics
        ]

    context = {
        'course': course,
        'topics': topics_with_status,
        'current_topic': current_topic,
    }

    if not topicRepository.is_first(current_topic.id):
        context['previous_topic_slug'] = topicRepository.get_previous_topic(current_topic.id).slug

    if not topicRepository.is_latest(current_topic.id):
        context['next_topic_slug'] = topicRepository.get_next_topic(current_topic.id).slug

    return render(request, 'course/course-details.html', context)

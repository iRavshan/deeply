from django.shortcuts import render
from .repositories.repositories import ArticleRepository, TagRepository


articleRepository = ArticleRepository()
tagRepository = TagRepository()


def blog(request):
    articles = articleRepository.get_list()
    all_tags = tagRepository.get_list()
    most_read_articles = articleRepository.get_most_read(3)

    context = {
        'articles': articles,
        'all_tags': all_tags,
        'most_read_articles': most_read_articles
    }

    return render(request, 'blog/blog.html', context)


def article(request, article_slug):
    article = articleRepository.get_by_slug(article_slug)
    related_articles = articleRepository.get_list()

    context = {
        'article': article,
        'related_articles': related_articles
    }
    
    return render(request, 'blog/article.html', context)


def tag(request, tag_slug):
    articles = articleRepository.get_by_tag(tag_slug)
    all_tags = tagRepository.get_list()
    tag_name = tagRepository.get_by_slug(tag_slug)
    most_read_articles = articleRepository.get_most_read(3)

    context = {
        'articles': articles,
        'all_tags': all_tags,
        'tag_name': tag_name,
        'most_read_articles': most_read_articles
    }

    return render(request, 'blog/tag.html', context)

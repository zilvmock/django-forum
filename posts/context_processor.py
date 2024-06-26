from posts.models import Post

def searchFunction(request):
    posts = Post.objects.all()

    context = {}
    if "search" in request.GET:
        query = request.GET.get("q")
        by_title = posts.filter(title__icontains=query, approved=True, closed=False)
        by_content = posts.filter(content__icontains=query, approved=True, closed=False)
        by_tags = posts.filter(tags__name__in=[query], approved=True, closed=False)
        all_query = by_title | by_content | by_tags
        
        for post in all_query.values_list('title', flat=True).distinct():
            posts.filter(pk__in=Post.objects.filter(title=post.title).values_list('id', flat=True)[1:]).delete()

        context = {
            "posts": all_query,
            "query": query,
        }
    return context

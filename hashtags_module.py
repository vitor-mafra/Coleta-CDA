import instaloader

def download_hashtag (counter, tag):
    '''
    Pega a hashtag passada, e o número de posts desejados e baixa
    essa quantidade de posts associados a hashtag. Retorna uma lista 
    com os shortcodes dos posts coletados.
    '''
    loader = instaloader.Instaloader()
    hashtag = instaloader.Hashtag.from_name(loader.context, tag)
    i = 0
    shortcodes = []

    for post in hashtag.get_posts():
        loader.download_post(post, target="#"+tag)
        shortcodes.append(post.shortcode)
        i += 1
        if i==counter:      
            break
    
    return shortcodes

def pega_likes (shortcodes):
    '''
    Recebe uma lista de shortcodes, e retorna uma lista com as quantidades
    de likes em cada post.
    '''
    loader = instaloader.Instaloader()
    likes = []
    Post = instaloader.Post
    for code in shortcodes:
        post = Post.from_shortcode (loader.context, code)
        likes.append(post.likes)
    
    return likes

def pega_comentarios (shortcodes):
    '''
    Recebe uma lista de shortcodes, e retorna uma lista com as quantidades
    de comentários em cada post.
    '''
    loader = instaloader.Instaloader()
    comentarios = []
    Post = instaloader.Post
    for code in shortcodes:
        post = Post.from_shortcode (loader.context, code)
        comentarios.append(post.comments)
    
    return comentarios